from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from wcag_checker.utils import get_webdriver

def check(url):
    driver = get_webdriver()
    try:
        driver.get(url)
        
        # すべての対話可能な要素を取得
        interactive_elements = driver.find_elements(By.CSS_SELECTOR, 'a, button, input, select, textarea')
        
        for element in interactive_elements:
            try:
                # 要素にフォーカスを当てる
                element.send_keys(Keys.TAB)
                
                # フォーカスが当たっているか確認
                focused_element = driver.switch_to.active_element
                if focused_element != element:
                    print(f"フォーカスの問題: 要素にフォーカスを当てることができません")
                    continue
                
                # エンターキーを押して操作を試みる
                focused_element.send_keys(Keys.ENTER)
                
                # 何らかの変化（ページ遷移やポップアップなど）が起きたか確認
                try:
                    WebDriverWait(driver, 3).until(EC.staleness_of(element))
                    return True
                except:
                    pass
                    
            except Exception as e:
                print(f"要素との対話中にエラーが発生: {str(e)}")
                continue
        
        return True
    except Exception as e:
        print(f"チェック実行中にエラーが発生: {str(e)}")
        return False
    finally:
        driver.quit()