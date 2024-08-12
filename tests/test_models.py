from src.pytemplate.domain.models import TrafficLightState


def test_enum_values():
    assert TrafficLightState.RED.value == "RED"
    assert TrafficLightState.YELLOW.value == "YELLOW"
    assert TrafficLightState.GREEN.value == "GREEN"


def test_enum_str_method():
    assert str(TrafficLightState.RED) == "RED"
    assert str(TrafficLightState.YELLOW) == "YELLOW"
    assert str(TrafficLightState.GREEN) == "GREEN"
