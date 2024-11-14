def bubble_sort(arr):
    ## This function takes a list (arr) and sorts it using the bubble sort algorithm.
    ## It iterates through the list, comparing adjacent elements and swapping them if they are out of order.

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
                
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def main():
    ## This main function handles user input, sorting, and storing lists.
    ## It provides options to retrieve sorted lists and specific variables.

    # Initialize an empty list to store all sorted lists
    sorted_lists = []

    # Main loop to allow user to input multiple arrays
    while True:
        # Ask the user to input a list of numbers
        user_input = input("Enter a list of numbers separated by commas (or type 'exit' to quit): ")
        
        # Check if the user wants to exit the loop
        if user_input.lower() == 'exit':
            print("Exiting input loop.")
            break

        # Convert the input string to a list of integers
        try:
            arr = list(map(int, user_input.split(',')))
        except ValueError:
            print("Invalid input. Please enter a list of numbers separated by commas.")
            continue

        # Print the unsorted list
        print("Unsorted list is:")
        print(arr)

        # Sort the list
        bubble_sort(arr)
        
        # Print the sorted list
        print("Sorted list is:")
        print(arr)

        # Store the sorted list in sorted_lists
        sorted_lists.append(arr)

    # After input loop ends, allow the user to retrieve data from stored lists
    while True:
        print("\nOptions:")
        print("1. Retrieve a specific element from a list")
        print("2. Retrieve elements from multiple lists")
        print("3. Retrieve elements from all lists")
        print("4. Exit")

        choice = input("Choose an option (1, 2, 3, or 4): ")

        # Exit the program if the user chooses '4'
        if choice == '4':
            print("Exiting the program.")
            break

        elif choice == '1':
            # Option to retrieve a specific element from a single list
            try:
                list_index = int(input(f"Enter the list index (0 to {len(sorted_lists)-1}): "))
                element_index = int(input("Enter the index of the element in the list: "))
                print(f"Element at index {element_index} in list {list_index}: {sorted_lists[list_index][element_index]}")
            except (IndexError, ValueError):
                print("Invalid index. Please enter valid list and element indices.")

        elif choice == '2':
            # Option to retrieve a specific element from multiple lists
            try:
                element_index = int(input("Enter the index of the element in each list: "))
                num_lists = int(input(f"Enter the number of lists to retrieve from (1 to {len(sorted_lists)}): "))
                for i in range(min(num_lists, len(sorted_lists))):
                    print(f"Element at index {element_index} in list {i}: {sorted_lists[i][element_index]}")
            except (IndexError, ValueError):
                print("Invalid index or number. Please enter valid values.")

        elif choice == '3':
            # Option to retrieve a specific element from all lists
            try:
                element_index = int(input("Enter the index of the element in each list: "))
                for i, sorted_list in enumerate(sorted_lists):
                    print(f"Element at index {element_index} in list {i}: {sorted_list[element_index]}")
            except IndexError:
                print("Invalid index. Some lists do not contain the specified index.")
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        else:
            print("Invalid choice. Please select an option from the menu.")

if __name__ == "__main__":
    main()
