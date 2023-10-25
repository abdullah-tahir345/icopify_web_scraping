import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# create a file
with open('web_scrape_sample.csv', 'w', encoding='utf-8') as file:
    file.write(
        "webpage_address;categories;traffic;ahref;mozda;spam_score;language;buy_post \n")


class Browser:

    def __init__(self):
        self.browser = webdriver.Chrome()

    def get_url(self, url):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def find_element_for_operations(self, xpath):
        button = self.browser.find_element(By.XPATH, value=xpath)
        button.click()

    # Login the specific
    def login_page(self, username, password):
        self.browser.find_element(
            By.XPATH, '//*[@id="Email"]').send_keys(username)
        self.browser.find_element(
            By.XPATH, '//*[@id="password"]').send_keys(password)
        self.browser.find_element(
            By.XPATH, '//*[@id="top"]/div[2]/div/div/div/div/div/div[2]/div/form/div[4]/button').click()

    # find data using the find elements
    def find_data_(self):
        webpage_address = self.browser.find_elements(
            By.XPATH, "//a[@data-toggle='popover']")
        categories = self.browser.find_elements(By.XPATH, "//tbody/tr/td[2]")
        traffic = self.browser.find_elements(By.XPATH, "//tbody/tr/td[3]/span")
        ahref = self.browser.find_elements(By.XPATH, "//tbody/tr/td[4]/strong")
        mozda = self.browser.find_elements(
            By.XPATH, "//tbody/tr/td[5]/strong[@class=' font-weight-bold']")
        spam_score = self.browser.find_elements(
            By.XPATH, "//tbody/tr/td[5]/strong[@class='text-facebook font-weight-bold']")
        language = self.browser.find_elements(By.XPATH, "//tbody/tr/td[6]")
        buy_post = self.browser.find_elements(
            By.XPATH, "//a[@class='btn bg-primary text-white']")
        return webpage_address, categories, traffic, ahref, mozda, spam_score, language, buy_post


if __name__ == '__main__':
    browser = Browser()

    # Get specific url
    browser.get_url('https://icopify.co/login')
    time.sleep(1)

    # pass keys to the specific places like username and password
    browser.login_page(#Username, #Password)
    time.sleep(1)

    # find element and click on that element
    browser.find_element_for_operations(
        '//*[@id="navbarVerticalCollapse"]/div/ul/li[3]/a/div/span[2]')
    time.sleep(1)

    browser.find_element_for_operations(
        '//*[@id="Aamir-9079"]/li[1]/a/div/span[2]')
    time.sleep(1)

    # data collection
    for k in range(3):
        webpage_address, categories, traffic, ahref, mozda, spam_score, language, buy_post = browser.find_data_()

        with open('web_scrape_sample.csv', 'a', encoding='utf-8') as file:
            for i in range(len(webpage_address)):
                file.write(webpage_address[i].text + ";" + categories[i].text + ";" + traffic[i].text + ";" + ahref[i].text +";" + mozda[i].text + ";" + spam_score[i].text + ";" + language[i].text + ";" + buy_post[i].text + "\n")
        browser.find_element_for_operations("//a[@aria-label='Next »']")

    # close the browser
    browser.close_browser()
