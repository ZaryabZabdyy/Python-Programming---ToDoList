
my_tasks = []  
task_id_counter = 1

print("\n--- DecodeLabs TO DO LIST  ---")  

while True:
    print("\n1. Add Task (Input/Process)")
    print("2. View Tasks (Output/Display)")
    print("3. Exit")
    
    choice = input("\nSelect option (1-3): ")
    

    if choice == '1':
        task_name = input("Enter Your Task: ")  
        task_row = {
            "id": task_id_counter,
            "task": task_name
        }
        
        my_tasks.append(task_row)  
        task_id_counter += 1
        print("[+] Success: Task inserted .")
        
    elif choice == '2':
        if len(my_tasks) == 0:
            print("[-] Database is empty.")
        else:
            print("\n=== List Of All Tasks ===")
            for row in my_tasks:  
                print(f"ID: {row['id']} | Task: {row['task']}")
            print("==============================")
            
    elif choice == '3':
        print("Shutting down engine. Goodbye!")
        break
        
    else:
        print("Invalid option. Try again.")