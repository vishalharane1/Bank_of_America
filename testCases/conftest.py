import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
chrome_option=Options()
chrome_option.add_argument("--headless")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        print("\n----> Lunching chrome browser")
        driver=webdriver.Chrome(service=service)
    elif browser=="edge":
        print("\n----> Lunching Edge browser")
        driver=webdriver.Edge()
    elif browser=="firefox":
        print("\n----> Lunching Firefox browser")
        driver=webdriver.Firefox()
    elif browser=="headless":
        print("\n----> Lunching headless chrome browser")
        driver=webdriver.Chrome(options=chrome_option)
    else:
        print("\n----> Lunching chrome browser")
        driver = webdriver.Chrome()
    driver.maximize_window()
    request.cls.driver=driver
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
