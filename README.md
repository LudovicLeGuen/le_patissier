# le-patissier

Welcome to le Patissier. This website constitutes the 5th and last portfolio project of Code Institute in order to be graduated from their Academy. This project uses Django, Javascript (jQuery), Python, CSS3, Bootstap and obviously HTML5 in ordee to build this eCommerce application. 
This website is a B2C platform allowing users to purchase professional pastry tools. <br>
Le patissier is built on products lists, browsable categories, product details, shopping basket and payments. <br>
On top of it, the site owners inntend to create a strong marketing campaign based on Facebook and Youtube.  

![Le Patissier on devices](assets/readme-files/wheel-of-fortune.PNG)

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
4. [Issues and Bugs](#Issues-and-Bugs)
5. [Technologies Used](#Technologies-Used)
     1. [Main Languages Used](#Main-Languages-Used)
     3. [Frameworks, Libraries & Programs Used](#Frameworks,-Libraries-&-Programs-Used)
6. [Testing](#Testing)
     1. [Testing.md](TESTING.md)
7. [Deployment](#Deployment)
     1. [Deploying on GitHub Pages](#Deploying-on-GitHub-Pages)
8. [Credits](#Credits)
     1. [Media](#Media)
     2. [Code](#Code)
9. [Acknowledgements](#Acknowledgements)
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
The website is built for 2 types of users
Buyers who want quality products and intend to spend on reviewed products.
People coming from the Social media 

### User-Stories
#### Frequent User Goals
* Frequent users want to see the recipes they have created and collected
* Frequent users want to log in with their usual credentials
* Frequent users want to see other users recipes
* Frequent users want to manage their FoodyBook

#### New User Goals
* New Users want to be able to see some of the content before registering
* New users want to understand what the site is about within seconds
* New users want to understand the functionalities quickly.

#### Site Administrators
* The admnistrators needs to control all aspects of the site
* The admins can remove users
* The admins need to moderate comments
* The admon needs to navigate between the site and admin easily.

#### Development Methodology
* The development followed an Agile methodology on the [Foody Book github Project](https://github.com/users/LudovicLeGuen/projects/4 "Link to the Foody Book github Project")

<details>
<summary>![Github project](assets/readme-files/images/project.png)</summary>
![Github project](assets/readme-files/images/project.png)
</details> 

* All project database was base on the following Database Shema.

<details>
<summary>![Database Schema](assets/readme-files/images/project.png)</summary>
* All project database was base on the following Database Shema.
![Database Schema](assets/readme-files/images/myFoodyBook.png)

[Back to top ⇧](#le-patissier)

</details>
### Development-Planes

The website has to answer the aforementioned needs of all users types and therefore must contain a a variety of CRUD finctionality for the recipes and a user profile management system. Furthrmoe, a simple yet intuitive collection method of recipe must be omplemented. Finally, an interactivity must be created trhough a comment section.


#### Strategy
The website will focus on the following target audience
* Audience
    * New Users
    * Frequent users
    * Food lovers with creativity
    * Curious people 
    * Serious cooks with the need to store content.
    
* Demographic
    * Adults 
    * Young adults
    * Independant adults
    * Beginner cooks
    * Artistic and creative people
    
* Psycho Characteristics
    * Sociable
    * Epicurian
    * Curious
    * Food knowledge

* The Users must find thisinformation:
    * The name of the recipe
    * The time it takes to cook it
    * The ingredients
    * The number of people it feeds
    * The steps to cook the dish
    * A picture of the dish
    * The number of people who collected it
    * The author of the recipe
    * The profile of the author
    * The possibility to Log in Log out or register
    * the possibility to post comments
    * A view of the previous comments

    
* The Administrator has to receive these information:
    * The name of the users
    * The profile of the users
    * The Recipes
    * The comments
    * the possibility to delete and manage all of the above

[Back to top ⇧](#le-patissier)

#### Scope

Now that we have established the goals of the website we can deduce the necessary features and content:
* Required Content
    * A quick description of the purpose of the site
    * Recipes by users 
    * Users profile

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
   2. **A Foodybook page** with your created and collected recipes.
   3. **A Register page** to register on the site.
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
    
![Homepage](assets/documentation/wireframes/landing-page.png)

</details> 

<details>
<summary>All products page</summary>
    
![Homepage](assets/documentation/wireframes/product-page.png)

</details> 

<details>
<summary>Product Details</summary>
    
![Landing-Page](assets/documentation/wireframes/product-details.png)

</details> 

<details>
<summary>My Foody Book page no recipe</summary>
    
![L](assets/readme-files/images/wireframes/Home-My-Foody-book-no-recipe.png)

</details> 

[Back to top ⇧](#le-patissier)

### Design
#### Colour Scheme

The color scheme used was kept as simple as possible with the use of Bootstrap colors.
In fact the color scheme is derived from the landing page image.
<details>
<summary>Palette</summary>
![Foody-book](assets/documentation/palette/palette-patissier.png)
</details>

Favicon

<details>
<summary>Favicon</summary>
![Foody-book](assets/readme-files/images/favicon.png)
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
![Le Patiissier](assets/documentation/features/)

* The logged out navbar
![Le Patiissier](assets/documentation/features/)

* The profile navbar
![Le Patiissier](assets/documentation/features/)

* The admin navbar
![Le Patiissier](assets/documentation/features/)

* The small device navbar
![Le Patiissier](assets/documentation/features/)

* The expanded navbar
![Le Patiissier](assets/documentation/features/)


#### Landing Page

* Landing Page 
![Le Patiissier](assets/documentation/features/)

#### Footer company section

* Footer company section 
![Le Patiissier](assets/documentation/features/)

#### Footer Legal Section

* Footer Legal Section 
![Le Patiissier](assets/documentation/features/)

#### Footer Brands links

* Footer Brands links 
![Le Patiissier](assets/documentation/features/)

#### Footer Social links

*  Footer Social links 
![Le Patiissier](assets/documentation/features/)

#### Newsletter 

* Newsletter 
![Le Patiissier](assets/documentation/features/)

#### Why Us? Section

* Why Us? Section 
![Le Patiissier](assets/documentation/features/)

#### Search field

* Search field 
![Le Patiissier](assets/documentation/features/)

#### Categories Section

* Categories Section 
![Le Patiissier](assets/documentation/features/)

#### Sort section

* Sort section 
![Le Patiissier](assets/documentation/features/)

#### All products page

* Product Card
![Le Patiissier](assets/documentation/features/)

#### Product details page

* Product Brand link
![Le Patiissier](assets/documentation/features/)

* Product Description
![Le Patiissier](assets/documentation/features/)

* Product Price
![Le Patiissier](assets/documentation/features/)

* The comment section in the product section
![Le Patiissier](assets/documentation/features/)


#### All brands page

* All brands page
![Le Patiissier](assets/documentation/features/)

#### My Basket Page

* My Basket Page 
![Le Patiissier](assets/documentation/features/)

#### Checkout Page

* Checkout Page 
![Le Patiissier](assets/documentation/features/)

#### Basket Snippet

* Basket snippet 
![Le Patiissier](assets/documentation/features/)

#### Message box

* Message box 
![Le Patiissier](assets/documentation/features/)

[Back to top ⇧](#le-patissier)

### Features to Implement in the future

The website would need the following features in the feature:
* A wishlist
* More categories such as ingredients
* A recipe section
* More pictures for each products
* A coupon system


[Back to top ⇧](#le-patissier)

## Issues and Bugs 
The development of the site was a continuous chain of bug and issues. The recording of those issues would probably be longer than the actual development (which took foerver BTW). 
Issues were mainly writing errors that threw minors errors, or tiny mistakes in the HTML. Nevertheless, here are the main issues that the developper encountered.

**The hero page would not stay centered**
The developper has decided to use a single hero page for all the messages on the site. The page had to fully cover the page and have a singfle centered jumbotron contianing the message. 
The Page has oftentimes been a challenge because of the placement of the div inthe HTML. Each HTML contains several if statements and having the jumbotron before, inside or outisde those statements made a differnce. 

**Bootstrap would not respond in certain pages**
It took sometime for the developper to understand Bootstrap and apply it confidently. ine of the main issues the developper had was understanding the necessaity of the first row. This hard erned lesson cost him several trials and waste of time on debugging. 

**Passing information between apps**
The developper has decided to have two apps for the website: 
-publish
-users
Passing information on template using the 2 apps has been particularly diificult for the developper. Several Tutoring intervention were necessary. So much so that the developement has not been completed and more work remains. The time management has been a real struggle for the deelopper. 

### Unfixed Bugs 

There are 3 bugs known to the developper.
**The user avatar** 
The logged in user avatar in the top right corner changes when a recipe author avatar on a recipe card is a placeholder. The bug is understood. Both user avatar and author avatar are ruled by the exact same if statement. If a placeholder is in the object image field, a default picture appears. 

**Recipe duplicates** 
When a user consults a foody booker profile, some recipes might be dupliacted. This is due to the number of times a r3ecipe has been collected. If the recipe is collected 2 times, the card appears twice. If the recipe is collected 3 times, it appears 3 times and so on. 
The class based function filtering the query has been a challenge for the developper. Even though the developper went through tutoring for a fix, he could not find the solution. 

**User profile redirection**
The developper simply did not have time to incorporate a sound variable passing in each page through class based functions of the author recipe. 
As such, only the Users page redirects to the correct foodybooker. 
The authors avatars on each recipe card are actually bugged. They all redirect to the logged in user. 


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
* cloudinary_storage',
* django_summernote',
* django.contrib.staticfiles',
* cloudinary',
* crispy_forms',
* django_extensions',
* publish',
* users',

[Back to top ⇧](#le-patissier)

## Testing
Refer to this [page](TESTING.md) please

## Deployment
The site was developped on Codeanywhere, commiting and pushing to github.

### Deploying on Heroku
Deploying on Heroky required the following:

* Type "pip freeze > requirements.txt" in your Github terminal to update the requirements.txt file with the list of dependencies used in the project . Save, commit and push.

* Create an Heroku account, select Python as the 'Primary development language'.

* Open the email sent to your address and click the link to verify your email address. Follow the instructions to create a password and log in.

* Click the 'create new app' button on the dashboard. Name your app, select your region and click 'Create App'

* In the "Settings" tab, add both the python and node.js build packs.

* Create a "Config VAR" named 'CREDS' KEY and copy/paste the creds.json file in it.

* Create another "Config VAR" called PORT as the KEY with 8000 as VALUE.

* In the "Deploy" tab, choose GitHub as a deployment method.

* Search for the wanted repository.

* Click on "enable automatic deploys" and then deploy branch.

* once the app built (a minute or two needed)click "View" to access the site.
   
## Credits 
### Code 
The developer has consulted countless times Stack Overflow and W3Schools in order to build the website.
The development choices were HEAVILY inspired by [Viva la nacho](https://viva-la-nacho.herokuapp.com/ "Viva la nacho ") by Matthey Hurrell, a fellow Code Institute student.
Also, The Code Institute "i Think Therefore I blog" course was a solid reference. 

[Back to top ⇧](#le-patissier)

## Acknowledgements
I would like to thank:
* My wife Dominika for her patience, support and tests to help me do as much as I could between my 3 jobs. 
* My fellow coding students of Code institue who have been invaluable on Slack.
* And last but most definitely not the least.... TUTORING!!!!!! I would not have made it without them.

[Back to top ⇧](#le-patissier)

***