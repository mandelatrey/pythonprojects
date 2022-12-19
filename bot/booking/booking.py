import selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time
import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


class Booking(webdriver.Chrome):
    def __int__(self, driver_path=r"/Users/trev/selenium driver/chromedriver"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()


    def __exit__(self, exc_type, exc_val, exc_tb):
        while True:
            user_input = input("Enter something (or press Enter to exit): ")
            if user_input == "":
                break
        print("You entered:", user_input)

    print("Getting Deals")

    def land_first_page(self):
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        self.get(const.BASE_URL)

    def unlock_screen(self):
        screen_height = self.execute_script("return window.screen.height;")
        get_button = self.find_element(By.XPATH, '//*[@id="pop"]/div/section/button')
        waiter = WebDriverWait(self, 10).until(EC.element_to_be_clickable(get_button))
        waiter.click()
        time.sleep(4)  # Delay the time SO the page opens properly
        self.execute_script("window.scrollBy(0,1000)","")

    def get_sales(self):
        title = self.find_element(By.XPATH, '//*[@id="jm"]/main/div[1]/div[4]/section/header/div[1]/h2')
        print(title.text)

    # while True:
    #     self.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height.values(), i=1))
    #     i += 1
    #     time.sleep(scroll_pause_time)
    #     scroll_height = self.execute_script("return document.body.scrollHeight;")
    #     # articles = self.find_elements(By.CLASS_NAME, 'col-sm-6 col-md-4 col')
    #     headline = self.find_elements(By.TAG_NAME, 'h3')
    #     link = self.find_elements(By.LINK_TEXT, 'link color')
    #     details = self.find_element(By.XPATH, "//a[1]")
    #
    #     articles = f"{headline}, {details.text}, {link}"
    #     for article in articles:
    #         print(article.text)
    def get_deals(self):
        deals = self.find_elements(By.CLASS_NAME, 'name')
        for deal in deals:
            print(deal.text)

            # html = self.find_element(By.TAG_NAME, 'html')
            # html.send_keys(Keys.END)
            # #
            # # clicker_epaper = self.find_element(By.LINK_TEXT, 'Archives')
