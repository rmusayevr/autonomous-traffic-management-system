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
