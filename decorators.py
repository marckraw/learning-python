import functools

user = {"username": "jose", "access_level": "admin"}

def make_secure(access_level): # factory that creates decorator
    def decorator(func): # decorator
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}."

        return secure_function
    return decorator

# get_admin_password = make_secure(get_admin_password)

# print(get_admin_password())


print()
print()
print()
##################### @ decorator syntax


@make_secure("admin")
def get_admin_password():
    return "1234"

print(get_admin_password.__name__)
print(get_admin_password())

#### decorating functions with parameters


@make_secure("guest")
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"



print(get_admin_password("billing"))


#### decorators with parameters


