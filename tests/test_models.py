from src.pytemplate.domain.models import Intersection, TrafficLightState


def test_enum_values():
    assert TrafficLightState.RED.value == "RED"
    assert TrafficLightState.YELLOW.value == "YELLOW"
    assert TrafficLightState.GREEN.value == "GREEN"


def test_enum_str_method():
    assert str(TrafficLightState.RED) == "RED"
    assert str(TrafficLightState.YELLOW) == "YELLOW"
    assert str(TrafficLightState.GREEN) == "GREEN"


def test_intersection_creation():
    intersection = Intersection(id="A1", connected_roads=["Road 1", "Road 2", "Road 3"])
    assert intersection.id == "A1"
    assert intersection.connected_roads == ["Road 1", "Road 2", "Road 3"]
