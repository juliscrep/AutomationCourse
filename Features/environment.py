
from selenium import webdriver
import allure_behave


def before_all(context):
    context.driver = webdriver.Chrome()


def after_all(context):
    context.driver.quit()
