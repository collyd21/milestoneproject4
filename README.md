# Big Boss SNKRS
**Full Stack Frameworks with Django Milestone 4 Project.**

Over the last 6-12 months I have noticed a massive increase in Competition sites. These competition sites are essentially lotteries/raffles where Users buy a ticket, and are given a number. One person wins based on the use of a random number generator (namely Google). 
Big Boss SNKRS is a competition site offering multiple raffles, with the winning prize of a brand-new pair of highly-sought after sneakers.


### User Stories
*As a user I want to:*

**Browse/Payment:**

 * View newest competitions.
 * Browse all available competitions easily
 * View extra information about a particular competition
 * Add competitions to my cart
 * View my cart total at anytime
 * View all items in my cart and total cost in detail
 * Use a pain free checkout format
 * Pay by credit/debit card
 * View a guide on how the competitions work

**Registering/Login:**

 *	Save my details for future checkouts
 *	Easily register with the site
 *	Easily login/logout of the site
 *	Recover my password if necessary

**User Profile:**

 * View my default user details
 * Update these details if necessary
 * View my previous orders/transactions with the site

**Contact:**

 * Use a simple form to contact the Administrators

**Reviews:**

 * View reviews from previous Users
 * Add my own review to the site


*As a Site Administrator I want to:*
 * View all competitions easily
 * Have an edit competition function
 * Have a delete competition function
 * View all user reviews in Django Admin
 * View all user contact messages in Django Admin

### Scope
The scope for this Milestone project is to develop a site that offers competitions/raffles where the prize is a pair of sneakers in the winners chosen size. The idea is that a winning user will receive a valuable/ highly-sought after pair of sneakers for a fraction of the price. Visitors can view all competitions, and extra information about a particular competition. They can then easily add multiple entries to their cart.

To complete their cart checkout, A visitor will need to register and login as a User. As a user they will be giving a profile page and be able to view previous transactions. Then will also then be able to save their information and purchase tickets to any of the competitions on offer.

I had previous begun this project as a html only site, as I had not yet learned Python or Django in the Code Institute course. I used the site as a bases for navigation and page/links ideas of the competition site. As sneakers are a personal interest of mine I decided to centre the whole site for that market.




### Skeleton

**Navbar**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/navbar.JPG"><img src="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/navbar.JPG" alt="Navbar" style="max-width:100%;"></a>

**Homepage**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/home.JPG"><img src="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/home.JPG" alt="Navbar" style="max-width:100%;"></a>

**Competition Preview Cards**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/comp_cards.JPG"><img src="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/comp_cards.JPG" alt="Navbar" style="max-width:100%;"></a>

**Competition Details Page**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/comp_info.JPG"><img src="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/comp_info.JPG" alt="Navbar" style="max-width:100%;"></a>

**How it Works Page**
<a target="_blank" rel="noopener noreferrer" href="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/how_works.JPG"><img src="https://github.com/collyd21/milestoneproject4/blob/master/static/wireframes/how_works.JPG" alt="Navbar" style="max-width:100%;"></a>


### Structure

#### Navbar
The navbar features a restyled logo of the site name on the left, this is shortened to “BB SNKRS”. Centred on the navbar are the links to “Competitions”, “Reviews”, “How it Works” and “Contact Us”. Finally on the right features the “Account” dropdown link to reveal “Register“ or “Login“ if not logged in yet. If User is logged in these options are “My Profile” or “Logout“. Additionally, if it is Admin that has logged in the dropdown will feature the “Add/Edit Comps” link. At the end there is a Cart icon with a Euro amount, showing the current total of the visitor’s cart.

#### Home Logo
By clicking on the “BB SNKRS” logo the user will be directed back to the homepage from wherever they are on the site.

#### Homepage  
Displayed here is the full site logo of “Big Boss SNKRS” on a back drop of sneakers, by use of jumbotron. Underneath the latest competitions are shown. These are sorted by newest date of addition and also limited to display only 3 competitions. There is a button here that links to view the all competitions page.

#### Competitions Page  
Here the user gets the full view of all the competitions on offer. They are aligned and shown by bootstrap card component, the same as the homepage.

#### Reviews Page
From time to time a user may feel like leaving a site review about their experience on the site. This may be what they like, don’t like, suggestions for competitions etc. All visitors to the site can view this reviews page and read these from newest to oldest. If the visitor to the site is logged in, below the reviews a form for submitting is revealed, containing Name, Email and Message. 

#### How it Works Page
This page is used as an easy guide to a new user of how the site works. It walks you through browsing, payment and finally the competition draw itself.

#### Contact Us Page
If a user has further question for us. They can contact us through the use of the Contact form. This form asks for User’s Name, Email, message Subject and the Message.

#### Register / Sign In Pages
A visitor to the site can use this link to sign up or sign in. They are asked to fill in a form on either page, which uses Django’s builtin Allauth feature. I have restyled the default allauth templates to make everything uniform throughout the site.

#### Competitions Details Page  
By clicking any of the competitions this will direct the user to a page that display more information about the competition. A User is shown a larger image of the sneakers, the name, size range, max entries, price and also asked for an entry quantity. Underneath there is a tab for displaying a description about the sneakers, then a tab for general competition details. 

#### Cart Page
Once a competition entry is added to the users cart, it will automatically total the price in Euro in the top right. When the user clicks the cart it bring them to the full cart display page. This shows what competition entries they have selected, the quantity of each, and the total cost of their items combined.
The user then has the option to return to the competitions or continue to the checkout page.
Only if the User has registered and logged in will they be given the checkout option.

#### Checkout page

Once the User is happy to checkout, this page will display a form, which asks for the users personal information. Underneath the details form is a checkbox asking the user if they would like their details saved for future use.
At the bottom there is also a field for the user to input their card details and then checkout.
To the right there is a summary of what the User has added to their cart so they can check one last time that they have added the right competition entries and quantities. 

#### Confirmation Page

If the User credentials are valid in the checkout form, they will they be directed to the confirmation page, thanking them for their order. It also informs them that they will receive a confirmation mail soon.

#### Profile Page

A register user can access their details under the account menu. This page gives the user a details form (pre-filled if checkbox is selected on checkout page). The User can edit and update these details using this form.
Below the details form is an order history display. Here previous orders made by the user are displayed, showing order number, order date, competitions entered and quantities of each and finally a total for the order.

#### Add Competition page

If the user is a site Admin, they have the option under account of adding new competitions. A form is displayed which requires the following, Competition Name, sneaker size range, description, price, max entries. There is then the option for the admin to either enter a URL for the image of the sneakers or to upload their own.

#### Edit Competition page

As an Admin, the user has extra options on the competitions details page,-. They can edit or delete that particular competition. If they choose edit, this will open a similar page to the add competitions page but all form details will be pre-filled. They then make their alterations and update the competition. 


### Surface
The colour scheme for this project includes a dark-red colour for the Navbar to stand out along side the dark jumbotron on the homepage. The main area of the page has a contrasting light colour background. This colour scheme runs throughout the site to keep it familiar to the user on each page. The same black header with a white text is used on each page. A black container header on each section of the pages helps the user flow through the page easily drawing the eye to each different section, while staying consistent to one another.
The colours used are:

![#000000](https://via.placeholder.com/15/000000/000000?text=+) #000000

![#343a40](https://via.placeholder.com/15/343a40/000000?text=+) #343a40

![#f1f1f1](https://via.placeholder.com/15/f1f1f1/000000?text=+) #f1f1f1

![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) #ffffff

![#ff1111](https://via.placeholder.com/15/ff1111/000000?text=+) #ff1111

![#be2d2e](https://via.placeholder.com/15/be2d2e/000000?text=+) #be2d2e

The logo image is one that I paid a graphic designer to make for me through freelancing site Fiverr. I had the idea of the laces as the font but not the time or expertise to bring it to fruition with Adobe Illustrator. 
The background image of the pile of sneakers is a stock image I found on google search and felt it merged great together with the main logo.
The reduced logo in the navbar is my own handy work with Adobe Illustrator using the logo I had made for me.

## Technologies
For this project I used the following technologies:

[Github](https://github.com/) - Used for repository hosting service.

[Gitpod](https://gitpod.io/) - an online IDE, used to create and edit the project code.

[Heroku](https://heroku.com) - a Cloud Application Platform that enables developers to build, run, and operate applications entirely in the cloud

[Bootstrap 4](https://getbootstrap.com/) - a CSS Framework for developing responsive and mobile-first websites

[HTML 5](https://en.wikipedia.org/wiki/HTML5) - a markup language used for structuring and presenting content on the World Wide Web

[CSS 3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Cascading Style Sheets that describe how HTML elements are to be displayed on screen

[Django]( https://www.djangoproject.com/) – a high-level Python Web framework that encourages rapid development and clean, pragmatic design

[SQlite3]( https://www.sqlite.org/index.html) – database used in development through Django

[PostgreSQL]( https://www.postgresql.org/) – database used in production through Heroku

[Google Fonts]( https://fonts.google.com/) – Used to set the Font Family for the whole site

[FontAwesome](https://www.bootstrapcdn.com/fontawesome/) – used for scalable vector icons

[jQuery](https://jquery.com/) - a JavaScript library that greatly simplifies JavaScript programming

[Slack](https://slack.com/intl/en-ie/) - used by the Code Institute community for open discussions, getting answers and sharing information

[Stackoverflow](https://stackoverflow.com/) - an open community for coders to ask questions and get answers

[W3Schools](https://www.w3schools.com/about/) - for tutorials and references on web development languages

[Free Formatter](https://www.freeformatter.com/javascript-beautifier.html) - a Javascript, HTML and CSS Beautifier.

[W3 Validator](https://validator.w3.org/) - a HTML and CSS Validator.

[Responsinator](http://www.responsinator.com/) - for testing site Responsiveness.

[PEP8 Online](http://pep8online.com/) - To format all Python code.


## Future Features

**Countdown Timer**: A countdown timer to be added to each competition details page. With the option for Admin to select a date in the future when adding a new competition.

**Stock Inventory**: A progress bar under the max entries field to show how many tickets for each competition are left. Also would need to implement code to decrease current available tickets by quantity after each cart checkout.

**Policies**: legal policies such as Terms & Conditions, Cookies Policy and Privacy Policy to be added to a footer at the bottom.

**Add question to each competition**: Under Ireland/UK laws this type of site must have a question of skill to be answered before purchasing a ticket for a draw. This is so that it is not classed as luck and doesn't not fall under gambling laws. I would like to add a multiple choice question to each competition, which must be correct for the User to gain a ticket to the draw.



## Testing
For testing I broke each page out on its own, and made sure each component of that page did what it was required to. The following are the tests that I conducted:

### Navbar (from base.html)

- BB Logo tested to direct to homepage.
- Test that logo is set to hidden for smaller screens and toggler icon shown instead.
- Tested toggler icon drops down to display navlinks.
- Test all navlinks to direct to appropriate pages.
- When not logged in test account button drops down to display “Register” & “Login”.
- When logged in as standard User, test account drops down to display “My Profile” & “Logout”.
- When logged in as Admin(superuser), test account drops down to display “Add/Edit Comps”, “My Profile” & “Logout”.
- Test “Register” and “Login” directs to correct pages.
- Test “Add/Edit Comps”, “My Profile” & “Logout” option direct to appropriate pages.
- Test empty cart brings you to “Cart empty” page.
- Add items to cart and ensure total accumulates correctly.

### Homepage (index.html)

- Large image shown on jumbotron correctly on desktop as per media query in CSS.
- Small logo image shown correctly on jumbotron for smaller devices, as per media query in CSS.
- Colour scheme correct
- All Competitions link directing to competitions page.
- Competition cards are displayed correctly (all in line and same heights/widths), cards are sorted as newest first, only 3 cards are displayed as a preview, full card is clickable, not just image.
- Box shadow and enlarged card when hovered.
- Card link directs to correct Competition details page.
 
### Competitions (comps.html, comps_info.html, add_comp.html, edit_comp.html)

- Competitions link displays all competitions page.
- Competition cards have same attributes as homepage.
- Card link directs to correct Competition details page.
- Individual competition info displayed correctly.
- Quantity selector operating as it should.
- Add to cart button adds correct quantity and cart icon updates total amount.
- Description tab and details tabs display their information when clicked.
- If Admin is logged in, “Edit” & “Delete” options are available.
- Delete button correctly deletes competition. (checked Django admin to confirm).
- Edit button directs to edit competitions form.
- Form fields are populated with current competition information.
- Updated information in each field separately and tested. All updated correct. Successful toast is displayed.
- Successful update redirects to that competition details page.
- Change competition image. Updates correctly. Successful toast is displayed.
- Drop down link in “Accounts” displays “New Competition” form, when “Add/Edit Competition” is clicked.
- New competition fields are marked as required with an asterix.
- Test that no individual field can be left blank, including image upload.
- Check price cannot be more than 6 digits and that an error is displayed under field. Error toast also displays. 
- Check max entries cannot be more than 4 digits and that an error is displayed under field. Error toast also displays.


### Reviews (reviews.html)

- Reviews link renders reviews page.
- All reviews are displayed correctly with correct CSS styling.
- If not logged in, reviews are visible.
- If a User is logged in, the form for adding a review is displayed.
- Check all fields are required.
- Check email address is valid format.
- After submitting form, reviews page refreshes displaying new review.
- Check Django Admin to confirm review is stored.


### How It Works (how_it_works.html)

- Test that link directs to How it Works page.
- Page renders correctly with correct CSS.
- “Go to Competitions” button redirect to Competitions page correctly.


### Contact Us (contact.html)

- Contact Us link renders contact page.
- Form is displayed correctly with correct CSS styling.
- Contact form available for all Users.
- Check all fields are required, exception is the “Subject” field.
- Check email address is valid format.
- After submitting form, redirect to Homepage.
- Toasts information message displayed.
- Check Django Admin to confirm contact message is stored.


### Cart(cart.html)

- Test empty cart brings you to “Cart empty” page.
- With items in cart test cart table is displayed correctly.
- If not a User and logged in, “Return to Competitions” and “Sign in” options are displayed.
- Test “Return to Competitions” button directs to Competitions page.
- Test “Sign in” link directs to sign in page.
- If User is logged in, “Return to Competitions” and “Checkout” options are displayed.
- Test “Return to Competitions” button directs to Competitions page.
- Test “Checkout” button directs to checkout page.


### Checkout(checkout.html, checkout_success.html)

- Test checkout page displays correctly with correct CSS.
- Check User’s information is pre-populated from profile (if User has filled in previously).
- Confirm cart snippet on right displays accurate information to what was in cart on previous page.
- Check all fields are required, exceptions are “County”, “Address 2” and “Postcode” fields.
- Check email address is valid format.
- Test on New User that “save information” button saves profile information correctly.
- Use Stripe test credit card details “card number - 4242 4242 4242 4242”, “Expiry Date – 0424” & “CCV – 424”. These allow for a test payment.
- Check my own Stripe profile to confirm payment was successful.
- Check invalid card number displays error.
- Check invalid Expiry Date displays error.
- Test “Pay Now” button submits form correctly. Success toast displays.
- Test that User is directed to payment successful page.
- Test “Return to Competitions” button directs to Competitions page.


### Allauth pages

- Test “Register”, “Login” & “Forgot Password”  pages display correctly. Check that these pages inherit typical CSS styling of the rest of the site.
- Check all fields are required on “Register” page.
- Check email addresses must match email repeat field.
Test email not in use already is valid.
- Check email address is valid format.
- Check Username must be minimum 4 characters
- Check password must be minimum 8 characters.
- Check password in not too common.
- Test “Sign Up” button redirects to homepage and logs new User in. Check successful toast displays.
- Check invalid details shows error on “Login” page.
- Test “Login” button redirects to homepage and logs User in. Check successful toast displays.

**All urls were check by typing them in and cofirming that a Vistor/User/Admin can only access the pages they are authorised to**

## Bugs/Issues

During the course of this project I became stuck on certain items, here are a few of the issues I faced and how I resolved them.

**Removing item from cart**
The page would refresh but item would not be deleted. I was not replacing the cart after popping the item out of it. Code below was missing

request.session['cart'] = cart

**Card Images**
The competition images in the Bootstrap card were not all the same heights. I used media queries in the CSS to allocate the height to each.

**Logo on Navbar**
The logo would not show on Heroku app. I had to add the { Background-image: url} into the CSS. Then the logo would display a border. I had left the src address empty on the Navbar logo div. I had to assign the address to the image folder to remove the border.

**Message field in Reviews**
When clicking into the message text box on Reviews form, the cursor would start tabbed in from the side. I realised I had a tab between the textarea tags in my html.

**Competition Cards**
Whole card was not clickable as a link to bring the User onto the competitions page. I wrapped the whole card in <a> tags.

  

## Deployment
A live demo can be found here [Big Boss SNKRS]( https://colmdoyle-milestone4.herokuapp.com/).

The website is hosted using Heroku. It is linked from the master branch of my milestone repository [Colm Doyle Milestone 4 GitHub]( https://github.com/collyd21/milestoneproject4). When new commits are added to the repository, Heroku will rebuild and the site will update with any changes.

**Cloning via Github**:

*	Open the Github Repository link.
*	Click on the 'Clone or Download' button.
*	Copy the URL provided.
*	Open Git Bash terminal.
*	Change the current working directory to the location where you want the cloned directory to be made.
*	Type 'git clone' and paste in the URL.
*	Press Enter.

**Deploying on Heroku**

- Navigate to [Heroku](https://heroku.com).
- Install the Heroku CLI (Command Line Interface)
- Creating an account is required. When at the Heroku dashboard, click the "New" button on top right. A dropdown appears and you now click "Create New app".
- Name your app. **Note app names must be unique**.
- Choose your region.
- On heroku dashboard navigate to "App connected to GitHub" and choose your relevant Github Repository to link to Heroku app.
- Go to your Bash Terminal.
- Login to Heroku using `$ heroku login`
- Create a requirements.txt file: `$ pip3 freeze --local > requirements.txt`.
- Create Procfile: `$ echo web: python manage.py > Procfile` **Note capital "P" in Procfile.
- Create a super user profile with ‘python3 manage.py createsuperuser’.
- Git add, commit and push.
- Again on your Heroku dashboard, find the apps name, click and then go to "settings".
- Navigate to "Config Vars", click "Reveal Vars" and enter the following Vars and their values:
*AWS_ACCESS_KEY_ID
*AWS_SECRET_ACCESS_KEY
*DATABASE_URL
*SECRET_KEY
*STRIPE_PUBLIC_KEY
*STRIPE_SECRET_KEY
*STRIPE_WH_SECRET
*USE_AWS
- Navigate to “Deploy”, click on Enable Automatic Deploy. Then click “Deploy Branch” (ensure master branch selected) for first time only.
- Herokuapp will now build
- Once built successfully, you can click open app in top right.

**Note to make sure site functions correctly, free account for Stripe and AWS with an S3 bucket are required**

## Credits
### Media

The main “Big Boss SNKRS” image. Was one I paid to have produced from [Fiverr]( https://www.fiverr.com/).

The Jumbotron background image from a google search, but ultimately came from a Thai website [boidapchay]( https://boidapchay.com/giay-tot-nhat-cho-runner/).

### Acknowledgements

The Code Institute tutor Chris (ckz8780). Firstly, for his excellent tutorial video for the Boutique_Ado project. Which a lot of my coding snippets came from and were redesigned by me to fit my project. Secondly, his excellent communication when messaging him about struggles/issues I had with certain parts of the tutorial.

The Code Institute community on Slack. Very helpful with issues and it was good to see I was not alone with the problems I was facing.

Stack Overflow community and threads/ questions that helped me through difficulties with my project.

The cart template that I took inspiration from and made it to suit my project he main “Big Boss SNKRS” image. Was one I paid to have produced from [Bootstrapious]( https://bootstrapious.com/p/bootstrap-shopping-cart/).

The Contact Us Tutorials from [Hello Web Books]( https://hellowebbooks.com/news/tutorial-setting-up-a-contact-form-with-django/) and [OverIQ]( https://overiq.com/django-1-10/building-contact-us-page/)

The Comment Tutorial that I made into my site reviews section from [DjangoCentral]( https://djangocentral.com/creating-comments-system-with-django/)

The checkout template from GetBootstrap which I made my own and suit this project [GetBootstrap]( https://getbootstrap.com/docs/4.5/examples/checkout/)

W3schools for some very helpful tips.
