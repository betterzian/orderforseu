import json
try:
    file = open('ur_ps.json','r')
    data = json.load(file)
    username = str(data["username"])
    password = str(data["password"])
except:
    username = input("username: ")
    password = input("password: ")
    dic = {
        "username":username,
        "password":password
    }
    with open("ur_ps.json","w") as outfile:
        json.dump(dic,outfile)

start_time = "11:00"
end_time = "23:50"
