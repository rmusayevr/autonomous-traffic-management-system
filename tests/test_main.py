from unittest.mock import patch

from src.pytemplate.domain.models import Intersection
from src.pytemplate.entrypoints.cli.main import get_intersection_input


def test_get_intersection_input():
    user_inputs = ["2", "A", "B, C", "B", "A, D"]

    with patch("builtins.input", side_effect=user_inputs):
        intersections = get_intersection_input()

    assert len(intersections) == 2
    assert isinstance(intersections["A"], Intersection)
    assert intersections["A"].connected_roads == ["B", "C"]
    assert intersections["B"].connected_roads == ["A", "D"]
