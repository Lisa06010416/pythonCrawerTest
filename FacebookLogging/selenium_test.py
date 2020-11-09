from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


options = Options()
# 設定封鎖彈出視窗
options.add_argument("--disable-notifications")
# 讓瀏覽器不顯示:chrom正在被控制
options.add_experimental_option("excludeSwitches", ['enable-automation'])
# 影藏可使化介面，linux系統下必須加
options.add_argument("--headless")

# 建立webdriver物件 ./chromedriver => chrom的驅動
chrome = webdriver.Chrome('../chromedriver', chrome_options=options)
# 使用chrome瀏覽器打開網站
chrome.get("https://www.facebook.com/")

# 尋找 填寫帳密的地方
email = chrome.find_element_by_id("email")
password = chrome.find_element_by_id("pass")

# 提交帳密
email.send_keys('yann0601@gmail.com')
password.send_keys('lisalin0416')
password.submit()

# 等程式載入
time.sleep(3)
# 前往粉絲專業
# chrome.get('https://www.facebook.com/learncodewithmike')

# 迴圈讓程式滾動頁面3次，每次暫停5秒載入資料
for x in range(1, 4):
    chrome.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)

# 將網頁內容抓下來，進行分析
soup = BeautifulSoup(chrome.page_source, 'html.parser')
titles = soup.find_all('span', {
    'class': 'a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7'})
for title in titles:
    print(title.getText())

chrome.quit()  # 關閉瀏覽器
