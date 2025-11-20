import json
import os
import datetime

def writeJson(jsonfile,data):
    with open(jsonfile, 'w') as json_file:
            json.dump(data,json_file, indent=2)

def addtask(jsonfile):
    with open(jsonfile) as json_file:
        data = json.load(json_file)
        temp = data["tasks"]
        f = {"id": (len(temp)+1), "description": str(command[1]), "status": "todo", "createdAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
        temp.append(f)
    writeJson(jsonfile,data)
    print("Task added with ID: " +str(len(temp)))

def listtask(jsonfile):
    with open(jsonfile) as json_file:
        data = json.load(json_file)
        temp = data["tasks"]
        if len(command) == 1:
            print(data)
        elif command[1] == "done":
            templist = []
            for i in range(0, len(temp)):
                if temp[i]["status"] == "done":
                    templist.append(temp[i])
            print(templist)
        elif command[1] == "in-progress":
            templist = []
            for i in range(0, len(temp)):
                if temp[i]["status"] == "in-progress":
                    templist.append(temp[i])
            print(templist)
        elif command[1] == "todo":
            templist = []
            for i in range(0, len(temp)):
                if temp[i]["status"] == "todo":
                    templist.append(temp[i])
            print(templist)

def delete(jsonfile):
    with open("taskdata.json") as json_file:
        data = json.load(json_file)
        temp = data["tasks"]
        del temp[int(command[1])-1]
        writeJson(jsonfile,data)

def updatedesc(jsonfile):
    with open(jsonfile) as json_file:
        data = json.load(json_file)
        temp = data["tasks"]
        tempid = temp[int(command[1])-1]["id"]
        temptime = temp[int(command[1])-1]["createdAt"]
        tempstatus = temp[int(command[1])-1]["status"]
        if type(int(command[1])) == int:
            temp[int(command[1])-1] = {"id": str(tempid), "description": str(command[2]), "status": str(tempstatus), "createdAt": str(temptime), "updatedAt": str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))}
        writeJson(jsonfile,data)

def updatestatus(jsonfile):
    with open(jsonfile) as json_file:
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
        writeJson(jsonfile,data)         

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
    
    possibleoptions = ["add", "list", "delete", "update", "mark-in-progress", "mark-done","exit"]

    try:
        assert command[0] in possibleoptions
        
        if command[0] == "add":
            addtask("taskdata.json")

        if command[0] == "list":
            possibleoptions = ["done","todo","in-progress"]
            try:
                if len(command) > 1:
                    assert command[1] in possibleoptions
                listtask("taskdata.json")
            except AssertionError as e:
                print("Please enter a valid task status to list by")

        if command[0] == "delete":
            try:
                assert int(command[1]) > 0
                delete("taskdata.json")
            except AssertionError as e:
                print("Please enter a valid index")
            except ValueError as e:
                print("Please enter a valid index")
            except IndexError as e:
                print("Task is not in list, please select a valid task")
            

        if command[0] == "update":
            print(type(command[1]))
            try:
                if int(command[1])<1:
                    raise ValueError
                if len(command) < 3:
                    raise AssertionError
                else:
                    updatedesc("taskdata.json")
            except ValueError as e:
                print("Please enter a valid index")
            except IndexError as e:
                print("Please enter a valid index")
            except AssertionError as e:
                print("Please enter a value to update")    

        if command[0] == "mark-in-progress" or command[0] == "mark-done":
            try:
                assert int(command[1]) > 0
                updatestatus("taskdata.json")
            except AssertionError as e:
                print("Please enter a valid index")
            except ValueError as e:
                print("Please enter a valid index")
            except IndexError as e:
                print("Task is not in list, please select a valid task")           

    except IndexError as e:
        print("Please enter a valid command")
    
    except AssertionError as e:
        print("Please enter a valid command")