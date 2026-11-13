import pytest
import math
from project import calculate_column_buckling, simulate_dynamic_impact, calculate_bearing_stress

def test_calculate_column_buckling():
    p_critical = calculate_column_buckling(0.089, 2.44, "pine")
    assert abs(p_critical - 95343.6) < 1.0

    p_oak = calculate_column_buckling(0.089, 2.44, "oak")
    assert p_oak > p_critical

    with pytest.raises(ValueError):
        calculate_column_buckling(-0.089, 2.44, "pine")
    with pytest.raises(ValueError):
        calculate_column_buckling(0.089, 0, "pine")
    with pytest.raises(ValueError):
        calculate_column_buckling(0.089, 2.44, "fake_wood")


def test_simulate_dynamic_impact():
    total_force = simulate_dynamic_impact(113.398, 2.0, 0.02)
    assert abs(total_force - 12452.23) < 1.0

    static_force = simulate_dynamic_impact(113.398, 0.0, 0.02)
    assert abs(static_force - 1112.43) < 0.1

    with pytest.raises(ValueError):
        simulate_dynamic_impact(-10, 2.0)
    with pytest.raises(ValueError):
        simulate_dynamic_impact(113.398, -2.0)


def test_calculate_bearing_stress():
    stress = calculate_bearing_stress(6226.11, 0.0334, 0.089)
    assert abs(stress - 2094499.7) < 1.0

    with pytest.raises(ValueError):
        calculate_bearing_stress(0, 0.0334, 0.089)
    with pytest.raises(ValueError):
        calculate_bearing_stress(6226.11, -0.0334, 0.089)
