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


# It is Hook  for adding environment info to HTML report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Swag E-commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sandro'
    config._metadata['PMO'] = 'Sandro'
    config._metadata['Build'] = 'App Version 1.0'


# It is Hook for Delete/Modify environment info to HTML Report

@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)