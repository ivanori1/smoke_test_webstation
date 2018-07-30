import pytest
from selenium import webdriver

baseURL = "http://webstationtest3.ttweb.net/WebStation.aspx"


@pytest.fixture(scope="class")
def one_time_setup(request, browser):
    if browser == "firefox":
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        print("Running test on Firefox")
    else:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseURL)
        print("Running test on Chrome")

    if request.cls is not None:
        request.cls.driver = driver
    yield driver


def pytest_addoption(parser):
    parser.addoption("--browser", help="choose firefox or chrome")


@pytest.fixture(scope="session")
def browser(request):
    return request.congig.getoption("--browser")
