from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/Users/xiencias/code/chromedriver')

driver.get('http://localhost:8100/')

# elem = driver.find_element_by_partial_link_text('Photo Gallery')

# elem.click()

driver.find_element_by_class_name('usuario').send_keys('andy')

driver.find_element_by_class_name('password').send_keys('rosa0000')

driver.find_element_by_id('login-button12').click()

driver.find_element_by_id('capital-list-item17').click()








#driver.findElement(input[@name='usuario']).setAttribute("value", "your value");



#driver.close()


# echo "export PATH=$PATH:/Users/xiencias/code/chromedriver" >> $HOME/.bash_profile

# export PATH=$PATH:/Users/xiencias/code/chromedriver