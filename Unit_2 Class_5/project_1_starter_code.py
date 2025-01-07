# Starter Code for the Shopping List Project

# Step 1: Create an empty shopping list
shopping_list = []

# Step 2: Display a menu of options
while True:
    print("\nChoose an option:")
    print("1. Add an item to the shopping list")
    print("2. Remove an item from the shopping list")
    print("3. View the shopping list")
    print("4. Check if an item is already in the shopping list")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    
    # Option 1: Add an item to the list
    if choice == "1":
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    
    # Option 2: Remove an item from the list
    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} has been removed from the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
    
    # Option 3: View the shopping list
    elif choice == "3":
        if shopping_list:
            print("Your shopping list:")
            for i, item in enumerate(shopping_list, start=1):
                print(f"{i}. {item}")
        else:
            print("Your shopping list is empty.")
    
    # Option 4: Check if an item is in the list
    elif choice == "4":
        item = input("Enter the item to check: ")
        if item in shopping_list:
            print(f"{item} is already in the shopping list.")
        else:
            print(f"{item} is not in the shopping list.")
    
    # Option 5: Exit the program
    elif choice == "5":
        print("Exiting the program. Goodbye!")
        break
    
    # Handle invalid input
    else:
        print("Invalid choice. Please try again.")
