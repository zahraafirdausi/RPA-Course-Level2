import os
import time

from RPA.Browser.Selenium import Selenium
from robot.api import logger
from selenium.webdriver.edge.options import Options as Edge_Options

seleniumLib = Selenium()
EdgeOptions = Edge_Options()
username = "rswara"
password = "Berc@1234"

timeout_selenium = int(os.getenv('timeout_selenium'))
long_timeout_selenium = int(os.getenv('long_timeout_selenium'))

def WriteLog(inMessage):
   logger.info("PY Log: " + str(inMessage))

def WriteConsole(inMessage):
   logger.console(str(inMessage))

class AZURE:
    def azure_login():
        WriteConsole("Try Azure AD Login page")
        WriteLog("Try Azure AD Login page")
        # Step Azure AD 1 - Wait until Email Text Input Visible and input username
        seleniumLib.wait_until_element_is_visible(locator='name:loginfmt', timeout=timeout_selenium)
        seleniumLib.input_text(locator='name:loginfmt', text=username + '@pmintl.net')
        WriteLog("Finish Input Text Azure AD 1")
        # Step Azure AD 2 - Click Next Button
        seleniumLib.wait_until_element_is_visible(locator='id:idSIButton9', timeout=timeout_selenium)
        seleniumLib.click_button(locator='id:idSIButton9')
        WriteLog("Finish Click Button Azure AD 2")
        # Step Azure AD 3 - Wait until Password Text Input Visible
        seleniumLib.wait_until_element_is_visible(locator='name:passwd', timeout=timeout_selenium)
        seleniumLib.input_password(locator='name:passwd',password=password)
        WriteLog("Finish Input Text Azure AD 3")
        # Step Azure AD 4 - Click Sign In Button
        seleniumLib.wait_until_element_is_visible(locator='id:idSIButton9', timeout=timeout_selenium)
        seleniumLib.click_button(locator='id:idSIButton9')
        WriteLog("Finish Click Button Azure AD 4")
        # Step Azure AD 5 - Wait until Remember Sign In "No" Button is Visible
        try:
            seleniumLib.wait_until_element_is_visible(locator='id:idBtn_Back', timeout=timeout_selenium)
            seleniumLib.click_button(locator='id:idBtn_Back')
            WriteLog("Finish Click Button Azure AD 5")
        except Exception as error:
            WriteLog(f"Remember Sign in not appear with message {error}")  
