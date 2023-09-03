from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
url = "https://twitter.com/search?q=%24tip&src=cashtag_click"
driver.get(url)

tm_div = driver.find_element(By.XPATH, '//div[@aria-label="时间线：搜索时间线"]')
tweet_elements = ttm_div.find_elements(By.CSS_SELECTOR, 'div[data-testid="cellInnerDiv"]')

for tweet in tweet_elements:
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, './/div[@data-testid="reply"]')))
        reply_button = tweet.find_element(By.XPATH, './/div[@data-testid="reply"]')
        reply_button.click()
        comment_text = "$tip @tipcoineth 感谢！冲冲冲"
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, './/div[@data-testid="tweetTextarea_0"]')))
        comment_box = driver.find_element(By.XPATH, './/div[@data-testid="tweetTextarea_0"]')
        comment_box.send_keys(comment_text)

      WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, './/div[@data-testid="tweetButton"]')))
        tweet_button = driver.find_element(By.XPATH, './/div[@data-testid="tweetButton"]')
        tweet_button.click()

    except Exception as e:
        print(f"Error: {e}")
        continue  
