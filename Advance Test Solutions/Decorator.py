'''
Python program that simulates a system storing sensitive informatio.
Create a decorator lock_sensitive_info to ve applied to fucntions, ensuring access
is restricted until a correct password is provided.
'''

def lock_sensitive_info(fx):
    def mod_info():
        while True:
            password = input('Password: ')
            if password == '1234':
                fx()
                break
            else:
                print('Invalid password Try again!!')
    return mod_info

@lock_sensitive_info
def get_sensitive_info():
    print('This is a very secret file')


get_sensitive_info()
