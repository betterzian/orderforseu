import json
try:
    file = open('./data/ur_ps.json','r')
    data = json.load(file)
    username = str(data["username"])
    password = str(data["password"])
    reason = str(data["reason"])
    site = str(data["site"])
except:
    username = input("username: ")
    password = input("password: ")
    reason = input("reason: ")
    site = input("site: ")
    dic = {
        "username":username,
        "password":password,
        "reason":reason,
        "site":site
    }
    with open("./data/ur_ps.json","w") as outfile:
        json.dump(dic,outfile)

start_time = "11:00"
end_time = "23:50"
