import os
import random
import re
import numpy as np
from sklearn.svm import SVC
from measures.privacy import Privacy
from methods.method import Method
from utils.file_utils import FileUtils
import config.config as Config

np.set_printoptions(threshold=np.nan)


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

                """ read all comments of specific user """
                comments = FileUtils.get_list_of_comments(
                    os.sep.join([path, file])
                )

                """ calculate count comments to be anonymous """
                count_of_comments = len(comments)
                unknown_cm_count = (count_of_comments * percentage) // 100

                """ generate a file name for the known and unknown (anonymous) path """
                unknown_file_name = re.findall(prefix_filename, file)[0]
                base_unknown_file_path = unknown_file_name + ".txt"
                base_known_file_path = base_unknown_file_path

                """ randomly get comments to be anonymous """
                unknown_set = random.sample(comments, unknown_cm_count)
                known_set = list(set(comments) - set(unknown_set))

                """ prepare comments for write in file """
                comment_unknown_text = "\n".join(unknown_set)
                comment_known_text = "\n".join(known_set)

                known_file_path = os.sep.join(
                    [
                        Config.DATASET_PATH_ONE_TO_ONE,
                        str(i),
                        "known",
                        base_known_file_path,
                    ]
                )

                unknown_file_path = os.sep.join(
                    [
                        Config.DATASET_PATH_ONE_TO_ONE,
                        str(i),
                        "unknown",
                        base_unknown_file_path,
                    ]
                )

                """ write comments in new known and unknown files based on the method """
                FileUtils.write_file(unknown_file_path, comment_unknown_text)
                FileUtils.write_file(known_file_path, comment_known_text)
        pass

    def privacy_measures(self):
        """Calculates privacy measures based on OneToOne method.
        """
        path = Config.DATASET_PATH_ONE_TO_ONE
        most_frequent_word_per_author = (
            Config.ONE_TO_ONE_MOST_FREQUENT_WORD_PER_USER
        )
        clf = SVC(C=2, kernel="linear", probability=False, cache_size=3092)
        Privacy.calcualte_privacy(path, clf, most_frequent_word_per_author)
