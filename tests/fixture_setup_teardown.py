

import pytest

@pytest.fixture
def yield_fixture():
   print('Start Test Phase') 
   yield 6 #this line and above is for set up, below this line is for tear down
   print('End Test Phase')

def test_example(yield_fixture):
   print('run-example-1')
   assert yield_fixture == 6