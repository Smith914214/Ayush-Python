

email = input("Enter your email: ")
username = ""
for i in email:
    if i == "@":
        break
    else:
        username = username + i

print("Username:", username)