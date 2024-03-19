from datetime import datetime
import subprocess
import time
import selenium
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

'''
don't load imgs or anything but words
'''

def getSelected():
    return subprocess.check_output(['xclip', '-selection', 'primary', '-o'])

def translate(content):
    content = str(content)
    content = content[:-1]
    content = content[::-1]
    content = content[:-1]
    content = content[:-1]
    content = content[::-1]
    ActionChains(driver).move_to_element(source_element).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    source_element.send_keys(Keys.BACKSPACE)
    source_element.send_keys(content)
    time.sleep(3)
    flg = 1
    while flg:
        try:
            dest_element = driver.find_element(By.CSS_SELECTOR, 'span.ryNqvb')
            print(dest_element.text)
            flg = 0
        except:
            print("oh no")
    

def main():
    last_content = ""
    while True:
        try:
            content = getSelected()
            print(content)
            last_time = datetime.now()
            if(content != last_content and len(content) != 0 and keyboard.is_pressed('ctrl+alt+e')''' here ''' ):
                translate(content)
                last_content = content
        except subprocess.CalledProcessError:
            pass

print(selenium.__version__)
chrome_path = '/usr/bin/google-chrome'
webdriver_path = '/usr/local/bin/chromedriver'
options = Options()
options.binary_location = chrome_path
service = Service(webdriver_path)
#options.add_argument("--headless")
print("shit")
driver = webdriver.Chrome(service = service, options = options)
print("driver started")
driver.get('https://translate.google.com/?sl=en&tl=fa&op=translate')
print("reached google!")
time.sleep(0.5)
source_element = driver.find_element(By.CSS_SELECTOR, 'textarea.er8xn')

if __name__ == "__main__":
    main()

driver.quit()
