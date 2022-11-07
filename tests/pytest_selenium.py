import pytest
from django.test import LiveServerTestCase
from selenium import webdriver

# # Example 1, using selenium with pytest
# class TestBrowser1(LiveServerTestCase):
#     def test_example(self):
#         driver = webdriver.Chrome("chromedriver/chromedriver")
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title


# # Example 2, using selemium with pytest and headless mode
# class TestBrowser2(LiveServerTestCase):
#     def test_example(self):
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         driver = webdriver.Chrome(executable_path=r"chromedriver/chromedriver", options=options)
#         driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in driver.title

# # Example 3
# # Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome_driver = webdriver.Chrome(executable_path=r"chromedriver/chromedriver", options=options)
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()




#fix with params input allow us to params or multiple test cases
@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Chrome(executable_path=r"chromedriver/chromedriver", options=options)
    if request.param == "firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(executable_path=r"./geckodriver", options=options)
    request.cls.driver = web_driver
    yield
    web_driver.close()

"""

"""

# #test case with usefixtures
# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title
#test case with multiple driver 

"""
Note about TestClassName
    - TestClassName have to start with Test to run the test
"""
@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title