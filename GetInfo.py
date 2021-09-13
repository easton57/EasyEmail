"""
Class to get the required info from the user
by: Easton Seidel
2/23/21
"""

from getpass import getpass


class GetInfo:
    """class to get the required info needed to send through outlook"""

    domain = "@domain.com"

    def get_email(self):
        """Function to grab the users outlook username"""
        print("\nThe rest of the email domain will be added, no need to enter it.")

        while True:
            print("Please enter your username: ", end='')
            email = input() + self.domain

            # Verify the email with the user
            print("\n" + email + "\n")
            print("Is the above email correct? Enter YES: ", end='')

            if input() == "YES":
                return email

    @staticmethod
    def get_password():
        """Function to get the users outlook password"""
        while True:
            password = getpass(prompt="Please enter your password: ")

            confirmation = getpass(prompt="Please confirm your password: ")

            if confirmation == password:
                return password

            print("Passwords do not match, please try again.")
