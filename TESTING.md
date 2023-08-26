
# Manual Testing

This table shows all the manual testing done for the website, and whether it worked as expected or not.

## Features

### General

#### Navbar

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
NavBar responsiveness | NavBar resizes according to devices | As expected | Pass
NavBar categories responsiveness| Categories become burger menu | As expected | Pass
NavBar categories hover opening| Categories menus open and close on hover with screens above 992px | As expected | Pass
Search field | Search field transforms in button with medium screens and lower | As expected | Pass
Search | Inserting a term gives a lst of products | As expected | Pass
Account icon | Account icon opens on click only | As expected | Pass
Account icon | Account icon is different for logged in admins and users | As expected | Pass
Account icon | Account icon shows log in and register for unlogged users | As expected | Pass
Shopping basket | redirects to the shopping basket template | As expected | Pass
Action messages | messages appears on the top right corner consistenly | As expected | Pass

#### Footer

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Footer responsiveness | Footer layout changes according to devices | As expected | Pass
Footer links | All external links open a new tab in the browser | As expected | Pass
Footer links | All links redirects to the correct content | As expected | Pass
Footer brands and legal links | Links are underlined on hover | As expected | Pass

---------------|-----------------|---------------|----------
Newsletter button | Button redirects to Newsletter registration form | As expected | Pass
Newsletter button hover | Button changes color on hover | As expected | Pass
Newsletter button responsiveness | Enveloppe icons dissapear on screens snmaller than 347px | As expected | Pass
Contact button | Button redirects to contact us form | As expected | Pass

<br>

### Landing Page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Hero image resizes on mobile | Images resize on mobile | As expected | Pass
Title size reduces on smaller screens | Title gets smaller | As expected | Pass
Shop now button reduces size | Buttons gets smaller on small screens | As expected | Pass
Shop now button redirection | Button redirects to all products | As expected | Pass
Why shopping with us section responsiveness | Boxes and title rearrange harmoniously | As expected | Pass

<br>

### All products page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All products | Shows all products by default | As expected | Pass
Product card layout | 4 cards per row on large screens | As expected | Pass
Product card layout responsiveness| number of items per reduces with smaller screens | As expected | Pass
Product card image| default no image shows when no pitcure given to product | As expected | Pass
Click on cards image | Opens the product detail page | As expected | Pass
Click on cards Brand | Shows only the products of the brand | As expected | Pass
Category Selection | shows the correct products | As expected | Pass
Discount category shows products on sale | products with a discount are shown | As expected | Pass
Sorting menu | sorts products correctly | As expected | Pass
Items quantity in the category | Show the correct number of different products | As expected | Pass
Edit and delete buttons | Show only for logged in admins | As expected | Pass

<br>

### Product details page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All products | Shows all products by default | As expected | Pass
Product card layout | 4 cards per row on large screens | As expected | Pass
Edit and delete buttons | Show only for logged in admins | As expected | Pass
Quantity selector | cannot go under 1 and cannot go above 99 | As expected | Pass
Adding product to basket | Add the coorect amount of the correct product in the basket | As expected | Pass
Keep shopping button | redirects to all products | As expected | Pass
Product details | Are from the correct product | As expected | Pass
Submitting a review | Success mesage is sent | As expected | Pass
Submitting a review | Does not show as long as not approved by admins | As expected | Pass
Submitting another review | Submitting review for same product updates product | As expected | Pass
No review form when user is not logged in | "Log in to post a review" appears with the button to log in| As expected | Pass
Rating a product in Review| Choosing a rating changes the overall rating | As expected | Pass
Rating a product in Review| Shows the number of reviews | As expected | Pass
No rating | Message "no rating" in product details | As expected | Pass

<br>

### Contact page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Contact form sent to admin panel | Message show in admin | As expected | Pass
User gets feedback on submission | Success or error message show | As expected | Pass

<br>

### Shopping Basket page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
One Reference pre row | Each product is repreented by a row | As expected | Pass
Product details | Are identical to the product details page | As expected | Pass
Price on basket Icon and grand total | prices are identical | As expected | Pass
Updating a quantity | Changes the price and grand total accordingly | As expected | Pass
Removing product | Removes product from basket | As expected | Pass
Removing product | Removes product Changes price accordingly | As expected | Pass
Delivery treshhold | Is 10% and 0euro with purchase over 50 euros  | As expected | Pass
Success messages | Feedback messages are given with each action | As expected | Pass

<br>

### Product Management page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Adding a product message | Success message when product is added | As expected | Pass
Cancel button | Redirects user to all product page | As expected | Pass
Adding a product | all Form fileds are blank | As expected | Pass
Edit a product | Form is prefilled with the product info | As expected | Pass
Edit product image | Edit Image field contains the actual picture | As expected | Pass
Removing image | Default picture will be seen on product  | As expected | Pass

<br>

### My Profile page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
My Profile link renders Profile page | profile.html is shown | As expected | Pass
User information is displayed on Profile page | Name and Address fields shown | As expected | Pass
Update button saves updated form | Message "Profile updated successfully" shown | As expected | Pass
User order history shown on Profile Orders tab | Orders tab shows all past orders | As expected | Pass
Delete Account tab opens account delete message | message "Warning! Account deletion is permanent. Proceed?" shown | As expected | Pass
Delete Account button opens account delete confirmation page | user-delete with user id in url shown | As expected | Pass
Return button on user_delete page redirects back to profile | profile.html renders | As expected | Pass
Confirm button on user_delete page redirects back to index.html | index.html renders | As expected | Pass
Confirmation message on user_delete shows | message "Profile successfully deleted" shown | As expected | Pass
All of a users orders are deleted on profile deletion | orders removed from database | As expected | Pass

<br>

### Logging pages

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Clicking on log in | opens log in form | As expected | Pass
Submitting log in | User is logged in | As expected | Pass
Logging in message | success Message shows up| As expected | Pass
Log in redirection | logged in User is redirected to home page | As expected | Pass
Clicking on log out | opens log out form | As expected | Pass
Submitting log out | User is logged out | As expected | Pass
Logging out message | success Message shows up| As expected | Pass
Log out redirection | logged out User is redirected to home page | As expected | Pass

<br>

### Subscribing pages

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Inserting incomplete email | Error message shows | As expected | Pass
Completing submission | Redirects to subscribe success page | As expected | Pass
Completing unsubscribe form | Redirects to unsubscribe success page | As expected | Pass

<br>


### Stripe Payment

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Payment being processed | Icon and overlay appears when payment is being processed | As expected | Pass
Confirmation page | order number created | As expected | Pass
Confirmation page | email sent to correct email | As expected | Pass

<br>

### Checkout page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Add to cart button shows success message | Success message and product image shown | As expected | Pass
Product details shown in cart | Products render in cart as table | As expected | Pass
Sale price of product shown in cart | Products on sale show their sale price | As expected | Pass
Update quantity button updates subtotal | Subtotal calculated correctly | As expected | Pass
Delete product button deletes product | Cart is updated without that product | As expected | Pass
Secure Checkout button shows checkout page | checkout.html renders | As expected | Pass
User information is prepoulated if saved in profile | Fields are automatically filled | As expected | Pass

<br>

