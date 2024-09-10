from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def main():
    "zhushi"

    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    service = ChromeService(executable_path="/Users/zhanggong/devTools/chromedriver-mac-arm64/chromedriver")

    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get("https://www.bilibli.com")

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)  # 设置最长等待时间为 10 秒

    # 等待输入框和按钮可以操作
    input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner_link > div > div > form > input")))
    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="banner_link"]/div/div/form/button')))

    # 接下来可以执行其他操作
    # 例如查找元素并输入文本
    input.send_keys("蔡徐坤 篮球")
    submit.click()

    print(driver.page_source)


if __name__ == '__main__':
    main(__doc__)
