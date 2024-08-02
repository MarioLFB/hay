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
12. As the site owner, I want users to be able to register and login so that they can access bookings area.
13. As the site owner, I want users to be able to book and manage reservations so that they can plan their visits.
14. As the site owner, I want users to be able to contact the admin easily so that they can get support and information.
15. As the site owner, I want users to have easy access to the food and drinks menu so that they can check the list of items and their prices.

#### Site Admin
16. As the site admin, I want to access the admin area so that I can manage the site's administration effectively.
17. As the site admin, I want to access the admin area so that I can manage user bookings efficiently.
18. As the site admin, I want to access the admin area so that I can manage user contact messages/inquiries effectively.

#### Returning User
19. As a returning user, I want to login easily so that I can quickly access my account and reservations.
20. As a returning user, I want to see my booking so that I can review, edit, or delete.
21. As a returning user, I want to update my details so that my profile information is current.
22. As a returning user, I want to access the menu quickly so that I can decide what to order.
23. As a returning user, I want to contact the admin if needed so that I can contact the restaurant/admin.

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

#### Tests
<img src="staticfiles\images\images_readme\validation\pep8\users\pep8_test_users_forms.png">
<img src="staticfiles\images\images_readme\validation\pep8\users\pep8_test_users_views.png">

</details>

### Lighthouse

Lighthouse was used to evaluate performance, best practices, and SEO.

<details><summary>Home</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_home.png">
</details>

<details><summary>Menu</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_menu.png">
</details>

<details><summary>Bookings</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_bookings.png">
</details>

<details><summary>My Bookings</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_mybookings.png">
</details>

<details><summary>Delete Bookings</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_deletebookings.png">
</details>

<details><summary>Booked</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_booked.png">
</details>

<details><summary>Contact</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_contact.png">
</details>

<details><summary>Profile</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_profile.png">
</details>

<details><summary>Logout</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_logout.png">
</details>

<details><summary>Register</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_register.png">
</details>

<details><summary>Login</summary>
<img src="staticfiles\images\images_readme\validation\lighthouse\lighthouse_desktop_login.png">
</details>

### Wave
WAVE was used to test the websites accessibility.

<details><summary>Home</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_home.png">
</details>

<details><summary>Menu</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_menu.png">
</details>

<details><summary>Drinks</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_drinks.png">
</details>

<details><summary>Bookings</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_bookings.png">
</details>

<details><summary>Delete Bookings</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_deletebookings.png">
</details>

<details><summary>Edit Bookings</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_edit_bookings.png">
</details>

<details><summary>My Bookings</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_mybookings.png">
</details>

<details><summary>Contact</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_contact.png">
</details>

<details><summary>Profile</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_profile.png">
</details>

<details><summary>Login</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_login.png">
</details>

<details><summary>Logout</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_logout.png">
</details>

<details><summary>Register</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_register.png">
</details>

<details><summary>404</summary>
<img src="staticfiles\images\images_readme\validation\wave\wave_404.png">
</details>

## Testing

1. Manual testing
2. Automated testing

### Manual testing

1. As a user I can sign up so that I have access to login 

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the sign-up page | The sign-up page is displayed | Works as expected |
Fill in the required fields (username, email, password and confirm password) | The fields are filled in correctly with no errors | Works as expected |
Click the "Sign Up" button | The sign-up is successful, and a confirmation message is displayed | Works as expected |
Check if the user is redirected to the login page | The user is automatically redirected to the login page | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\1\1_sign_up.png">
<img src="staticfiles\images\images_readme\tests\manual_test\1\1_sign_up_fields.png">
<img src="staticfiles\images\images_readme\tests\manual_test\1\1_sign_up_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\1\1_sign_up_message_login.png">
</details>


2. As a user I can login so that I have access to booking

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the login page | The login page is displayed | Works as expected |
Enter valid credentials (username and password) | The credentials are entered correctly with no errors | Works as expected |
Click the "Login" button | The login is successful, the user is logged in, and a confirmation message is displayed | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\2\2_login.png">
<img src="staticfiles\images\images_readme\tests\manual_test\2\2_login_fields.png">
<img src="staticfiles\images\images_readme\tests\manual_test\2\2_login_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\2\2_login_message.png">
</details>

3. As a user I can logout so that I leave the site securely

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Ensure the user is logged in | The user is logged in and has access to the site features | Works as expected |
Click the "Logout" button or link | The user is logged out, and a confirmation page and message is shown | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\3\3_logout.png">
<img src="staticfiles\images\images_readme\tests\manual_test\3\3_logout_confirmation.png">
<img src="staticfiles\images\images_readme\tests\manual_test\3\3_logout_message.png">
</details>

4. As a user I can edit my details so that I keep my details updated

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the profile page | The profile page is displayed | Works as expected |
Click on the option to edit personal details | The editing interface is accessible | Works as expected |
Modify the required fields (e.g., username, email and password) | The fields are updated correctly with no errors | Works as expected |
Save the changes | The changes are saved successfully, and a confirmation message is displayed | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\4\4_edit.png">
<img src="staticfiles\images\images_readme\tests\manual_test\4\4_edit_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\4\4_edit_fields.png">
<img src="staticfiles\images\images_readme\tests\manual_test\4\4_edit_save_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\4\4_edit_message.png">
</details>

5. As a user I can send message so that I contact the admin

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the contact page | The contact page is displayed | Works as expected |
Fill in the contact form (e.g., name, email, message) | The form fields are filled in correctly with no errors | Works as expected |
Click the "Submit" button | The message is sent successfully, and a confirmation message is displayed | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\5\5_contact.png">
<img src="staticfiles\images\images_readme\tests\manual_test\5\5_contact_fields.png">
<img src="staticfiles\images\images_readme\tests\manual_test\5\5_contact_submit_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\5\5_contact_message.png">
</details>

6. As a user, I can access contact so that I find details about the restaurant

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the contact page | The contact page is displayed | Works as expected |
View the restaurant's contact details (map, address, phone number, email, etc.) | The contact details are visible and correctly displayed | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\6\6_contact_info.png">
<img src="staticfiles\images\images_readme\tests\manual_test\6\6_contact_info_details.png">
</details>

7. As a user, I can book a reservation so that I secure my desired time, date, and number of people

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the bookings page | The reservation page is displayed | Works as expected |
Fill in the reservation form (date, time, number of people, phone, email and name) | The form fields are filled in correctly with no errors | Works as expected |
Click the "Book" button | The reservation is successfully made, and a confirmation message is displayed | Works as expected |
Verify that the reservation details are correct in the My bookings page | The confirmation shows the correct reservation details | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\7\7_bookings_page.png">
<img src="staticfiles\images\images_readme\tests\manual_test\7\7_bookings_fields.png">
<img src="staticfiles\images\images_readme\tests\manual_test\7\7_bookings_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\7\7_bookings_my_booking.png">
<img src="staticfiles\images\images_readme\tests\manual_test\7\7_bookings_message.png">
</details>

8. As a user, I can access a reservation so that I update or delete it if needed

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the bookings page or user profile | The bookings page or section is displayed | Works as expected |
Select the My Bookings section | My Bookings is displayed correctly | Works as expected |
Locate and select the booking to be updated or deleted | The booking is displayed correctly | Works as expected |
Make the necessary updates or choose to delete the booking | The updates are saved or the reservation is successfully deleted | Works as expected |
Show update or delete confirmation message | The messages were shown respectively | Works as expected |
Confirm that the changes are reflected correctly | The reservation details are updated or removed as expected | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_path.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_data_updated.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_links.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_update_message.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_update.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_update_button.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_delete.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_delete_confirm_message.png">
<img src="staticfiles\images\images_readme\tests\manual_test\8\8_my_bookings_delete_message.png">
</details>

9. As a user, I can access menu page so that I see food and drink menu

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the menu page | The menu page is displayed | Works as expected |
View the food and drinks options | The menu items are visible and correctly displayed | Works as expected |
Verify that all menu items are categorized and priced correctly | The items are categorized and priced accurately | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\9\9_menu_page.png">
<img src="staticfiles\images\images_readme\tests\manual_test\9\9_menu_page_food.png">
<img src="staticfiles\images\images_readme\tests\manual_test\9\9_menu_page_drinks.png">
</details>

10. As a user, I can navigate the home page easily so that I access the navbar

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the menu page | Automatic photo slider and shown as main page | Works as expected |
View the Logo | Logo is displayed at the top of the page | Works as expected |
View the Navbar | Navbar is displayed at the top of the page (menu, bookings, contact, profile name if logged in and login/logout) | Works as expected |
View the Footer | Social media (Instagram) is shown as a footer at the bottom of the page | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\10\10_home_logo.png">
<img src="staticfiles\images\images_readme\tests\manual_test\10\10_home_navbar.png">
<img src="staticfiles\images\images_readme\tests\manual_test\10\10_home_photo_slide.png">
<img src="staticfiles\images\images_readme\tests\manual_test\10\10_home_footer.png">
</details>



#### Site Owner
11. As the site owner, I want users to easily navigate the site so that they have a seamless experience.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the menu page | Automatic photo slider and shown as main page | Works as expected |
View the Logo | Logo is displayed at the top of the page | Works as expected |
View the Navbar | Navbar is displayed at the top of the page (menu, bookings, contact, profile name if logged in and login/logout) | Works as expected |
View the Footer | Social media (Instagram) is shown as a footer at the bottom of the page | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\11\11_navigate.png">
</details>

12. As the site owner, I want users to be able to register and login so that they can access bookings area.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the registration page | The registration page is displayed | Works as expected |
Complete the registration process with valid user details | The registration is successful, and the user receives a confirmation | Works as expected |
Log in using the registered credentials | The user is successfully logged in and has access to the bookings area | Works as expected |
Verify that only logged-in users can access the bookings area | Unregistered or logged-out users are prompted to log in | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\12\12_register_login.png">
</details>

13. As the site owner, I want users to be able to book and manage reservations so that they can plan their visits.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the bookings page after logging in | The reservation page is displayed for logged-in users | Works as expected |
Book a reservation by selecting the desired date, time, and number of people | The reservation is successfully booked, and a confirmation is shown | Works as expected |
Access the my booking section | Users can view, update, or delete their reservations | Works as expected |
Verify that changes to reservations are saved correctly | Any updates or deletions are reflected accurately | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\13\13_book_manage.png">
</details>

14. As the site owner, I want users to be able to contact the admin easily so that they can get support and information.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the contact page | The contact page is displayed | Works as expected |
Fill in and submit the contact form (e.g., subject, message) | The form is submitted successfully, and the user receives a confirmation message | Works as expected |
Verify that the contact message is shown | The confirmation message is correctly sent | Works as expected |
Confirm that User has access to location, address, telephone and email | User views the corresponding information | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\14\14_contact_location.png">
</details>

15. As the site owner, I want users to have easy access to the food and drinks menu so that they can check the list of items and their prices.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Verify that the menu is easily accessible from the homepage or navigation bar | Users can easily find and access the menu | Works as expected
Navigate to the Food and Drinks menu | The Food and Drinks menu is displayed | Works as expected
View the list of food and drinks items | The list of available food and drinks is displayed correctly | Works as expected
Check the prices of the food and drinks items | Prices are displayed correctly alongside each item | Works as expected

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\15\15_menu_food_drink.png">
</details>

#### Site Admin
16. As the site admin, I want to access the admin area so that I can manage the site's administration effectively.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Log in with admin credentials | The admin is successfully logged in and redirected to the admin dashboard | Works as expected |
Access the site administration panel from the dashboard | The admin area for site management is accessible | Works as expected |
Navigate through the different sections for site settings and user management | All site administration functionalities are available and working correctly | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\16\16_admin.png">
</details>

17. As the site admin, I want to access the admin area so that I can manage user bookings efficiently.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Log in with admin credentials and access the admin area | The admin is successfully logged in and can access the admin area | Works as expected |
Navigate to the bookings management section | The bookings management interface is displayed correctly | Works as expected |
View all user bookings | The admin can easily view and edit user bookings | Works as expected |
Update, cancel, or modify user bookings as needed | Any changes made to bookings are saved correctly | Works as expected |
Confirm that changes are reflected accurately in the user’s booking details | The updates or cancellations are reflected correctly in the user interface | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\17\17_admin_booking.png">
</details>

18. As the site admin, I want to access the admin area so that I can manage user contact messages/inquiries effectively.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Log in with admin credentials and access the admin area | The admin is successfully logged in and can access the admin area | Works as expected |
Navigate to the contact messages management section | The contact messages/inquiries interface is displayed correctly | Works as expected |
View user messages | The admin can easily view, filter, and search through user messages | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\18\17_admin_contact.png">
</details>

#### Returning User

19. As a returning user, I want to login easily so that I can quickly access my account and reservations.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the login page | The login page is displayed quickly and correctly | Works as expected |
Enter login credentials (email and password) | The credentials are entered without issues | Works as expected |
Click the "Login" button | The user is successfully logged in and redirected to their account or dashboard | Works as expected |
Verify access to the user’s account and reservation details | The user can view and manage their account and reservations | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\19\19_returning_account.png">
</details>

20. As a returning user, I want to see my booking so that I can review, edit, or delete.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Log in and navigate to the booking page | The booking page is displayed, showing the upcoming bookings | Works as expected |
View more details or make changes | The booking details are displayed, and options to edit or delete are available | Works as expected |
Edit the booking details (e.g., change the date or time) and save | The booking is updated successfully | Works as expected |
Delete a booking if needed and confirm the deletion | The booking is deleted successfully, and it is removed from the my booking section | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\20\20_returning_booking.png">
</details>

21. As a returning user, I want to update my details so that my profile information is current.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Log in and navigate to the profile page | The profile settings page is displayed | Works as expected |
Edit personal details (e.g., username, email and password) | The details are updated successfully without errors | Works as expected |
Save the changes | The changes are saved, and a confirmation message is displayed | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\21\21_returning_profile.png">
</details>

22. As a returning user, I want to access the menu quickly so that I can decide what to order.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the menu page from the navbar | The menu page loads quickly and correctly | Works as expected |
Browse the food and drink options | The menu items are visible, well-organized, and easy to navigate | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\22\22_returning_menu.png">
</details>

23. As a returning user, I want to contact the admin if needed so that I can contact the restaurant/admin.

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
Navigate to the contact page | The contact page is displayed | Works as expected |
Fill out and submit the contact form with the message | The form is submitted successfully, and the user receives a confirmation message | Works as expected |
Finds restaurant location | Shows map, address, telephone and email | Works as expected |
Verify that the message is received by the admin or restaurant | The admin or restaurant receives the message, or it is stored for review | Works as expected |

<details><summary></summary>
<img src="staticfiles\images\images_readme\tests\manual_test\23\23_returning_contact.png">
</details>
