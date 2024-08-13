import time

from pytemplate.domain.models import TrafficSystem
from src.pytemplate.service.traffic_control import TrafficControlService


class SimulationEngine:
    def __init__(self, traffic_system: TrafficSystem, control_service: TrafficControlService):
        self.traffic_system = traffic_system
        self.control_service = control_service

    def run(self, duration: int):
        print(f"Running simulation for {duration} seconds...")
        for _ in range(duration):
            self.control_service.manage_traffic_lights(self.traffic_system)
            for vehicle in self.traffic_system.vehicles.values():
                vehicle.move_to_next_intersection()
            self.print_status()
            time.sleep(1)

    def print_status(self):
        for vehicle in self.traffic_system.vehicles.values():
            position = vehicle.current_position.id if vehicle.current_position else "unknown"
            print(f"Vehicle {vehicle.id} at {position}")
