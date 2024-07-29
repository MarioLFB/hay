# hay

# H.A.Y

![Am I Responsive]()

**Developer: Mario Borges**

💻 [Visit live website](https://hay-project-ddcf084b85ed.herokuapp.com/)  
(Ctrl + click to open in new tab)

## Table of Contents
  - [Introduction](#Introduction)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Introduction
H.A.Y is the website of a Steak House restaurant. The site provides users with a clear visual experience and easy access to information and tools, such as: a food and drinks menu, individualized table booking for registered users, where they can update and delete their reservations. The site also allows users to contact the admin through the contact page, which includes the restaurant's information such as address, phone number, and email. Users have a personalized experience since registration is required to access the exclusive reservation area, as well as for login and logout purposes. Once the user registration is completed, users can access their personal page where they can update their registered information.

### User Goals
- To create a table booking.
- To be able to view, edit, and cancel bookings.
- To view menus and contact information.

### Site Owner Goals
- To provide a solution that allows users to book a table online.
- To attract more users with a well-crafted site.
- To provide a modern application with easy navigation.
- To ensure the site is fully responsive and accessible.

## User Experience

### Target Audience
- Users who wish to book a table for a meal or a party with family and friends.
- Past and new customers of the business.
- Fans visiting the area for a events.
- People in the area looking to eat and drink after work.

### User Requirements and Expectations
- Fully responsive design.
- Accessibility for all users.
- A welcoming and aesthetically pleasing design.
- Integration with social media(Instagram).
- Clear and accessible contact information.


### User Stories

#### As a user...
1. As a user I can sign up so that I have access to login 
2. As a user I can login  so that I have access to booking 
3. As a user I can logout so that I leave the site securely 
4. As a user I can edit my details so that I keep my details updated 
5. As a user I can send message so that  I contact the admin 
6. As a user, I can access contact so that I find details about the restaurant  
7. As a user, I can book a reservation so that I secure my desired time, date, and number of people 
8. As a user, I can access a reservation so that I update or delete it if needed 
9. As a user, I can access menu page so that I see food and drink menu 
10. As a user, I can navigate the home page easily so that I access the navbar 

#### Site Owner
11. As the site owner, I want users to easily navigate the site so that they have a seamless experience.
12. As the site owner, I want users to be able to register and login so that they can access exclusive features.
13. As the site owner, I want users to be able to book and manage reservations so that they can plan their visits.
14. As the site owner, I want users to be able to contact the admin easily so that they can get support and information.
15. As the site owner, I want to update the menu page regularly so that users see the latest offerings.
16. As the site owner, I want to manage user accounts so that I can ensure the security and accuracy of user information.
17. As the site owner, I want to receive messages from users so that I can address their inquiries and feedback.
18. As the site owner, I want to track user activity so that I can improve the site and services based on user behavior.

#### Returning User
19. As a returning user, I want to login easily so that I can quickly access my account and reservations.
20. As a returning user, I want to see my past reservations so that I can review my booking history.
21. As a returning user, I want to update my details so that my profile information is current.
22. As a returning user, I want to book new reservations easily so that I can plan my next visit.
23. As a returning user, I want to access the menu quickly so that I can decide what to order.
24. As a returning user, I want to contact the admin if needed so that I can get assistance or provide feedback.
25. As a returning user, I want to see any new updates or changes to the restaurant so that I am informed about new offerings or events.

### Milestones, Epics, and User Stories (Acceptance Criteria and tasks)
- The project followed the agile framework, using Milestones to mark significant checkpoints, Epics to organize large blocks of work, and User Stories to detail specific functionalities (Acceptance Criteria and tasks).

<details><summary>Epics, Acceptance Criteria and Task</summary>
<img src="staticfiles\images\images_readme\agile\sample_user_story.png">
</details>

<details><summary>User Stories</summary>
<img src="staticfiles\images\images_readme\agile\user_stories.png">
</details>

<details><summary>Milestones</summary>
<img src="staticfiles\images\images_readme\agile\milestones.png">
</details>

<details><summary>Agile Progress</summary>
<img src="staticfiles\images\images_readme\agile\agile_progress.png">
</details>


## Design

### Colours
The website is designed using dark colors, with a carousel of restaurant photos as the background.


### Fonts
The chosen fonts were sourced from Google Fonts, with Electrolize as the primary font and sans-serif as the fallback option.

### Structure

#### Website pages
The site is developed with a responsive template for all types of screens. The homepage features a navigation bar for easy access. The Home page provides a visual experience with photos of the restaurant, while the footer is minimalist, containing only a direct link to the establishment's social media (Instagram).

- Home page: The Home page features a photo carousel as the background, providing a visual experience of the restaurant. It includes a responsive logo and navigation bar for easy access, and a minimalist footer containing only a link to the restaurant's social media (Instagram).
- Menu page: The Menu page is divided into two tabs: Food and Drinks, each providing detailed information about the restaurant's offerings. This structure allows users to easily browse the available menu items.
- Bookings page: The Bookings page requires users to log in. Once logged in, users fill out a form to book a table and are then directed to the My Bookings page, where they can delete or update their reservation. If a user chooses to delete a reservation, they are taken to a confirmation page beforehand.
- Contact page: The Contact page connects users with the admin. It includes a contact form and provides essential information about the restaurant's location, such as a map, address, phone number, and email, making it easy for users to get in touch.
- Profile page: The Profile page allows users to edit their registration details, including Username, Email, and Password. It also provides a link for users to access and manage their reservations, ensuring their information is always up to date.
- Sign Up page: The Sign Up page offers users a straightforward registration process, enabling them to access the booking and profile tools. This ensures that users have a personalized experience on the site.
- Login/Logout page: The Login/Logout page secures user data by ensuring that only the registered user can access their information. This feature protects user privacy and maintains the security of personal data entered on the site.
- 404 error page to display if a 404 error is raised

#### Database

- Developed using Python and the Django framework, with a PostgreSQL database for the production version hosted on Heroku.
- Bookings Model and Contact Model shows all the fields stored in the database

<details><summary>Show diagram</summary>
<img src="staticfiles\images\images_readme\data_base_diagram.png">
</details>

##### Bookings Model
- table_name
- table_phone
- table_email
- table_capacity
- table_date
- table_time
- user

##### Contact Model
- name
- email 
- message
- created_at


## Technologies Used

### Languages & Frameworks
- HTML
- CSS / Bootstrap
- Javascript / JQuery
- Python
- Django

### Libraries & Tools
- [Am I Responsive](http://ami.responsivedesign.is/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

## Features

### Home page
- Homepage includes a navigation bar, main body (automatic image slideshow), and a footer (link to Instagram).

<details><summary>Home Page</summary>

<img src="staticfiles\images\images_readme\Features\home.png">
</details>

### Logo and Navigation
- Custom logo designed for the business
- Fully responsive design
- Switches to a hamburger menu on smaller screens
- Displays login/logout status
- Present on all pages

<details><summary>Logo</summary>

<img src="staticfiles\images\images_readme\Features\logo.png">
</details>

<details><summary>Nav Bar</summary>

<img src="staticfiles\images\images_readme\Features\navbar.png">
</details>

<details><summary>Responsiveness</summary>

<img src="staticfiles\images\images_readme\Features\navbar_responsive.png">
</details>

### Footer
- Contains a link to the restaurant's Instagram
- Displayed only on the Homepage

<details><summary>Footer</summary>

<img src="staticfiles\images\images_readme\Features\footer.png">
</details>

### Sign up / Register
- Enable users to create an account
- Username, password and email are required

<details><summary>Sign up</summary>

<img src="staticfiles\images\images_readme\Features\sign_up.png">
</details>

### Login, Logout and Profile
- Users can log in and out, and access their user area, where they can view their profile page to update their information and find a link to the booking page.

<details><summary>Login</summary>

<img src="staticfiles\images\images_readme\Features\login.png">
</details>

<details><summary>Logout</summary>

<img src="staticfiles\images\images_readme\Features\logout.png">
</details>

<details><summary>Profile</summary>

<img src="staticfiles\images\images_readme\Features\profile.png">
</details>

### Contact
- The Contact page provides any user (registered or not/logged in or not) the ability to get in touch with the Admin. 
- The Contact page also includes a map, address, phone number, and contact email.
- Admin has access to messages through the site's Admin panel

<details><summary>Contact</summary>

<img src="staticfiles\images\images_readme\Features\contact.png">
</details>

### Bookings
- The Bookings page allows users to make reservations by providing details such as the number of people, name, phone number, email, date, and time.
- Users can view and manage their bookings.
- The page features two buttons: "Book" for making a new reservation and "My Bookings" to review existing ones.

<details><summary>Bookings</summary>

<img src="staticfiles\images\images_readme\Features\bookings.png">
</details>

### My Bookings
- The My Bookings page allows users to view their current reservations. 
- If no bookings are found, the page displays: "You have no bookings yet. Click here to make a booking."
- If bookings exist, details such as name, phone number, email, capacity, date, and time are shown.
- Users can manage their bookings with "Delete" and "Update" buttons.

<details><summary>My Bookings</summary>

<img src="staticfiles\images\images_readme\Features\my_bookings.png">
</details>

### Edit Bookings
- The Edit Bookings page allows users to modify their existing reservation details.
- Users can update the number of people, name, phone number, email, date, and time of the booking.

<details><summary>Edit Bookings</summary>

<img src="staticfiles\images\images_readme\Features\edit_bookings.png">
</details>

### Menu
- Contains two tabs: Food and Drinks.
- Accessible to any user, even without login or registration.

<details><summary>Menu</summary>

<img src="staticfiles\images\images_readme\Features\menu.png">
</details>


## Validation

The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_home.png">
</details>

<details><summary>Menu and Drinks</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_menu.png">
<img src="staticfiles\images\images_readme\validation\w3\w3_drinks.png">
</details>

<details><summary>Bookings</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_bookings.png">
</details>

<details><summary>My Bookings</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_my_bookings.png">
</details>

<details><summary>Booked</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_booked.png">
</details>

<details><summary>Edit Booking</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_my_bookings.png">
</details>

<details><summary>Delete Bookings</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_delete_bookings.png">
</details>

<details><summary>Contact</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_contact.png">
</details>

<details><summary>Register(Sign up)</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_register.png">
</details>

<details><summary>Profile</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_profile.png">
</details>

<details><summary>Login</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_login.png">
</details>

<details><summary>Logout</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_logout.png">
</details>

<details><summary>404</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3_404.png">
</details><hr>

### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="staticfiles\images\images_readme\validation\w3\w3c_css.png">
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="staticfiles\images\images_readme\validation\w3\jshint.png">
</details><hr>

### PEP8 Python Validator (provided by Code Institute)
The Code Institute’s PEP8 Python linter was employed to check the Python code for this project.

All code was verified and found to be error-free.

<details>
<summary>Bookings</summary>

#### Admin
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_admin_bookings.png">

#### Forms
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_forms_bookings.png">

#### Models
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_models_bookings.png">

#### Urls
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_urls_bookings.png">

#### Views
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_views_bookings.png">

#### Tests
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_test_bookings_forms.png">
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_test_bookings_models.png">
<img src="staticfiles\images\images_readme\validation\pep8\bookings\pep8_test_bookings_views.png">

</details>

<details>
<summary>Contact</summary>

#### Admin
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_admin_contact.png">

#### Forms
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_forms_contact.png">

#### Models
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_models_contact.png">

#### Urls
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_urls_contact.png">

#### Views
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_views_contact.png">

#### Tests
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_test_contact_forms.png">
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_test_contact_models.png">
<img src="staticfiles\images\images_readme\validation\pep8\contact\pep8_test_contact_views.png">

</details>

<details>
<summary>Home</summary>

#### Urls
<img src="staticfiles\images\images_readme\validation\pep8\home\pep8_urls_home.png">

#### Views
<img src="staticfiles\images\images_readme\validation\pep8\home\pep8_views_home.png">

</details>

<details>
<summary>Menu</summary>

#### Urls
<img src="staticfiles\images\images_readme\validation\pep8\menu\pep8_urls_menu.png">

#### Views
<img src="staticfiles\images\images_readme\validation\pep8\menu\pep8_views_menu.png">

</details>

<details>
<summary>Users</summary>

#### Forms
<img src="staticfiles\images\images_readme\validation\pep8\users\pep8__forms_users.png">

#### Urls
<img src="staticfiles\images\images_readme\validation\pep8\users\pep8__urls_users.png">

#### Views
<img src="staticfiles\images\images_readme\validation\pep8\users\pep8__views_users.png">

</details>


