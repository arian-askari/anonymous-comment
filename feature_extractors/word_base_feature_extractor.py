import re
import operator
import os
import collections
from statistics import mean
from nltk.tokenize import TweetTokenizer
from utils.file_utils import FileUtils

tweet_tokenizer = TweetTokenizer()


class WordBaseFeatureExtractor:
    @staticmethod
    def __remove_mentions_from_comments(comment, word_set):
        """ extracts all usernames are mention in the comment and remove them, also count them as word_set
        :param comment:
        :param word_set:
        :return: comment text without any mention
        """

        regular_expression_mention = "@([A-Za-z0-9_](?:(?:[A-Za-z0-9_]|(?:\.(?!\.))){0,28}(?:[A-Za-z0-9_]))?)"
        for mention in re.findall(regular_expression_mention, comment):
            if ("@" + mention) in word_set:
                word_set["@" + mention] += 1
            else:
                word_set["@" + mention] = 1
            comment = comment.replace("@" + mention, "")

        return comment

    @staticmethod
    def __remove_emojis_from_comments(comment, word_set):
        """ extracts all emojis are in the comment and remove them, also count them as word_set
        :param comment:
        :param word_set:
        :return: comment text without any emoji
        """

        regular_expression_emoji = (
            ":[a-zA-z_-]+:"
        )  # :heart: :heart: :heart::heart:
        for emoji in re.findall(regular_expression_emoji, comment):
            comment = comment.replace(emoji, " ")
            emoji = emoji.strip()
            if emoji in word_set:
                word_set[emoji] += 1
            else:
                word_set[emoji] = 1

        comment = re.sub(" +", " ", comment.strip())
        return comment

    @staticmethod
    def get_word_list_frequency(comments):
        """counts words frequency of specific user's comments
        :param comments:
        :return: words frequency dictionary
        """
        comments = [comment.lower() for comment in comments]

        word_set = {}  # {"word":"freq"}
        for comment in comments:
            """remove mentions"""
            comment = WordBaseFeatureExtractor.__remove_mentions_from_comments(
                comment, word_set
            )
            """remove emojis"""
            comment = WordBaseFeatureExtractor.__remove_emojis_from_comments(
                comment, word_set
            )

            """ give comments without any mentions or emojis to tweet tokenizer of NLTK """
            splited_comment = tweet_tokenizer.tokenize(comment)
            for word in splited_comment:
                if word in word_set:
                    word_set[word] += 1
                else:
                    word_set[word] = 1

        """sort words by repetition in all comments of that user"""
        word_set = sorted(
            word_set.items(), key=operator.itemgetter(1), reverse=True
        )
        return word_set

    @staticmethod
    def get_count_of_once_used_word(comments):
        """calculates the count of once used words of specific user's comments
        :param comments:
        :return: count of once used words
        """
        word_list_freq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        return len(
            [word_freq for word_freq in word_list_freq if word_freq[1] == 1]
        )

    @staticmethod
    def get_count_of_all_word(comments):
        """calculates the count of words of specific user's comments
        :param comments:
        :return: count of all words
        """
        return len(WordBaseFeatureExtractor.get_word_list_frequency(comments))

    @staticmethod
    def get_count_of_short_word(comments):
        """calculates the count of words are smaller than four character of specific user's comments
        :param comments:
        :return: count of words smaller than four character
        """
        word_list_with_freq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        return len(
            [
                wordFreq
                for wordFreq in word_list_with_freq
                if len(wordFreq[0]) < 4
            ]
        )

    @staticmethod
    def get_count_of_long_word(comments):
        """calculates the count of words are greater than six character of specific user's comments
        :param comments:
        :return: count of words smaller than four character
        """
        wordListWithFreq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        return len(
            [wordFreq for wordFreq in wordListWithFreq if len(wordFreq[0]) > 6]
        )

    @staticmethod
    def get_mean_word_len(comments):
        """calculates mean length of comments of specific user
        :param comments:
        :return: mean length of comments
        """
        word_list_with_freq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        word_len_list = [len(wordFreq[0]) for wordFreq in word_list_with_freq]
        return mean(word_len_list)

    @staticmethod
    def lexical_diversity(comment):
        """calculates lexical diversity of a comment
        :param comment:
        :return: lexical diversity of a comment
        """
        if (len(comment)) == 0:
            return 0
        return len(set(comment)) / len(comment)

    @staticmethod
    def lexical_diversities(comments):
        """calculates lexical diversity of a comment
        :param comments:
        :return: lexical diversity of comments of specific user
        """
        total = 0
        for comment in comments:
            total += WordBaseFeatureExtractor.lexical_diversity(comment)
        total = total / len(comments)
        return total

    @staticmethod
    def get_count_of_word_greater_than(comments, size):
        """calculates the count of words are size than specific size of specific user's comments
        :param comments:
        :return: count of words are greater than size
        """
        word_list_with_freq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        return len(
            [
                wordFreq
                for wordFreq in word_list_with_freq
                if len(wordFreq[0]) > size
            ]
        )

    @staticmethod
    def get_count_of_word_len(comments, wordLen):
        """calculates the count of words have specific size of specific user's comments
        :param comments:
        :param wordLen:
        :return: count of words have specific size
        """
        word_list_with_freq = WordBaseFeatureExtractor.get_word_list_frequency(
            comments
        )
        return len(
            [
                wordFreq
                for wordFreq in word_list_with_freq
                if len(wordFreq[0]) == wordLen
            ]
        )

    @staticmethod
    def get_most_frequent_word_betwenn_all_commenters(
        path, most_frequent_word_per_author
    ):
        """get most frequent words used between all commenters (users)
        :param path: path of commenter's comments
        :param most_frequent_word_per_author: count of most frequent word per user to be consider
        :return: most frequent words set
        """
        most_frequent_words = set()
        for users_comments_file in sorted(os.listdir(path)):
            """ for each author get top-most frequent word and added that to word-set"""
            comments_train = FileUtils.get_list_of_comments(
                os.sep.join([path, users_comments_file])
            )
            word_list_train = WordBaseFeatureExtractor.get_word_list_frequency(
                comments_train
            )

            top_words = [word_freq[0] for word_freq in word_list_train]
            top_words = collections.OrderedDict.fromkeys(top_words)
            top_words = list(top_words.keys())
            top_words = [
                word for word in top_words[:most_frequent_word_per_author]
            ]
            most_frequent_words |= set(list(top_words))
        return most_frequent_words
