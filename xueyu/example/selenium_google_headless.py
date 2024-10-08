from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')

    service = ChromeService(executable_path="/Users/zhanggong/devTools/chromedriver-mac-arm64/chromedriver")

    driver = webdriver.Chrome(options=chrome_options, service=service)
    driver.get("https://www.google.com")

    # 等待页面加载完成
    wait = WebDriverWait(driver, 10)  # 设置最长等待时间为 10 秒
    wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))

    # 接下来可以执行其他操作
    # 例如查找元素并输入文本
    input = driver.find_element(By.ID, 'APjFqb')
    input.send_keys("canglaoshi")

    # 查找搜索按钮并点击
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
    button.click()

    print(driver.page_source)


if __name__ == '__main__':
    main()
