from src.pytemplate.domain.events import TrafficLightChanged, VehicleEnteredIntersection
from src.pytemplate.domain.models import TrafficLightState


def test_vehicle_entered_intersection_initialization():
    event = VehicleEnteredIntersection(vehicle_id="V123", intersection_id="I456")

    assert event.vehicle_id == "V123"
    assert event.intersection_id == "I456"


def test_traffic_light_changed_initialization():
    event = TrafficLightChanged(light_id="TL123", new_state=TrafficLightState.RED)

    assert event.light_id == "TL123"
    assert event.new_state == TrafficLightState.RED
