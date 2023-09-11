# # import pywhatkit
# # card_path = "D:\Sakshi\weddinginvitation\input\short_invitation.pdf"

# # # syntax: phone number with country code, message, hour and minutes
# # pywhatkit.sendwhats_image('+919462556397', card_path, "Choudhary Invitation")

 



import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Sender:
    def __init__(self):
        # import pdb; pdb.set_trace()
        # Specify the path to your chromedriver executable
        chromedriver_path = r'C:\Users\wfh\Downloads\chromedriver_win32\chromedriver.exe'

        # Specify the path to the PDF file you want to send
        # pdf_file_path = r'D:\Sakshi\weddinginvitation\input\short_invitation.pdf'

        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(chromedriver_path)
        self.driver.get('https://web.whatsapp.com')

        # Wait for the user to scan the QR code to log in
        input('Press Enter after scanning the QR code')

    def send(self, contact_name, pdf_file_path):
        time.sleep(2)
        # Replace 'contact_name' with the name of the WhatsApp contact or group you want to send the PDF to
        # Locate the search input and enter the contact name
        search_input_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, search_input_xpath)))
        search_input.send_keys(contact_name)
        time.sleep(2)

        search_input.send_keys(Keys.ENTER)

        # Wait for the chat to load
        time.sleep(5)

        # Locate the attachment button and click on it
        attachment_button_xpath = '//div[@title="Attach"][@role="button"]'
        attachment_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, attachment_button_xpath)))
        attachment_button.click()

        # Locate the file attachment option and click on it
        file_attachment_option_xpath = '//input[@accept="*"]'
        file_attachment_option = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, file_attachment_option_xpath)))
        file_attachment_option.send_keys(pdf_file_path)

        # Wait for the file to be uploaded
        time.sleep(5)

        # Locate the send button and click on it
        send_button_xpath = '//span[@data-icon="send"]'
        send_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, send_button_xpath)))
        send_button.click()

        # Wait for the message to be sent
        time.sleep(15)

        # Close the browser
        # self.driver.quit()
