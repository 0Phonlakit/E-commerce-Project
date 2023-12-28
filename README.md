# E-commerce-Project

This project was created to study the creation of web applications using the Django framework and to improve the author's coding skills. It is not intended for commercial purposes.

In general, this project simulates a web-based store. It consists of four major systems:
1. <em> **Storefront system** </em>
2. <em> **User registration system** </em> 
3. <em> **Shopping cart system**  </em>
4. <em> **Order history system** </em>
   
For more detailed information, please refer to the following sections.

The code includes comments that explain how it works. You can view the code and comments, but the comments are in Thai. We apologize for any inconvenience this may cause.

**Requirements**
* Python 
* Django 
* Pillow 

## Details

When the user opens the website, they will be on the store's landing page. This page contains a nav-bar (1), which displays a list of the menus available on the website. The website also has a footer (2), which is located at the bottom of the page. When the user clicks the "go to shop" button, they will be taken to the homepage.

![Advertisingpage](images/Advertising%20page.png)
<hr />

When the user arrives at the homepage, they will see a list of the most popular products. Each product will have a picture, name, price, and a button to add it to the cart. The user can tell that they are on the popular products page by looking at the URL (4). If the user is on any other page, they can click the "Home" button (5) to return to the popular products page.

![Homepage](images/Home%20page.png)
<hr />

If the user clicks the "All Products" button (6), they will be taken to a page that lists all of the products available in the store.

![Allproductpage](images/All%20product%20page.png)
<hr />

At the bottom of the page, the user will see a pagination tab (7). Clicking on a page number will take the user to that page of products.

![Tabbarinbutton](images/Tabbar%20in%20button.png)
<hr />

If the user clicks the "Category" button (8), they will be taken to a page that lists all of the products in each category. This makes it easier for users to find the products they are looking for.

![Category](images/category.png)
<hr />

For example, if the user searches for hard drives by category, they can check the URL (9).

![Seachwithcategory](images/seach%20with%20category.png)
<hr />

When the user clicks the profile icon (10), a dropdown will appear with two options: login and register. If the user clicks the login option, a login window will appear, as shown in the image below. The user can check the URL (11) to verify that they are on the login page. 

![Loginpage](images/login%20page.png)
<hr />

From the dropdown, if the user goes to the register page, they can check the URL (12). When the user arrives at the register page, they will be asked to enter their information, as shown in the image below.

![Registerpage](images/register%20page.png)
<hr />

If the user does not enter all of the required information, an alert will appear to let them know what information is missing (13). In this case, the user did not enter their email address, so an alert will appear to let them know that they need to enter their email address.

![Registeruncompletepage](images/register%20uncomplete%20page.png)
<hr />

Once the user has entered all of the required information, an alert will appear with a green border and a pop-up tab (14). When the user clicks "OK", the website will take them to the login page.

![Registercompletepage](images/register%20complete%20page.png)
<hr />

When the user enters the login page, if they enter incorrect information, an alert will appear to let them know that their information is incorrect (15).

![Loginuncompletepage](images/login%20uncomplete%20page.png)
<hr />

If the user successfully logs in, a green alert with a pop-up tab will appear (16). When the user clicks "OK", the website will take them to the homepage.

![Logincompletepage](images/login%20complete%20page.png)
<hr />

Then, when the user clicks the profile icon (17), the information in the dropdown will change to show the Order history and Logout pages.

![Tabafterlogin](images/Tab%20after%20login.png)
<hr />

When the user clicks on a product image, they will be taken to the product details page, which can be checked from the URL (18). The product details page will include the following information:

* Image
* Stock
* Name
* Details
* Quantity remaining in stock
* Price
* Add to cart button

![Detailpage](images/detail%20page.png)
<hr />

The user can search for products using the search bar (19).

![Searchitem](images/search%20item.png)
<hr />

When the user searches for a product, the website will take them to the search results page, which can be checked from the URL (20).

![Searchitemcomplete](images/search%20item%20complete.png)
<hr />

If the user searches for a product and does not find it, the website will show them a page that can be checked from the URL (21).

![Searchnotfoundpage](images/search%20not%20found%20page.png)
<hr />

When the user clicks on the cart icon in the top right corner, the website will take them to the checkout page, which can be checked from the URL (22).

![Cartwithitem](images/cart%20with%20item.png)
<hr />

When the user clicks on "Payment", they will be taken to a page where they can enter their phone number and shipping address. Once they have entered all of the required information, they can click on the "Submit" button (23) to confirm their purchase.

![Orderpage](images/order%20page.png)
<hr />

When the user clicks on the "Submit" button, the website will show them a page that confirms their purchase, which can be checked from the URL (24).

![Ordercompletepage](images/order%20complete%20page.png)
<hr />

After the user has completed their purchase, if they click on the cart icon in the top right corner, the website will show them a page that indicates that they have no items in their cart, which can be checked from the URL (25).

![Cartnotitempage](images/cart%20not%20item%20page.png)
<hr />

After the user has completed their purchase, they can check the order details by clicking on the profile icon (17) and then clicking on "Order history". This will show them a page with the order number, date, total price, and a link to view the order details (27). This page can be checked from the URL (26).

![Orderhistorypage](images/order%20history%20page.png)
<hr />

When the user clicks on the link to view the order details, they will be taken to the order details page, which can be checked from the URL (28). This page will include the name and surname that the user entered on the register page, as well as the phone number and address that they entered on the checkout page. It will also include the details of the products that they purchased, including the quantity and price.

![Orderdetailpage](images/order%20detail%20page.png)
<hr />

To delete an item from the cart, the user can click on the trash can icon (29). When they do this, a popup (30) will appear to confirm that they want to delete the item.

![Deleteitemincart](images/delete%20item%20in%20cart.png)
<hr />

When the user returns to the order details page, they will see that the quantity of the product in stock (31) has decreased after the order has been placed.

![Itemafterbuy](images/item%20after%20buy.png)
<hr />

In this case, the user has purchased the same product twice. The quantity in the quantity field (32) is 2, so the price of the product has increased to the price of the product multiplied by the quantity. The total price is also added together for all of the products.

![Itemquantitychack](images/item%20quantity%20chack.png)
<hr />

<em> **Thank you for your attention. I have now completed my presentation on the E-commerce project. If you have any feedback, please feel free to share it with me. I appreciate your time and consideration.** </em>
