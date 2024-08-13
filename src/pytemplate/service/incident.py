from pytemplate.domain.models import Intersection, TrafficSystem


class IncidentService:
    def calculate_alternative_route(self, start: Intersection, end: Intersection) -> list[Intersection]:
        return [start, end]

    def handle_incident(self, traffic_system: TrafficSystem, location: Intersection):
        for vehicle in traffic_system.vehicles.values():
            if vehicle.current_position == location:
                new_route = self.calculate_alternative_route(location, vehicle.current_route[-1])
                vehicle.current_route = new_route
