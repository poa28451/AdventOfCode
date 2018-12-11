def check_frequency(filename: str):
    input_file = open(filename)
    freq_change_list = input_file.readlines()
    freq_list = set()  # Use set instead of list because of element searching performance
    frequency = 0
    is_duplicated = False

    round = 0
    while not is_duplicated:  # Perform frequency changing until the duplicate number has been found
        for freq_change in freq_change_list:
            frequency += int(freq_change)  # Change the frequency

            if frequency in freq_list:  # Check if this frequency has already existed
                print("Freq ", frequency, " is duplicated")
                is_duplicated = True  # Set the duplication flag
                break
            else:
                freq_list.add(frequency)  # If it's not duplicated, add to the frequency set


check_frequency("Day1-input.txt")
