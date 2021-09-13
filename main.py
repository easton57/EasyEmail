"""
Main file to control all other modules
"""

from SendEmails import SendEmails


def main():
    """Driver that can have other functions added for a multifunction program"""

    # Print a menu
    print("Welcome!\nSelect an option from the list below:")
    print("1: Send New Hire Emails")
    # Add new options here
    print("0: Exit Program")

    # Define the input variable
    option = input("Option: ")

    try:
        option = int(option)
    except ValueError:
        # Freak out and restart if the input isn't a number
        print("\nInput is not a number!\n")
        main()

    # Define valid options
    valid = [0, 1]

    # Verify valid input
    if option not in valid:
        print("\nEntered option not valid!\n")
        main()
    elif option == 1:
        SendEmails()
    elif option == 0:
        quit()


if __name__ == '__main__':
    SendEmails()
