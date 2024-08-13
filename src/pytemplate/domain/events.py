from dataclasses import dataclass

from src.pytemplate.domain.models import TrafficLightState


@dataclass
class VehicleEnteredIntersection:
    vehicle_id: str
    intersection_id: str


@dataclass
class TrafficLightChanged:
    light_id: str
    new_state: TrafficLightState
