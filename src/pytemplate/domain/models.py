from dataclasses import dataclass
from enum import Enum


class TrafficLightState(Enum):
    RED = "RED"
    GREEN = "GREEN"
    YELLOW = "YELLOW"

    def __str__(self):
        return self.value


@dataclass
class Intersection:
    id: str
    connected_roads: list[str]


def intersection_factory(id: str, connected_roads: list[str]) -> Intersection:
    return Intersection(id=id, connected_roads=connected_roads)


@dataclass
class TrafficLight:
    id: str
    state: TrafficLightState
    intersection: Intersection

    def change_state(self, new_state: TrafficLightState):
        self.state = new_state


def traffic_light_factory(id: str, state: TrafficLightState, intersection: Intersection) -> TrafficLight:
    return TrafficLight(id=id, state=state, intersection=intersection)


@dataclass
class Vehicle:
    id: str
    type: str
    speed: int
    current_route: list[Intersection]
    current_position: Intersection | None = None

    def move_to_next_intersection(self):
        if self.current_route:
            self.current_position = self.current_route.pop(0)

    def has_reached_destination(self) -> bool:
        return len(self.current_route) == 0 and self.current_position is not None


def vehicle_factory(
    id: str, type: str, speed: int, current_route: list[Intersection], current_position: Intersection | None = None
) -> Vehicle:
    return Vehicle(id=id, type=type, speed=speed, current_route=current_route, current_position=current_position)


@dataclass
class TrafficSystem:
    intersections: dict[str, Intersection]
    traffic_lights: dict[str, TrafficLight]
    vehicles: dict[str, Vehicle]

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.id] = vehicle

    def update_traffic_light(self, traffic_light_id: str, new_state: TrafficLightState):
        self.traffic_lights[traffic_light_id].change_state(new_state)

    def move_vehicle(self, vehicle_id: str):
        vehicle = self.vehicles[vehicle_id]
        vehicle.move_to_next_intersection()


def traffic_system_factory(
    intersections: dict[str, Intersection],
    traffic_lights: dict[str, TrafficLight],
    vehicles: dict[str, Vehicle],
) -> TrafficSystem:
    return TrafficSystem(intersections=intersections, traffic_lights=traffic_lights, vehicles=vehicles)
