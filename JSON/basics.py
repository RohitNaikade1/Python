import json

student={
    "Name":"rohit",
    "age":22,
    "Subject":["OOP","DSA","MP"]
}


#printing json object
# b=json.dumps(student)

# print(b)


#writing json object
# with open("data.json","w") as write_file:
#     json.dump(student,write_file)


#reading json object

with open("data.json","r") as read_file:
    b=json.load(read_file)
    print(b)