from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import random
from time import sleep

#path where my Google Chrome's driver is. From: https://pypi.org/project/selenium/
webdriver_path = "A:\Program Files (x86)\Microsoft Visual Studio\Shared\Python36_64\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(webdriver_path)

test_site_url = 'http://automationpractice.com/index.php?'
expected_title = 'My Store'

#just a way to rerun tests without having to manually change the new email
repeated_name = "YouName"#HERE, set a name you like to be used on generating an new email.
email_generator_file = "email_generator_file.txt"

file = open(email_generator_file,"a+")
file.seek(0)
if(file.read() == ""):
    file.write('0')
    
file.seek(0)
last_email_number = file.readline()
file.close()
file = open(email_generator_file,"w+")
file.write(str(int(last_email_number)+1))
file.close()
    
email = "test_"+repeated_name+"_"+last_email_number+"@gmail.com"#email for new account
randoms = random.sample(range(8-1),3)
#driver.maximize_window()
driver.get(test_site_url)
assert expected_title in driver.title

homeproducts = driver.find_element_by_id('homefeatured')
products = homeproducts.find_elements_by_tag_name('li')
selected_products = []
for random in randoms:
    selected_products.append(products[random])

for selected_product in selected_products:
    #logic to add item to cart goes here
    add_button = selected_product.find_element_by_css_selector('a[title="Add to cart"]')
    add_button.click()
    sleep(2)
    continue_button  = driver.find_element_by_css_selector('span[title="Continue shopping"]')
    continue_button.click()
    sleep(2)
#hover over cart panel to make it visible
cart_panel = driver.find_element_by_css_selector('a[title="View my shopping cart"]')
hover = ActionChains(driver).move_to_element(cart_panel)
hover.perform()
sleep(1)
checkout_button = driver.find_element_by_id('button_order_cart')
checkout_button.click()

#TODO: check if items are in cart

sleep(5)
checkout_button = driver.find_elements_by_css_selector('a[title="Proceed to checkout"]')[1]
checkout_button.click()

#creates new account
email_textbox = driver.find_element_by_id('email_create')
email_textbox.send_keys(email)
create_account_button = driver.find_element_by_id('SubmitCreate')
create_account_button.click()

sleep(2)
#filling up the "YOUR PERSONAL INFORMATION FORM"
gender_options = driver.find_elements_by_name('id_gender')
gender_options[1].click()#TODO: make it random
first_name_textbox = driver.find_element_by_id('customer_firstname')
last_name_textbox = driver.find_element_by_id('customer_lastname')
email_textbox = driver.find_element_by_id('email')#autofilled
password_textbox = driver.find_element_by_id('passwd')
#SELECT
select_days = Select(driver.find_element_by_name('days'))
select_months = Select(driver.find_element_by_name('months'))
select_years = Select(driver.find_element_by_name('years'))

gender_options[1].click()#TODO: make it random
first_name_textbox.send_keys(repeated_name)
last_name_textbox.send_keys("Last Name")
password_textbox.send_keys("test"+last_email_number)

select_days.select_by_value('6')
select_months.select_by_value('9')
select_years.select_by_value('1993')

newsletter_checkbox = driver.find_element_by_id('newsletter')
newsletter_checkbox.click()
receive_offers_checkbox = driver.find_element_by_id('optin')
receive_offers_checkbox.click()

address1_textbox = driver.find_element_by_id('address1')
address1_textbox.send_keys('Line Adress, 123')

city_textbox = driver.find_element_by_id('city')
city_textbox.send_keys('New York City')

select_state = Select(driver.find_element_by_id('id_state'))
select_state.select_by_value('32')

postcode_textbox = driver.find_element_by_id('postcode')
postcode_textbox.send_keys('99524')

mobilephone_textbox = driver.find_element_by_id('phone_mobile')
mobilephone_textbox.send_keys('53932232112')

submit_button = driver.find_element_by_id('submitAccount')
submit_button.click()
sleep(2)
checkout_button = driver.find_element_by_name('processAddress')
checkout_button.click()

terms_button = checkout_button = driver.find_element_by_id('cgv')
terms_button.click()

checkout_button = driver.find_element_by_name('processCarrier')
checkout_button.click()

payment_button = driver.find_element_by_css_selector('a[class="bankwire"]')
payment_button.click()

confirm_button = driver.find_elements_by_css_selector('button[type="submit"]')[1]
confirm_button.click()

input()
driver.close()


##elem = driver.find_element_by_name("q")
##elem.clear()
##elem.send_keys("pycon")
##elem.send_keys(Keys.RETURN)
##assert "No results found." not in driver.page_source
#driver.close()
