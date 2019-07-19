import re
import sys
import os
import configparser


class FileUtils(object):
    @staticmethod
    def getListOfComments(path):
        """Loads comments of an instagram user.
        :param path: user comments file path
        :return: comments list
        """

        # opens comments file
        try:
            return [
                re.sub(" +", " ", comment.strip().rstrip())
                for comment in list(open(path, "r"))
            ]
        except Exception as e:
            print("Error loading comments file: ", e)
            sys.exit(1)

    @staticmethod
    def load_config(path):
        """Loads config as dictionary.
        :param config: config.ini file path
        :return: config dictionary
        """
        # opens config file
        try:
            config = configparser.ConfigParser()
            config.read(path)
            return config
        except Exception as e:
            print("Error loading config file: ", e)
            sys.exit(1)

    @staticmethod
    def write_file(path, data):
        """writing data to path.
        :param path: file path
        :param data: data to write
        """
        # opens file
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            f = open(str(path), "w")
            f.write(data)
            f.close()
        except Exception as e:
            print("Error writing file: ", e)
            sys.exit(1)
