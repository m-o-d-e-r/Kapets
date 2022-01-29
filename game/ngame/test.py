import requests
import bs4

#responce = requests.Session()
#responce = requests.get("https://vstup.osvita.ua/y2021/r19/168/848107/")


#soup = bs4.BeautifulSoup(responce.text, "lxml")

#names = soup.findAll("td", attrs = {"data-th" : "ПІБ"})
#nums = soup.findAll("td", attrs = {"class" : "num"})
#priority = soup.findAll("td", attrs = {"data-th" : "П"})
#marks = soup.findAll("td", attrs = {"data-th" : "Бал"})


#with open("test.html", "w", encoding = "utf-8") as file_:
#    for n, name in enumerate(names):

 #       if priority[n].text.strip() == "1":
  #          file_.write(f"{nums[n].text}\t{marks[n].text.replace('розрахунок', '')}\t\t{name.text}\n")




import time
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
driver = webdriver.Firefox(
    executable_path = r"D:\pyrus\driver\geckodriver",
    firefox_options = options
)
action = webdriver.ActionChains(driver)



driver.get('https://vstup.osvita.ua/y2021/r19/168/848107/')


element = driver.find_element_by_xpath("//div[@class='detail-link']//span")


l = [1, 0]
for i in range(10):
    if random.choice(l) == 1:
        driver.execute_script(f"window.scrollTo(0, {random.randint(0, 100)})")
    else:
        action.move_by_offset(random.randint(0, 500), random.randint(0, 500))

    time.sleep(random.uniform(0, 0.5))


#for i in range(10):
driver.execute_script("arguments[0].click();", element)
#    time.sleep(random.randint(0, 3))


page = driver.execute_script("return document.documentElement.outerHTML;")#driver.page_source

print("=====================")
#soup = bs4.BeautifulSoup(page, "lxml")

#names = soup.findAll("td", attrs = {"data-th" : "ПІБ"})
#nums = soup.findAll("td", attrs = {"class" : "num"})
#priority = soup.findAll("td", attrs = {"data-th" : "П"})
#marks = soup.findAll("td", attrs = {"data-th" : "Бал"})


with open("test.html", "w", encoding = "utf-8") as file_:
    file_.write(page)
#    for n, name in enumerate(names):

 #       if priority[n].text.strip() == "1":
  #          file_.write(f"{nums[n].text}\t{marks[n].text.replace('розрахунок', '')}\t\t{name.text}\n")
