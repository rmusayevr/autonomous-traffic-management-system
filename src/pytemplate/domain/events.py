from dataclasses import dataclass


@dataclass
class VehicleEnteredIntersection:
    vehicle_id: str
    intersection_id: str
