
# Le Patissier - Testing Documentation

![TaW Devices](https://github.com/PPindel/test-a-wheel/assets/114284732/297cc3b7-e11e-4e0a-a9aa-81a7420abdf6)

Below is the documentation of my testing process.

## Table of contents
- [Test a Wheel - Testing Documentation](#test-a-wheel---testing-documentation)
  * [Table of contents](#table-of-contents)
  * [Validation Testing](#validation-testing)
    + [CSS](#css)
    + [JavaScript](#javascript)
    + [Python](#python)
  * [Visual (UI) Testing: Cross Browser and Cross Device Testing](#visual--ui--testing--cross-browser-and-cross-device-testing)
  * [Lighthouse](#lighthouse)
      - [Desktop Results](#desktop-results)
      - [Mobile Results](#mobile-results)
  * [Manual Testing](#manual-testing)
  * [Defensive programming testing](#defensive-programming-testing)
    + [Testing User Stories](#testing-user-stories)
  * [Outstanding Defects](#outstanding-defects)
  * [Defects of Note](#defects-of-note)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Validation Testing
[W3C](https://validator.w3.org/) was used to validate all pages HTML and CSS of Le Patissier site. 

All Brands Page:
![all-brands-valid](documentation/testings/images/validator/html/all-brands-validator.PNG)

All Products page:
![all-products-valid](documentation/testings/images/validator/html/all-products-validator.PNG)

Checkout success page:
![checkout-success-valid](documentation/testings/images/validator/html/checkout-success-validator.PNG)

Checkout page:
![checkout-valid](documentation/testings/images/validator/html/checkout-validator.PNG)

Contact us page:
![contact-valid](documentation/testings/images/validator/html/contact-validator.PNG)

Error 404 page:
![eror404-valid](documentation/testings/images/validator/html/eror404-validator.PNG)

Our Guarantee page:
![guarantee-valid](documentation/testings/images/validator/html/guarantee-validator.PNG)

Landing page:
![landing-page-valid](documentation/testings/images/validator/html/landing-page-validator.PNG)

Legal page:
![legal-valid](documentation/testings/images/validator/html/legal-validator.PNG)

Login page:
![login-valid](documentation/testings/images/validator/html/login-validator.PNG)

logout page:
![logout-valid](documentation/testings/images/validator/html/logout-validator.PNG)

One Brand page:
![one-brand-valid](documentation/testings/images/validator/html/one-brand-validator.PNG)

Privacy Policy page:
![privacy-policy-valid](documentation/testings/images/validator/html/privacy-policy-validator.PNG)

Product details page:
![product-details-valid](documentation/testings/images/validator/html/product-details-validator.PNG)

Profile page:
![profile-valid](documentation/testings/images/validator/html/profile-validator.PNG)

Register page:
![register-valid](documentation/testings/images/validator/html/register-validator.PNG)

Terms Conditions page:
![terms-conditions-valid](documentation/testings/images/validator/html/terms-conditions-validator.PNG)


### CSS

[W3C](https://validator.w3.org/) was used to validate the CSS. 

Static CSS file:
![static-css-valid](documentation/testings/images/validator/css/css-validator.PNG)

Profile CSS file:
![profile-css-valid](documentation/testings/images/validator/css/profile-css-validator.PNG)


### JavaScript

[JS Hint](https://jshint.com/) was used to validate the JavaScript.

JS Stripe file:
![js-hint-stripe-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/02c185be-f605-4172-b388-4dad8c3509fe)


### Python

[Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python.

Blog admin py:
![blog-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/1bb8ef58-3597-4739-8c92-116e58810fe1)

Blog models py:
![blog-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/39308b0b-acf5-408b-b41e-e828059c1c4b)

Blog views py:
![blog-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/45d6751c-3c22-4e74-9d09-ca6553c88254)

Cart contexts py:
![cart-contexts-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/531f7a09-8e04-451d-a12d-0cbef04ff6ec)

Cart views py:
![cart-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/54a10889-656c-4e3f-b4c5-dd6c1cb8dde5)

Checkout admin py:
![checkout-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/5406d88b-e6db-4654-a848-19a585d78bff)

Checkout forms py:
![checkout-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/51e5746d-dd82-4577-85f5-da60eb9a3e97)

Checkout models py:
![checkout-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/70620fca-f9f9-4c7f-87bd-97541c8fb3d0)

Checkout views py:
![checkout-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/daf72e0f-c292-4dfa-bacf-2dc4d52d43cf)

Checkout webhook handler py:
![checkout-webhook-handler-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/861dc931-5a8d-47eb-bdf2-aca6fca8a745)

Checkout webhooks py:
![checkout-webhooks-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/e61fc8c0-bb62-4711-acfc-a3aec730b089)

Home views py:
![home-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/fed654dd-987f-45be-95d8-b26d96930ddb)

Products admin py:
![products-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/7d648d4e-c238-4301-b7b0-ee24fbac8bca)

Products forms py:
![products-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/b4d42307-12c4-4892-8cd2-1cd64d6922cf)

Products views py:
![products-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/6eed62b6-cd6a-4512-9937-b7c966482ea9)

Profiles forms py:
![profiles-forms-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/c14a1a5a-2d29-4314-b3f7-916c6c26b9dc)

Profiles models py:
![profiles-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/1a1f2d2c-c837-4a7e-98f6-630c25f1a04f)

Profiles views py:
![profiles-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/8b63f61d-1da8-433d-8381-d17167bbe040)

Reviews admin py:
![reviews-admin-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/07e8dd9f-fa68-4eb5-af25-697cc3668375)

Reviews models py:
![reviews-models-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/cf720354-524d-41d0-b3ce-57acd7d51d25)

Reviews views py:
![reviews-views-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/bef79bf3-7f00-43d4-a66f-2398e3d8549a)

Test a Wheel settings py:
![test-a-wheel-settings-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/169e2507-d508-442e-a6f9-697b169c946e)

Test a Wheel urls py:
![test-a-wheel-urls-python-valid](https://github.com/PPindel/test-a-wheel/assets/114284732/8f1e5575-ab4e-4307-8607-827f3147b4b2)

## Lighthouse

For the performance, accessibility, best practices, and SEO of the site for mobile and desktop I used the Chrome Lighthouse tool:

#### Desktop Results

Index Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6ac84fc1-a0dc-494a-9335-aafd7a031b5d)


Services Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/16b4f0b9-bea9-41df-9aba-8a48e237f12e)


User Profile:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/c9f45fbb-14d3-4980-b90a-07ef7f90df29)


Blog Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/7f87c0b6-54c5-48ab-91f0-98a0406414d7)


Reviews Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/d0ed979c-84ba-4356-ab2f-a463552adf05)


Checkout Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/0dacd201-2493-445f-8360-4104391854ff)


- Desktop performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)

#### Mobile Results

Index Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/6e75fbb3-95f4-40fc-a007-a135afade965)


Services Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/063f0293-69d3-4cb4-8b5d-f64d44aeb1e9)


User Profile:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/a5635fbf-2b7d-41b8-bf54-52636865f78d)


Blog Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/515248ef-64ac-46e3-8966-afaf264e2d57)


Reviews Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/ed2f9137-865a-43a7-8d7e-16c485116747)


Checkout Page:
![image](https://github.com/PPindel/test-a-wheel/assets/114284732/422b7b3d-e781-40c5-97df-2fb450d678b7)


- Mobile performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)

## Manual Testing

This table shows all the manual testing done for the website, and whether it worked as expected or not.

### General

#### Navbar

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar responsiveness | NavBar resizes according to devices | As expected | Pass

<details>
<summary>NavBar responsiveness</summary>

![NavBar responsiveness](documentation/testings/images/navbar/navbar-responsiveness-1.JPG)
</details>

<details>
<summary>NavBar responsiveness</summary>

![NavBar responsiveness](documentation/testings/images/navbar/navbar-responsiveness-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar categories responsiveness| Categories become burger menu | As expected | Pass

<details>
<summary>NavBar categories responsiveness</summary>

![NavBar categories responsiveness](documentation/testings/images/navbar/navbar-categories-responsiveness-1.JPG)
</details>

<details>
<summary>NavBar categories responsiveness</summary>

![NavBar categories responsiveness](documentation/testings/images/navbar/navbar-categories-responsiveness-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar categories hover opening| Categories menus open and close on hover with screens above 992px | As expected | Pass

<details>
<summary>NavBar categories hover opening</summary>

![NavBar categories hover opening](documentation/testings/images/navbar/navbar-categories-hover-opening.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Search field | Search field transforms in button with medium screens and lower | As expected | Pass

<details>
<summary>Search field</summary>

![Search field](documentation/testings/images/navbar/search-field-1.JPG)
</details>

<details>
<summary>Search field</summary>

![Search field](documentation/testings/images/navbar/search-field-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Search | Inserting a term gives a list of products | As expected | Pass

<details>
<summary>Search</summary>

![Search]()
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Account icon | Account icon opens on click only | As expected | Pass

<details>
<summary>Account icon</summary>

![Account icon](documentation/testings/images/navbar/account-icon-on-one-click.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Account icon | Account icon is different for logged in admins and users | As expected | Pass

<details>
<summary>Account icon</summary>

![Account icon](documentation/testings/images/navbar/account-icon-admin-login.JPG)
</details>

<details>
<summary>Account icon</summary>

![Account icon](documentation/testings/images/navbar/account-icon-user-login.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Account icon | Account icon shows log in and register for unlogged users | As expected | Pass

<details>
<summary>Account icon</summary>

![Account icon](documentation/testings/images/navbar/account-icon-unlogged-users.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Shopping basket | redirects to the shopping basket template | As expected | Pass

<details>
<summary>Shopping basket</summary>

![Shopping basket](documentation/testings/images/navbar/shopping-basket.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Action messages | messages appears on the top right corner consistenly | As expected | Pass

<details>
<summary>Action messages</summary>

![Action messages](documentation/testings/images/navbar/action-messages.JPG)
</details>


#### Footer

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Footer responsiveness | Footer layout changes according to devices | As expected | Pass

<details>
<summary>Footer responsiveness</summary>

![Footer responsiveness](documentation/testings/images/footer/footer-responsiveness-1.JPG)
</details>

<details>
<summary>Footer responsiveness</summary>

![Footer responsiveness](documentation/testings/images/footer/footer-responsiveness-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Footer links | All external links open a new tab in the browser | As expected | Pass

<details>
<summary>Footer links</summary>

![Footer links ](documentation/testings/images/footer/footer-links-1.JPG)
</details>

<details>
<summary>Footer links</summary>

![Footer links ](documentation/testings/images/footer/footer-links-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Footer links | All links redirects to the correct brand | As expected | Pass
Footer brands and legal links | Links are underlined on hover | As expected | Pass

<details>
<summary>Footer brands and legal links</summary>

![Footer brands and legal links](documentation/testings/images/footer/footer-brands-and-legal-links.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Newsletter button | Button redirects to Newsletter registration form | As expected | Pass

<details>
<summary>Newsletter button</summary>

![Newsletter button](documentation/testings/images/footer/newsletter-button.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Newsletter button hover | Button changes color on hover | As expected | Pass

<details>
<summary>Newsletter button hover</summary>

![Newsletter button hover](documentation/testings/images/footer/newsletter-button-hover.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Newsletter button responsiveness | Enveloppe icons dissapear on screens snmaller than 347px | As expected | Pass

<details>
<summary>Newsletter button responsiveness</summary>

![Newsletter button responsiveness](documentation/testings/images/footer/newsletter-button-responsiveness.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Contact button | Button redirects to contact us form | As expected | Pass

<details>
<summary>Contact button</summary>

![Contact button](documentation/testings/images/footer/contact-button.JPG)
</details>

<br>

### Landing Page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Hero image resizes on mobile | Images resize on mobile | As expected | Pass

<details>
<summary>Hero image resizes on mobile</summary>

![Hero image resizes on mobile](documentation/testings/images/landing_page/hero-image-resizes-on-mobile.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Title size reduces on smaller screens | Title gets smaller | As expected | Pass

<details>
<summary>Title size reduces on smaller screens</summary>

![Title size reduces on smaller screens](documentation/testings/images/landing_page/title-size-reduces-on-smaller-screens.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Shop now button reduces size | Buttons gets smaller on small screens | As expected | Pass

<details>
<summary>Shop now button reduces size</summary>

![Shop now button reduces size](documentation/testings/images/landing_page/shop-now-button-reduces-size.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Shop now button redirection | Button redirects to all products | As expected | Pass

<details>
<summary>Shop now button redirection</summary>

![Shop now button redirection](documentation/testings/images/landing_page/shop-now-button-redirection.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Why shopping with us section responsiveness | Boxes and title rearrange harmoniously | As expected | Pass

<details>
<summary>Why shopping with us section responsiveness</summary>

![Why shopping with us section responsiveness](documentation/testings/images/landing_page/why-shopping-with-us-section-responsiveness.JPG)
</details>

<br>

### All products page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All products | Shows all products by default | As expected | Pass

<details>
<summary>All products</summary>

![All products](documentation/testings/images/all_products_page/all-products.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product card layout | 4 cards per row on large screens | As expected | Pass

<details>
<summary>Product card layout</summary>

![Product card layout](documentation/testings/images/all_products_page/product-card-layout.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product card layout responsiveness| number of items per reduces with smaller screens | As expected | Pass

<details>
<summary>Product card layout responsiveness</summary>

![Product card layout responsiveness](documentation/testings/images/all_products_page/product-card-layout-responsiveness.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product card image | Opens the product detail page | As expected | Pass
Product card image| default no image shows when no pitcure given to product | As expected | Pass

<details>
<summary>Product card image</summary>

![Product card image](documentation/testings/images/all_products_page/product-card-image.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Click on cards Brand | Shows only the products of the brand | As expected | Pass

<details>
<summary>Click on cards Brand</summary>

![Click on cards Brand](documentation/testings/images/all_products_page/click-on-cards-brand.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Category Selection | shows the correct products | As expected | Pass

<details>
<summary>Category Selection</summary>

![Category Selection](documentation/testings/images/all_products_page/category-selection.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Discount category shows products on sale | products with a discount are shown | As expected | Pass

<details>
<summary>Discount category shows products on sale</summary>

![Discount category shows products on sale](/workspaces/le_patissier/documentation/testings/images/all_products_page/discount-category-shows-products-on-sale.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Sorting menu | sorts products correctly | As expected | Pass

<details>
<summary>Sorting menu</summary>

![Sorting menu](documentation/testings/images/all_products_page/sorting-menu.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Items quantity in the category | Show the correct number of different products | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Edit and delete buttons | Show only for logged in admins | As expected | Pass

<details>
<summary>Edit and delete buttons</summary>

![Edit and delete buttons](documentation/testings/images/all_products_page/edit-and-delete-buttons.JPG)
</details>

<br>

### Product details page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All products | Shows all products by default | As expected | Pass

<details>
<summary>All products</summary>

![All products](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product card layout | 4 cards per row on large screens | As expected | Pass

<details>
<summary>Product card layout</summary>

![Product card layout](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Edit and delete buttons | Show only for logged in admins | As expected | Pass

<details>
<summary>Edit and delete buttons</summary>

![Edit and delete buttons](documentation/testings/images/all_products_page/edit-and-delete-buttons.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Quantity selector | cannot go under 1 and cannot go above 99 | As expected | Pass

<details>
<summary>Quantity selector</summary>

![Quantity selector](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Adding product to basket | Add the coorect amount of the correct product in the basket | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Keep shopping button | redirects to all products | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product details | Are from the correct product | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Submitting a review | Success mesage is sent | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Submitting a review | Does not show as long as not approved by admins | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Submitting another review | Submitting review for same product updates product | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
No review form when user is not logged in | "Log in to post a review" appears with the button to log in| As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Rating a product in Review| Choosing a rating changes the overall rating | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Rating a product in Review| Shows the number of reviews | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
No rating | Message "no rating" in product details | As expected | Pass

<details>
<summary>Items quantity in the category</summary>

![Items quantity in the category](documentation/testings/images/all_products_page/items-quantity-in-the-category.JPG)
</details>

<br>

### Contact page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Contact form sent to admin panel | Message show in admin | As expected | Pass

<details>
<summary>Contact form sent to admin panel</summary>

![Contact form sent to admin panel](documentation/testings/images/contact_page/contact-form.JPG)
</details>

<details>

<summary>Contact form sent to admin panel</summary>

![Contact form sent to admin panel](documentation/testings/images/contact_page/contact-form-saves-to-admin-panel.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
User gets feedback on submission | Success or error message show | As expected | Pass

<details>
<summary>User gets feedback on submission</summary>

![User gets feedback on submission](documentation/testings/images/contact_page/user-gets-feedback-on-contact-form-submission.JPG)
</details>

<br>

### Shopping Basket page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
One Reference per row | Each product is repreented by a row | As expected | Pass

<details>

<summary>One Reference per row</summary>

![One Reference per row](documentation/testings/images/shopping_basket_page/one-reference-per-row.JPG)

</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product details | Are identical to the product details page | As expected | Pass

<details>

<summary>Product details</summary>

![Product details](documentation/testings/images/shopping_basket_page/product-details.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Price on basket Icon and grand total | prices are identical | As expected | Pass

<details>

<summary>Price on basket Icon and grand total</summary>

![Price on basket Icon and grand total](documentation/testings/images/shopping_basket_page/price-on-basket-icon-and-grand-total.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Updating a quantity | Changes the price and grand total accordingly | As expected | Pass

<details>

<summary>Updating a quantity</summary>

![Updating a quantity](documentation/testings/images/shopping_basket_page/updating-a-quantity.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Removing product | Removes product from basket | As expected | Pass

<details>

<summary>Removing product</summary>

![Removing product](documentation/testings/images/shopping_basket_page/removing-product-from-basket.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Removing product | Removes product Changes price accordingly | As expected | Pass

<details>

<summary>Removing product</summary>

![Removing product](documentation/testings/images/shopping_basket_page/removing-product-changes-price-accordingly.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Delivery treshhold | Is 10% and 0euro with purchase over 50 euros  | As expected | Pass

<details>

<summary>Delivery treshhold</summary>

![Delivery treshhold](documentation/testings/images/shopping_basket_page/delivery-treshhold.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Success messages | Feedback messages are given with each action | As expected | Pass

<details>

<summary>Success messages</summary>

![Success messages](documentation/testings/images/contact_page/contact-form-saves-to-admin-panel.JPG)
</details>

<br>

### Product Management page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Adding a product message | Success message when product is added | As expected | Pass

<details>

<summary>Adding a product message</summary>

![Adding a product message](documentation/testings/images/product_management_page/adding-a-product-message-success.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Cancel button | Redirects user to all product page | As expected | Pass

<details>

<summary>Cancel button</summary>

![Cancel button](documentation/testings/images/product_management_page/cancel-button.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Adding a product | all Form fileds are blank | As expected | Pass

<details>

<summary>Adding a product</summary>

![Adding a product](documentation/testings/images/product_management_page/adding-a-product-all-form-fields.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Edit a product | Form is prefilled with the product info | As expected | Pass

<details>

<summary>Edit a product</summary>

![Edit a product](documentation/testings/images/product_management_page/edit-a-product.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Edit product image | Edit Image field contains the actual picture | As expected | Pass

<details>

<summary>Edit product image</summary>

![Edit product image](documentation/testings/images/product_management_page/edit-product-image.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Removing image | Default picture will be seen on product  | As expected | Pass

<details>

<summary>Removing image</summary>

![Removing image ](documentation/testings/images/product_management_page/removing-image.JPG)
</details>

<br>

### My Profile page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All of a users orders are deleted on profile deletion | orders removed from database | As expected | Pass
My Profile link renders Profile page | profile.html is shown | As expected | Pass

<details>

<summary>My Profile link renders Profile page</summary>

![My Profile link renders Profile page](documentation/testings/images/my_profile_page/my-profile-link-renders-profile-page.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
User information is displayed on Profile page | Name and Address fields shown | As expected | Pass

<details>

<summary>User information is displayed on Profile page</summary>

![User information is displayed on Profile page](documentation/testings/images/my_profile_page/user-information-is-displayed-on-profile-page.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Update button saves updated form | Message "Profile updated successfully" shown | As expected | Pass

<details>

<summary>Update button saves updated form</summary>

![Update button saves updated form](documentation/testings/images/my_profile_page/update-button-saves-updated-form.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
User order history shown on Profile Orders tab | Orders tab shows all past orders | As expected | Pass

<details>

<summary>User order history shown on Profile Orders tab</summary>

![User order history shown on Profile Orders tab](documentation/testings/images/my_profile_page/user-order-history-shown-on-profile-orders-tab.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Delete Account tab opens account delete message | message "Warning! Account deletion is permanent. Proceed?" shown | As expected | Pass

<details>

<summary>Delete Account tab opens account delete message</summary>

![Delete Account tab opens account delete message](documentation/testings/images/my_profile_page/delete-account-tab-opens-account-delete-message.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Delete Account button opens account delete confirmation page | user-delete with user id in url shown | As expected | Pass

<details>

<summary>Delete Account button</summary>

![Delete Account button](documentation/testings/images/my_profile_page/delete-account-button.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Return button on user_delete page redirects back to profile | profile.html renders | As expected | Pass

<details>

<summary>Return button</summary>

![Return button](documentation/testings/images/my_profile_page/return-button-1.JPG)
</details>

<details>

<summary>Return button</summary>

![Return button](documentation/testings/images/my_profile_page/return-button-2.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Confirm button on user_delete page redirects back to index.html | index.html renders | As expected | Pass

<details>

<summary>Confirm button</summary>

![Confirm button](documentation/testings/images/my_profile_page/confirm-button-on-user_delete-page-redirects-back-to-index.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Confirmation message on user_delete shows | message "Profile successfully deleted" shown | As expected | Pass

<details>

<summary>Confirmation message</summary>

![Confirmation message](documentation/testings/images/my_profile_page/confirmation-message-on-user_delete-shows.JPG)
</details>

<br>

### Logging pages

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Clicking on log in | opens log in form | As expected | Pass

<details>

<summary>Clicking on log in</summary>

![Clicking on log in](documentation/testings/images/logging_pages/clicking-on-log-in.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Submitting log in | User is logged in | As expected | Pass

<details>

<summary>Submitting log in</summary>

![Submitting log in](documentation/testings/images/logging_pages/submitting-log-out.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Logging in message | success Message shows up| As expected | Pass

<details>

<summary>Logging in message</summary>

![Logging in message](documentation/testings/images/logging_pages/logging-in-message.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Log in redirection | logged in User is redirected to home page | As expected | Pass

<details>

<summary>Log in redirection</summary>

![Log in redirection](documentation/testings/images/logging_pages/log-in-redirection.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Clicking on log out | opens log out form | As expected | Pass

<details>

<summary>Clicking on log out</summary>

![Clicking on log out](documentation/testings/images/logging_pages/clicking-on-log-out.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Submitting log out | User is logged out | As expected | Pass

<details>

<summary>Submitting log out</summary>

![Submitting log out](documentation/testings/images/logging_pages/submitting-log-out.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Logging out message | success Message shows up| As expected | Pass

<details>

<summary>Logging out message</summary>

![Logging out message](documentation/testings/images/logging_pages/logging-out-message.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Log out redirection | logged out User is redirected to home page | As expected | Pass

<details>

<summary>Log out redirection</summary>

![Log out redirection](documentation/testings/images/logging_pages/log-out-redirection.JPG)
</details>

<br>

### Subscribing pages

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Completing submission | Redirects to subscribe success page | As expected | Pass
Completing unsubscribe form | Redirects to unsubscribe success page | As expected | Pass
Not inserting email | Error message | As expected | Pass

<details>

<summary>Not inserting email</summary>

![Not inserting email](documentation/testings/images/subscribing_pages/inserting-incomplete-email.JPG)
</details>

<br>

### Stripe Payment

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Payment being processed | Icon and overlay appears when payment is being processed | As expected | Pass

<details>

<summary>Payment being processed</summary>

![Payment being processed](documentation/testings/images/stripe_payment/payment-being-processed.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Confirmation page | order number created | As expected | Pass

<details>

<summary>Confirmation page</summary>

![Confirmation page](documentation/testings/images/stripe_payment/confirmation-page-order-number-created.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Confirmation page | email sent to correct email | As expected | Pass

<details>

<summary>onfirmation page</summary>

![Confirmation page](documentation/testings/images/stripe_payment/confirmation-page-email-sent.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------

<br>

### Checkout page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Adding product shows feedback message | Message shows in top right corner | As expected | Pass

<details>

<summary>Adding product shows feedback message</summary>

![Adding product shows feedback message](documentation/testings/images/checkout_page/add-to-cart-button-shows-success-message.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Product details shown in Basket | Products are arranged in a table | As expected | Pass

<details>

<summary>Product details shown in Basket</summary>

![Product details shown in Basket](documentation/testings/images/checkout_page/product-details-shown-in-cart.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Discount price of product shown in basket | Products show dicount price | As expected | Pass

<details>

<summary>Discount price of product shown in basket</summary>

![Delivery treshhold](documentation/testings/images/checkout_page/sale-price-of-product-shown-in-cart.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Update quantity button updates subtotal | Subtotal calculated correctly | As expected | Pass

<details>

<summary>Update quantity button updates subtotal</summary>

![Update quantity button updates subtotal](documentation/testings/images/checkout_page/update-quantity-button-updates-subtotal.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Delete product button removes product | Product is removed from Basket| As expected | Pass

<details>

<summary>Delete product button removes product</summary>

![Delete product button removes product](documentation/testings/images/checkout_page/delete-product-button-deletes-product.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Secure Checkout button opens checkout page | checkout.html renders | As expected | Pass

<details>

<summary>Secure Checkout button opens checkout page</summary>

![Delivery treshhold](documentation/testings/images/checkout_page/secure-checkout-button-shows-checkout-page.JPG)
</details>

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
User details prepoulated when saved | Fields are filled with info| As expected | Pass

<details>

<summary>User details prepoulated when saved</summary>

![User details prepoulated when saved](documentation/testings/images/checkout_page/user-information-is-prepopulated-if-saved-in-profile.JPG)
</details>

<br>

