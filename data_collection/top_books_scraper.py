from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
import time
driver.implicitly_wait(20) 

chrome_path = which('chromedriver')

driver = webdriver.Chrome(executable_path=chrome_path)

driver.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books_home_all?pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583&pf_rd_s=center-5&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=YZ53ZYJHCB578RWPV713&pf_rd_r=YZ53ZYJHCB578RWPV713&pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583')

book_items = driver.find_elements_by_xpath("//li[@class='zg-item-immersion']")

for i in range(len(book_items)):
    last_height = driver.execute_script("return document.body.scrollHeight")
    i += 1
    book = driver.find_element_by_xpath("//li[@class='zg-item-immersion'][{}]".format(i))
    book.click()
    time.sleep(1.43)
    print(driver.find_element_by_xpath("//div[@class='a-section a-spacing-none']/h1/span[1]").text)
    driver.back()
    time.sleep(2.1)
    driver.execute_script("window.scrollTo(0, {})".format(last_height+500))