https://roadmap.sh/projects/task-tracker

When starting the Task Tracker you will be prompted with the following options:

1. add
2. update
3. delete
4. mark-in-progress
5. mark-done
6. list
7. exit

If a task file does not exists, it will create one, otherwise the existing task list will be loaded.

add:
adds a new task

The below command will create a new task named Buy eggs at the end of the task list
add Buy eggs

update:
updates the name of an existing task.

The below command will update the task name at index 1 to Buy milk
update 1 Buy milk

delete:
deletes task at given index

The below command will delete the task at index 1
delete 1

mark-in-progress:
updates a task's status to in-progress

The below command will update the status of the task at index 1 to in-progress
mark-in-progress 1

mark-done:
updates a task's status to done

The below command will update the status of the task at index 1 to done
mark-done 1

list:
lists the tasks that are currently in the tracker depending on the arguments provided

The below command will list all the tasks currently in the tracker
list

The below command will list all of the tasks that are currently in progress
list in-progress

The below command will list all of the tasks that are done

list done

exit:
exits the program


