import pytest

@pytest.mark.xfail
def test_example():

    assert 1 == 1

@pytest.mark.slow
def test_example_one():

    assert 1 == 1

def test_example_wrong():

    assert 1 == 2