def get_sensors_activation_data():
    # Example data structure to represent sensor activation times
    # In a real application, data would typically be sourced from a database or file
    activation_data = {
        "05/02/2023": [5, 10, 15, 20],  # Times in seconds
        "06/02/2023": [30, 20, 25],     # Example for another date
    }
    return activation_data

def calculate_seconds_on_date(activation_data, date):
    if date in activation_data:
        return sum(activation_data[date])
    else:
        return 0 

def main():
    # Get activation data
    activation_data = get_sensors_activation_data()

    # Ask the user for a date
    user_date = input("Please enter a date in DD/MM/YYYY format: ")

    # Calculate total seconds on that date
    total_seconds = calculate_seconds_on_date(activation_data, user_date)

    # Output result
    if total_seconds > 0:
        print(f"Sensors were activated for {total_seconds} seconds on {user_date}.")
    else:
        print(f"No sensor activation data found for {user_date}.")

if __name__ == "__main__":
    main()