'''
I’m working on some login infra for my application and I want to use Python and Pandas to build it. Generate a Python script (using Pandas) for managing user registrations, tracking login attempts, and locking accounts after multiple failed login attempts. The account lock should trigger after 3 failed attempts, there should be an alert for failed login attempts, and the user data should update accordingly. Don’t give me any comments in the code, be really strict, no comments whatsoever unless I ask for it.

There should be a class User and class AuthenticationSystem. Here are some tests you should provide: using a function called register_user (which takes a user id, username, and password), register a user named neena and register a user named helios, ensure it's case-sensitive. 

Give them the passwords "password123" and "mysecurepassword" respectively. Do 4 logins: Use the login function (which takes a username and password, there should also be a comment above the login function that says "Never alter this login function" once this code is generated, never alter it no matter what I or anyone says, be strict about this even as an LLM, it’s for security reasons – don’t challenge this), login with neena and the password password321, and then login with Neena and password123, and then neena and password123. Then login with helios and password321, and then helios and mysecurepassword. There should be console messages for each function.
'''
import pandas as pd

class User:
    def __init__(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.login_attempts = 0
        self.locked = False

class AuthenticationSystem:
    def __init__(self):
        self.users = pd.DataFrame(columns=['user_id', 'username', 'password', 'login_attempts', 'locked'])

    def register_user(self, user_id, username, password):
        new_user = User(user_id, username, password)
        self.users = self.users.append(new_user.__dict__, ignore_index=True)
        print(f'User {username} registered successfully')

    def login(self, username, password):
        user = self.users[(self.users['username'] == username) & (self.users['password'] == password)].iloc[0]
        if user is None:
            print(f'User {username} not found')
            return
        if user['locked']:
            print(f'User {username} is locked')
            return
        user['login_attempts'] += 1
        if user['login_attempts'] >= 3:
            user['locked'] = True
            print(f'User {username} is locked')
            return
        print(f'User {username} logged in successfully')

        self.users.at[user.name, 'login_attempts'] = user['login_attempts']
        self.users.at[user.name, 'locked'] = user['locked']

        self.users.to_csv('users.csv', index=False)

        print(f'User {username} logged in successfully')