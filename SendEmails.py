"""
Program to email the new hire letters
By: Easton Seidel
2/23/21
"""

from EmailServices import EmailServices
from ConfirmedNewHires import ConfirmedNewHires
from DirectoryServices import DirectoryServices
from GetInfo import GetInfo

ds = DirectoryServices()
cnh = ConfirmedNewHires()
gi = GetInfo()


class SendEmails:
    """Class to control the programs functions"""

    def __init__(self):
        # Get the names of the users
        # names = ds.get_names()

        # Verify which users need the email
        # names = cnh.confirm_letters(names)
        names = cnh.auto_confirm()

        # Quit if list is empty
        if names == 0:
            exit()

        # Get the username and password of the user
        # email = gi.get_email()
        # password = gi.get_password()

        # Send the letters and move the folders
        for i in names:

            # initialize the email services
            es = EmailServices()

            # Send the emails
            es.send_email(i)

            # move the folders
            try:
                ds.move_folder(i)
            except FileNotFoundError:
                print(f"{i}.new folder exists! Clean up a bit and move the folder!")
