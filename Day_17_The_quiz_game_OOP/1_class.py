# class User: # name of the class sshould be start with capital letter(Pascal case)

# user_1 = User()   # Here this line need to come uder this class but because of no indent after class there ll be an error . same a 
# 
# class User:
    # # pass #This pass help u to leave the class empty and after that u can use any syntax without indent.
# 
# 
# user_1 = User()
# user_1.id = "001"
# user_1.username = "Monty"
# print(user_1.username)
# 
# user_2 = User()
# user_2.id = "002"
# user_2.username = "Robo"
# print(user_2.username)
# To avoid the making the methods again and again we can use init atrrbute.

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # If we are using a attribute which can be a repeated so we dont need to pass the argument for it that .

user_1 = User("001","Monty")
user_1 = User("002","Robo")

print(user_1.id)

