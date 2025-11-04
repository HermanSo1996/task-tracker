import json
import os


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
            f = {"taskname": str(command[1]), "status": "created"}
            temp.append(f)
        with open("taskdata.json", 'w') as json_file:
            json.dump(data, json_file)
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
            json.dump(data,json_file)