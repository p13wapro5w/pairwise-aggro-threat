import pytest
import math
from gameplay import aggro_threat as mod

CASES = [
    ("heal", 'm.heal_threat(100, 0.5) == 50'),
    ("taunt", 'm.taunt_locked(3, 5) is True'),
    ("los", 'm.in_los(10, 45) is True'),
    ("death", 'm.clear_on_death(False) is True'),
    ("dot", 'm.dot_merge([1, 2, 3]) == 6'),
    ("pet", 'm.pet_owner("cat", "A") == "A"'),
    ("stack", 'm.taunt_stack(2, 3) == 5'),
    ("phase", 'm.phase_keep(100, 0.5) == approx(50.0)'),
    ("decay", 'm.decay(100, 0.1, 2) == approx(80.0)'),
    ("hardcut", 'm.in_hardcut(0.2, 0.5) is True'),
    ("add", 'm.add_threat(1, 2) == 3'),
    ("top", 'm.top_threat([1, 3, 2]) == 3'),
    ("range", 'm.range_ok(3, 5) is True'),
    ("key", 'm.aggro_key(3, 2) == "3:2"'),
    ("reset", 'm.reset_threat(9) == 0')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
