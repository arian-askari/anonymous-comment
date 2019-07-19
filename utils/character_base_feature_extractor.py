from statistics import mean


class CharacterBaseFeatureExtractor:
    @staticmethod
    def get_mean_of_char(comments):
        """calculates mean length of comments of specific user
        :param comments:
        :return: mean length of comments
        """
        total = []
        for comment in comments:
            total.append(len(comment))
        return mean(total)

    @staticmethod
    def get_count_of_lower_case(comments):
        """for specific user's comments, calculates the occurrence of lower case
        :param comments:
        :return: count of lower case
        """
        lower_case_count = 0
        for comment in comments:
            for character in comment:
                if character.islower():
                    lower_case_count += 1
        return lower_case_count

    @staticmethod
    def get_count_of_upper_case(comments):
        """for specific user's comments, calculates the occurrence of upper case
        :param comments:
        :return: count use of lower case
        """
        upper_case_count = 0
        for comment in comments:
            for character in comment:
                if character.isupper():
                    upper_case_count += 1
        return upper_case_count

    @staticmethod
    def is_vowel(character):
        """check character is vowel
        :param character:
        :return: boolean
        """
        character = character.lower()
        if character in ["a", "e", "o", "i", "u"]:
            return True
        return False

    @staticmethod
    def get_count_of_vowels(comments):
        """count vowels characters in list of comments
        :param comments:
        :return: count of vowels
        """
        vowel_count = 0
        for comment in comments:
            for character in comment:
                if CharacterBaseFeatureExtractor.is_vowel(character):
                    vowel_count += 1
        return vowel_count

    @staticmethod
    def get_count_of_character(comments, find):
        """count specific character in list of comments
        :param comments:
        :param find:
        :return: count of specific character
        """
        total = 0
        for comment in comments:
            for character in comment:
                character = character.lower()
                if character == find:
                    total += 1
        return total

    @staticmethod
    def get_count_of_alphabets(comments):
        """calculates the count of alphabets of specific user's comments
        :param comments:
        :param find:
        :return: count of alphabets
        """
        total = 0
        for comment in comments:
            alpha_count = 0
            for character in comment:
                if character.isalpha():
                    alpha_count += 1
            total += alpha_count
        return total

    @staticmethod
    def get_count_of_special_characters(comments, special_char_list=None):
        """calculates the count of special characters of specific user's comments
        :param special_char_list:
        :param comments:
        :param find:
        :return: count of special characters
        """
        total = 0
        if special_char_list is None:
            special_char_list = [
                "(",
                "(",
                "|",
                "‪@",
                "#",
                "$",
                "%",
                "’",
                "{",
                "}",
                ",",
                "~",
                "%",
                "^",
                "&",
                "*",
                "-",
                "=",
                "+",
                ">",
                "<",
                "[",
                "]",
                "{",
                "}",
                "/",
                "\\",
            ]
        for comment in comments:
            for character in comment:
                if character.lower() in special_char_list:
                    total += 1
        return total

    @staticmethod
    def get_count_of_punctuation(comments, punctuation_list=None):
        """calculates the count of punctuation characters of specific user's comments
        :param comments:
        :param find:
        :return: count of special characters
        """
        total = 0
        if punctuation_list is None:
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
            for character in comment:
                if character.lower() in punctuation_list:
                    total += 1
        return total
