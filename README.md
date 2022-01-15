# TRAININGS DIARY
#### Video Demo:  https://youtu.be/WnBYfuybJxI
#### Description:
Every athlete wants to document his trainings and successes. But what is the ideal way? I have always lacked a simple digital solution
that meets my expectations.Training Diary is the answer.

With the help of Trainings Diary you can log all activities, get an overview of all logged activities, and additionally there is a
summary page that shows all logged activities grouped by activity (with aggregated training times resp. duration). The web based responsive mobile-first application is usable by multiple users


## Technology stack:
- Flask application
- SQLite database
- Bootstrap Frontend

## SQLite database

The application uses a relatively simple databank. The database consists of 2 tables.

 **TABLE users**
 This table stores all users, with necessary data for registrationand log in.
- id (PRIMARY KEY)
- username
- HASH (password)

 **TABLE history**
This table stores all information which are related to logged activities
- id (PRIMARY KEY)
- user_id (FOREIGN KEY related to user in table(users))
- date
- activity
- hardness
- duration
- description

## Navbar of Application

The display of the navbar differs depending on whether the user is logged in or not.
If the user is not logged in, there is only the logo (with link to index.html). Logged in users have the options history,
log training and diary within the navbar.

## List of all functionalities and pages:

- Multi-user support: Each user can create an account
- Homepage: shows the last 5 logged activities
- log training: capture date, activity type, hardness of training, duration in minutes, and a free-field description
- diary: Shows in tabular form all logged activities with date, activity, hardness, duration and description
- Summary: Shows in tabular form all logged activities grouped by activity. Per row you see quantity of trainings and total time

## Detailed Description of functionalities:

**Registration:**

You can register with a username and password. The application can handle an unlimited number of users. For registration you need a username and
a password. In the process there is a password confirmation field to ensure that you enter 2 times the same password.

**Homepage:**

On the homepage there is a short description of the app and the last 5 logged activities of the currently logged in user.

**Log Training:**

Capture: date, activity type, hardness of training, duration in minutes, and a free-field description.
The fields date and duration are mandatory to fill. If they are not filled in, you will receive an error message, when you try to submit.
- To enter a date you have a date picker.
- You can choose from different activities.
- Hardness hs the attributes easy, moderate, hard and very hard.
- In the description field you can make notes about your training. For example: Weather, how you felt, special equipment or comments about it etc.

**Diary:**

The diary is your personal trainings history:
Shows in tabular form all logged activities with
- date,
- activity,
- hardness,
- duration and
- description (free text field)
The entries are sorted in descending order by log date (or more precisely: id)

**Summary**

Shows in tabular form all logged activities:
- grouped by activity
- quantity of trainings based on the grouped activity and
- total time (it is the aggregated times per grouping)

## Structure of Project Folder

- Folder: static (all images, css file and favicon)
- Folder: templates (apology.html, history.html, index.html, layout.html, log.html, login.html, register.html, summary.html)
- File: app.py (python file with the application's business logic)
- File: diary.db (SQLite database-file)
- File: helpers.py (necessary functions for application)
- File README.md (in this file you are reading now)
- File requirements.txt 