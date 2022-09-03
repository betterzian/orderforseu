from multiprocessing.util import is_exiting
from selenium import webdriver
import time
import datetime
import userdata
import random

order_time = str(datetime.date.today())

script = 'Object.defineProperty(navigator,"webdriver",{get:() => undefined,});'
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('window-size=1920x3000')
option.add_experimental_option("detach", True)
option.add_experimental_option('useAutomationExtension', False)
option.add_experimental_option('excludeSwitches', ['enable-automation'])

browser = webdriver.Chrome(options=option)
browser.execute_script(script)

#自动请假
browser.get("http://ehall.seu.edu.cn/appShow?appId=5869188708264821")
browser.find_element_by_id("username").send_keys(userdata.username)
browser.find_element_by_id("password").send_keys(userdata.password)
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//*[@id='casLoginForm']/p[5]/button").click()
time.sleep(10)
try:
    browser.find_element_by_link_text("销假").click()
    time.sleep(random.uniform(0.5,1.5))
    browser.find_element_by_link_text("确认").click()
    time.sleep(random.uniform(0.5,1.5))
except:
    time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_link_text("我要请假").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_id("CheckCns").click()
browser.find_element_by_xpath("//*[@id='buttons']/button").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@data-name='DZQJSY']/div/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@class='bh-paper-pile-dialog single ']/following-sibling::div[2]/div/div/div/div[2]/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@data-name='QJXZ']/div/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@class='bh-paper-pile-dialog single ']/following-sibling::div[3]/div/div/div/div[2]/div/div[2]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@data-name='QJKSRQ']/input").send_keys(order_time+" "+userdata.start_time)
browser.find_element_by_xpath("//div[@data-name='QJJSRQ']/input").send_keys(order_time+" "+userdata.end_time)
browser.find_element_by_xpath("//*[@id='add-form-qjxx']/div/div[1]/div[2]/div[11]/div[1]/div/div/div/textarea").send_keys("健身")
browser.find_element_by_xpath("//div[@data-name='HDXQ']/div/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@class='bh-paper-pile-dialog single ']/following-sibling::div[8]/div/div/div/div[2]/div/div[1]/div").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@data-name='HDXQ']/div/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//input[@data-name='XXDZ']").send_keys("拿铁健身")
time.sleep(2)
browser.find_element_by_xpath("//div[@data-name='DZSFLN']/div/div/div[1]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@class='bh-paper-pile-dialog single ']/following-sibling::div[9]/div/div/div/div[2]/div/div[3]").click()
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//a[@data-action='请假保存']").click()
time.sleep(random.uniform(0.5,1.5))
#自动申报
browser.get("http://ehall.seu.edu.cn/appShow?appId=5821102911870447")
browser.find_element_by_xpath("//div[@data-action='add']").click()
time.sleep(random.uniform(0.5,1.5))
temp = random.randint(5,9)
browser.find_element_by_xpath("//input[@data-name='DZ_JSDTCJTW']").send_keys("36."+str(temp))
time.sleep(random.uniform(0.5,1.5))
browser.find_element_by_xpath("//div[@data-action='save']").click()
time.sleep(random.uniform(0.5,1.5))

browser.close()
