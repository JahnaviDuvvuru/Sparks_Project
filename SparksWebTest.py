from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="D:\Chrome Driver for Selenium\chromedriver.exe")
driver.get("https://www.thesparksfoundationsingapore.org/")

# Check the parameter 'LOGO'  (Testcase : 1)
print('\nTestCase : 1')
logo = driver.find_element_by_xpath('//*[@id="home"]/div/div[1]/h1/a/img')
if logo.is_displayed():
    print("Successful : Logo is Present\n")
else:
    print("Logo is not visible\n")

time.sleep(2)

# Check the parameter 'Title'  (Testcase : 2)
print('TestCase : 2')
try:
    assert 'The Sparks Foundation' in driver.title
    print('Successful : Title is present\n')
except:
    print('Title is absent\n')

time.sleep(2)

# Check the parameter 'Navigation Bar'  (Testcase : 3)
print('TestCase : 3')
bar = driver.find_element_by_tag_name('nav')
if bar.is_displayed():
    print("Successful : Navigation Bar is displayed\n")
else:
    print("Navigation Bar is not displayed\n")

time.sleep(2)

# The parameter 'Home' page (Testcase : 4)
print('TestCase : 4')
try:
    driver.find_element_by_partial_link_text("The Sparks Foundation").click()
    print("Successful : Home page link is working\n")
except:
    print("Home page link is not working\n")

time.sleep(2)

# The parameter 'Join Us'  (Testcase : 5)
print('TestCase : 5')
try:
    join_us = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[5]/a')
    join_us.click()
    time.sleep(2)
    why_join_us = driver.get('https://www.thesparksfoundationsingapore.org/join-us/why-join-us/')
    time.sleep(2)
    name = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[1]')
    email = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/input[2]')
    role = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/form/select')

    # Scrolling Action
    driver.execute_script("window.scrollBy(0,400)", name)
    time.sleep(2)

    name.send_keys('Jahnavi Duvvuru')
    time.sleep(2)

    email.send_keys('jahnaviduvvuru9@gmail.com')
    time.sleep(2)

    choose = Select(role)
    choose.select_by_visible_text('Student')
    print('Join US page is visited and Form filled successfully\n')
except:
    print('Join US page is not visited\n')

time.sleep(3)

# Check the 'About Us'  (Testcase : 6)
print('TestCase : 6')
try:
    about_us = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/a')
    time.sleep(2)
    vision = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[1]/ul/li[1]/a')
    actions = ActionChains(driver)
    actions.move_to_element(about_us).click().move_to_element(vision).click().perform()
    print('Successful : About page is visited\n')
except:
    print('About Page not visited\n')

time.sleep(3)

# Check the 'Policies' page (Testcase : 7)
print('TestCase : 7')
try:
    policies = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/a')
    time.sleep(2)
    code = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[2]/ul/li[2]/a')
    actions = ActionChains(driver)
    actions.move_to_element(policies).click().move_to_element(code).click().perform()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,200)", "")
    print('Policies page is visited successfully\n')
except:
    print('Policies page not visited\n')

time.sleep(3)

# Check the 'Programs page'  (Testcase : 8)
print('TestCase : 8')
try:
    program = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/a')
    mentor = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[3]/ul/li[2]/a')
    action = ActionChains(driver)
    action.move_to_element(program).click().move_to_element(mentor).click().perform()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,400)", "")
    print('Successful : Programs page visited\n')
except:
    print('Programs page not visited successfully\n')

time.sleep(3)

# Check the 'Links' page (Testcase : 9)
print('Testcase : 9')
try:
    links = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[4]/a')
    software = driver.find_element_by_xpath('//*[@id="link-effect-3"]/ul/li[4]/ul/li[1]/a')
    action = ActionChains(driver)
    action.move_to_element(links).click().move_to_element(software).click().perform()
    time.sleep(3)
    driver.execute_script("window.scrollBy(0,300)", "")
    print('Links page visited successfully\n')
except:
    print('Links page not visited successfully\n')

time.sleep(3)

# Check the 'Contact Us' Page (Testcase : 10)
print('Testcase : 10')
try:
    driver.find_element_by_link_text('Contact Us').click()
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300)", "")
    print('Successful : Contact Page visited\n')
except:
    print('Contact Page not visited\n')

time.sleep(3)

print('******** All Testcases executed successfully ********')

cls = driver.close()
