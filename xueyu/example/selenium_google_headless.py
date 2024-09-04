from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    service = ChromeService(executable_path="/Users/x/devTools/chromedriver-mac-arm64/chromedriver")

    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get("https://www.google.com")
    print(driver.page_source)
    driver.close()


if __name__ == '__main__':
    main()
