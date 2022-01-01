from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    driver = webdriver.Chrome("C:/old lap/Bharath/2021/Learn Python/Selenium/chromedriver_win32/chromedriver.exe")
    return driver

#     if browser=='chrome':
#         driver = webdriver.Chrome("C:/old lap/Bharath/2021/Learn Python/Selenium/chromedriver_win32/chromedriver.exe")
#         print("Chrome...............")
#     elif browser=='firefox':
#         driver = webdriver.Firefox("C:/old lap/Bharath/2021/Learn Python/Selenium/firefox/geckodriver.exe")
#         print("Firefox.............")
#     else:
#         driver = webdriver.Chrome("C:/old lap/Bharath/2021/Learn Python/Selenium/chromedriver_win32/chromedriver.exe")
#     return driver
#
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# def pytest_configure(config):
#     config._metadata['Project Name'] ='nop Commerce'
#     config._metadata['Module Name'] ='Customers'
#     config._metadata['Tester'] ='Bharath'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
