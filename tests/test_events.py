from src.pytemplate.domain.events import VehicleEnteredIntersection


def test_vehicle_entered_intersection_initialization():
    event = VehicleEnteredIntersection(vehicle_id="V123", intersection_id="I456")

    assert event.vehicle_id == "V123"
    assert event.intersection_id == "I456"
