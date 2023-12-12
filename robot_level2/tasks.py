from RPA.Browser.Selenium import Selenium #buka browser
from RPA.Tables import Tables
from RPA.HTTP import HTTP #download excel
from RPA.PDF import PDF #export pdf
from RPA.Excel.Files import Files #baca file excel 
from RPA.Archive import Archive
from time import sleep #wait time
from RPA.FileSystem import FileSystem # untuk membuat directory
# from resources.variables import AZURE

import time
from robot.api import logger
import os

## bisa di set global seperti ini 
lib = Selenium()
lib_pdf = PDF()

def WriteLog(inMessage):
   logger.info("PY Log: " + str(inMessage))

def WriteConsole(inMessage):
   logger.console(str(inMessage))

# timeout_selenium           = int(os.getenv('timeout_selenium'))
# url="https://d-9367052e24.awsapps.com/start/#/saml/custom/162683562641%20%28pmi-app-robotics-prd%29/NjUyNTQ0NTIwNDIxX2lucy0wYzE1OGQ0ZTE4MjUzX3AtN2FiODg4ZjkyYTYxZjM1ZQ=="


def minimal_task():
    """
    Orders robots from RobotSpareBin Industries Inc.
    Saves the order HTML receipt as a PDF file.
    Saves the screenshot of the ordered robot.
    Embeds the screenshot of the robot to the PDF receipt.
    Creates ZIP archive of the receipts and the images.
    """
    # open_browser_instance()

def order_robots_from_RobotSpareBin():
   open_order_robot_website_2()
   download_csv()
   orders = get_orders()

   for row in orders:
    #    close_annoying_program()
       fill_the_form(row)
    #    fill_the_row_xpath(row)
       store_receipts_as_pdf(str(row["Order number"]))
    
   archive_receipts()

     
def open_order_robot_website():
    try:
        lib.open_browser("https://robotsparebinindustries.com/")
        sleep(5)
        lib.click_link('#/robot-order')
        sleep(5)
        lib.click_button('OK')
        print("Open Browser Success")
    except:
        print("Open Browser Failed")

def open_order_robot_website_2():
    try:
        lib.open_browser("https://robotsparebinindustries.com/#/robot-order")
        # lib.open_chrome_browser("https://robotsparebinindustries.com/#/robot-order")
        sleep(5)
        lib.click_button("OK")
        print("Open Browser Success")
    except Exception as e:
        print(f"Open Browser Failed {e}") 

def download_csv():
    try:
        http = HTTP()
        http.download("https://robotsparebinindustries.com/orders.csv", overwrite=True)
        sleep(10)
        print("Downloading excel file Success") 
    except:
        print("Downloading excel file failed") 

def get_orders():
    try:   
        lib2 = Tables()
        orders = lib2.read_table_from_csv("orders.csv", columns=["Order number", "Head", "Body", "Legs","Address"])
        print("Read CSV Success")
        return orders
    except:
        print("Read CSV Failed")

def close_annoying_program():
    try:
        lib.click_button("OK")
        print("close annoying success")
    except:
        print("close annoying failed")

def fill_the_form(row):
    try:
        lib.select_from_list_by_value('head', str(row["Head"]))
        sleep(5)
        lib.select_radio_button('body', str(row["Body"]))
        sleep(5)

        lib.find_element('address')
        lib.input_text('address', row["Address"])
        sleep(5)
        lib.find_element('class:form-control')
        lib.input_text("class:form-control", row["Legs"])
        # lib.input_text('xpath://input[@id="1698303255535"]', row["Legs"])
        sleep(5)
        # lib.input_text("class:form-control", str(row["Legs"]))
        # lib.input_text("1698223392997", row["Legs"])
        # sleep(10)

        locator_preview = 'xpath://button[@id="preview"]'
        lib.scroll_element_into_view(locator_preview)

        lib.click_button("preview")
        sleep(10)
        lib.click_button("order")

        # while(lib.get_selected_list_value("#receipt") is None):
        #     lib.click_button('order')
        
        # while not(lib.is_element_visible("receipt", missing_ok=True)):
        #     lib.click_button("order")

    except Exception as e:
        print(f"Fill the form failed {e}")

def fill_the_row_xpath(row):
    try:
        WriteConsole("Try fill the row")
        WriteLog("Try fill the row")
        lib.wait_until_element_is_visible(locator='//select[@id="head"]', timeout=30)
        lib.select_from_list_by_value('//select[@id="head"]', str(row["Head"]))
        WriteLog("Finish 1. Fill head")
        WriteConsole("Finish 1. Fill head")
        sleep(5)

        lib.wait_until_element_is_visible(locator='//div[contains(@class, "stacked")]', timeout=30)
        lib.select_radio_button('body', str(row["Body"]))
        WriteLog("Finish 2. Fill body")
        WriteConsole("Finish 2. Fill Body")
        sleep(5)

        # lib.scroll_element_into_view(locator='class:form-control')
        # lib.wait_until_element_is_visible(locator='xpath://div[@class="mb-3"]/input[contains(@id, "1698303255535")]', timeout=30)
        try:
            lib.wait_until_element_is_visible(locator='//div[@class="mb-3"]/input[@class="form-control"]', timeout=30)
            lib.input_text('class:form-control', row["Legs"])
            lib.input_text('class:form-control', row["Legs"])
            WriteLog("Finish 3. Fill Legs")
            WriteConsole("Finish 3. Fill Legs")
            sleep(5)

        except:
            lib.wait_until_element_is_visible(locator='class:form-control', timeout=30)
            lib.input_text('class:form-control', row["Legs"])
            WriteLog("Finish 3. Fill Legs")
            WriteConsole("Finish 3. Fill Legs")
            sleep(5)
        
        try:
            lib.input_text('address', row["Address"])
            sleep(3)
            WriteLog("Finish 3. Fill Legs")
            WriteConsole("Finish 3. Fill Legs")
        except:
            lib.input_text('address', row["Address"])
            sleep(3)
            WriteLog("Finish 4. Fill Address")
            WriteConsole("Finish 4. Fill Address")
 
        try:
            lib.wait_until_element_is_visible('//button[@id="preview"]')
            lib.click_button("preview")
            sleep(10)
            lib.click_button("order")
        # locator_preview = 'xpath://button[@id="preview"]'
        # lib.scroll_element_into_view(locator_preview)
        except:
            lib.click_button("preview")
            sleep(10)
            lib.click_button("order")

    except:
        print("failed fill the row")

def screenshot_robot(order_number):
    lib.screenshot(locator="robot-preview-image", filename="output/receipts/"+order_number+".png")

def store_receipts_as_pdf(order_num):
    receipt_html = lib.get_element_attribute(locator="receipt", attribute='innerHTML')
    sleep(10)
    lib_pdf = PDF()
    libsystem = FileSystem()
    libsystem.create_directory("output/receipts")
    pdf_path = "output/receipts/order_"+order_num+".pdf"
    sleep(10)
    lib_pdf.html_to_pdf(receipt_html, pdf_path) 

    screenshot_robot(order_num)

    embed_screenshot_to_receipt("output/receipts/"+order_num+".png", pdf_path)
    
    lib.click_button("order-another")
    lib.click_button("OK")
    sleep(10)

def embed_screenshot_to_receipt(screenshot, pdf_file):
    list_of_files = [
        screenshot + ':align=center'
    ]

    lib_pdf.open_pdf(pdf_file)
    lib_pdf.add_files_to_pdf(files=list_of_files,target_document=pdf_file,append=True)
    lib_pdf.save_pdf(output_path=pdf_file)
    lib_pdf.close_all_pdfs()

def archive_receipts():
    lib_archive = Archive()
    lib_archive.archive_folder_with_zip("output/receipts", "receipts.zip")

# def open_browser_instance():
#     try:
#         lib.open_available_browser(
#             url=url, browser_selection = "Edge", maximized = True
#         )
#         WriteConsole("Open Browser Instance Success")
#         WriteLog("Open Browser Instance Success")
#     except Exception as e:
#         WriteConsole(f"Failed to open browser Intance : {e}")
#         WriteLog(f"Failed to open browser Intance : {e}") 

#     # If Azure AD Popup
#     try:
#         AZURE.azure_login()
#     except Exception as error:
#         WriteLog(f"Azure AD does not appear with message {error}")
#         WriteConsole(f"Azure AD does not appear")
