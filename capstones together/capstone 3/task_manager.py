#imported the date module from the datetime module
from datetime import date

#user menu
def menu(username):
    print("please choose one of the following options:")
    print("va - view all tasks")
    print("vm - view my tasks")
    print("e - exit")
    

#register function
def register(username):
    if username == "admin":
        new_user = input("please enter new user name: ") #used inputs to get new user name and password then to comfirm the password
        new_password = input("please enter new password: ")
        pass_check = input("please confirm new password: ")
        if pass_check == new_password: #created a condition to check if the passwords are the same
            file = open("new user.txt", "w+")
            file.write("This is the new added user: " + new_user + "| ") #made this to be the format formy outputs into the text file 
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
    task_status = "NO" #made the variable equal NO until the task is completed
    task_file = open("tasks.txt", "w")
    task.write(task_user + ", " + task_title + ", " + task_details + "\n" + current_date.strftime("%d %m %Y") + ", " + due_date + ", " + task_status)
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
    with open("tasks.txt", "r") as file:
        all_tasks = file.readlines()
        check_task = len(all_tasks) #made the length function read the length of my task line to give the count of ther amount of tasks
        for line in all_tasks:
            print(line, "\nthis is the number of tasks:" + " " + str(check_task))
    with open("user.txt", "r") as file:
        all_users = file.readlines()
        check_user = len(all_users)
        for line in all_users:
            print(line, "\nthis is the number of users:" + " " + str(check_user))
        
#login
option = ""
login = False

def login():
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
                if choice == "no":
                    login = False
                    menu(username)
                    while login == True:
                        print("please select an option")
                        if username == "admin":
                            print("r - register user")
                            print("a - add task")
                            print("va - view all tasks")
                            print("vm - view my tasks")
                            print("e - exit")
                            if username == "admin":
                                print("ds - display")
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
                        

    
                    

            


        
