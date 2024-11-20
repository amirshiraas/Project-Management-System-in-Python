 #Creating a table to store all data
projects=[]
#declaring variable
available_workers=0

#Project Management Menu (Fig 1)
while True:
    print()
    print("             XYZ Company Main Menu")
    print()
    print("1. Add a new project to existing projects.")
    print("2. Remove a completed project from existing projects.")
    print("3. Add new workers to available workers group.")
    print("4. Update details on ongoing projects.")
    print("5. Project Statistics")
    print("6. Exit")
    choice = input("Please enter your Choice: ")

    if choice == '1':
        #Adding space to seperate Fig1  
        print()
        print("             Adding New Project")
        print()
#Adding project
        temp={} 
        temp["project_code"] =int(input("Enter project code (Enter '0' to restart): "))
    #If the user enters 0 restarting the loop
        if temp["project_code"] == 0:
            continue
        temp["clients_name"] = input("Enter client's name: ")
        temp["start_date"] = input("Enter starting date of the project: ")
        temp["end_date"] = input("Enter expected end date: ")
        temp["num_workers"] =int(input("Enter the number of workers needed: "))
    #Checking if there are enough available workers.
        if temp["num_workers"] > available_workers :
               print("Not enough workes available for the project.")
               continue
        temp["status"] = input("Enter project status (ongoing/completed/hold): ")
    #Displaying project details to the user for rechecking.
        print()
        print("Project code-",temp["project_code"])
        print("Clients Name-",temp["clients_name"])
        print("Start date-",temp["start_date"])
        print("End date-",temp["end_date"])
        print("Number of workers",temp["num_workers"])
        print("Project status",temp["status"])
    #Re-ask the user to save or delete the project.
        yes_or_no =input("Do you want to save the projec (yes/no)? ")
        if yes_or_no == 'yes':
    #Removing workers for available workers
            available_workers -= temp["num_workers"]
            projects.append(temp)
            print("Project saved succesfully")
        elif yes_or_no == 'no':
            print("Project deleted ")
            temp.clear()
        
    elif choice == '2':
    #Adding space to seperate Fig1
        print()
        print("             Remove Project")
        print()
#Removeing a completed project.
        project_code = int(input("Enter project code: "))
        for project in projects:
    #Cheaking if the project code is available and if the project is completed
            if project["project_code"] == project_code and project["status"] == "completed":
    #Re-asking the user if he/she wants to remove the completed project
                yes_or_no = input("Do you want to delete the project (yes/no)? ")
                if yes_or_no == 'yes':
                    projects.remove(project)
                    print("Project removed successfully.")
                    break  
            elif yes_or_no == 'no':
                continue
        else:
            print("Invalid code or project no completed.")      

    elif choice == '3':
    #Adding space to seperate Fig1
        print()
        print("       Adding new workers ")
#Adding new workers
        add_workers = int(input("Number of Workers to add: "))
        if add_workers<1:
            print("Please enter a postive number")
            continue
        yes_or_no =input("Do you want to save the projec (yes/no)? ")
    #Re-asking the user if he/she wants to add workers to availabe workers
        if yes_or_no == 'yes':
            available_workers += add_workers
            print("Workers added successfully.")
        elif yes_or_no == 'no':
            print()
            print("No workers added")
        

    elif choice == '4':
    #Adding space to seperate Fig1
        print()
        print("             Updating Project")
        print()
#Updating Project
        project_code =int(input("Enter project code (Enter '0' to restart): "))
    #If the user enters 0 restarting the loop
        if project_code == 0:
            continue
        temp_project=None
        for project in projects:
    #Cheacking if the code is valid or not
            if project["project_code"] == project_code:
                #Asking user the updated details
                available_workers += project["num_workers"]
                temp_project = project.copy()
                temp_project["clients_name"] = input("Enter client's name: ")
                temp_project["start_date"] = input("Enter starting date of the project: ")
                temp_project["end_date"] = input("Enter expected end date: ")
                temp_project["num_workers"] =int(input("Enter the number of workers needed: "))
                #Checking if there are enough available workers.
                if temp_project["num_workers"] > available_workers :
                    print("Not enough workes available for the project.")
                    continue
                temp_project["status"] = input("Enter project status (ongoing/completed/hold): ")
                yes_or_no=input("Do you wanna update this project (yes/no)?  ")
                if yes_or_no=='yes':
                #Removing workers for available workers
                    available_workers -= temp_project["num_workers"]
                    projects.remove(project)
                    projects.append(temp_project)
                    print("Project updated successfully.")
                else:
                    print("Project not updated.")

                break
            else:
                print("Invalid code Try Again.")
                

                

    elif choice == '5':
    #Adding space to seperate Fig1
        print()
        print("             Project Statitics")
        print()
#Showing Project Statistics
    #Adding all saved project to the status category
        ongoing_projects = sum(1 for project in projects if project["status"] == "ongoing")
        completed_projects = sum(1 for project in projects if project["status"] == "completed")
        hold_projects = sum(1 for project in projects if project["status"] == "hold")
    #Printing the sum of all status category
        print("Number of ongoing projects:", ongoing_projects)
        print("Number of completed projects:", completed_projects)
        print("Number of on hold projects:", hold_projects)
        print("Number of available workers to assign:", available_workers)
        user_input=input("Do you want to add a new project (Yes/No)? ")
        if user_input == "yes" :
            #Leaving space 
            print()
            print("Please type 1 and press enter ")
            #Leaving space
            print()
        elif user_input == "no" :
            continue
        else:
            print("Invalid choice")
    elif choice == '6':
    #Ending the whole program if user input 6
        print("Ending the program. bye!!")
        break
                
    else:
    #If user input invalid choice saying user its invalid and try again
        print()
        print("Not a valid choice. Please enter a valid choice between 1 and 6.")


