from msedge.selenium_tools import Edge, EdgeOptions
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import string
import random
import time
import logging
import traceback

# Launch Microsoft Edge (Chromium)
edge_options = EdgeOptions()
edge_options.use_chromium = True
# Optinal option
# edge_options.add_argument('headless')
# edge_options.add_argument('log-level=3')
# edge_options.add_argument('disable-gpu')
driver = Edge(EdgeChromiumDriverManager().install(), options=edge_options)

# Wait(er)
wait = WebDriverWait(driver, 10)

# Base URL
url = ''

for i in range(0,10):
    try:
        # Go to URL
        driver.get(url)
    except Exception as e:
        traceback.print_exc()
        logging.error('Error : ' + str(e))