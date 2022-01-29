from classes.user import User

def user_resolver(obj, info, name: str) -> User:
    try:
        user: User = User(name)
    except Exception as error:
        user = None
        print(error)
    return user