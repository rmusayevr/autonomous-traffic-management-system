from pytemplate.domain.models import intersection_factory, traffic_light_factory, TrafficLightState, TrafficSystem
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
