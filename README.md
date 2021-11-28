# pythonshopbot
A shopbot to buy products on various websites


Originally run via a virtual environment with Anaconda. 

This bot uses Selenium to first login to amazon with a given username and password, and then 
will navigate to the given product page and attempt to add the product to cart. 

If the item is out of stock, the bot will continue to reload the product page every 
couple of minutes. 

Once an item is available, it will be added to the cart and the purchase will be made
with the default payment/shipping info connected to the user's account, as long as 
the total amount is less than the user given total price. 
