from pytemplate.domain.models import intersection_factory, traffic_light_factory, TrafficLightState, TrafficSystem, vehicle_factory
from src.pytemplate.service.incident import IncidentService
from src.pytemplate.service.traffic_control import TrafficControlService


def test_manage_traffic_lights():
    intersection = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    traffic_light1 = traffic_light_factory(id="TL1", state=TrafficLightState.RED, intersection=intersection)
    traffic_light2 = traffic_light_factory(id="TL2", state=TrafficLightState.GREEN, intersection=intersection)
    traffic_light3 = traffic_light_factory(id="TL3", state=TrafficLightState.YELLOW, intersection=intersection)

    system = TrafficSystem(
        intersections={"I1": intersection},
        traffic_lights={"TL1": traffic_light1, "TL2": traffic_light2, "TL3": traffic_light3},
        vehicles={},
    )

    service = TrafficControlService()
    service.manage_traffic_lights(system)

    assert system.traffic_lights["TL1"].state == TrafficLightState.GREEN
    assert system.traffic_lights["TL2"].state == TrafficLightState.YELLOW
    assert system.traffic_lights["TL3"].state == TrafficLightState.RED


def test_calculate_alternative_route():
    start = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    end = intersection_factory(id="I2", connected_roads=["R2", "R3"])

    service = IncidentService()
    route = service.calculate_alternative_route(start, end)

    assert route == [start, end]


def test_handle_incident():
    start = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    end = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[end], current_position=start)

    system = TrafficSystem(intersections={"I1": start, "I2": end}, traffic_lights={}, vehicles={"V1": vehicle})

    service = IncidentService()
    service.handle_incident(system, start)

    # Check if the vehicle's route has been updated
    assert vehicle.current_route == [start, end]
