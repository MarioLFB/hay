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
As a user I can sign up so that I have access to login 
As a user I can login  so that I have access to booking 
As a user I can logout so that I leave the site securely 
As a user I can edit my details so that I keep my details updated 
As a user I can send message so that  I contact the admin 
As a user, I can access contact so that I find details about the restaurant  
As a user, I can book a reservation so that I secure my desired time, date, and number of people 
As a user, I can access a reservation so that I update or delete it if needed 
As a user, I can access menu page so that I see food and drink menu 
As a user, I can navigate the home page easily so that I access the navbar 

#### Site Owner
As the site owner, I want users to easily navigate the site so that they have a seamless experience.
As the site owner, I want users to be able to register and login so that they can access exclusive features.
As the site owner, I want users to be able to book and manage reservations so that they can plan their visits.
As the site owner, I want users to be able to contact the admin easily so that they can get support and information.
As the site owner, I want to update the menu page regularly so that users see the latest offerings.
As the site owner, I want to manage user accounts so that I can ensure the security and accuracy of user information.
As the site owner, I want to receive messages from users so that I can address their inquiries and feedback.
As the site owner, I want to track user activity so that I can improve the site and services based on user behavior.

#### Returning User
As a returning user, I want to login easily so that I can quickly access my account and reservations.
As a returning user, I want to see my past reservations so that I can review my booking history.
As a returning user, I want to update my details so that my profile information is current.
As a returning user, I want to book new reservations easily so that I can plan my next visit.
As a returning user, I want to access the menu quickly so that I can decide what to order.
As a returning user, I want to contact the admin if needed so that I can get assistance or provide feedback.
As a returning user, I want to see any new updates or changes to the restaurant so that I am informed about new offerings or events.


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

##### Bookings Model
table_name
table_phone
table_email
table_capacity
table_date
table_time
user

##### Contact Model
name
email 
message
created_at