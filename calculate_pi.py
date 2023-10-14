from mpmath import mp
import msvcrt

try:
    # Get the number of decimal places for pi from the user
    num_decimal_places = int(input("Enter the number of decimal places for pi: "))

    # Validate the input
    if num_decimal_places < 1:
        raise ValueError("Please enter a valid number of decimal places (1 or more).")

    # Increase the number of decimal places by 2 to account for rounding
    num_decimal_places += 2

    # Set the decimal places for mp
    mp.dps = num_decimal_places

    # Calculate pi
    pi = mp.pi
    pi_str = str(pi)

    # Print the first num_decimal_places digits of pi
    for i in range(num_decimal_places):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':  # Pause on space bar
                input("\nPress Enter to continue...")
            elif key == b'\x1b':  # Stop on escape key
                break
        print(f"{pi_str[i]}", end='')

    print()
except ValueError as error:
    print(f"Error: Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
