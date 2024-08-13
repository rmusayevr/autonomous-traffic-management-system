from unittest.mock import Mock, patch

import pytest

from pytemplate.domain.models import intersection_factory, traffic_light_factory, vehicle_factory
from src.pytemplate.service.simulator import SimulationEngine
from src.pytemplate.service.traffic_control import TrafficControlService, TrafficLightState, TrafficSystem


@pytest.fixture
def mock_traffic_system():
    intersection_a = intersection_factory(id="A", connected_roads=["B"])
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[intersection_a])
    traffic_light = traffic_light_factory(id="TL_A", state=TrafficLightState.RED, intersection=intersection_a)

    traffic_system = TrafficSystem(intersections={"A": intersection_a}, traffic_lights={"TL_A": traffic_light}, vehicles={"V1": vehicle})
    return traffic_system


@pytest.fixture
def mock_control_service():
    return Mock(spec=TrafficControlService)


def test_simulation_engine_run(mock_traffic_system, mock_control_service):
    simulation_engine = SimulationEngine(mock_traffic_system, mock_control_service)

    with patch("time.sleep", return_value=None):
        simulation_engine.run(duration=2)

    assert mock_control_service.manage_traffic_lights.call_count == 2
    assert mock_traffic_system.vehicles["V1"].current_position == mock_traffic_system.intersections["A"]


def test_simulation_engine_print_status(mock_traffic_system, mock_control_service, capsys):
    simulation_engine = SimulationEngine(mock_traffic_system, mock_control_service)

    mock_traffic_system.vehicles["V1"].move_to_next_intersection()

    simulation_engine.print_status()

    captured = capsys.readouterr()
    assert "Vehicle V1 at A" in captured.out
