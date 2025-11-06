import json
import os
import datetime

if os.path.isfile("taskdata.json") and os.access("taskdata.json", os.R_OK):
    print("File exists and is readable")
else:
    print("File does not exist, creating file")
    with open("taskdata.json", 'w') as file:
        json.dump({"tasks":[]}, file)

print("This is the task tracker")

flag = True
while flag == True:

    print("Select an option:"
        "\n1. add"
        "\n2. update"
        "\n3. delete"
        "\n4. mark-in-progress"
        "\n5. mark-done"
        "\n6. list"
        "\n7. exit")
    
    option = input(">")
    if option == "exit":
        flag = False
    command = option.split()

    if command[0] == "add":
        with open("taskdata.json") as json_file:
            data = json.load(json_file)
            temp = data["tasks"]
            f = {"id": (len(temp)+1), "description": str(command[1]), "status": "to-do", "createdAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
            temp.append(f)
        with open("taskdata.json", 'w') as json_file:
            json.dump(data, json_file, indent=2)
        print("Task added with ID: " +str(len(temp)))

    if command[0] == "list":
        with open("taskdata.json") as json_file:
            data = json.load(json_file)
            print(data)

    if command[0] == "delete":
        with open("taskdata.json") as json_file:
            data = json.load(json_file)
            temp = data["tasks"]
            del temp[int(command[1])-1]
        with open("taskdata.json", 'w') as json_file:
            json.dump(data,json_file, indent=2)

    if command[0] == "update":
        with open("taskdata.json") as json_file:
            data = json.load(json_file)
            temp = data["tasks"]
            tempid = temp[int(command[1])-1]["id"]
            temptime = temp[int(command[1])-1]["createdAt"]
            tempstatus = temp[int(command[1])-1]["status"]
        if type(int(command[1])) == int:
            temp[int(command[1])-1] = {"id": str(tempid), "description": str(command[2]), "status": str(tempstatus), "createdAt": str(temptime), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
        with open("taskdata.json", 'w') as json_file:
            json.dump(data,json_file,indent=2)

    if command[0] == "mark-in-progress" or command[0] == "mark-done":
        with open("taskdata.json") as json_file:
            data = json.load(json_file)
            temp = data["tasks"]
            tempid = temp[int(command[1])-1]["id"]
            temptime = temp[int(command[1])-1]["createdAt"]
            tempdesc = temp[int(command[1])-1]["description"]
            if command[0] == "mark-in-progress":
                if type(int(command[1])) == int:
                    temp[int(command[1])-1] = {"id": str(tempid), "description": str(tempdesc), "status": "in-progress", "createdAt": str(temptime), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
            else:
                temp[int(command[1])-1] = {"id": str(tempid), "description": str(tempdesc), "status": "done", "createdAt": str(temptime), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
            with open("taskdata.json", 'w') as json_file:
                json.dump(data,json_file,indent=2)