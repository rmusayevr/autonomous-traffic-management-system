from unittest.mock import patch

from src.pytemplate.domain.models import (
    Intersection,
    intersection_factory,
    traffic_light_factory,
    TrafficLight,
    TrafficLightState,
    vehicle_factory,
)
from src.pytemplate.entrypoints.cli.main import get_intersection_input, get_traffic_light_input, get_vehicle_input, main


def test_get_intersection_input():
    user_inputs = ["2", "A", "B, C", "B", "A, D"]

    with patch("builtins.input", side_effect=user_inputs):
        intersections = get_intersection_input()

    assert len(intersections) == 2
    assert isinstance(intersections["A"], Intersection)
    assert intersections["A"].connected_roads == ["B", "C"]
    assert intersections["B"].connected_roads == ["A", "D"]


def test_get_traffic_light_input():
    intersections = {
        "A": intersection_factory(id="A", connected_roads=["B"]),
        "B": intersection_factory(id="B", connected_roads=["A", "C"]),
    }

    user_inputs = ["2", "TL1", "A", "TL2", "B"]

    with patch("builtins.input", side_effect=user_inputs):
        traffic_lights = get_traffic_light_input(intersections)

    assert len(traffic_lights) == 2
    assert isinstance(traffic_lights["TL1"], TrafficLight)
    assert traffic_lights["TL1"].state == TrafficLightState.RED
    assert traffic_lights["TL1"].intersection == intersections["A"]
    assert traffic_lights["TL2"].intersection == intersections["B"]


def test_get_traffic_light_input_invalid_intersection():
    intersections = {
        "A": intersection_factory(id="A", connected_roads=["B"]),
        "B": intersection_factory(id="B", connected_roads=["A", "C"]),
    }

    user_inputs = ["1", "TL1", "C", "A"]

    with patch("builtins.input", side_effect=user_inputs):
        traffic_lights = get_traffic_light_input(intersections)

    assert len(traffic_lights) == 1
    assert traffic_lights["TL1"].intersection == intersections["A"]


def test_get_vehicle_input_valid_route():
    intersections = {
        "A": intersection_factory(id="A", connected_roads=["B"]),
        "B": intersection_factory(id="B", connected_roads=["A", "C"]),
        "C": intersection_factory(id="C", connected_roads=["B"]),
    }

    user_inputs = ["1", "V1", "Car", "60", "A, B, C"]

    with patch("builtins.input", side_effect=user_inputs):
        vehicles = get_vehicle_input(intersections)

    assert len(vehicles) == 1
    assert vehicles["V1"].id == "V1"
    assert vehicles["V1"].type == "Car"
    assert vehicles["V1"].speed == 60.0
    assert [i.id for i in vehicles["V1"].current_route] == ["A", "B", "C"]


def test_get_vehicle_input_invalid_route():
    intersections = {
        "A": intersection_factory(id="A", connected_roads=["B"]),
        "B": intersection_factory(id="B", connected_roads=["A", "C"]),
    }

    user_inputs = ["1", "V1", "Car", "60", "A, X, B", "A, B"]

    with patch("builtins.input", side_effect=user_inputs):
        vehicles = get_vehicle_input(intersections)

    assert len(vehicles) == 1
    assert vehicles["V1"].id == "V1"
    assert vehicles["V1"].type == "Car"
    assert vehicles["V1"].speed == 60.0
    assert [i.id for i in vehicles["V1"].current_route] == ["A", "B"]


@patch(
    "builtins.input",
    side_effect=[
        "2",  # Number of intersections
        "A",
        "B,C",  # Intersection A
        "B",
        "A,C",  # Intersection B
        "C",
        "B",  # Intersection C
        "2",  # Number of traffic lights
        "TL1",
        "A",  # Traffic light TL1
        "TL2",
        "B",  # Traffic light TL2
        "1",  # Number of vehicles
        "V1",
        "Car",
        "60",  # Vehicle V1
        "A,B,C"  # Route for Vehicle V1
        "10",  # Simulation duration
    ],
)
def test_main_function(mock_input):
    # Mock the methods to return sample data
    with (
        patch(
            "src.pytemplate.entrypoints.cli.main.get_intersection_input",
            return_value={
                "A": intersection_factory(id="A", connected_roads=["B", "C"]),
                "B": intersection_factory(id="B", connected_roads=["A", "C"]),
                "C": intersection_factory(id="C", connected_roads=["B"]),
            },
        ) as mock_get_intersection_input,
        patch(
            "src.pytemplate.entrypoints.cli.main.get_traffic_light_input",
            return_value={
                "TL1": traffic_light_factory(
                    id="TL1", state=TrafficLightState.RED, intersection=Intersection(id="A", connected_roads=["B", "C"])
                ),
                "TL2": traffic_light_factory(
                    id="TL2", state=TrafficLightState.RED, intersection=Intersection(id="B", connected_roads=["A", "C"])
                ),
            },
        ) as mock_get_traffic_light_input,
        patch(
            "src.pytemplate.entrypoints.cli.main.get_vehicle_input",
            return_value={
                "V1": vehicle_factory(
                    id="V1",
                    type="Car",
                    speed=60,
                    current_route=[
                        intersection_factory(id="A", connected_roads=["B", "C"]),
                        intersection_factory(id="B", connected_roads=["A", "C"]),
                        intersection_factory(id="C", connected_roads=["B"]),
                    ],
                )
            },
        ) as mock_get_vehicle_input,
    ):
        # Call the main function
        main()

        # Check if the methods were called correctly
        mock_get_intersection_input.assert_called_once()
        mock_get_traffic_light_input.assert_called_once_with(
            {
                "A": intersection_factory(id="A", connected_roads=["B", "C"]),
                "B": intersection_factory(id="B", connected_roads=["A", "C"]),
                "C": intersection_factory(id="C", connected_roads=["B"]),
            }
        )
        mock_get_vehicle_input.assert_called_once_with(
            {
                "A": intersection_factory(id="A", connected_roads=["B", "C"]),
                "B": intersection_factory(id="B", connected_roads=["A", "C"]),
                "C": intersection_factory(id="C", connected_roads=["B"]),
            }
        )
