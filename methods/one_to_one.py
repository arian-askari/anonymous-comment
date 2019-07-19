import os
import random
import re

import config.config as Config
from methods.method import Method
from utils.file_utils import FileUtils


class OneToOne(Method):
    def dataset_generator(self):
        """Generates dataset of users comments based on OneToOne method.
       """

        percentage = Config.ONE_TO_ONE_PERCENTAGE
        retry_number = (
            Config.ONE_TO_ONE_RETRY_NUMBER
        )  # for prevent bias, creation of train and test set repeated one hundred times randomly

        path = Config.DATASET_PATH_ORIGINAL
        prefix_filename = "^(\d+A)"

        for i in range(retry_number):

            for file in os.listdir(path):
                if file == ".gitignore":
                    continue

                comments = FileUtils.getListOfComments(
                    os.sep.join([path, file])
                )

                count_of_comments = len(comments)
                unknown_cm_count = (count_of_comments * percentage) // 100

                unknown_file_name = re.findall(prefix_filename, file)[0]
                base_unknow_file_path = unknown_file_name + ".txt"
                base_know_file_path = base_unknow_file_path

                unknown_set = random.sample(comments, unknown_cm_count)
                known_set = list(set(comments) - set(unknown_set))

                comment_unknown_text = "\n".join(unknown_set)
                comment_known_text = "\n".join(known_set)

                known_file_path = os.sep.join(
                    [
                        Config.DATASET_PATH_ONE_TO_ONE,
                        str(i),
                        "known",
                        base_know_file_path,
                    ]
                )

                unknown_file_path = os.sep.join(
                    [
                        Config.DATASET_PATH_ONE_TO_ONE,
                        str(i),
                        "unknown",
                        base_unknow_file_path,
                    ]
                )

                FileUtils.write_file(unknown_file_path, comment_unknown_text)
                FileUtils.write_file(known_file_path, comment_known_text)
        pass
