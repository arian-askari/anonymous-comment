import os
import re
from feature_extractors.character_base_feature_extractor import (
    CharacterBaseFeatureExtractor as CharacterBaseFeature,
)
from feature_extractors.word_base_feature_extractor import (
    WordBaseFeatureExtractor as WordBaseFeature,
)
from feature_extractors.sentence_base_feature_extractor import (
    SentenceBaseFeatureExtractor as SentenceBaseFeature,
)
from utils.file_utils import FileUtils


class FeatureExtractor:
    @staticmethod
    def get_word_list_frequency(comments):
        """counts words frequency of specific user's comments
        :param comments:
        :return: words frequency dictionary
        """
        return WordBaseFeature.get_word_list_frequency(comments)

    @staticmethod
    def get_most_frequent_word_betwenn_all_commenters(
        path, most_frequent_word_per_author
    ):
        """get most frequent words used between all commenters (users)
        :param path: path of commenter's comments
        :param most_frequent_word_per_author: count of most frequent word per user to be consider
        :return: most frequent words set
        """
        return WordBaseFeature.get_most_frequent_word_betwenn_all_commenters(
            path, most_frequent_word_per_author
        )

    @staticmethod
    def get_basic_features(comments):  # 62 features

        """ character base features"""
        mean_of_char = CharacterBaseFeature.get_mean_of_char(comments)  # f1
        count_of_lower_case = CharacterBaseFeature.get_count_of_lower_case(
            comments
        )  # f2
        count_of_upper_case = CharacterBaseFeature.get_count_of_upper_case(
            comments
        )  # f3
        count_of_vowels = CharacterBaseFeature.get_count_of_vowels(
            comments
        )  # f4
        count_of_vowels_a = CharacterBaseFeature.get_count_of_character(
            comments, "a"
        )  # f5
        count_of_vowels_e = CharacterBaseFeature.get_count_of_character(
            comments, "e"
        )  # f6
        count_of_vowels_i = CharacterBaseFeature.get_count_of_character(
            comments, "i"
        )  # f7
        count_of_vowels_o = CharacterBaseFeature.get_count_of_character(
            comments, "o"
        )  # f8
        count_of_vowels_u = CharacterBaseFeature.get_count_of_character(
            comments, "u"
        )  # f9
        count_of_alphabets = CharacterBaseFeature.get_count_of_alphabets(
            comments
        )  # f10
        count_punc_exclamation = CharacterBaseFeature.get_count_of_character(
            comments, "!"
        )  # f11
        count_of_special_characters = CharacterBaseFeature.get_count_of_special_characters(
            comments
        )  # f12
        count_of_punctuation = CharacterBaseFeature.get_count_of_punctuation(
            comments
        )  # f13

        """alphabet features"""
        alphabet_b = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["b"]
        )  # f14
        alphabet_c = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["c"]
        )  # f15
        alphabet_d = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["d"]
        )  # f16
        alphabet_f = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["f"]
        )  # f17
        alphabet_g = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["g"]
        )  # f18
        alphabet_h = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["h"]
        )  # f19
        alphabet_j = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["j"]
        )  # f20
        alphabet_k = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["k"]
        )  # f21
        alphabet_l = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["l"]
        )  # f22
        alphabet_m = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["m"]
        )  # f23
        alphabet_n = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["n"]
        )  # f24
        alphabet_p = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["p"]
        )  # f25
        alphabet_q = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["q"]
        )  # f26
        alphabet_r = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["r"]
        )  # f27
        alphabet_s = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["s"]
        )  # f28
        alphabet_t = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["t"]
        )  # f29
        alphabet_u = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["u"]
        )  # f30
        alphabet_v = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["v"]
        )  # f31
        alphabet_w = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["w"]
        )  # f32
        alphabet_x = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["x"]
        )  # f33
        alphabet_y = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["y"]
        )  # f34
        alphabet_z = CharacterBaseFeature.get_count_of_special_characters(
            comments, ["z"]
        )  # f35

        """ word base features"""
        unique_word_count = WordBaseFeature.get_count_of_once_used_word(
            comments
        )  # f36
        all_word_count = WordBaseFeature.get_count_of_all_word(comments)  # f37
        count_of_short_word = WordBaseFeature.get_count_of_short_word(
            comments
        )  # f38
        count_of_long_word = WordBaseFeature.get_count_of_long_word(
            comments
        )  # f39
        mean_word_len = WordBaseFeature.get_mean_word_len(comments)  # f40
        lexical_diversity = WordBaseFeature.lexical_diversities(
            comments
        )  # f41
        greatherThan12Word = WordBaseFeature.get_count_of_word_greater_than(
            comments, 12
        )  # f42
        word_len1 = WordBaseFeature.get_count_of_word_len(comments, 1)  # f43
        word_len2 = WordBaseFeature.get_count_of_word_len(comments, 2)  # f44
        word_len3 = WordBaseFeature.get_count_of_word_len(comments, 3)  # f45
        word_len4 = WordBaseFeature.get_count_of_word_len(comments, 4)  # f46
        word_len5 = WordBaseFeature.get_count_of_word_len(comments, 5)  # f47
        word_len6 = WordBaseFeature.get_count_of_word_len(comments, 6)  # f48
        word_len7 = WordBaseFeature.get_count_of_word_len(comments, 7)  # f49
        word_len8 = WordBaseFeature.get_count_of_word_len(comments, 8)  # f50
        word_len9 = WordBaseFeature.get_count_of_word_len(comments, 9)  # f51
        word_len10 = WordBaseFeature.get_count_of_word_len(comments, 10)  # f52
        word_len11 = WordBaseFeature.get_count_of_word_len(comments, 11)  # f53
        word_len12 = WordBaseFeature.get_count_of_word_len(comments, 12)  # f54
        word_len13 = WordBaseFeature.get_count_of_word_len(comments, 13)  # f55
        word_len14 = WordBaseFeature.get_count_of_word_len(comments, 14)  # f56
        word_len15 = WordBaseFeature.get_count_of_word_len(comments, 15)  # f57
        word_len16 = WordBaseFeature.get_count_of_word_len(comments, 16)  # f58
        word_len17 = WordBaseFeature.get_count_of_word_len(comments, 17)  # f59
        word_len18 = WordBaseFeature.get_count_of_word_len(comments, 18)  # f60
        word_len22 = WordBaseFeature.get_count_of_word_len(comments, 22)  # f61
        word_len24 = WordBaseFeature.get_count_of_word_len(comments, 24)  # f62

        """sentence base features"""
        meanLenOfSentences = SentenceBaseFeature.get_mean_len_of_sentences(
            comments
        )  # f63
        countOfMissingUperCase = SentenceBaseFeature.get_count_of_sentence_missing_start_with_upper_case(
            comments
        )  # f64
        countOfMissingPunctuation = SentenceBaseFeature.get_count_of_sentence_missing_end_with_punctuation(
            comments
        )  # f65
        countOfMissingIOrWe = SentenceBaseFeature.get_count_of_sentence_missing_start_with_i_or_we(
            comments
        )  # f66

        featuresValueList = [
            mean_of_char,
            count_of_lower_case,
            count_of_upper_case,
            count_of_vowels,
            count_of_vowels_a,
            count_of_vowels_e,
            count_of_vowels_i,
            count_of_vowels_o,
            count_of_vowels_u,
            count_of_alphabets,
            count_of_punctuation,
            unique_word_count,
            all_word_count,
            count_of_short_word,
            count_of_long_word,
            mean_word_len,
            greatherThan12Word,
            word_len1,
            word_len2,
            word_len3,
            word_len4,
            word_len5,
            word_len6,
            word_len7,
            word_len8,
            word_len9,
            word_len10,
            word_len11,
            word_len12,
            alphabet_b,
            alphabet_c,
            alphabet_d,
            alphabet_f,
            alphabet_g,
            alphabet_h,
            alphabet_j,
            alphabet_k,
            alphabet_l,
            alphabet_m,
            alphabet_n,
            alphabet_p,
            alphabet_q,
            alphabet_r,
            alphabet_s,
            alphabet_t,
            alphabet_u,
            alphabet_v,
            alphabet_w,
            alphabet_x,
            alphabet_y,
            alphabet_z,
            lexical_diversity,
            word_len13,
            word_len14,
            word_len15,
            word_len16,
            word_len17,
            word_len18,
            word_len22,
            word_len24,
            meanLenOfSentences,
            count_of_special_characters,
            count_punc_exclamation,
            countOfMissingUperCase,
            countOfMissingPunctuation,
            countOfMissingIOrWe,
        ]
        return featuresValueList

    @staticmethod
    def get_vector(user_comments_full_path, most_frequent_words):
        """ calculate feature vector for user, based on most frequent words and basic features of that comments
        :param user_comments_full_path: path all comments of specific user
        :param most_frequent_words: set of most_frequent_words
        :return: feature vector for user
        """
        comments_train = FileUtils.get_list_of_comments(
            user_comments_full_path
        )

        word_feq_dict_train = dict(
            FeatureExtractor.get_word_list_frequency(comments_train)
        )

        basic_features_value_list = FeatureExtractor.get_basic_features(
            comments_train
        )

        word_freq_feature_value_list = []

        for word in most_frequent_words:
            if word in word_feq_dict_train:
                word_freq_feature_value_list.append(word_feq_dict_train[word])
            else:
                word_freq_feature_value_list.append(0)

        vector = basic_features_value_list + word_freq_feature_value_list
        return vector

    @staticmethod
    def get_train_set(path, most_frequent_words):
        """calculate train set for all user's comments in specific path, consider most frequent words
        :param path:
        :param most_frequent_words:
        :return: train set for all user's comments in specific path
        """
        x_train = []
        y_train = []

        user_prefix_identity = "^(\d+)A"
        for user_comments_filename in sorted(os.listdir(path)):
            user_identity = re.findall(
                user_prefix_identity, user_comments_filename
            )[0]
            user_comments_full_path = os.sep.join(
                [path, user_comments_filename]
            )

            """ get feature vector for that user"""
            user_feature_vector = FeatureExtractor.get_vector(
                user_comments_full_path, most_frequent_words
            )

            x_train.append(user_feature_vector)
            y_train.append(user_identity)

        return x_train, y_train
