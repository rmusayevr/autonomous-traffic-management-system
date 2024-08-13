from src.pytemplate.domain.models import intersection_factory


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
