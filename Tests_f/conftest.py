import pytest
from selenium import webdriver
import time
from Base.webdriverfactory import WebDriverFactory
from Pages.home.login_page import LoginPage

@pytest.yield_fixture()
def setUp():
    print("\n Running method level setUp")
    yield
    print("\n Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser, osType):
    print("\n Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login("adiel@newit.co.il", "abcabc")
    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(2)
    #driver.quit()
    print("\n Running one time tearDown")
    driver.close()

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")