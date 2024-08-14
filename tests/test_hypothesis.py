import hypothesis

from src.pytemplate.domain.events import VehicleEnteredIntersection
from src.pytemplate.domain.models import Intersection


@hypothesis.given(
    id=hypothesis.strategies.text(min_size=1),
    connected_roads=hypothesis.strategies.lists(hypothesis.strategies.text(min_size=1), min_size=1),
)
def test_valid_intersection(id, connected_roads):
    intersection = Intersection(id=id, connected_roads=connected_roads)
    assert intersection.id == id
    assert intersection.connected_roads == connected_roads


@hypothesis.given(
    connected_roads=hypothesis.strategies.lists(hypothesis.strategies.text(min_size=1), min_size=1),
)
def test_empty_id(connected_roads):
    intersection = Intersection(id="", connected_roads=connected_roads)
    assert intersection.id == ""
    assert intersection.connected_roads == connected_roads


@hypothesis.given(
    id=hypothesis.strategies.text(min_size=1),
)
def test_empty_connected_roads(id):
    intersection = Intersection(id=id, connected_roads=[])
    assert intersection.id == id
    assert intersection.connected_roads == []


@hypothesis.given(
    vehicle_id=hypothesis.strategies.text(min_size=1),
    intersection_id=hypothesis.strategies.text(min_size=1),
)
def test_valid_vehicle_entered_intersection(vehicle_id, intersection_id):
    event = VehicleEnteredIntersection(vehicle_id=vehicle_id, intersection_id=intersection_id)
    assert event.vehicle_id == vehicle_id
    assert event.intersection_id == intersection_id


@hypothesis.given(
    intersection_id=hypothesis.strategies.text(min_size=1),
)
def test_empty_vehicle_id(intersection_id):
    event = VehicleEnteredIntersection(vehicle_id="", intersection_id=intersection_id)
    assert event.vehicle_id == ""
    assert event.intersection_id == intersection_id


@hypothesis.given(
    vehicle_id=hypothesis.strategies.text(min_size=1),
)
def test_empty_intersection_id(vehicle_id):
    event = VehicleEnteredIntersection(vehicle_id=vehicle_id, intersection_id="")
    assert event.vehicle_id == vehicle_id
    assert event.intersection_id == ""
