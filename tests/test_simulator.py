from unittest.mock import Mock, patch

from pytemplate.domain.models import intersection_factory, traffic_light_factory, vehicle_factory
from src.pytemplate.service.simulator import SimulationEngine
from src.pytemplate.service.traffic_control import TrafficControlService, TrafficLightState, TrafficSystem


def create_mock_traffic_system():
    intersection_a = intersection_factory(id="A", connected_roads=["B"])
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[intersection_a])
    traffic_light = traffic_light_factory(id="TL_A", state=TrafficLightState.RED, intersection=intersection_a)

    traffic_system = TrafficSystem(intersections={"A": intersection_a}, traffic_lights={"TL_A": traffic_light}, vehicles={"V1": vehicle})
    return traffic_system


def create_mock_control_service():
    return Mock(spec=TrafficControlService)


def test_simulation_engine_run():
    traffic_system = create_mock_traffic_system()
    control_service = create_mock_control_service()
    simulation_engine = SimulationEngine(traffic_system, control_service)

    with patch("time.sleep", return_value=None):
        simulation_engine.run(duration=2)

    assert control_service.manage_traffic_lights.call_count == 2
    assert traffic_system.vehicles["V1"].current_position == traffic_system.intersections["A"]


def test_simulation_engine_print_status(capsys):
    traffic_system = create_mock_traffic_system()
    control_service = create_mock_control_service()
    simulation_engine = SimulationEngine(traffic_system, control_service)

    simulation_engine.run(duration=1)

    captured = capsys.readouterr()
    assert "Vehicle V1 at A" in captured.out
