
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
Newsletter button | Button redirects to Newsletter registration form | As expected | Pass
Newsletter button hover | Button changes color on hover | As expected | Pass
Newsletter button responsiveness | Enveloppe icons dissapear on screens snmaller than 347px | As expected | Pass
Contact button | Button redirects to contact us form | As expected | Pass


### Landing Page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Hero image resizes on mobile | Images resize on mobile | As expected | Pass
Title size reduces on smaller screens | Title gets smaller | As expected | Pass
Shop now button reduces size | Buttons gets smaller on small screens | As expected | Pass
Shop now button redirection | Button redirects to all products | As expected | Pass
Why shopping with us section responsiveness | Boxes and title rearrange harmoniously | As expected | Pass


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

### Product details page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
All products | Shows all products by default | As expected | Pass
Product card layout | 4 cards per row on large screens | As expected | Pass
Clicking Review This Product as logged in user | Review form opens | As expected | Pass
Submitting a review as logged in user | Message "Your review has been successfully added!" | As expected | Pass
No review form when user is not logged in  | Log in to post a review appears with the link to log in| As expected | Pass

### Contact page

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Contact form saves to admin panel | admin panel shows message, name and email | As expected | Pass
User gets feedback on contact form submission | Message "Your message was sent! We'll be in touch shortly." shows | As expected | Pass



My Profile link renders Profile page | profile.html is shown | As expected | Pass
User information is displayed on Profile page | Name and Address fields shown | As expected | Pass
Update Address button saves updated form | Message "Profile updated successfully" shown | As expected | Pass
User order history shown on Profile Orders tab | Orders tab shows all past orders | As expected | Pass
Delete Account tab opens account delete message | message "Warning! Account deletion is permanent. Proceed?" shown | As expected | Pass
Delete Account button opens account delete confirmation page | user-delete with user id in url shown | As expected | Pass
Return button on user_delete page redirects back to profile | profile.html renders | As expected | Pass
Confirm button on user_delete page redirects back to index.html | index.html renders | As expected | Pass
Confirmation message on user_delete shows | message "Profile successfully deleted" shown | As expected | Pass
All of a users orders are deleted on profile deletion | orders removed from database | As expected | Pass
Add Product redirects to add_product.html form | add_product.html form renders | As expected | Pass
Edit Product redirects to update form | edit_product form renders | As expected | Pass
Delete Product link renders delete confirmation modal | Modal renders | As expected | Pass
Delete Product cancel button closes Modal | Modal is closed | As expected | Pass
Delete Product delete button redirects to Products page | products.html renders | As expected | Pass
Product deleted from database on confirmation | Product deleted | As expected | Pass
User redirected to logout confirmation when Logout is clicked | account/logout.html renders | As expected | Pass
User redirected when Profile Logout is cancelled | index.html renders | As expected | Pass
User redirected to Index page when logged out | index.html renders | As expected | Pass
User shown log out message feedback | message "You have signed out." shown | As expected | Pass

<br>

### Checkout

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Add to cart button shows success message | Success message and product image shown | As expected | Pass
Product details shown in cart | Products render in cart as table | As expected | Pass
Sale price of product shown in cart | Products on sale show their sale price | As expected | Pass
Update quantity button updates subtotal | Subtotal calculated correctly | As expected | Pass
Delete product button deletes product | Cart is updated without that product | As expected | Pass
Secure Checkout button shows checkout page | checkout.html renders | As expected | Pass
User information is prepoulated if saved in profile | Fields are automatically filled | As expected | Pass
Coupon code field renders | Coupon form is shown | As expected | Pass
Correct coupon is entered | Sucess popup message "Coupon code: -code- applied" | As expected | Pass
Correct coupon is entered | Text "Applied coupon -code- for -amount-% off!" | As expected | Pass
Correct coupon is entered | Discount applied to Grand Total | As expected | Pass
Remove coupon link clicked | Discount removed from Grand Total | As expected | Pass
Stripe validation works on incorrect/incomplete card number | Stripe validation error shown | As expected | Pass
Successful checkout | Checkout loading overlay shown | As expected | Pass
Successful checkout | Checkout Success page shown | As expected | Pass
Successful checkout | Confirmation email sent | As expected | Pass
Checkout other products button clicked | Products page shown | As expected | Pass

<br>

## Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Registration page validates each input for empty or whitespaces | message "Please fill in this field is shown" | As expected | Pass
Registration page validates email address | message "A user is already registered with this e-mail address." | As expected | Pass
Registration page validates username | message "A user with that username already exists." | As expected | Pass
Submitting an empty review as logged in user | Message "Your review has not been submitted" | As expected | Pass
Add Product form has validation | Product won't add without title, price, SKU | As expected | Pass
Contact form validates for whitespaces | message "Please fill in this field" shows | As expected | Pass
Item Quantity can't be less than 1 or more than 99 | Buttons disabled on 1 and 99 | As expected | Pass
User tried to render profile URL when not logged in | user redirected to log in page | As expected | Pass
User tried to render delete_profile URL when not logged in | user redirected to login page | As expected | Pass
User tried to render profile URL for another user | user redirected to 403 page | As expected | Pass
User tried to render delete_profile URL for another user | user redirected to 403 page | As expected | Pass