from src.pytemplate.domain.models import intersection_factory, traffic_light_factory, TrafficLightState


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
