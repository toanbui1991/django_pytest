import pytest

# function  Run once per test
# class	    Run once per class of tests
# module	  Run once per module
# session	  Run once per session
"""
- parttern of tesing:
    - arrange (set up)
    - act (function run)
    - assert (check between result of function and expected)
- fixture is a concept which help us arrange (set up or tear down) to prepare resource or clean up which is common between test. This will reduce 
- fixture scope:
    - default fixture scope is function, which run every time a test function run
    - session will help fixture run one and used by many test function
"""

@pytest.fixture()
def fixture_1():
   print('run-fixture-1')
   return 1

def test_example1(fixture_1):
    print('run-example-1')
    num = fixture_1
    assert num == 1

def test_example2(fixture_1):
    print('run-example-2')
    num = fixture_1
    assert num == 1