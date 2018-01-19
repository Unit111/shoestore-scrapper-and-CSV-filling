import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def setup_firefox():
    driver_path = os.path.dirname(os.path.realpath(__file__)).replace(r"\app", "\conf\geckodriver.exe")
    firefoxdriver = webdriver.Firefox(executable_path = driver_path)
    firefoxdriver.maximize_window()
    return firefoxdriver


driver = setup_firefox()
webDriverWaitInSeconds = 5


def open_main_page():
    shoes_url = "https://lojamelissa.com.br/mapping"
    driver.get(shoes_url)
    wait_for_exact_page(shoes_url)


def open_page(url):
    driver.get(url)
    wait_for_page(url)


###########
def wait_for_page(url):
    wait = WebDriverWait(driver, webDriverWaitInSeconds)
    wait.until(EC.url_contains(url))


def wait_for_exact_page(url):
    wait = WebDriverWait(driver, webDriverWaitInSeconds)
    wait.until(EC.url_matches(url))


def find_element(selector):
    element = WebDriverWait(driver, webDriverWaitInSeconds).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
    return element


def find_elements(selector):
    return driver.find_elements_by_css_selector(selector)


def find_elements_by_class(selector):
    return driver.find_elements_by_class_name(selector)