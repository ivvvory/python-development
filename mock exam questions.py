def get_sensors_activation_data():
    ## This function simulates fetching sensor activation data.
    ## In a real application, this data might be read from a database or file.
    ## Here, it is represented as a dictionary where the keys are dates (DD/MM/YYYY)
    ## and the values are lists of activation times in seconds for that date.
    activation_data = {
        "05/02/2023": [5, 10, 15, 20],  # Example activation times for this date
        "06/02/2023": [30, 20, 25],     # Example activation times for another date
    }
    return activation_data

def calculate_seconds_on_date(activation_data, date):
    ## This function calculates the total activation time for a given date.
    ## It takes in the activation_data dictionary and the date as parameters.
    ## If the date exists in activation_data, it sums up all activation times
    ## in the list for that date and returns the total seconds.
    ## If the date is not in activation_data, it returns 0.
    if date in activation_data:
        return sum(activation_data[date])
    else:
        return 0 

def main():
    ## This is the main function where the program logic is handled.
    ## First, it retrieves the activation data by calling get_sensors_activation_data().
    activation_data = get_sensors_activation_data()

    ## Enter an infinite loop to continually ask for user input
    ## until the user decides to exit.
    while True:
        ## Prompt the user to enter a date in the required format.
        ## Adding an option for 'exit' allows the user to end the loop.
        user_date = input("Please enter a date in DD/MM/YYYY format (or type 'exit' to quit): ")
        
        ## Check if the user entered "exit" (in any case format).
        ## If so, print an exit message and break out of the loop.
        if user_date.lower() == 'exit':
            print("Exiting the program.")
            break

        ## Call calculate_seconds_on_date() to get the total activation
        ## time for the date entered by the user.
        total_seconds = calculate_seconds_on_date(activation_data, user_date)

        ## Print the result. If there are activation seconds for that date,
        ## display them; otherwise, inform the user that no data was found.
        if total_seconds > 0:
            print(f"Sensors were activated for {total_seconds} seconds on {user_date}.")
        else:
            print(f"No sensor activation data found for {user_date}.")

## The following line ensures that the main function runs when
## the script is executed directly.
if __name__ == "__main__":
    main()
