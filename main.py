from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Directory for saving session
profile_dir = "./whatsapp_profile"

# Chrome options set karna
options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={os.path.abspath(profile_dir)}")

# Chrome driver ko start karna with the profile directory
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('https://web.whatsapp.com')

# Agar pehli baar run kar rahe hain, to QR code scan karein
input("Press Enter after scanning QR code and WhatsApp Web is loaded completely")

# Phone number aur message define karna
phone_number = '+9998887777'
message = 'Happy Birthday Bhai'

# Contact ko search aur select karne ka function
def search_contact(phone_number):
    try:
        print("Searching for contact input box...")
        search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
        search_box.click()
        search_box.send_keys(phone_number)
        search_box.send_keys(Keys.ENTER)
        print(f"Contact {phone_number} selected.")
        time.sleep(2)
    except Exception as e:
        print(f"Error in search_contact: {e}")

# Message send karne ka function
def send_message(message):
    try:
        print("Sending message...")
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="6"]')
        message_box.click()
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        print("Message sent.")
        time.sleep(1)
    except Exception as e:
        print(f"Error in send_message: {e}")

# Contact search aur 5001 baar message bhejne ka loop
search_contact(phone_number)
for i in range(501):
    print(f"Sending message {i+1} of 501")
    send_message(message)

# Browser ko band na karein taaki session active rahe
# driver.quit()
