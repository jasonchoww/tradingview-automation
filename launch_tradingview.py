import time


def launch(driver):
    # launches tradingview
    driver.get("https://www.tradingview.com/")

    # login
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[4]/span[2]/a').click()
    time.sleep(2)

    # google+ login
    driver.find_element_by_xpath(
        '//*[@id="overlap-manager-root"]/div/div[2]/div/div/div/div/div/div[1]/div[2]/span[2]').click()
    time.sleep(2)

    # switches to second window
    driver.switch_to.window(driver.window_handles[1])

    # send_keys: email account
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys("example@email.com")
    driver.find_element_by_xpath('//*[@id="identifierNext"]/content/span').click()
    time.sleep(2)

    # send_keys: password
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys("password_goes_here")
    driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    time.sleep(2)

    # switches back to original window after logging in
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(3)

    # opens chart
    driver.find_element_by_xpath('/html/body/div[3]/div[2]/div[2]/ul/li[6]').click()
