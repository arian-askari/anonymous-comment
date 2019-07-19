from nltk.tokenize import sent_tokenize


class SentenceBaseFeatureExtractor:
    @staticmethod
    def mean_len_of_sentence(comment):
        """calculates mean length of sentences in a comment of specific user
        :param comment:
        :return: mean length of sentences in a comment
        """
        total = 0
        sent_tokenize_list = sent_tokenize(comment)
        for sentence in sent_tokenize_list:
            total += len(sentence)

        if len(sent_tokenize_list) == 0:
            return 0

        total = total / len(sent_tokenize_list)
        return total

    @staticmethod
    def get_mean_len_of_sentences(comments):
        """calculates mean length of sentences in comments of specific user
        :param comments:
        :return: mean length of sentences in comments
        """
        total = 0
        for comment in comments:
            total += SentenceBaseFeatureExtractor.mean_len_of_sentence(comment)
        if len(comments) == 0:
            return 0
        total = total / len(comments)
        return total

    @staticmethod
    def get_count_of_sentence_missing_start_with_upper_case(comments):
        """for specific user's comments, calculates the sentences missing start with upper case
        :param comments:
        :return: count sentences missing start with upper case
        """
        total = 0
        for comment in comments:
            sent_tokenize_list = sent_tokenize(comment)
            for sentence in sent_tokenize_list:
                sentence = sentence.strip()
                if sentence[0].islower():
                    total += 1
        return total

    @staticmethod
    def get_count_of_sentence_missing_end_with_punctuation(comments):
        """for specific user's comments, calculates the sentences missing end with punctuation
        :param comments:
        :return: count sentences missing end with punctuation
        """
        total = 0
        punctuation_list = [
            "‘",
            "’",
            "'",
            ",",
            ".",
            "!",
            ":",
            ";",
            '"',
            "...",
            "-",
            "–",
            "—",
        ]
        for comment in comments:
            sent_tokenize_list = sent_tokenize(comment)
            for sentence in sent_tokenize_list:
                sentence = sentence.strip()
                if sentence[len(sentence) - 1] not in punctuation_list:
                    total += 1
        return total

    @staticmethod
    def get_count_of_sentence_missing_start_with_i_or_we(comments):
        """for specific user's comments, calculates the sentences missing start with i or we
        :param comments:
        :return: count sentences missing  start with i or we
        """
        total = 0
        for comment in comments:
            sent_tokenize_list = sent_tokenize(comment)
            for sentence in sent_tokenize_list:
                sentence = sentence.strip()
                sentence = sentence.lower()
                if len(sentence) < 2:
                    continue
                if sentence[0] != "i" or (
                    sentence[0] != "w" or sentence[1] != "e"
                ):
                    total += 1
        return total
