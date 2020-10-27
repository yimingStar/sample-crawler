from .logger import logger

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import time
import os
import traceback
import random

CHROME_LOCAL_DRIVER_PATH = './chromedriver'
def set_chrome_driver():
    """set up chrome driver by local driver's file or selenium container"""
    try:
        driver = webdriver.Chrome(CHROME_LOCAL_DRIVER_PATH)
        if not driver:
            return None
        return driver
    except Exception as e:
        logger.exception(f'set chrome driver failed, {e}')

def get_cookie(driver):
    """get driver's cookie"""
    if not driver:
        return
    cookies_list = driver.get_cookies()   
    return cookies_list