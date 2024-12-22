# Motorcycle website

My final CS50X projest built using:

- HTML
- CSS
- JavaScript
- Flask
- MySQL

Flask is a lightweight Python framework for web applications.

I'm going to rebuild it here (with improvements) and deploy it to Hostinger.

## This was the original README

Final project for CS50 2023
MOTORCYCLE website showcasing exclusive motorcycles

1 x Homepage 4 x Product pages 4 x Staff pages 1 x Newsletter/Contact/Go to blog page 1 x Register/Signup page 1 x Blog page 1 x Interact with blogs page

Newsletter to check if email address is already subscribed.

Register to allow user to register with an user name and email address.

Sign In to get user name, email address, and (hashed) password and validate them against existing database

How I got here:

This is the final project for my Harvard CS50 course. I had originally planned on using the homepage I designed for problem set 8, adding database functionality.

Didn't like the basic look of that project for this one so I changed things.

Followed Kevin Powell on Scrimba coding this Frontend Mentor challenge and used that as a template:

https://www.frontendmentor.io/challenges/space-tourism-multipage-website-gRWj1URZ3

I chose this as a template because I had built the original Space Tourism challenge copying the Figma design following along with this video, and I had appreciated the functionality as well as the accessibility options for assisted technologies.

Added Flask functionality for routing and connecting to MySQL database

These are the tables I created in the users.db database:

CREATE TABLE contact ( id INTEGER PRIMARY KEY AUTOINCREMENT, contact_name TEXT NOT NULL, contact_email TEXT NOT NULL, contact_message TEXT NOT NULL );

CREATE TABLE newsletter ( id INTEGER PRIMARY KEY AUTOINCREMENT, newsletter_email TEXT NOT NULL );

CREATE TABLE user ( id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT NOT NULL, password_hash TEXT NOT NULL );

CREATE TABLE blog ( id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP, blog_title TEXT NOT NULL, blog_user TEXT NOT NULL, content TEXT NOT NULL, replies INTEGER NOT NULL, likes INTEGER NOT NULL );
