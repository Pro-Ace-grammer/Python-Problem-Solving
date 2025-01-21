'''
Write a decorator that adds authentication by checking if a given user has the required role to execute a function.
'''

def check_role(admin_role):
    def decorator(func):
        def wrapper(user_role, *args, **kwargs):
            if admin_role == user_role:
                func(*args, **kwargs)
            else:
                print(f'Access Denied! required {admin_role} but got {user_role}')
            import time
            time.sleep(2)
        return wrapper
    return decorator

@check_role('Admin')
def on_item(task):
    print(f'Task to "{task}" is completed')

on_item('User', 'Delete Item')
on_item('Admin', 'Delete Item')
