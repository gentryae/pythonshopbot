from selenium import webdriver as wd
import chromedriver_binary
import time 
import random
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime
from pytz import timezone
tz = timezone('EST')




wd = wd.Chrome()
# Wait up to 10 seconds for a elements to become available when 
#loading a page
wd.implicitly_wait(10)

def load_page(url):
    #enter the URL for the item here
    wd.get(url)

#random wait time used to avoid being detected as a bot
#random_wait_time = randrange(2.0, 6.0)
def random_wait(x, y):
    random_wait_time = random.randrange(x, y)
    time.sleep(random_wait_time)
    
def login(username, password):
    #open up email field
    email_login = wd.find_element_by_xpath('//*[@id="ap_email"]')
    type(email_login)

    # TO DO: enter your email in this command
    email_login.send_keys(username)

    random_wait(2, 6)
    #click continue button
    continue_button = wd.find_element_by_xpath('//*[@id="continue"]')
    continue_button.click()

    random_wait(2, 6)
    password_entry = wd.find_element_by_xpath('//*[@id="ap_password"]')
    type(password_entry)

    # TO DO: enter your password in this command
    password_entry.send_keys(password)

    random_wait(2, 4)
    # stay logged in button
    stay_logged_in = wd.find_element_by_xpath('//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input')
    stay_logged_in.click()
    
    #login button
    login_button = wd.find_element_by_xpath('//*[@id="signInSubmit"]')
    login_button.click() 
    
def place_order(max_price_float):
    price = wd.find_element_by_xpath('//*[@id="subtotals-marketplace-table"]/tbody/tr[7]/td[2]').text
    print('the price is: ', price)
    price = price[1:]
    price = float(price)
    # check that price is correct
    if price <= max_price_float:
        #if price is correct, place order
        place_order_button = wd.find_element_by_xpath('//*[@id="submitOrderButtonId"]/span/input')
        place_order_button.click()
    else:
        #price is from a third party seller, dont buy! 
        print(f"Price is ${price} and therefore I will not place the order")

def main():
    
    #give the url of the sign in page
    wd.get("https://www.amazon.com")
    #login with user and password 
    login('email@email.com', 'password_')

    random_wait(3,6)
        
    #in a loop, keep trying to find the add to cart button in the page 
    while True:
        #load the page
        print("loading page at ", datetime.now(tz))
        # page of the item you want to buy
        wd.get("itempage.com/product_to_buy")
        
        try:
            #try to click add to cart button
            add_to_cart_button = wd.find_element_by_xpath('//*[@id="add-to-cart-button"]')
            add_to_cart_button.click()
            break
        except NoSuchElementException:
            print("out of stock at: ", datetime.now(tz))
            #reload page in two minutes
            random_wait(100, 180)

    random_wait(1, 3)
    
    #go to checkout
    
    checkout_button = wd.find_element_by_xpath('//*[@id="hlb-ptc-btn-native"]') #//*[@id="attach-sidesheet-checkout-button"]/span/input
    checkout_button.click()
    
    # place the order if the price is correct, giving
    # a maximum price allowed (i.e. $550 for the xbox)
    place_order(15.0)
    

if __name__ == "__main__":
    main()
