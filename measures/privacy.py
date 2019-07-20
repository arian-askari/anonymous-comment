import os
import numpy as np
from sklearn import preprocessing
from sklearn.svm import SVC
from statistics import mean
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
)
from feature_extractors.feature_extractor import FeatureExtractor

np.set_printoptions(threshold=np.nan)


class Privacy:
    @staticmethod
    def calcualte_privacy(path, clf, most_frequent_word_per_author):
        """ iterate on each randomly creation of train and test set"""
        k = 0
        total_accuracy_score_value = 0
        total_f1_score_value = 0
        total_precision_score_value = 0
        total_recall_score_value = 0
        for file in sorted(os.listdir(path)):
            if file == ".gitignore":
                continue
            k += 1

            base_path = os.sep.join([path, file])
            print("iterate on path: ", base_path)
            known_path = os.sep.join([base_path, "known"])
            unknown_path = os.sep.join([base_path, "unknown"])

            print("calculate most_frequent_words...")
            most_frequent_words = FeatureExtractor.get_most_frequent_word_betwenn_all_commenters(
                known_path, most_frequent_word_per_author
            )
            print("calculated")
            most_frequent_words = sorted(list(most_frequent_words))

            """ get train set"""
            print("calculate train set...")
            x_train, y_train = FeatureExtractor.get_train_set(
                known_path, most_frequent_words
            )
            print("calculated")
            x_train = np.array(x_train)
            x_train_zscore = preprocessing.scale(x_train)

            """ get test set"""
            print("calculate test set...")
            x_test, y_test = FeatureExtractor.get_train_set(
                unknown_path, most_frequent_words
            )
            print("calculated")
            x_test = np.array(x_test)
            x_test_zscore = preprocessing.scale(x_test)

            print("model fitting")
            clf.fit(x_train_zscore, y_train)
            print("model fitted")

            y_pred = clf.predict(x_test_zscore)

            accuracy_score_value = accuracy_score(y_test, y_pred)

            f1_score_value = mean(
                f1_score(y_test, y_pred, labels=y_test, average=None)
            )
            precision_score_value = mean(
                precision_score(y_test, y_pred, labels=y_test, average=None)
            )
            recall_score_value = mean(
                recall_score(y_test, y_pred, labels=y_test, average=None)
            )

            print(
                "iterate "
                + str(k)
                + " accuracy_score : "
                + str(accuracy_score_value)
            )
            print("iterate " + str(k) + " f1_score: " + str(f1_score_value))
            print(
                "iterate "
                + str(k)
                + " precision_score: "
                + str(precision_score_value)
            )
            print(
                "iterate "
                + str(k)
                + " recall_score: "
                + str(recall_score_value)
            )
            print("\n\t--------------------------------------")
            total_accuracy_score_value += accuracy_score_value
            total_f1_score_value += f1_score_value
            total_precision_score_value += precision_score_value
            total_recall_score_value += recall_score_value

        print(
            " mean  accuracy score over randomly iterate: ",
            (total_accuracy_score_value / k),
        )
        print(
            " mean  f1_score score over randomly iterate : ",
            (total_f1_score_value / k),
        )
        print(
            " mean  precision score over randomly iterate: ",
            (total_precision_score_value / k),
        )
        print(
            " mean  recall score over randomly iterate: ",
            (total_recall_score_value / k),
        )
