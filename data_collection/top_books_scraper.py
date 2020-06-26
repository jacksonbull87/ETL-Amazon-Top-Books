from selenium import webdriver
from shutil import which
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd 

def get_top_books_data():
    chrome_path = which('chromedriver')

    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.implicitly_wait(20) 
    driver.get('https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books_home_all?pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583&pf_rd_s=center-5&pf_rd_t=2101&pf_rd_i=home&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=YZ53ZYJHCB578RWPV713&pf_rd_r=YZ53ZYJHCB578RWPV713&pf_rd_p=c37c53ab-de39-45c8-93ea-0bdb20185583')

    SCROLL_PAUSE_TIME = 0.5
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    data_bucket = []
    book_items = driver.find_elements_by_xpath("//li[@class='zg-item-immersion']")

    for i in range(len(book_items)):
        
        i += 1
        rank = driver.find_element_by_xpath("//li[@class='zg-item-immersion'][{}]/span/div/div/span/span".format(i)).text
        book = driver.find_element_by_xpath("//li[@class='zg-item-immersion'][{}]".format(i))
        book.click()
        time.sleep(1.43)
        title = driver.find_element_by_xpath("//div[@class='a-section a-spacing-none']/h1/span[1]").text
        
        try:
            author = driver.find_element_by_xpath("//span[@class='author notFaded'][1]/a").text
        except:
            author = driver.find_element_by_xpath("//span[@class='author notFaded']/span[1]/a[1]").text
        try:
            rating = driver.find_element_by_id('acrPopover').get_attribute('title')
        except:
            rating = 'None'
        driver.execute_script("window.scrollTo(0, {})".format(last_height+500))
        cover = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[1]/b").text
        num_pages = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[1]").text
        publisher = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[2]").text
        

        data_tuple = (rank,title,author, rating, cover, num_pages, publisher)
        print(data_tuple)
        data_bucket.append(data_tuple)
        driver.back()
        time.sleep(1.6)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        

    next_page = driver.find_element_by_xpath("//li[@class='a-last']/a")
    if next_page:
        next_page.click()
        time.sleep(2.132)
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(SCROLL_PAUSE_TIME)

            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        book_items = driver.find_elements_by_xpath("//li[@class='zg-item-immersion']")
        for i in range(len(book_items)):
            
            i += 1
            rank = driver.find_element_by_xpath("//li[@class='zg-item-immersion'][{}]/span/div/div/span/span".format(i)).text
            book = driver.find_element_by_xpath("//li[@class='zg-item-immersion'][{}]".format(i))
            book.click()
            time.sleep(1.43)
            title = driver.find_element_by_xpath("//div[@class='a-section a-spacing-none']/h1/span[1]").text
            try:
                author = driver.find_element_by_xpath("//span[@class='author notFaded'][1]/a").text
            except:
                author = driver.find_element_by_xpath("//span[@class='author notFaded']/span[1]/a[1]").text
            try:
                rating = driver.find_element_by_id('acrPopover').get_attribute('title')
            except:
                rating = 'None'
            driver.execute_script("window.scrollTo(0, {})".format(last_height+500))
            cover = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[1]/b").text
            num_pages = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[1]").text
            publisher = driver.find_element_by_xpath("//td[@class='bucket']/div/ul/li[2]").text
            

            data_tuple = (rank, title,author, rating, cover, num_pages, publisher)
            print(data_tuple)
            data_bucket.append(data_tuple)
            driver.back()
            time.sleep(2.1)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    df = pd.DataFrame(data=data_bucket, columns=['rank', 'title','author', 'rating', 'cover', 'num_pages', 'publisher'])
    return df