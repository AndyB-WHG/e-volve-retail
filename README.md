
# E-volve Retail

Climate change is now the most pressing and urgent problem facing the world today.  It is imperative that we move to a sustainable way of life before the consequences become irreversible.

The E-volve Retail store aims to be part of the solution by providing fully sustainable and beautiful clothing, beauty and home products for an increasingly ecologically aware customer base.



A live website can be found [here](https://e-volve-retail.herokuapp.com/).


 **September 1, 2021**

## Table of Contents

`Highlights in yellow`

_Make's the text italic_

1. Text 
2. *Also makes the text italic*
3. Text
4. Text
5. Text

------

```
Example of a
black background
```

---


1. [User Experience (UX)](#user-experience-UX)
    1. [Project Goals](#project-goals)
    2. [User Stories](#user-stories)
    3. [Color Scheme](#color-scheme)
    4. [Data Model](#data-model)
2. [Features](#features)
    1. [User Information Input](#user-information-input)
   
   
3. [Technologies Used](#technologies-used)
    1. [Language Used](#language-used)
    2. [Frameworks, Libraries and Programs Used](#frameworks-libraries-and-programs-used)
4. [Testing](#testing)
    1. [Testing User Stories](#testing-user-stories)
    2. [Code Validation](#code-validation)
    3. [Manual Testing](#manual-testing)
5. [Deployment](#deployment)
6. [Credits](#credits)
7. [Acknowledgements](#acknowledgements)

***

## User Experience (UX)

### Project Goals

* Provide an online retail website which is instantly recognisible as an e-commerce store selling products to the general public. 

* The site must be modern, pleasant to view, easy to navigate and provide all the ususal features customers expect to see on a retail website.


* Customers should be able to make secure credit card payments and be able to create an account in order to save details of orders and delivery addresses for use and viewing at a later date. 

* The site should be easily navigable and provide intuitive features to help the user find a specific product/s they may be interersted in.

* The site should be secure with only approved Admin Superusers able to make changes to products and orders.  Superusers should also have the ability to change another user's account details where required/authorised.

### User Stories

* As a user, I want to immediately understand the site's main function.

* As a shopper, I want to easily understand how to begin viewing products.

* As a shopper, I want to easily understand the navigation options available  and the types of products available.

* As a shopper, I want to be able to easily identify specific products I may be looking for (via a 'search' box for example). 

* As a shopper, I want to be able to list products on screen to better suit my search requirements (eg. sort by price or by category).

* As a shopper I want to be able to click into individual products to see more details and a larger picure of a product I'm interested in.

* As a shopper I want to be able to store my selections in a shopping trolley and be able to alter my selections as necessary.

* As a shopper I want clear notifications each time I add, remove or alter items in my shopping trolley.

* As a shopper I want to be able to make secure credit card payments for the items I've chosen including relavant delivery address details.

* As a returning shopper I want to be able to create my own account in order to save my personal and delivery details. 

* As a returning shopper, I want to be able to see details of previous orders I've placed.

* As a returning shopper with an account, I want my shopping bag to remain saved for as long as I stay logged in to my account.

* As an Admin Superuser I want to be able to view and make changes to products, orders or user account details as and when necessary by logging in via my Superuser account.

### Color Scheme

Here are the colors being used :


* Site-wide text, product prices and Navbar icons:

    Charcoal Grey   -  `rgb(55, 56, 56)`

* Default Background :

    White  -  `#ffffff`

* E-volve Logo :

    Terracotta Orange - `#c06e2c`

* 'Add to Basket' and 'Checkout' buttons :

    Green  -  `rgb(126, 170, 126);`


### Data Model

* Category Model

    - name = models.CharField(max_length=254) 
    - friendly_name = models.CharField(max_length=254, null=True, blank=True)

* Product Model
    - category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    - sku = models.CharField(max_length=254, null=True, blank=True)
    - name = models.CharField(max_length=254)
    - description = models.TextField()
    - has_sizes = models.BooleanField(default=False, null=True, blank=True)
    - price = models.DecimalField(max_digits=6, decimal_places=2)
    - image_url = models.URLField(max_length=1024, null=True, blank=True)
    - image = models.ImageField(null=True, blank=True)

* Order Model
    - order_number = models.CharField(max_length=32, null=False, editable=False)
    - user_profiles = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                      null=True, blank=True, related_name='orders')
    - full_name = models.CharField(max_length=50, null=False, blank=False)
    - email = models.EmailField(max_length=254, null=False, blank=False)
    - phone_number = models.CharField(max_length=20, null=False, blank=False)
    - country = CountryField(blank_label='Country *', null=False, blank=False)
    - postcode = models.CharField(max_length=20, null=True, blank=True)
    - town_or_city = models.CharField(max_length=40, null=False, blank=False)
    - street_address1 = models.CharField(max_length=80, null=False, blank=False)
    - street_address2 = models.CharField(max_length=80, null=True, blank=True)
    - county = models.CharField(max_length=80, null=True, blank=True)
    - date = models.DateTimeField(auto_now_add=True)
    - delivery_cost = models.DecimalField(max_digits=6, decimal_places=2,
                                        null=False, default=0)
    - order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    - grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    - original_shopping_bag = models.TextField(null=False, blank=False, default='')
    - stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
* Order Line-Item Model (used to create an order line for each item in a given order)

    - order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    - product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    - product_size = models.CharField(max_length=2,
                                    choices=SIZE_CHOICES, null=True,
                                    blank=True)  `'SIZE_CHOICES'` variable derived from `'SIZE_CHOICES'` selection listed below.
    - quantity = models.IntegerField(null=False, blank=False, default=0)
    - lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)

    - `SIZE_CHOICES`= [
        (SIZE_6, 'Size 6'),
        (SIZE_8, 'Size 8'),
        (SIZE_10, 'Size 10'),
        (SIZE_12, 'Size 12'),
        (SIZE_14, 'Size 14'),
        (SIZE_16, 'Size 16'),
        (SIZE_18, 'Size 18'),
        (SIZE_20, 'Size 20'),
    ]   `'SIZE'` variable derived from the `'SIZE'` selection listed below.

    - SIZE_6 = "6"
    SIZE_8 = "8"
    SIZE_10 = "10"
    SIZE_12 = "12"
    SIZE_14 = "14"
    SIZE_16 = "16"
    SIZE_18 = "18"
    SIZE_20 = "20"

* User Profile Model
    - user = models.OneToOneField(User, on_delete=models.CASCADE)
    - default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    - default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    - default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    - default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    - default_county = models.CharField(max_length=80, null=True, blank=True)
    - default_postcode = models.CharField(max_length=20, null=True, blank=True)
    - default_country = CountryField(blank_label='Country', null=True, blank=True)


## Features

### Home Page `'Carousel'` imagery

 - Carousel of three eye-catching product images, each with a simple headline message to educate the user as to the websites main function and unique selling point (USP).
 - Each image has a 'Shop Now' button to prompt the user to begin browsing.  The buttons take the user to the Department relevant to the image on screen.
- The Carousel also has left and right arrows to enable the user to manually scroll left or right should they so choose.


### Navbar

- A Navbar is fix to the top of the page in order to provide the user with browsing options during their visit.
- On smaller screens the Navbar features:
    - A choice of 'Search', 'User' and 'Shopping Bag' icons at top right dependant upon screen size
    -  a drop-down 'burger' toggle at top left, with . The 'burger' drop-down includes links to: 
        * The main Product Departments pages
        * User Login / Register / Account Page options
        * Product Review page
    
- On larger screens the central Navbar area comprises 
    - At top left, the 'Home / Logo' link to return to the Carousel
    - Links to the three main store departments. plus an additional link to display 'All Products'.  

### 'Search' function

- A 'Search Box' (large screens) or 'Search Icon' (small screens) is provided to enable users to search for a keyword located in either in the Product Name or Product Description.  If the keyword is found - the relevant products are displayed/listed on screen.

### Products Page

- After clicking a Department / Category link (Fashion, Home, Beauty or All), or after successully searching for a product using the 'Search' function, the relevant products are listed on the 'Products' page.

-  Items are listed in columns dependent upon screen size.  Each listed product includes the :
    - Product Image 
    - Product Name
    - Product Price 
    - Product Category/Department link

- Clicking a product directs the user to the 'Description' page for the item in question.
- Clicking the product's Category/Deprtment link prompts the site to display all products for the Department concerned.


### 'Sort' Function

- Items listed on the 'Products' page can be sorted using a number of pre-set options within the 'Sort by' box, located at top middle on small screens and top right on larger screens.

    Options for sorting include:

    - Price (high to low)
    - Price (low to high)
    - Name (A-Z)
    - Name (Z-A)
    - Category (A-Z)
    - Category (Z-A)

   


