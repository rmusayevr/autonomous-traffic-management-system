from src.pytemplate.domain.models import (
    Intersection,
    intersection_factory,
    traffic_light_factory,
    traffic_system_factory,
    TrafficLight,
    TrafficLightState,
    TrafficSystem,
    Vehicle,
    vehicle_factory,
)


def test_enum_values():
    assert TrafficLightState.RED.value == "RED"
    assert TrafficLightState.YELLOW.value == "YELLOW"
    assert TrafficLightState.GREEN.value == "GREEN"


def test_enum_str_method():
    assert str(TrafficLightState.RED) == "RED"
    assert str(TrafficLightState.YELLOW) == "YELLOW"
    assert str(TrafficLightState.GREEN) == "GREEN"


def test_intersection_creation():
    intersection = Intersection(id="A1", connected_roads=["Road 1", "Road 2", "Road 3"])
    assert intersection.id == "A1"
    assert intersection.connected_roads == ["Road 1", "Road 2", "Road 3"]


def test_intersection_factory():
    intersection = intersection_factory(id="C3", connected_roads=["Road 4", "Road 5"])
    assert isinstance(intersection, Intersection)
    assert intersection.id == "C3"
    assert intersection.connected_roads == ["Road 4", "Road 5"]


def test_traffic_light_creation():
    intersection = intersection_factory(id="A1", connected_roads=["Road 1", "Road 2"])
    traffic_light = TrafficLight(id="TL1", state=TrafficLightState.RED, intersection=intersection)
    assert traffic_light.id == "TL1"
    assert traffic_light.state == TrafficLightState.RED
    assert traffic_light.intersection == intersection


def test_change_state():
    intersection = intersection_factory(id="B2", connected_roads=["Road 3", "Road 4"])
    traffic_light = TrafficLight(id="TL2", state=TrafficLightState.RED, intersection=intersection)

    # Test changing to YELLOW
    traffic_light.change_state(TrafficLightState.YELLOW)
    assert traffic_light.state == TrafficLightState.YELLOW

    # Test changing to GREEN using string
    traffic_light.change_state(TrafficLightState.GREEN)
    assert traffic_light.state == TrafficLightState.GREEN

    # Test changing back to RED
    traffic_light.change_state(TrafficLightState.RED)
    assert traffic_light.state == TrafficLightState.RED


def test_traffic_light_factory():
    intersection = intersection_factory(id="A1", connected_roads=["Road 1", "Road 2"])
    traffic_light = traffic_light_factory(id="TL1", state=TrafficLightState.RED, intersection=intersection)

    assert isinstance(traffic_light, TrafficLight)
    assert traffic_light.id == "TL1"
    assert traffic_light.state == TrafficLightState.RED
    assert traffic_light.intersection == intersection


def test_traffic_light_factory_change_state():
    intersection = intersection_factory(id="C3", connected_roads=["Road 5", "Road 6"])
    traffic_light = traffic_light_factory(id="TL3", state=TrafficLightState.YELLOW, intersection=intersection)

    # Ensure the initial state is correct
    assert traffic_light.state == TrafficLightState.YELLOW

    # Change the state to RED
    traffic_light.change_state(TrafficLightState.RED)
    assert traffic_light.state == TrafficLightState.RED

    # Change the state to GREEN
    traffic_light.change_state(TrafficLightState.GREEN)
    assert traffic_light.state == TrafficLightState.GREEN


def test_vehicle_creation():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = Vehicle(id="V1", type="Car", speed=60, current_route=[intersection1, intersection2])

    assert vehicle.id == "V1"
    assert vehicle.type == "Car"
    assert vehicle.speed == 60
    assert vehicle.current_route == [intersection1, intersection2]
    assert vehicle.current_position is None


def test_move_to_next_intersection():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = Vehicle(id="V2", type="Bus", speed=50, current_route=[intersection1, intersection2])

    # Move to the first intersection
    vehicle.move_to_next_intersection()
    assert vehicle.current_position == intersection1
    assert vehicle.current_route == [intersection2]

    # Move to the next (final) intersection
    vehicle.move_to_next_intersection()
    assert vehicle.current_position == intersection2
    assert vehicle.current_route == []


def test_has_reached_destination():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = Vehicle(id="V3", type="Truck", speed=40, current_route=[intersection1, intersection2])

    # Initially, the vehicle hasn't reached the destination
    assert not vehicle.has_reached_destination()

    # Move to the first intersection
    vehicle.move_to_next_intersection()
    assert not vehicle.has_reached_destination()

    # Move to the next (final) intersection
    vehicle.move_to_next_intersection()
    assert vehicle.has_reached_destination()


def test_vehicle_factory():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[intersection1, intersection2])

    assert isinstance(vehicle, Vehicle)
    assert vehicle.id == "V1"
    assert vehicle.type == "Car"
    assert vehicle.speed == 60
    assert vehicle.current_route == [intersection1, intersection2]
    assert vehicle.current_position is None


def test_vehicle_factory_with_position():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V2", type="Bus", speed=50, current_route=[intersection1, intersection2], current_position=intersection1)

    assert isinstance(vehicle, Vehicle)
    assert vehicle.id == "V2"
    assert vehicle.type == "Bus"
    assert vehicle.speed == 50
    assert vehicle.current_route == [intersection1, intersection2]
    assert vehicle.current_position == intersection1


def test_vehicle_factory_move_to_next_intersection():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V3", type="Truck", speed=40, current_route=[intersection1, intersection2])

    # Move to the first intersection
    vehicle.move_to_next_intersection()
    assert vehicle.current_position == intersection1
    assert vehicle.current_route == [intersection2]

    # Move to the next (final) intersection
    vehicle.move_to_next_intersection()
    assert vehicle.current_position == intersection2
    assert vehicle.current_route == []
    assert vehicle.has_reached_destination()


def test_add_vehicle():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[intersection1, intersection2])

    system = TrafficSystem(intersections={}, traffic_lights={}, vehicles={})
    system.add_vehicle(vehicle)

    assert "V1" in system.vehicles
    assert system.vehicles["V1"] == vehicle


def test_update_traffic_light():
    intersection = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    traffic_light = traffic_light_factory(id="TL1", state=TrafficLightState.RED, intersection=intersection)

    system = TrafficSystem(intersections={}, traffic_lights={"TL1": traffic_light}, vehicles={})

    # Update to YELLOW
    system.update_traffic_light("TL1", TrafficLightState.YELLOW)
    assert system.traffic_lights["TL1"].state == TrafficLightState.YELLOW


def test_move_vehicle():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    vehicle = vehicle_factory(id="V2", type="Bus", speed=50, current_route=[intersection1, intersection2])

    system = TrafficSystem(intersections={}, traffic_lights={}, vehicles={})
    system.add_vehicle(vehicle)

    # Move vehicle to the first intersection
    system.move_vehicle("V2")
    assert vehicle.current_position == intersection1
    assert vehicle.current_route == [intersection2]

    # Move vehicle to the next intersection
    system.move_vehicle("V2")
    assert vehicle.current_position == intersection2
    assert vehicle.current_route == []
    assert vehicle.has_reached_destination()


def test_traffic_system_factory():
    intersection1 = intersection_factory(id="I1", connected_roads=["R1", "R2"])
    intersection2 = intersection_factory(id="I2", connected_roads=["R2", "R3"])
    traffic_light = traffic_light_factory(id="TL1", state=TrafficLightState.RED, intersection=intersection1)
    vehicle = vehicle_factory(id="V1", type="Car", speed=60, current_route=[intersection1, intersection2])

    intersections = {"I1": intersection1, "I2": intersection2}
    traffic_lights = {"TL1": traffic_light}
    vehicles = {"V1": vehicle}

    system = traffic_system_factory(intersections, traffic_lights, vehicles)

    assert isinstance(system, TrafficSystem)
    assert system.intersections == intersections
    assert system.traffic_lights == traffic_lights
    assert system.vehicles == vehicles


def test_traffic_system_factory_empty():
    system = traffic_system_factory({}, {}, {})

    assert isinstance(system, TrafficSystem)
    assert system.intersections == {}
    assert system.traffic_lights == {}
    assert system.vehicles == {}
