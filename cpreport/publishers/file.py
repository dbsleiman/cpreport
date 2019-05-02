"""FilePublisher class"""

import os
from .base import BasePublisher

class FilePublisher(BasePublisher):

    """Publisher Class that writes to a file on the file system"""

    directory = None
    file_name = None

    def __init__(self, directory, file_name):
        """Initializes publisher with directory and file name

        Args:
            directory: The desired directory where the file will reside
            file_name: The desired name of the file
        """
        if directory is None or file_name is None:
            raise ValueError("directory and file_name must be non None values")

        if not os.path.exists(directory):
            os.makedirs(directory)

        self.directory = directory
        self.file_name = file_name

    def publish(self, report_string):
        """Writes report string to file system"""

        f = open("{}/{}".format(self.directory, self.file_name), "w")
        f.write(report_string)
        f.close()
