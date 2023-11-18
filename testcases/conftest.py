import pytest
from selenium import webdriver
from PageObject.credentials import url


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Edge()
    driver.get(url)
    driver.implicitly_wait(10)
    driver.maximize_window()

    request.cls.driver = driver
    yield driver


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)