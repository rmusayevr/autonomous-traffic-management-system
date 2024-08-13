from unittest.mock import patch

import pytest

from pytemplate.domain.events import TrafficLightChanged, VehicleEnteredIntersection
from pytemplate.domain.models import TrafficLightState
from src.pytemplate.service.dispatcher import EventDispatcher


def test_dispatch_vehicle_entered_intersection():
    dispatcher = EventDispatcher()
    event = VehicleEnteredIntersection(vehicle_id="V123", intersection_id="I456")

    with patch("builtins.print") as mocked_print:
        dispatcher.dispatch(event)
        mocked_print.assert_called_once_with("Vehicle V123 entered intersection I456.")


def test_dispatch_traffic_light_changed():
    dispatcher = EventDispatcher()
    event = TrafficLightChanged(light_id="TL123", new_state=TrafficLightState.GREEN)

    with patch("builtins.print") as mocked_print:
        dispatcher.dispatch(event)
        mocked_print.assert_called_once_with("Traffic light TL123 changed to GREEN.")


def test_dispatch_unhandled_event():
    dispatcher = EventDispatcher()

    with pytest.raises(ValueError):
        dispatcher.dispatch("SomeUnsupportedEvent")
