from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
import time
import random

class LinkedInBot:
    def __init__(self, service_path):
        chrome_options = Options()
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')
        chrome_options.add_argument('--disable-web-security')
        chrome_options.add_argument('--allow-running-insecure-content')
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument("user-data-dir=C:\\Users\\2004r\\AppData\\Local\\Google\\Chrome\\User Data\\Default")

        self.service = Service(executable_path=service_path)
        self.driver = webdriver.Chrome(service=self.service, options=chrome_options)

    def open_linked(self):
        self.driver.get('https://linkedin.com')
        time.sleep(random.uniform(2, 4))  # Simulate human-like delays
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        print("LinkedIn homepage opened.")

    def login(self):
        try:
            login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/nav/div/a[2]'))
            )
            time.sleep(random.uniform(1, 3)) 
            login.click()
            print("Login button clicked.")
        except Exception as e:
            print(f"Error locating the Log In button: {e}")
    def existing(self):

        try:
            login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div/div[3]/div/div/div[1]/div[1]'))
            )
            time.sleep(random.uniform(1, 3)) 
            login.click()
            print("Login button clicked.")
        except Exception as e:
            print(f"Error locating the Log In button: {e}")
    def postlogin(self):
        self.driver.execute_script("windows.scrollby")
        try:

            self.driver.get('https://www.linkedin.com/in/tarun-rao-97529b33b/')
            time.sleep(3)
            name=self.driver.find_element((By.CSS_SELECTOR,'.text-heading-xlarge')).text
            print(f"Name:{name}")
        except Exception as e:
            print(f"Error occured {e} ")
    def like(self):
        try:
            # Primary strategy based on the successful previous approach
            like_strategy = "//button[contains(@class, 'social-actions-button')]"
            
            # Scroll to ensure element is in view
            self.driver.execute_script("window.scrollBy(0, 300);")
            time.sleep(random.uniform(1.5, 3))
            
            try:
                # Wait for element to be clickable
                like_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, like_strategy))
                )
                
                # Use JavaScript click to bypass potential overlay issues
                self.driver.execute_script("arguments[0].click();", like_button)
                print(f"Like button clicked using strategy: {like_strategy}")
                return
            
            except Exception as e:
                print(f"Failed to click like button: {e}")
                
                # Take screenshot for debugging
        
        except Exception as e:
            print(f"Comprehensive error in like method: {e}")


       







    def close_browser(self):
        self.driver.quit()
        print("Browser closed.")


# Main Execution
if __name__ == "__main__":
    bot = LinkedInBot(service_path="chromedriver.exe")

    try:
        bot.open_linked()
        bot.like()
        # bot.login()
        # bot.existing()
        # bot.postlogin()
        


        input("Complete the account creation process and press Enter to close the browser...")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        bot.close_browser()


# ".social-actions button",