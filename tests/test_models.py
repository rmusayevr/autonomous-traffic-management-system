import pytest

from src.pytemplate.domain.models import Intersection, intersection_factory, TrafficLight, TrafficLightState


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


def test_intersection_factory():
    intersection = intersection_factory(id="C3", connected_roads=["Road 4", "Road 5"])
    assert isinstance(intersection, Intersection)
    assert intersection.id == "C3"
    assert intersection.connected_roads == ["Road 4", "Road 5"]


def test_traffic_light_creation():
    intersection = intersection_factory(id="A1", connected_roads=["Road 1", "Road 2"])
    traffic_light = TrafficLight(id="TL1", state=TrafficLightState.RED, intersection=intersection)
    assert traffic_light.id == "TL1"
    assert traffic_light.state == TrafficLightState.RED
    assert traffic_light.intersection == intersection


def test_change_state():
    intersection = intersection_factory(id="B2", connected_roads=["Road 3", "Road 4"])
    traffic_light = TrafficLight(id="TL2", state=TrafficLightState.RED, intersection=intersection)

    # Test changing to YELLOW
    traffic_light.change_state(TrafficLightState.YELLOW)
    assert traffic_light.state == TrafficLightState.YELLOW

    # Test changing to GREEN using string
    traffic_light.change_state(TrafficLightState.GREEN)
    assert traffic_light.state == TrafficLightState.GREEN

    # Test changing back to RED
    traffic_light.change_state(TrafficLightState.RED)
    assert traffic_light.state == TrafficLightState.RED
