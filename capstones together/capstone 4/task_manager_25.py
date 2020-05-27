import datetime
from datetime import date

#register function
def reg_user(username):
    if username == "admin":
        new_user = input("please enter new user name: ") #used inputs to get new user name and password then to comfirm the password
        new_password = input("please enter new password: ")
        pass_check = input("please confirm new password: ")
        if pass_check == new_password: #created a condition to check if the passwords are the same
            file = open("user.txt", "w")
            file.write("This is the new added user: " + new_user + ", ") #made this to be the format formy outputs into the text file 
            file.write("This is the new added password: " + new_password)
            file.close()
        else:
            print("invalid entry")
           
#add task function
def add_task(username):
    current_date = date.today()
    task_user = input("who will the task be given to: ") #used inputs to get the information about the tasks
    task_title = input("what is the name of the task: ")
    task_details = input("give details about the task: ")
    task_day = str(input("what day is the task due: "))
    task_month = str(input("what month is the task due: "))
    task_year = str(input("what year is the task due: "))
    due_date = f"{task_day}/{task_month[0:3]}/{task_year}"
    task_status = "NO" #made the variable equal NO until the task is completed
    print("Edit the task: yes or no\n")
    edit = input("edit: ")
    if edit == "yes":
        print(edit_task())
    else:
        with open("tasks.txt", "w") as task:
            task.write(task_user + ", " + task_title + ", " + task_details + "\n" + current_date.strftime("%d %m %Y") + ", " + due_date + ", " + task_status)
            task.close()

def edit_task():
    if task_key in task_dict.keys() and task_dict[task_key]["task_status"] == "NO":
        user_edit = input("enter the new user you would like to assign the task to: ")
        user_edit = task_dict[task_key]["task_user"]
        print("New user has been entered")
        rewrite_tasks(task_dict)
    if task_key in task_dict.keys() and task_dict[task_key]["task_status"] == "NO":
        title_edit = input("enter the new name of the task: ")
        title_edit = task_dict[task_key]["task_title"]
        print("New name of the task has been has been entered")
        rewrite_tasks(task_dict)    
    if task_key in task_dict.keys() and task_dict[task_key]["task_status"] == "NO":
        due_date_edit = input("enter new due dute day/month/year: ")
        due_date_edit = task_dict[task_key]["task_due_date"]
        print("New due date has been entered")
        rewrite_tasks(task_dict)
    if task_key in task_dict.keys() and task_dict[task_key]["task_status"] == "NO":
        status_edit = input("Has the task been completed YES or NO: ")
        status_edit = task_dict[task_key]["task_status"]
        print("Status of the task has been changed")
        rewrite_tasks(task_dict)

def rewrite_tasks(task_dict):
    task_file = open("task.txt", "w")
    for task in task_dict.values():
        for key, value in task.items():
            task_file.write(value + ", ")
        task_file.write("\n")
    task_file.close()

                  
#view all tasks function
def view_all(username):
    task = open("tasks.txt", "r")
    line = task.strip()
    task_line = line.split(", ")
    view = False
    count = 0
    for read in task_line:
        count += 1
        if read in username:
            print(f"Task Number: {count}")  
            print(f"Assigned to: {task_line[0]}")  
            print(f"Title: {task_line[1]}")  
            print(f"Details of the task: {task_line[2]}")  
            print(f"Date Assigned: {task_line[3]}")  
            print(f"Due Date: {task_line[4]}")  
            print(f"Task Complete: {task_line[5]}")
            view = True
    if view == False:
        print(f"{username}, there are not any tasks currently")
   
    
#view my tasks function
def view_mine(username):
    task = open("tasks.txt", "r")
    list_task = task.split(", ")
    task_list = task_list.strip()
    view = True
    count = 0
    task_number = 0
    for line in list_task:
        if count == 0:
            task_number += 1
            print(f"Task_number: {task_number}")
            print(f"Assigned to: {line}")
            count += 1
        elif count == 1:
            print(f"Title: {line}")
            count += 1
        elif count == 2:
            print(f"Details of the task: {line}")
            count += 1
        elif count == 3:
            print(f"Date assigned: {line}")
            count += 1
        elif count == 4:
            print(f"Due date: {line}")
            count += 1
        elif count == 5:
            print(f"Completion: {line}")
            count += 1
    task.close()
    if view == False:
            print("admin only")
          
#exit function
def leave(username):
    leave = input("are you sure you want to leave?: yes or no ")
    if leave == "yes":
        print("have a nice day")
        
#display function
def display(username):
    print("Display Statistics")
    task_overview = open('task_overview.txt', 'r')
    user_overview = open('user_overview.txt', 'r')
    report()
    load_tasks()

    if task_overview and not task_overview:
        print("Reports Have Not Been Generated.")
    print("Task Overview:")
    for report in task_overview:
        report = report.strip()
        print(report)
    task_overview.close()
    print("User Overview:")
    for report in user_overview:
        report = report.strip()
        print(report)


    

#this function generates the task report
def report(username):
    total_tasks = len(task_dict)
    completed = 0
    for task in task_dict.values():
        if task["task completed"] == "YES":
            completed = task_status[5]
            completed += 1

        incompleted_tasks = total_tasks - completed
        incompleted_percent = int((incomplete_tasks/ total_tasks) * 100)
        

    overdue = 0
    today = datetime.today()
    for task in task_dict.values():
        due_date = task["due_date"]
        check_date = datetime.fromisoformat(due_date)

        if check_date < today:
            overdue += 1

        overdue_tasks = total_tasks - overdue
        overdue_percent = int((overdue_tasks/ total_tasks) * 100)
        print(f"The total tasks are: , {total_tasks}\n, The completed tasks are: , {completed}\n , The incompleted tasks are: , {incompleted_tasks}\n, The overdue tasks are: , {overdue_tasks}")

        file = open("task_overview.txt", "w+")
        file.write("Task report")
        file.close()

        def dict_load():
            task_indexes = {}
            task_dict = {}
            index = 1

            task_file = open("tasks.txt")
            for line in task_file:
                if line.startswith("assigned to: "):
                    if task_dict:
                        task_indexes[index] = task_dict
                        index += 1
                        task_dict = {}
                check = line.find(":")
                if check != -1:
                    task_key = line[:check].strip()
                    task_value = line[check + 1 :].strip()
                    task_dict[task_key] = task_value

            task_dict = task_indexes[index]
            task_file.close()
            return task_indexes
   
   
            
        
#login


def login():
    login = False
    while login == False:
        user = open("user.txt","r")
        for line in user:
            line1 = line.strip()
            line2 = line1.split(",")
            username = input("please enter user name: ")
            password = input("please enter password: ")
            if line2[0] == username and line2[1] == password:
                choice = input("do you want to log in: yes or no ")
                if choice == "yes":
                    login = True
                    print("welcome")
                    while login == True:
                        print("please select an option")
                        if username == "admin":
                            print("r - register user")
                            print("a - add task")
                            print("va - view all tasks")
                            print("vm - view my tasks")
                            print("e - exit")
                            if username == "admin":
                                print("ds - display statistics")
                                print("gr - generate report")
                                option = input(": ")
                                if option == "r":
                                    register(username)
                                if option == "a":
                                    add_task(username)
                                if option == "va":
                                    view_all(username)
                                if option == "vm":
                                    view_mine(username)
                                if option == "e":
                                    leave(username)
                                    login = False
                                if username == "admin" and option == "ds":
                                    display(username)
                                if username == "admin" and option == "gr":
                                    report(username)
                        

login()

    
                    

            


        
