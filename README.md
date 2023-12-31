# le-patissier

Welcome to le Patissier. This website constitutes the 5th and last portfolio project of Code Institute in order to be graduated from their Academy. This project uses Django, Javascript (jQuery), Python, CSS3, Bootstap and obviously HTML5 in order to build this eCommerce application. 
This website is a B2C platform allowing users to purchase professional pastry tools. <br>
Le patissier is built on products lists, browsable categories, product details, shopping basket and payments. <br>
On top of it, the site owners inntend to create a strong marketing campaign based on Facebook and Youtube.  

![Le Patissier on devices](documentation/features/amiresponsive.PNG)

[Click here to access live project](https://le-patissier-b2d63743796c.herokuapp.com/)
## Table of contents
1. [Introduction](#Introduction)
2. [UX](#UX)
    1. [Ideal User Demographic](#Ideal-User-Demographic)
    2. [User Stories](#User-Stories)
    3. [Development Planes](#Development-Planes)
    4. [Design](#Design)
3. [Features](#Features)
    1. [Design Features](#Design-Features) 
    2. [Existing Features](#Existing-Features)
    3. [Features to Implement in the future](#Features-to-Implement-in-the-future)
4. [Business Model](#Business-Model)
    1. [Marketing Strategy](#Marketing-Strategy)
    2. [SEO](#SEO)
5. [Issues and Bugs](#Issues-and-Bugs)
6. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     2. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
7. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
8. [Deployment](#Deployment)
     1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
9. [Credits](#Credits)
     1. [Media](#Media)
     2. [Code](#Code)
10. [Acknowledgements](#Acknowledgements)
***

## Introduction
Le Patissier is the 5th and last project for Code Institute's full stack development degree.
The minimum requirements of this project are:
* Building an E-commerce platform
* Use of Search Engine Optimization on the website
* Insert Web Marketing strategies
* Insert a robot.txt file
* Insert a sitemap.xml
* Descriptive metatags
* Creating a Facebook page
* Incorporating a newsletter
* Providing a business model
* Have at least 3 original models
* Implement a custom 404 page
* Show and use an agile methodlogy throughout the project

[Back to top ⇧](#le-patissier)

## UX
### Ideal User Demographic
The users targeted have to enjoy baking and most of all have to be serious about it.
The website is built for 3 types of users:
* First time user who want to see what products we have and at what price
* Recurrent Buyers
* The site admins

### User-Stories
#### Recurrent Buyer Goals
* Log in and see their profile
* Find their favorites products
* Browse the catalog and find the correct products
* Save their info to speed payments process

#### New User Goals
* New Users need to understand the site easily
* New Users need to browse content quickly
* New Users want to experience the site 
* new Users want to feel secure to make a first purchase

#### Site Administrators
* The admnins need to control all aspects of the site
* The admins need to moderate comments
* The admin need to create edit and delete products, categories, and brands
* The admin need to navigate between the site and admin easily.

#### Development Methodology
* The development followed an Agile methodology on the [le Patissier github Project](https://github.com/users/LudovicLeGuen/projects/6 "Link to Le Patissier github Project")

<details>
<summary>Agile board</summary>

![Github project](documentation/methodology/agile.PNG)
</details> 

* All project database was base on the following Database Shema.

<details>
<summary>Database Schema</summary>

![Database Schema](documentation/methodology/le-patissier-db-schema.png)

[Back to top ⇧](#le-patissier)

</details>
### Development-Planes

The website has to answer the aforementioned needs of all users types and therefore must contain a variety of CRUD functionality for the products and a user profile management system. Furthermore, a simple yet intuitive payment system must be implemented. Users might also want to subscribe to see the new products. Finally, a review section is imperative.


#### Strategy
The website will focus on the following target audience
* Audience
    * New Users
    * Frequent users
    * Pastry enthusiasts
    * Curious people 
    
* Demographic
    * Adults 
    * Young adults
    * Independant adults
    * Professional chefs
    * Artistic and creative people
    
* Psycho Characteristics
    * Epicurian
    * Curious

* The Users must find this information:
    * The name of the categories
    * The name of the products
    * The price of the products
    * The Brand
    * The picture of the product
    * The review of the product
    * All product by categories for comparaison
    * A shopping basket
    * Total to pay
    * The possibility to Log in Log out or register
    * The possibility to post reviews
    * The possibility to subscribe to a newsletter
    * Clear validation of their actions
    * The legal statements of the company

    
* The Administrator has to receive these information:
    * The profile of the users
    * The products
    * the Brands
    * The Categories
    * The review
    * the possibility to delete and manage all of the above

[Back to top ⇧](#le-patissier)

#### Scope

Now that we have established the goals of the website we can deduce the necessary features and content:
* Required Content
    * A quick description of the purpose of the site
    * A full product information card 
    * Users profile
    * Legal neceesities
    * Payment information

* Required functionality
    * A form to register
    * A form to login with the same credentials
    * A form to log out
    * An automatic profile creation
    * A form to update a profile
    * A page to show a profile
    * a page to show all profiles
    * A form to create a recipe
    * A form to update a recipe
    * A form to delete a recipe
    * A Page to display all recipes
    * A method to collect a recipe
    * A method to discard a recipe
    * A method to comment a recipe
    * An administration to manage the site

[Back to top ⇧](#le-patissier)

#### Structure

The website will consist of 12 pages. 

   1. **A Home page** with the purpose of the site for first users and the recipe content or the logged in users.     
   2. **An all products page** with all products
   3. **A product detail page** to register on the site.
   4. **A Log in page** to log in with your credentials.
   5. **A log out page** to confirm if users want to leave.
   6. **A profile page** to show your Bio and your recipe too.This will act as the user foodybook
   7. **An update profile page** to change your bio
   8. **An all users page** to show all users.
   9. **An create recipe page** to create your recipes
   10. **An update recipe page** to update your recipes
   11. **A delete recipe page** to confirm your action
   12. **An admin page** for admins

With the needed structure defined the developper has created the following Wireframes.

[Back to top ⇧](#le-patissier)

### Skeleton

With the structure above the designer has created the following wireframes on [Balsamiq Wireframes](https://balsamiq.com) to visualize the website. The developper, being also the designer, took the wireframes as a base and took the initiative to modify certain things along the way.

<details>
<summary>Home Page</summary>
    
![Homepage](documentation/wireframes/landing-page.png)

</details> 

<details>
<summary>All products page</summary>
    
![Homepage](documentation/wireframes/product-page.png)

</details> 

<details>
<summary>Product Details</summary>
    
![Landing-Page](documentation/wireframes/product-details.png)

</details> 

<details>
<summary>All Brands</summary>
    
![Landing-Page](documentation/wireframes/brands.png)

</details> 

[Back to top ⇧](#le-patissier)

### Design
#### Colour Scheme

The color scheme used was kept as simple as possible with the use of Bootstrap colors.
In fact the color scheme is derived from the landing page image.
<details>
<summary>Palette</summary>

![Le Patissier](documentation/palette/palette-patissier.png)

</details>

Favicon
<details>
<summary>Favicon</summary>

![Le Patissier](static/favicon/android-chrome-192x192.png)

</details>
 
#### Typography
The developper has chosen Roboto from [Google Fonts](https://fonts.google.com/).


#### Imagery
The images used on the website are sourced from various websites which are listed in the [Credits section](##Credits) of this README.

[Back to top ⇧](#le-patissier)


## Features
### Existing 

#### Navbar

* The logged in navbar

![Le Patissier](documentation/features/the-logged-in-navbar.JPG)

* The logged out navbar

![Le Patissier](documentation/features/the-logged-out-navbar.JPG)

* The profile navbar

![Le Patissier](documentation/features/the-profile-navbar.JPG)

* The admin navbar

![Le Patissier](documentation/features/the-admin-navbar.JPG)

* The small device navbar

![Le Patissier](documentation/features/the-small-device-navbar.JPG)

* The expanded navbar

![Le Patissier](documentation/features/the-expanded-navbar.JPG)


#### Landing Page

* Landing Page 

![Le Patissier](documentation/features/landing-page.JPG)

#### Footer 

* Footer company section 

![Le Patissier](documentation/features/footer-company-section.JPG)


* Footer Legal Section 

![Le Patissier](documentation/features/footer-legal-section.JPG)


* Footer Brands links 

![Le Patissier](documentation/features/footer-brands-links.JPG)


*  Footer Social links 

![Le Patissier](documentation/features/footer-social-links.JPG)

#### Newsletter 

* Newsletter 

![Le Patissier](documentation/features/newsletter-1.JPG)
![Le Patissier](documentation/features/newsletter-2.JPG)

#### Why Us? Section

* Why Us? Section 

![Le Patissier](documentation/features/why-us-section.JPG)

#### Search field

* Search field 

![Le Patissier](documentation/features/search-field.JPG)

#### Categories Section

* Categories Section 

![Le Patissier](documentation/features/categories-section.JPG)

#### Sort section

* Sort section 

![Le Patissier](documentation/features/sort-section.JPG)

#### All products page

* Product Card

![Le Patissier](documentation/features/product-card.JPG)

#### Product details page

* Product Brand link

![Le Patissier](documentation/features/product-brand-link.JPG)

* Product Description

![Le Patissier](documentation/features/product-description.JPG)

* Product Price

![Le Patissier](documentation/features/product-price.JPG)

* The comment section in the product section

![Le Patissier](documentation/features/comment-section.JPG)


#### All brands page

* All brands page

![Le Patissier](documentation/features/all-brands-page.JPG)

#### My Basket Page

* My Basket Page 

![Le Patissier](documentation/features/my-basket-page.JPG)

#### Checkout Page

* Checkout Page 

![Le Patissier](documentation/features/checkout-page.JPG)

#### Basket Snippet

* Basket snippet 

![Le Patissier](documentation/features/basket-snippet.JPG)

#### Message box

* Message box 

![Le Patissier](documentation/features/message-box.JPG)

[Back to top ⇧](#le-patissier)

### Features to Implement in the future

The website would need the following features in the feature:
* A wishlist
* A favorite products page
* More categories such as ingredients
* A recipe section
* More pictures for each products
* A coupon system


[Back to top ⇧](#le-patissier)

## Business Model
This website follows a B2C model. It sells pastry related products directly to the customer. The Users can very quickly create a basket of products and get enticed to spend money. The Website advertises that the company is the exclusive supplier for renowned professional brands. The entire strategy is build on strong Facebook and youtube presence and also on a more traditional approcah with newsletter subscription. 

### Marketing Strategy

#### Social Media

Le patissier intends to have a strong social footmark and will achieve this with 2 main medias:
Facebook 
Youtube

Both medias will be regularly fed with recipes, tests and also announcememts. 
Youtube will most probablyy the most time consuming element of the strtegy and perhaps also the most expensive. But the reputation and the authority gained is worth the investment.

![Le Patissier](documentation/marketing/lepatiisieryoutube.png)
![Le Patissier](documentation/marketing/lepatissiefb.jpg)
![Le Patissier](documentation/marketing/lepatissierfb2.jpg)

The newsletter is also a strong (and necessary) tool. 
A frequency of 1 newsletter per month is a good start. 

### SEO

The developper has chosen his key meta words based on [worTracker](https://www.wordtracker.com/search)
A sitemap and a robot.txt file were also included during the development


[Back to top ⇧](#le-patissier)


## Issues and Bugs 
Apart from the classical small issues such as mispelling in the code or omission to add urls that threw usual errors, the developper encountered some puzzling issues.

**Newsletter.html would not appear**
The developper intended to include a newsletter from in the footer by using Django tags.
Unfortunately, for a reason that the developper still ignores, the footer would not load with the tags in it. 
The developper had to compromise and create a button to redirect the user to the rendered newsletter.html page

**Discrepancies between IDE and Production**
The developper realized that the production site would not laod the landing page picture properly after the deployment to heroku.
It took the developpper several days and the help of tutors to understand that the project was build and deployed on 2 different databases. After connecting the correct database to the developement environment, the problem was gone.

**Showing all the brands and their products**
The developper wanted to have a page with all Brands neatly represented and the possibility to click on any to show the related products. 
The developper struggled to make it work. 
The view did retrieve the correct data from the database, but the developper did not understand without the help of Tutoring that he needed to create anoth page in which to render the products according to the brand. 

### Unfixed Bugs 

**Decrement and increment button**

In the Product detail page it is still possibleto add a negative amount of products in the large screen view.
It is a JS problem. In essence, the problem is not catastrophic since having a negative amount of products simply removes the product and does not affect the Total amount to pay but it definitely is a bad user experience.
The developper simply did not have enough time to correct it. 

[Back to top ⇧](#le-patissier)

## Technologies Used
### Main Languages Used
* HTML5
* CSS3
* Python
* Javascript

### Framework
* Django
* Bootstrap

### Sofwares
* [Heroku](https://heroku.com/ "Link to Heroku") was used to deploy the website.
* [CodeAnywhere](https://app.codeanywhere.com/ "Link to Codeanywhere homepage") was used for writing, commiting, and pushing code.
* [GitHub](https://github.com/ "Link to GitHub") was used as repository of the site.
* [Am I Responsive?](http://ami.responsivedesign.is/# "Link to Am I Responsive Homepage") was used to verify responsiveness and to create the top picture of this README.md
* [ElephantSQL](https://customer.elephantsql.com/ "Link to ElephantSQL") was used as a PostgreSQL database.
* [Balsamiq](https://balsamiq.com// "Link to balsamiq") was used for wireframes.
* [Slack](https://slack.com/ "Link to Slack") was used to communicate with my fellow Code institute students and alumni.
* [Lucid-Charts](https://lucid.app/documents#/documents?folder_id=recent"Link to Lucid Charts) was used to create the database schemes.
* [Google-Fonts](https://fonts.google.com/ "Link to google font") was used to get the Roboto font.
* [Google-dev-tools](https://heroku.com/ "Link to google dev tools") was used to test, develop and debug thes site on the fly.
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/ "Link to Lighthouse") was used to test performances and compliance.
* [Coolors](https://coolors.co/ "Link to Coolors") was used to create a palette based on the landing page picture.

### Libraries
* django.contrib.admin
* django.contrib.auth',
* django.contrib.contenttypes',
* django.contrib.sessions',
* django.contrib.messages',
* django.contrib.sites',
* allauth',
* allauth.account',
* allauth.socialaccount',
* django_storage',
* django.contrib.staticfiles',
* pillow',
* crispy_forms',
* crispy bootstrap,
* django_extensions',
* stripe,
* django-countrie,
* gunicorn,
* mailchimp-marketing,


[Back to top ⇧](#le-patissier)

## Testing
Refer to this [page](TESTING.md) please.

## Deployment
The site was developped on Codeanywhere, commiting and pushing to github.

### Deployment guide
Refer to this [page](deployment.md) please.
   
## Credits 
### Code 
The developer has consulted countless times Stack Overflow and W3Schools in order to build the website. 
<br>
The development choices were HEAVILY inspired by Boutique Ado, the code instute walkthrough website.
<br>
Also, several fellow students PP5 works were consulted for inspirations purposes but the work by [Victoria Traynor](https://github.com/VictoriaT87/level_up_loot_vt/tree/main) has been particularly admired by the developper.
<br>
In fact the deployment.md page has been simply copy pasted from her github: [deployment guide of victoria](https://github.com/VictoriaT87/level_up_loot_vt/blob/main/documentation/deployment.md). When you can't make it better, copy it! All credits goes to her on this one. 
<br>
All content for the website has been copied from the French website [Le Meilleur du chef](https://www.meilleurduchef.com/) All pictures, descriptions and details of the products are a direct copy of their website. The developper does not have any intention to sell these products. This website is purely educational in scope. 


[Back to top ⇧](#le-patissier)

## Acknowledgements
I would like to thank:
* My Dear wife Dominika for her patience, support and tests to help me do as much as I could between my 3 jobs. 
* My fellow coding students of Code institue who have been invaluable on Slack.
* And last but most definitely not the least.... TUTORING!!!!!! I would not have made it without them.
* Finally, a huge thank you to Code Institute for building such a great learning platform. I am so grateful. I thank the ENTIRE team from the bottom of my heart.

[Back to top ⇧](#le-patissier)

***