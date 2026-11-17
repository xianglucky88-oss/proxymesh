import pytest

def test_sticky_is_open_gap():
    from src.proxymesh import sticky
    with pytest.raises(NotImplementedError):
        sticky.process({"id": "x"})

def test_geo_policy_is_open_gap():
    from src.proxymesh import geo_policy
    with pytest.raises(NotImplementedError):
        geo_policy.process({"id": "x"})
