from django.contrib.auth.models import User


def is_uservalid(func):
    def wrapper(*args, **kwargs):
        if args["user"]:
            try:
                user = User.objects.get(username=user)
            except:
                print("ok")
                return "user is not valid"
            else:
                print("ok")
                return func(*args, **kwargs)
            
        elif args["receiver"]:
            try:
                user = User.objects.get(username=args["receiver"])
            except:
                print("ok")
                return "user is not valid"
            else:
                print("ok")
                return func(*args, **kwargs)
        
        elif args["sender"]:
            try:
                user = User.objects.get(username=args["sender"])
            except:
                print("ok")
                return "user is not valid"
            else:
                print("ok")
                return func(*args, **kwargs)
            