from src.pytemplate.domain.models import intersection_factory, traffic_light_factory, TrafficLightState, vehicle_factory


def get_intersection_input():
    intersections = {}
    num_intersections = int(input("Enter the number of intersections: "))

    for i in range(num_intersections):
        intersection_id = input(f"Enter the ID for intersection {i+1}: ")
        connected_roads = input(f"Enter the connected roads for {intersection_id} (comma separated): ").split(",")
        intersections[intersection_id] = intersection_factory(
            id=intersection_id.strip(), connected_roads=[road.strip() for road in connected_roads]
        )

    return intersections


def get_traffic_light_input(intersections):
    traffic_lights = {}

    # Prompt the user for the number of traffic lights
    num_traffic_lights = int(input("Enter the number of traffic lights: "))

    # Loop through to get the details of each traffic light
    for _ in range(num_traffic_lights):
        traffic_light_id = input("Enter the traffic light ID: ")
        intersection_id = input("Enter the intersection ID for this traffic light: ")

        # Validate the intersection ID
        while intersection_id not in intersections:
            print(f"Intersection ID {intersection_id} not found. Please enter a valid intersection ID.")
            intersection_id = input("Enter the intersection ID for this traffic light: ")

        # Create the TrafficLight object and add it to the dictionary
        intersection = intersections[intersection_id]
        traffic_lights[traffic_light_id] = traffic_light_factory(
            id=traffic_light_id, state=TrafficLightState.RED, intersection=intersection
        )

    return traffic_lights


def get_vehicle_route(intersections):
    route_valid = False
    while not route_valid:
        route = input("Enter the route (comma-separated intersection IDs): ").strip().split(",")
        route = [id.strip() for id in route]

        if all(intersection_id in intersections for intersection_id in route):
            vehicle_route = [intersections[intersection_id] for intersection_id in route]
            route_valid = True
            return vehicle_route
        else:
            print("Invalid route. Please make sure all intersection IDs are valid and try again.")


def get_vehicle_input(intersections):
    vehicles = {}

    # Prompt the user for the number of vehicles
    num_vehicles = int(input("Enter the number of vehicles: "))

    # Loop through to get the details of each vehicle
    for _ in range(num_vehicles):
        vehicle_id = input("Enter the vehicle ID: ").strip()
        vehicle_type = input("Enter the vehicle type: ").strip()
        vehicle_speed = int(input("Enter the vehicle speed: ").strip())
        vehicle_route = get_vehicle_route(intersections)

        # Create the Vehicle object and add it to the dictionary
        vehicles[vehicle_id] = vehicle_factory(id=vehicle_id, type=vehicle_type, speed=vehicle_speed, current_route=vehicle_route)

    return vehicles
