
# E-volve Retail

Climate change is now the most pressing and urgent problem facing the world today.  It is imperative that we move to a sustainable way of life before the consequences become irreversible.

The E-volve Retail store aims to be part of the solution by providing fully sustainable and beautiful clothing, beauty and home products for an increasingly ecologically aware customer base.



A live website can be found [here](https://e-volve-retail.herokuapp.com/).

[Link to all wireframes created for this project](https://github.com/AndyB-WHG/e-volve-retail/tree/main/documentation_assets/wireframes)


## Table of Contents

------

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

## 1. User Experience (UX)

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


### Data Models

![Database Schema](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/database_schema/Database%20Schema.png)

https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/database_schema/Database%20Schema.png


## 2. Features

### Home Page 'Carousel' imagery

 - Carousel of three eye-catching product images, each with a simple headline message to educate the user as to the websites main function and unique selling point (USP).
 - Each image has a 'Shop Now' button to prompt the user to begin browsing.  The buttons take the user to the Department relevant to the image on screen.
- The Carousel also has left and right arrows to enable the user to manually scroll left or right should they so choose.


### Navbar

- A Navbar is fixed to the top of the page in order to provide the user with browsing options during the visit.
- On smaller screens the Navbar features:
    - At top right : 
        - Search Icon, 
        - User/Account icon (visible on tablet screens but not on mobile phones)
        - Shopping Bag icon
    -  At top left : 
        - a drop-down 'burger' toggle which includes links to : 
            * The main Product Departments pages
            * User Login / Register / Account Page options
            * Product Review page
    - Top Centre :
        - A Logo / Home link to take the User back to the Carousel home page.

    
- On larger screens the central Navbar area comprises 
    - At top right :
        - Search Icon, 
        - User/Account icon
        - Shopping Bag icon

    - At top left : 
        - The 'Home / Logo' link to return the User to the Carousel

    - At top centre :

        - Links to the three main store departments. plus an additional link to display 'All Products'.  
 
            Each of the four links include dropdowns when hovering. These allow the user to pre-sort the results, should the user choose to. The sort selection includes :
            - By Price
            - By Name
            - By Category (option only displayed for the 'All' products link) 

    
### 'Search' function

- A 'Search Box' (large screens) or 'Search Icon' (small screens) is provided to enable users to search for a keyword located in either in the Product Name or Product Details.  If the keyword is found - the relevant products are displayed/listed on screen.

### Products Page

- After clicking a Department / Category link (Fashion, Home, Beauty or All), or after successully searching for a product using the 'Search' function, the relevant products are listed on the 'Products' page.

-  Items are listed in columns dependent upon screen size.  Each listed product includes the :
    - Product Image 
    - Product Name
    - Product Price 
    - Product Category/Department link

- Clicking a product directs the user to the 'Product Detail' page for the item in question.
- Clicking the product's Category/Deprtment link prompts the site to display all products for the Department concerned.


### Products Page 'Sort' Function

- Items listed on the 'Products' page can be sorted using a number of pre-set options within the 'Sort by' box, located at top middle on small screens and top right on larger screens.

    Options for sorting include:

    - Price (high to low)
    - Price (low to high)
    - Name (A-Z)
    - Name (Z-A)
    - Category (A-Z)
    - Category (Z-A)

### Product Detail Page

Clicking on a product image, name or price takes the user to the 'Product Detail' page. A larger image of the selected product is displayed along with a product description and the product's price.  

Here the user can select to add the product to their shopping bag, or write a review if they so wish.  The following options are provided:

- 'Choose size' box (user selects from a pre-defined dropdown list of sizes).  Note: appears only when the product in question has a range of sizes to choose from.
- 'Enter Quantity' box (user types in the quantity of the item they wish to purchase).
- 'Add To Bag'
- 'Write a Review'


### Shopping Bag

Accessed by clicking the 'Shopping Bag' icon at top right of the screen, this page lists all items currently selected for purchase by the user.

The top of the page details:
- the page title including the total quanity of items currently selected.
- total value of the items selected.
- delivery charges, if any (currently, orders over £50.00 have free delivery)
- total value of the order including delivery costs
- value still required to be spent to gain free delivery.
- a green 'Checkout' button enabling the user to pay for the items selected.

Beneath this section the page lists each of the selected items in turn, detailing:
- a product image
- the product name
- price of the item
- quantity chosen
    - Can be amended by the user should the original quantity selected be incorrect.
- 'Update Quantity' button  (highlighted in green)
    - Altering the quantity and then clicking this button enables the user to amend the quantity required. 
    - Once amended the shopping bag total is recalculated accordingly.
- 'Remove Item' button (highlighted in red)
    - Clicking the button removes the item permanently from the shopping bag.


### Shopping Bag 'Pop Up Notification'

Following an addition or change to the shopping bag, a pop-up notification appears at top right of the screen beneath the Shopping Bag item.

The notification : 
- displays a green header and a 'Success!' message.
- confirms the change in writing for the user.  
- displays the number of items currently in the shopping bag.
- lists the quantity and size (if relevant) of each item.
- allows the user scroll down to view the list of items.
- confirms the total value of the shopping bag including delivery.
- confirms the amount still required to be spent before free delivery is acquired (if appropriate).
- displays a link inviting the user to 'Go to Secure Checkout'. Clicking this link takes the user to the Shopping Page'.  Here the green 'Checkout' button takes the user to the 'Checkout Page'.


### Checkout Page

The 'Checkout Page' allows the user to securely pay for the chosen items.

The top of the page confirms the items to be purchased, including:
- Confirmation of the number of items within the current order.
- A list of the items in the order including for each item:
    - an image
    - the size of the item (if relevant)
    - the quantity ordered
- Order total
- Delivery cost
- Grand Total including delivery

The bottom section of the page consists of a 'Payment Form' within which the user must add their :
- name 
- delivery address 
- credit card details.  

Plus :

- a button to 'Adjust the Shopping Bag' if required.
- a button to 'Complete Order' once the user is ready to make payment.
- confirmation of the value of the order including delivery.


###  Order Confirmation Page

The Order Confirmation Page confirms that:
- payment was successful via a 'pop-up confirmation' and, 
- confirms that an email will be sent to the users email address. 

Also listed are details of the order,  including:
- Order Number.
- Order date and time.
- Items purchased, including quantity and value each.
- Delivery address details
- Order and delivery totals

The bottom of the confirmation includes a link to enable the user to continue shopping should they choose to.

## 3. Technologies Used

### Languages Used

* [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
* [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)


### Frameworks, Libraries and Programs Used

* [GitPod](https://gitpod.io/) was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/) was used to store the project after pushing.

* [Heroku](https://id.heroku.com/) was used to deploy the application.

* [PEP8 online check](http://pep8online.com/) was used to validate the Python code.
* [Bootstrap.com](https://getbootstrap.com/docs/4.6/getting-started/introduction/) helped provide structure, styling and responsiveness to various viewports. 
* [jQuery](https://en.wikipedia.org/wiki/JQuery) helped simplify the JavaScript coding.
* [Django](https://en.wikipedia.org/wiki/Django_(web_framework)) web framework was used to provide pre-built structure and functionality to the Python code.
* [pip3 / Python Package Index](https://pypi.org/) provided open-source Python software packages.
* [Google Fonts](https://fonts.google.com/) provided the 'Exo' and 'Lato' fonts utilised within the site.

* [Font Awesome](https://fontawesome.com/) provided the various icons used within the site.
* [Stripe](https://en.wikipedia.org/wiki/Stripe_(company)) - provides secure credit card payment and verification service.

## 4. Testing

### Testing User Stories

* As a user, I want to immediately understand the site's main function.

    - Carousel images together with 'Headline' banners showcase site products whilst imparting the main 'sustainability' message.

* As a shopper, I want to easily understand how to begin viewing products.
    - Carousel images include a clear 'Shop Now' button to prompt the user to begin exploring the site.
    - On medium and larger screens, the main Navigation Elements are displayed prominently at top middle of the page.
    - In smaller screens, the familiar drop-down 'burger' button is displayed prominently at top left of the page, to enable easy navigation from the drop-down list.

* As a shopper, I want to easily understand the navigation options available  and the types of products available.
    - All 'text-based' links are descriptive of their function, both within the main Navbar and within the 'burger' icon drop-down.
    - All 'icon' based links are familiar to most general web users making the site feel intuitive and simple to navigate. 

* As a shopper, I want to be able to easily identify specific products I may be looking for (via a 'search' box for example).
    - On both mobile and large screens a recognisable 'search icon' is displayed prominently in the Navbar at the top of the page.  Clicking the icon displays a standard text text box with an instruction to 'search our site'.

* As a shopper, I want to be able to list products on screen to better suit my search requirements (eg. sort by price or by category).
    - On Desktop screens the main 'Department/Category' links in the centre of the Navbar display dropdown links to enable the user to pre-sort the products for display. The user can choose between:
        - Sorted by Price,
        - Sorted by Name,
        or (if selecting the 'All Products' link)
        - Sorted by Category

    - Additionlly, for both Desktop and Mobile users, a 'Sort Box' is displayed at the top of a Category list to allow users to sort via a number of options:

        - Price (high to low)
        - Price (low to high)
        - Name (A-Z)
        - Name (Z-A)
        - Category (A-Z)
        - Category (Z-A)

* As a shopper I want to be able to click into individual products to see more details and a larger picure of a product I may be interested in.
    - Selecting any product directs the user to a 'Product Detail' page, within which a larger image of the product is displayed along side a description of the product and the price.
    - Clicking the image from within the 'Product Detail' page opens a new tab to display an even larger version of the image.

* As a shopper I want to be able to store my selections in a shopping trolley and be able to alter my selections as necessary.
    - User can add products to a 'Shopping Bag' from within the 'Product Detail' page, via the 'Add to Shopping Bag' button. 
    - Shopping Bag button changes colour on hover to highlight it's functionality to the user.

    - Shopping bag accessed directly via the Navbar.  Pop-up messages appear following additions to the shopping bag.
    
    - From within the Shopping Bag, quantities can be amended and products removed entirely using 'Change Quantity' and 'Remove Item' buttons.

* As a shopper I want clear notifications each time I add, remove or alter items in my shopping trolley.

    - Pop-up messages appear at top right of the screen beneath the shopping bag confirming: 
        - additions to the shopping bag
        - deletion of items from within the shopping bag
        - change of quantity from within the shopping bag


* As a shopper I want to be able to make secure credit card payments for the items I've chosen including relavant delivery address details.

    - Orders are recorded to the users account. Payments are validated and processed via the 'Stripe' application.

* As a returning shopper I want to be able to create my own account in order to save my personal and delivery details. 

    - Via the 'User' icon on the Navbar users are able to: 
        - Register new accounts
        - Login to accounts to view pesonal details and delivery addresses
        - Logout of accounts

* As a returning shopper, I want to be able to see details of previous orders I've placed.

    - Users are able to log in to their account and see a ful list of previous orders. Clicking an order displays the original order confirmation including:
        - date of order 
        - times of order
        - delivery addresse
        - items ordered
        - order number.


* As a returning shopper with an account, I want my shopping bag to remain saved for as long as I stay logged in to my account.
    
* As an Admin Superuser I want to be able to view and make changes to products, orders or user account details as and when necessary by logging in via my Superuser account.

### Manual Testing

Category | Test No. | Test Name     | Result        | Pass/Fail 
-------- | -------- | ------------- | ------------- | ---------
Carousel Links | 1 | Shop Now Link - Carousel Page 1 - Beauty Products | Beauty Products Page Displayed as expected. | Pass |
Carousel Links | 2 | Shop Now Link - Carousel Page 2 - Fashion Products | Fashion Products Page Displayed as expected. | Pass |
Carousel Links | 3 | Shop Now Link - Carousel Page 3 - Home Products | Home Products Page Displayed as expected. | Pass |
Carousel Links | 4 | Carousel indicator links - Page 1 | Links worked as expected moving the carousel to the required image. | Pass |
Carousel Links | 5 | Carousel indicator links - Page 2 | Links worked as expected moving the carousel to the required image. | Pass |
Carousel Links | 6 | Carousel indicator links - Page 3 | Links worked as expected moving the carousel to the required image. | Pass |
Carousel Links | 7 | Carousel left arrow - Page 1 | Link worked as expected moving the carousel to the previous image. | Pass |
Carousel Links | 8 | Carousel right  arrow - Page 1 | Link worked as expected moving the carousel to the next image. | Pass |
Carousel Links | 9 | Carousel left arrow - Page 2 | Link worked as expected moving the carousel to the previous image. | Pass |
Carousel Links | 10 | Carousel right  arrow - Page 2 | Link worked as expected moving the carousel to the next image. | Pass |
Carousel Links | 11 | Carousel left arrow - Page 3 | Link worked as expected moving the carousel to the previous image. | Pass |
Carousel Links | 12 | Carousel right  arrow - Page 3 | Link worked as expected moving the carousel to the next image. | Pass |
Navbar Links | 13 | Logo at top left - click | Link works as expected from all pages on the site. | Pass |
Navbar Links | 14 | Central 'Department' links (Fashion. Home Health. All) | Link works as expected from all pages on the site. | Pass |
Navbar Links | 15 | Central 'Department links : hover | Drop-down options appear beneath the main links upon hover as expected.  | Pass |
Navbar Links | 16 | Central 'Department drop-down' sorting links | Drop-down links take the user the requested Products page and sort as expected (by 'name' or by 'price'). | Pass |
Navbar Links | 17 | Search Icon click | Search box appears and disappears as expected on all pages on the site. | Pass |
Navbar Links | 18 | Search box function - enter text and click search button | Text search works correctly and displays matching products as expected. | Pass |
Navbar Links | 19 | User / Account Icon  click -  user not logged in | Clicking icon produces drop-down of 'Register' and 'Login' options as expected. | Pass |
Navbar Links | 20 | User / Register button click | Takes user to the 'Sign Up' page as expected. | Pass |
Navbar Links | 21 | User / Login button click | Takes user to the 'Sign In' page as expected. | Pass |
Navbar Links | 22 | User / Add Product (superusers only)  | Displays as designed only when a Superuser/Admin is logged in. Takes the user to the Add Product Page as expected. | Pass |
Navbar Links | 23 | User / Reviews Admin | Displays as designed only when a Superuser/Admin is logged in. Takes the user to the 'Reviews Admin Page' as expected. | Pass |
Navbar Links | 24 | User / Send Newsletter | Displays as designed only when a Superuser/Admin is logged in. Takes the user to the 'Send Newsletter Page' as expected. | Pass |
Navbar Links | 25 | User / Logout | Displays only when user is logged in as expected.  Takes the user to the 'Sign Out' page as designed. | Pass |
Navbar Links | 29 | Shopping Bag button click | Takes user to Shopping Bag page as ex[ected. | Pass |
Products Page | 30 | Product count | Number of products listed displays at top left as expected. | Pass |
Products Page | 31 | Product image and details links | Clicking takes the user to the 'Product Details' page as expected. | Pass |
Products Page | 32 | Department link beneath each item | Click takes useer to Products page for the Dept in question. | Pass |
Products Page | 33 | 'Sort by…' box | All sorting options work as expected. | Pass |
Products Page | 34 | Back to Top button | Button works as expected. | Pass |
Product Details Page | 35 | Page render | Page renders and includes all elements as expected. | Pass |
Product Details Page | 36 | Size seletor box | Box displays drop-down selection of pre-set sizes as expected. | Pass |
Product Details Page | 37 | Quantity selection box | Box accepts only numerical inputs between 0 and 99 as expected. | Pass |
Product Details Page | 38 | 'Add to Bag' button | Adds product to shopping bag with correct quantity and size as expected. | Pass |
Product Details Page | 39 | Department link  | Renders Products page as expected. Lists only products for the dept concerned as expected. | Pass |
Product Details Page | 40 | 'Write a Review' button | Takes the user to the 'Write a Review' page as expcted. | Pass |
Product Details Page | 41 | Reviews Section | Takes input correctly. Checks if user has purchased the product. If the user has purchased the product the review is accepted. If not a message is displayed advising only purchased products can be revewed and the review is rejected. | Pass |
Shopping Bag page | 42 | Desk top page | Renders as designed.  | Pass |
Shopping Bag page | 43 | Tablet size page | Renders as designed.  | Pass |
Shopping Bag page | 44 | Mobile Page | Renders as designed.  | Pass |
Shopping Bag page | 45 | 'Spend required for Free Delivery' message | Renders in correct location as designed, and quotes correct value. | Pass |
Shopping Bag page | 46 | Order Value | Calculates correctly. | Pass |
Shopping Bag page | 47 | Delivery value | Calculates correctly. | Pass |
Shopping Bag page | 48 | Total value | Calculates correctly. | Pass |
Shopping Bag page | 49 | Checkout button | Works as expected to render the Checkout Page. | Pass |
Shopping Bag page | 50 | Products Listing | Products, descriptions and prices render as expected. | Pass |
Shopping Bag page | 51 | Quanity boxes | Render correctly and can be updated as expected.  | Pass |
Shopping Bag page | 52 | 'Update Qty' button | Updates the quantity in the Shopping Bag for the item in question as expected. Also updates the Shopping Bag value as expected. | Pass |
Shopping Bag page | 53 | 'Remove Item' button | Removes the item in question from the Shopping Bag as expected. | Pass |
Checkout Page | 54 | Page render | Page renders correctly with items, sizes and quantities list at the top of the page, order and delivery totals displayed mid-page, delivery details form beneath the total and card payment details at the bottom of the page, together with 'Adjust Bag' and 'Complete Order' buttons. | Pass |
Checkout Page | 55 | Saved user details  | User address details are saved and updated as expected. | Pass |
Checkout Page | 56 | 'Complete Order' button | Works as expected to start the payment transaction process and render the 'Payment Success' page where appropriate. | Pass |
Checkout Page | 57 | 'Adjust Bag' button | Works as expected to render the Shopping Bag page. | Pass |
Checkout Success page | 58 | Page render | Page renders correctly following validated order and card details.  All orders details are listed correctly and delivery address details also listed in full in correct order.  Order number and date/time displayed correctly.  | Pass |
Checkout Success page | 59 | 'Keep Shopping' button | Works as expected - takes user to the 'All Products' page. | Pass |
Register (new user) page | 60 | Registration form fields inputs | Inputs work as expected.  Auto-verification checks password is not too common and not too short, checks if email account already used/registered, and checks if username is already used. | Pass |
Register (new user) page | 61 | Verification email sent to users email address | Email is sent and is received as expected. | Pass |
Sign Out page | 62 | Sign out button on Sign Out page | Button functions as expect and logs the user out whilst simultaneously deleting the Shopping Bag cookie.  Success message also confirms user is signed out. | Pass |
Sign Out page | 63 | Cancel Sign Out button  | Works as expected and the user remains logged in.  Success message also confirms user is logged in. | Pass |
Add Product Page | 64 | Cancel Button | Works as expected and takes the user back the Products Page | Pass |
Add Product Page | 65 | Add a Product Button | Works as expected to create a new product in the database.  | Pass |
Reviews Admin Page | 66 | Edit Button | Allows superusers to edit any review in the database via the Edit Review page | Pass |
Reviews Admin Page | 67 | Delete Button | Allows superusers to delete any review in the database. | Pass |
My Reviews Page | 68 | Edit Button | Allows users to edit any of their own reviews via the Edit Review Page | Pass |
My Reviews Page | 69 | Delete Button | Allows users to delete any of their own reviews. | Pass |
Send Newsletter Page | 70 | Send Newletter button | Works as expected and sends email to subscribed users as expected. | Pass |
Subscribe to Newsletter Page | 71 | Subscribe button  | Adds the user to the Newsletter Subscription database and send a confirmation email as expected. | Pass |


All HTML and CSS files were tested using the [W3 HTML Validator website](https://validator.w3.org/) and the [W3 Jigsaw CSS Validator website](https://jigsaw.w3.org/css-validator/).  

All code passes correctly through the validator except where HTML pages include 'Jinja Template Language' code for interaction with Django/Python variables and logic.  This is normal and to be expected.

A number of issues highlighted by the 'Pylint' system in Gitpod also require investigation.


## Bugs and issues

**Current Known Issues**

- Confirmation emails following purchases are not currently being sent to the user.  This may be to do with 'webhook' issues to the Stripe payment platform although this is yet to be confirmed/investigated.
 
- When editing reviews, the product image does not display on screen. Instead, the placeholder image is displayed.

- The 'footer' section merges into the bottom of the 'Product Details' and 'Product Review' pages.

- The 'shopping-bag' icon in the Navbar on Tablet and Mobile screens appears out of line when deployed via Heroku, but is inline when deployed via Github in Development mode.  Requires investigation.

- When adjusting the quantity of an item in the shopping bag, where the the item has a 'size' option, the size is not saved after the amendment and instead displays as blank (ie. 'Size   ').

Due to time constraints it has not been possible investigate/correct these issues at the present time so are to be corrected at a later date.



## Deployment

The application has been deployed using Github, Heroku, Amazon AWS and Stripe and can be replicated via the following process:

### Part 1.  Github & Heroku

1. Log in to Github and clone the e-volve-retail repository to your local machine. Instructions can be found here: 

    https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository


2. Install the packages listed in the 'requirements.txt' file using the following command. Ensure you are on the same directory level as the 'requirements.txt' file before commencing:

    pip3 install -r requirements.txt

3. Log in to the Heroku website (or create a new account if required).
4. From the main 'Dashboard' click 'New', then 'Create New App'.
5. Give the app a name (in this case 'e-volve-retail') and select the nearest region.
6. Click 'Create App'
7. Click the 'Resources' tab
8. In the 'Add-ons' search bar type 'postgres' and click on the 'Heroku Postgres' option in order to provision a new Postgres database in which to store your models and databases.
9. Select the 'Hobby Dev - Free' plan if you don't have a plan already.
10. Click 'Provision'.

11. Run migrations in order to migrate the data to the new 'Postgres' database:
    python3 manage.py migrate

12. Import the 'categories.json' and 'products.json' data files to Postgres.
    
    It is important to do them in this order as the products rely on the categories being in place first:

    python3 manage.py loaddata categories

    python3 manage.py loaddata products

13. Create 'superuser' for the Postgres database:

    python3 manage.py createsuperuser
    
    provide:

    Username, email and password

14. Login to Heroku via the CLI:

    heroku login -i

    enter your Heroku email and password login details

15. Temporarily disable 'COLLECTSTATIC' files so that Heroku won't try to collect static files upon deployment:

    heroku config:set DISABLE_COLLECTSTATIC=1 --app e-volve-retail

16. Add the 'Host Name' of the Heroku app to the 'Allowed Hosts' section of the 'settings.py' file:

    ALLOWED_HOSTS = ['e-volve-retail.herokuapp.com', 'localhost']

    (note: the 'localhost' setting also allows the app to be run from GitPod or other CLI)

17. Add, commit and push changes to a fork in the original Github repository, or alternatively create a new repository and push it there.

18. On the Heroku website, login and select the app.

19. 23. Click the 'Settings' tab and add a 'SECRET_KEY' variable to the 'Config Vars' section:

    KEY = "SECRET_KEY"

    VALUE = any password or secret key of your choice.  
    
    (Note: A 'Django secret key' can be generated online for you if required. Search 'Django secret key generator' in google).

20. Click the 'Deploy' tab and in the 'Deployment Method' section select 'Connect to Github'.

21. Search for the repository and, once found, click connect.

22. In the 'Manual Deploy' section click 'Deploy Branch'.

23. Once the app has successfully deployed, click 'Enable Automatic Deploys' to allow future changes to the repository to automatically flow through to the Heroku deployment.

24. Click the settings tab again, and scroll down to the 'Domains' section. Here you will find a url for the deployed website, which can be copied and pasted into your browser address bar.

### Part 2: Amazon AWS S3  -  File storage

25.  Navigate to aws.amazon.com.

26.  Login or create an AWS account as necessary.

27. Once logged in click 'My Account', then 'AWS Management Console'.

28. Search for 'S3' in the search bar at the top of the page.

29. Create a new bucket to store the sites image files.

30. Give the bucket a name (ideally, the same as the Heroku app name).

31. Select the region closest to you.

32. Unselect 'Block all public access'.  This needs to be public to allow public access to the sites static files.

33. Click 'Create Bucket'.  The bucket will now be created and listed on the 'Buckets' page.

34. Click the bucket.

35. Click the 'Properties' tab and copy the 'Amazon Resource Name' (ARN) and save it to a notepad document or something similar as it will be needed later. It will look something like this:

    arn:aws:s3:::e-volve-retail

36. Scroll down to 'Static Website Hosting' and click the 'Edit' button, then click 'Enable', then 'Save Changes'.

37. Next, click the 'Permissions' tab.

38. Scroll to the CORS section (bottom of the page at the time of writing) and click edit.  Now paste in the following code:

    [
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]

39. Click save.

40. Scroll up to the 'Bucket Policy' section and click 'Edit'.

41. Click 'Policy Generator', and choose the following:

    Policy Type:  S3 Bucket Policy

    Effect:  Allow

    Principal:  *  (ie. type a star in the box:  shift + 8)

    Actions:  Get object

42. Now paste the 'Amazon Resource Name' (ARN) you saved earlier into the Amazon Resource Name (ARN) box.  Keep the number handy as it will be required again later.

43. Click 'Add Statement'

44. Click 'Generate Policy'

45. Copy the 'Policy JSON Document' code.

46. Go back to the Sessions Tab and Edit the 'Bucket Policy' section.

47. Delete any existing code and paste in the 'Policy JSON Document' code.

48. On the line which starts "Resource": "arn:aws:s3:::" add a "/*" to the end of the line. Eg:

    "Resource": "arn:aws:s3:::e-volve-retail/*",

49. Click Save 

50. Remain in the 'Permission's tab and up to the 'Block Public Access (Bucket Settings)' section.  Ensure this is off (click edit and ensure all the boxes are unchecked).

### Create a 'User' and 'Policy' in the 'IAM' section

51. In the search bar at the top of the Amazon AWS page, search for 'IAM' (Identity and Access Management).

52. Click on the IAM link.  You will be taken to the main IAM Dashboard.

53. In the left hand menu click 'User Groups'.

54. Click 'Create Group'.

55. Give the group a name eg. manage-evolve-retail.

56. Scroll down a click 'Create Group'.

57. Create a policy to control access to the group by clicking 'Policies' in the left-hand menu, then click 'Create Policy'.

58. Click 'JSON' tab and select 'Import managed policy'.

59. Search for 'S3'.

60. Select and import the 'AmazonS3FullAccess' policy.

61. Copy the 'ARN' number you saved earlier and paste it in to the 'Resource' section of the 'JSON' text. Eg:

    "Resource": [
        "arn:aws:s3:::e-volve-retail",
        "arn:aws:s3:::e-volve-retail/*"
    ]

    (Note: the first line gives access to the bucket. The 2nd gives access to the contents within the bucket.)

62. Click 'Review Policy'.

63. Click 'Next', then click 'Next' again.

63. Give it a name. Eg:  e-volve-retail-policy.

64. Add a description. Eg. "Access to S3 bucket for e-volve-retail static files."

65. Click 'Create Policy'.  You will be returned to the 'Policies' page where the new policy will be listed at the top.

67. Click 'User Groups' again in the left hand menu.

68. Click the group you created earlier. Eg. manage-evolve-retail.

69. Click 'Permissions'.

70. Click 'Add Permissions', then 'Attach Policies'.

71. Click the 'checkbox' to the left of the policy you just created (should be top of the list, but if not, search for the policy using the search bar.)

72. Scroll down and click 'Add Permissions'.  You will be returned to the 'user group' with a confirmation that the policy was added.

### Create a User 

73. Click 'User' in the left-hand menu.

74. Click 'Add Users'

75. Give the user a name. Eg. e-volve-retail-static-files-user.

76. Select 'Access key - Programmatic access', then click 'Next: Permissions'.

77. Click the 'Add User to Group' box then click the check-box next to the group you just created Eg. manage-evolve-retail.

78. Click 'Next: Tags', then 'Next: Review', then 'Create User'.

79. Click to download the csv (this contains the user's 'Access Key' and 'Secret Access Key')  and save it immediately.

    Important:  save the downloaded file as it cannot be downloaded again.

### Connect Django to the AWS S3 Bucket

80. Back in your IDE, select the 'settings.py' file and change the name of the bucket to the newly created bucket, and the region to your chosen region: Eg.

    AWS_STORAGE_BUCKET_NAME = 'e-volve-retail'
    AWS_S3_REGION_NAME = 'eu-west-2

81. In Heroku, click 'settings' and add the 'Access Key' and 'Secret Access Key' downloaded earlier into the config vars section:

    Key: AWS_ACCESS_KEY_ID,  Value:  Your 'access key'
    Key: AWS_SECRET_ACCESS_KEY,  Value:  Your 'secret access key'

82. Add, commit and push your changes to Github.

### Add media files to AWS S3

83. In AWS S3, select your bucket, and in the 'Objects' tab click 'Create Folder'.

84. Name the folder 'media', select 'Disable, and click 'Create Folder'.

85. The folder will appear in the list. Click and select 'Upload' and either drag and drop the product image files from a windows/mac os folder or select 'Add Files' and select the folder from there. 

    Note: you will need to download the image files from Github into a folder of your choice first.

86. Scroll down to the 'Permissions' section and select 'Grant public-read access'.

87. Click 'Upload'.  The images will now be stored in your AWS S3 bucket.

### Verify Superuser email address

88. Naviate to the Heroku deployed website using the url provided in the 'Settings' tab in Heroku.

89. Add '/admin' to the end of the url to access the Admin login screen, then login user the superuser details you provided earlier via the CLI.

90. Click the 'Email addresses' link at the top of the left-hand menu, then click your email address and tick/check 'Verified' and 'Primary'.

91. Click 'Save'.

### Add Stripe Keys

92. Log in to your Stripe account and retrieve the 'Publishable Key' and 'Secret Key'.

93. Add both keys to the Config Vars section in the Heroku settings tab:

    KEY:  STRIPE_PUBLIC_KEY,  VALUE:  Your 'Publishable Key'
    KEY:  STRIPE_SECRET_KEY,  VALUE:  Your 'Secret Key'

94. Back in Stripe, click 'Developers', then 'Webhooks', then click 'Add Endpoint'. 

95. In the endpoint url box, add the Heroku website url and add '/checkout/wh/' to the end of the url.

96. Click 'Select Events' and choose 'Select All Events', then click 'Add Events'.

97. Scroll to the bottom and click 'Add Endpoint'.

98. Click 'Reveal' under the 'Signing Secret' heading and copy the secret key.

99. Add the 'Signing Secret' to the config vars in Heroku:

    KEY:  STRIPE_WH_SECRET,   VALUE:  Your 'Signing Secret'

100. Success!  The application is now ready and fully deployed.


## Images

**Home Page**

![Home Page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/home_page_image_1.PNG)

**Products Page**

![Products Page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/products_page.PNG)

**Product Details Page**

![User Profile](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/product_details_page.PNG)

**Shopping Bag Page**

![Shopping Bag](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/shopping_bag_page.PNG)

**Submit a Review Page**

![Submit a Review](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/submit_review_page.PNG)

**Edit a Review Page**

![Edit a Review](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/edit_a_review_page.PNG)

**User's Review List - View/Edit/Delete**

![Users Reviews - View/Edit/Delete](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/user_reviews_page.PNG)

**Checkout Page**

![Checkout Page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/checkout_page.PNG)

**Order Confirmation Page**

![Order Confirmation Page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/order_confirmation_page.PNG)

**User Profile Page**

![User Profile Page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/user_profile.PNG)

**Subscribe to Newsletter page**

![Subscribe to Newsletter page](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/subscribe_to_newsletter_page.PNG)

**Create Newsletter**

![Create Newsletter](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/create_newsletter_page.PNG)

**Add New Product**

![Add New Product](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/add_new_product_page.PNG)

**Edit a Product**

![Edit a Product](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/edit_a_product_page.PNG)

**Reviews Admin Page - for superusers**

![Reviews Admin Page - for superusers](https://github.com/AndyB-WHG/e-volve-retail/blob/main/documentation_assets/live_screenshots/reviews_admin_page_for_superusers.PNG)




## Credits

* [KenBroTech](https://www.youtube.com/watch?v=hWtlskOaFNI&t=3407s) on Youtube provided inspiration and guidance in building the Newsletter and Newsletter Subscription Models and functionality.

* Marcel Mulders (Mentor) provided some assistance dealing with an issue with Stripe.

* College tutors provided invaluable assistance in dealing with a number of Django / Python issues.

* General advice regarding Python, HTML and CSS usage: https://www.w3schools.com/


### Content

* Base code is based on the Code Institute's 'Boutique Ado' project.

* Product images were provided by:  
    - [Unsplash.com](https://unsplash.com/) (9 x images)
    - [Pexels.com](https://www.pexels.com/) (3 x images)
    - [Next UK](https://www.next.co.uk/) (1 x image - Pink Jumper)
    - [Neatclean.com](https://neatclean.com/) (1 x image - Cleaning Product)

* Social Media and button icons provided by Font Awesome.

* Lato and Exo fonts provided by Google Fonts at : https://fonts.google.com/














   


