"""
Class to do everything that's needed with folders and directories
by: Easton Seidel
2/23/21
"""

from os import listdir, path
from shutil import move, Error


class DirectoryServices:
    """Class for the file management portion of this program"""
    # Declare Directories
    delivered_letters = "delivered directory"
    undelivered_letters = "undelivered directory"

    def delivered(self):
        """Returns the delivered letter directory"""
        return self.delivered_letters

    def undelivered(self):
        """Returns the undelivered letter directory"""
        return self.undelivered_letters

    def get_names(self):
        """Pulls the names of each folder in the directory"""
        return [f for f in listdir(self.undelivered_letters)
                if path.isdir(path.join(self.undelivered_letters, f))]

    def create_directories(self, names):
        """Creates a list of full directories for the undelivered letters"""
        # Create a new list
        directories = []

        # iterate through the names and create a directory list
        for i in names:
            directories.append(self.undelivered_letters + i)

        return directories

    def move_folder(self, name):
        """Creates the delivered directory and moves the folders"""
        # Try to move the folder
        try:
            move(self.undelivered_letters + name, self.delivered_letters)
        except Error:
            print("Folder already exists! Saving with .new!")
            move(self.undelivered_letters + name, self.undelivered_letters + name + ".new")
            move(self.undelivered_letters + name + ".new", self.delivered_letters)
