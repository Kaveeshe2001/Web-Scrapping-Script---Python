from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from datetime import datetime
import os
import sys

#get a path as executable
application_path = os.path.dirname(sys.executable)

now = datetime.now()
month_day_year = now.strftime("%m%d%Y")

website = "https://www.dailymirror.lk/"
path = "C:/Users/user/Downloads/chromedriver-win64/chromedriver.exe"

#headless-node
options = Options()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1080")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/143.0.0.0 Safari/537.36"
)

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

wait = WebDriverWait(driver, 20)
containers = wait.until(
    EC.presence_of_all_elements_located(
        (By.XPATH, '//div[@class="inner_rx_content"]')
    )
)

titles = []
links = []

for container in containers:
    title = container.find_element(by="xpath", value='./p').text
    link = container.find_element(by="xpath", value='.//p/a').get_attribute('href')
    titles.append(title)
    links.append(link)

mt_dict = {"title": titles, "link": links}
df = pd.DataFrame(mt_dict)

file_name = f"daily_mirror_headlines-{month_day_year}.csv"
final_path = os.path.join(application_path, file_name)
df.to_csv(final_path)

driver.quit()