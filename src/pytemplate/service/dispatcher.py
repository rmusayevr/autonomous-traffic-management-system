from pytemplate.domain.events import TrafficLightChanged, VehicleEnteredIntersection


class EventDispatcher:
    def dispatch(self, event):
        if isinstance(event, VehicleEnteredIntersection):
            self.handle_vehicle_entered_intersection(event)
        elif isinstance(event, TrafficLightChanged):
            self.handle_traffic_light_changed(event)
        else:
            raise ValueError(f"Unhandled event type: {type(event).__name__}")

    def handle_vehicle_entered_intersection(self, event: VehicleEnteredIntersection):
        print(f"Vehicle {event.vehicle_id} entered intersection {event.intersection_id}.")
        # Add logic to handle the event

    def handle_traffic_light_changed(self, event: TrafficLightChanged):
        print(f"Traffic light {event.light_id} changed to {event.new_state}.")
        # Add logic to handle the event
