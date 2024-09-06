from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def check(url):
    driver = webdriver.Chrome()
    try:
        driver.get(url)
        
        # すべての対話可能な要素を取得
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for element in interactive_elements:
            # 要素にフォーカスを当てる
            element.send_keys(Keys.TAB)
            
            # 1秒待機してからエンターキーを押す
            time.sleep(1)
            element.send_keys(Keys.ENTER)
            
            # さらに1秒待機
            time.sleep(1)
            
            # 操作が成功したか確認（この部分は実際のウェブサイトの挙動に応じて調整が必要）
            # ここでは単純に、エラーメッセージが表示されていないかをチェック
            error_messages = driver.find_elements(By.CSS_SELECTOR, '.error-message')
            if error_messages:
                return False
        
        return True
    finally:
        driver.quit()