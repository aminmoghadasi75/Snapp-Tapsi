from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime , timedelta
import json
import os

service = Service(executable_path=r'C:\Users\This pc\Desktop\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://app.tapsi.cab/?_gl=1*1yb6lc*_ga*MjExNDU1OTQ4My4xNzE0NjU4MDk4*_ga_0F24611KVS*MTcxNDY1ODA5Ny4xLjAuMTcxNDY1ODA5Ny42MC4wLjA.')

input_num = driver.find_element(By.ID, "exampleField")
input_num.send_keys('09017295436')

# Wait until the button becomes clickable
button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'BottomButton-container')))
button = driver.find_element(By.CLASS_NAME, 'BottomButton-container')  # Refresh the element

# Click the button
button.click()

# Input code
code = input('Give me the code : ')
for i in range(min(len(code), 5)):
    digit_input = driver.find_element(By.NAME, f"digit-input-{i}") 
    digit_input.clear()
    digit_input.send_keys(code[i])

# Wait until the image element is present
image_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img.service-card__img[src*='ride-request.png']")))
image_element = driver.find_element(By.CSS_SELECTOR,"img.service-card__img[src*='ride-request.png']")
image_element.click()

# Wait until the origin selection button is present and clickable
try :
    time.sleep(5)
    button_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, ".//span[@class='button__label' and text()='انتخاب مبدا']")))
    button_element = driver.find_element(By.XPATH,".//span[@class='button__label' and text()='انتخاب مبدا']")
    button_element.click()
    # Fill in the origin
    input_origin = driver.find_element(By.ID,"origin-input")
    input_origin.clear()
    input_origin.send_keys("ایستگاه مترو استاد معین")

    # Click on the origin option
    origin_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='ایستگاه مترو استاد معین']]")))

    origin_option = driver.find_element(By.XPATH,"//div[@class='text' and .//*[contains(@class,'title') and text()='ایستگاه مترو استاد معین']]")
    origin_option.click()

    confirm_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='BottomButton-text' and text()='تایید مبدأ']")))

    # Click on the "تایید مبدأ" button
    confirm_button.click()

    # Fill in the destination
    destination_input = driver.find_element(By.ID, "destination-input")
    destination_input.clear()
    destination_input.send_keys("میدان مادر")

    # Click on the destination option
    destination_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='م. مادر']]")))

    destination_option = driver.find_element(By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='م. مادر']]")
    destination_option.click()
    time.sleep(5)
    destination_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='BottomButton-text' and text()='ثبت مقصد']")))

    # Click on the "ثبت مقصد" button
    destination_button.click()
    # Initialize empty dictionary to store prices
    data = {}
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)
    while datetime.now() < end_time:
        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")
        try :
            price_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ride-preview-card__price__primary__price")))
            price = price_element.text
            
            end_time_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='text-base' and contains(text(), 'پایان سفر:')]")))
            end_time_text = end_time_element.text.split('پایان سفر: ')[1]

            print(f'Time : {current_time} - Price : {price} - End Time: {end_time_text}')
            data[current_time] = {'price': price, 'end_time': end_time_text}
            print(f'Time : {current_time} - Price : {price}')
        except InterruptedError :
            break
        except :
            continue

        # Wait for 30 sec
        time.sleep(30)

except :
    address_label = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='AddressLabel-container']")))

    # Click on the "AddressLabel-container" element
    address_label.click()

    # Fill in the origin
    input_origin = driver.find_element(By.ID,"origin-input")
    input_origin.clear()
    input_origin.send_keys("ایستگاه مترو استاد معین")

    # Click on the origin option
    origin_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='ایستگاه مترو استاد معین']]")))

    origin_option = driver.find_element(By.XPATH,"//div[@class='text' and .//*[contains(@class,'title') and text()='ایستگاه مترو استاد معین']]")
    origin_option.click()

    confirm_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='BottomButton-text' and text()='ثبت مبدأ']")))

    # Click on the "تایید مبدأ" button
    confirm_button.click()
    # Wait for the "ایستگاه مترو استاد معین" element to become clickable
    metro_station = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[@class='AddressLabel-text' and text()='ایستگاه مترو استاد معین']")))

    # Click on the "ایستگاه مترو استاد معین" element
    metro_station.click()

    # Fill in the destination
    destination_input = driver.find_element(By.ID, "origin-input")
    destination_input.clear()
    destination_input.send_keys("میدان مادر")

    # Click on the destination option
    destination_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='م. مادر']]")))

    destination_option = driver.find_element(By.XPATH, "//div[@class='text' and .//*[contains(@class,'title') and text()='م. مادر']]")
    destination_option.click()
    time.sleep(5)
    destination_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='BottomButton-text' and text()='ثبت مقصد']")))

    # Click on the "ثبت مقصد" button
    destination_button.click()
    # Initialize empty dictionary to store prices
    data = {}
    start_time = datetime.now()
    end_time = start_time + timedelta(hours=24)
    while datetime.now() < end_time:
        # Get current time
        current_time = datetime.now().strftime("%H:%M:%S")
        try :
            price_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "ride-preview-card__price__primary__price")))
            price = price_element.text

            end_time_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='text-base' and contains(text(), 'پایان سفر:')]")))
            end_time_text = end_time_element.text.split('پایان سفر: ')[1]

            print(f'Time : {current_time} - Price : {price} - End Time: {end_time_text}')
            data[current_time] = {'price': price, 'end_time': end_time_text}

            # Wait for 30 sec
            time.sleep(30)
        except InterruptedError :
            break
        except :
            continue
finally:
    file_path = os.path.join(".", "tapsi4.json")
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
        print('File Saved !')

    driver.quit()
        
        
        

