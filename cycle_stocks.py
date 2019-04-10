import time


# Add tickers for cycle
def cycle(driver):
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('GERN' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('SRNE' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('IDRA' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('VSTM' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('HTGM' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('GALT' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('NVAX' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('BCRX' + "\n")
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="header-toolbar-symbol-search"]/div/input').send_keys('RIGL' + "\n")
