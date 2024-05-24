from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
from datetime import datetime, timedelta
import json
import os

# Set up the Chrome WebDriver
service = Service(executable_path=r'C:\Users\This pc\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://app.snapp.taxi/?utm_source=website&utm_medium=webapp-button&utm_campaign=body')

try:
    input_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[aria-label='شمارهٔ موبایل']")))
    input_field.clear()
    input_field.send_keys('09207810554')
    
    svg_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and @color='primary']")))
    svg_element.click()

    time.sleep(60)

    prices = {}
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)

    while datetime.now() < end_time:
        current_time = datetime.now().strftime("%H:%M:%S")

        try:
            back_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='بازگشت']")))
            back_button.click()

            element_to_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-address-input_searchAddressInput__81I0O.css-1x3la9m.css-hbfmh2")))
            element_to_click.click()

            input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "css-1wf1gx2")))
            input_field.clear()
            input_field.send_keys('میرداماد، بلوار میرداماد تقاطع میدان مادر')

            # Adjust the XPath to match the given structure
            p_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//p[@class='css-11zm5fi' and contains(text(), 'میرداماد، میدان مادر تقاطع بلوار میرداماد')]")))
            #element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//p[text()="میرداماد، میدان مادر تقاطع بلوار میرداماد"]/preceding-sibling::p[@class="css-1y6dg5"]')))
            #distance = element.text
            
            #print (f' The distance of this way is equel to : {distance}')
            p_element.click()

            confirm_des = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[text()='تأیید مقصد']"))
            )
            confirm_des.click()

            price_span = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='css-1avyp1d css-1w8aat1']//span[@color='surface.high']"))
            )
            price_text = price_span.text
            price = ''.join(filter(str.isdigit, price_text))

            print(f'Time : {current_time} - Price : {price}')
            prices[current_time] = price

        except TimeoutException as e:
            print(f"TimeoutException at {current_time}: {e}")
        except NoSuchElementException as e:
            print(f"NoSuchElementException at {current_time}: {e}")
        except Exception as e:
            print(f"An error occurred at {current_time}: {e}")

        time.sleep(10)

finally:
    file_path = os.path.join(".", "snapp2.json")
    with open(file_path, "w") as json_file:
        json.dump(prices, json_file)
    print('File Saved !')
    #driver.quit()
