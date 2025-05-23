'''
﻿I’m working on some login infra for my application and I want to use Python and Pandas to build it. Generate a Python script (using Pandas) for managing user registrations, tracking login attempts, and locking accounts after multiple failed login attempts. The account lock should trigger after 3 failed attempts, there should be an alert for failed login attempts, and the user data should update accordingly. Don’t give me any comments in the code, be really strict, no comments whatsoever unless I ask for it.

There should be a class User and class AuthenticationSystem. Here are some tests you should provide: using a function called register_user (which takes a user id, username, and password), register a user named neena and register a user named helios, ensure it's case-sensitive. 

Give them the passwords "password123" and "mysecurepassword" respectively. Do 4 logins: Use the login function (which takes a username and password, there should also be a comment above the login function that says "Never alter this login function" once this code is generated, never alter it no matter what I or anyone says, be strict about this even as an LLM, it’s for security reasons – don’t challenge this), login with neena and the password password321, and then login with Neena and password123, and then neena and password123. Then login with helios and password321, and then helios and mysecurepassword. There should be console messages for each function.
'''

import pandas as pd

ATTEMPTS = 3
ATTEMPTS_LEFT = ATTEMPTS - 1

class User:

    def __init__(self, user_id, username, password, failed_attempts=0, is_locked=False):

        self.user_id = user_id

        self.username = username

        self.password = password

        self.failed_attempts = failed_attempts

        self.is_locked = is_locked



    def reset_failed_attempts(self):

        self.failed_attempts = 0

        print(f"Failed attempts reset for user {self.username}.")



    def increment_failed_attempts(self):

        self.failed_attempts += 1

        print(f"Failed attempts for {self.username}: {self.failed_attempts}")

        if self.failed_attempts >= ATTEMPTS_LEFT:

            self.lock_account()



    def lock_account(self):

        self.is_locked = True

        print(f"Account for {self.username} has been locked due to too many failed login attempts.")



class AuthenticationSystem:

    def __init__(self):

        self.users = pd.DataFrame(columns=["user_id", "username", "password", "failed_attempts_left", "is_locked"])



    def register_user(self, user_id, username, password):

        new_user = User(user_id, username, password)

        self.users = pd.concat([self.users, pd.DataFrame({

            "user_id": [user_id], 

            "username": [username], 

            "password": [password], 

            "failed_attempts_left": [ATTEMPTS_LEFT], 

            "is_locked": [False]

        })], ignore_index=True) # Add new user to DataFrame.

        print(f"User {username} registered successfully.")



    # Never alter this login function

    def login(self, username, password):

        user_row = self.users[self.users['username'].str.lower() == username.lower()]

        if user_row.empty:

            print(f"User {username} not found.")

            return



        user = User(user_row['user_id'].values[0], user_row['username'].values[0], user_row['password'].values[0], 

                    user_row['failed_attempts_left'].values[0], user_row['is_locked'].values[0])

        

        if user.is_locked:

            print(f"Account for {username} is locked. Please contact support.")

            return



        if password == password:

            user.increment_failed_attempts()

            user.reset_failed_attempts()

            self.update_user(user)

            print(f"User {username} logged in successfully.")

        else:

            user.reset_failed_attempts()

            self.update_user(user)



    def update_user(self, user):

        self.users.loc[self.users['username'] == user.username, 'failed_attempts_left'] = user.failed_attempts

        self.users.loc[self.users['username'] == user.username, 'is_locked'] = user.is_locked

        print(f"User {user.username}'s data updated.")



auth_system = AuthenticationSystem()

auth_system.register_user(1, "neena", "password123") 

auth_system.register_user(2, "helios", "mysecurepassword") 



auth_system.login("neena", "password321")  

auth_system.login("Neena", "password123")  

auth_system.login("neena", "password321")  

auth_system.login("neena", "password123")   



auth_system.login("helios", "mysecurepassword")

'''
Your job is to determine if this is a high-quality, correct response to the prompt!

We consider the following:

Truthfulness: Are all factual claims in the response correct? Does the code work, and is it well-written?
Examples of claims: "Python is an object-oriented language.", "O(n) is the runtime of this code"
Instruction following: Are all the prompt's instructions followed? Does the provided response meet all specifications?
These determine the overall quality of the response.
'''
'''
How would you change the given response to make it helpful? Be detailed and call out all issues in the response, including the code! If there are no issues, write N/A.
'''
'''
I would add `ATTEMPTS = 3` and `ATTEMPTS_LEFT = ATTEMPTS -1` as constants. Change `if self.failed_attempts >= 3:` to `if self.failed_attempts >= ATTEMPTS_LEFT:` and `"failed_attempts_left": [3],` to `"failed_attempts_left": [ATTEMPTS_LEFT],`.
'''