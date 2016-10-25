import read_corpus_util
import trie_util
import co_occurrence

import progressbar
import string
import glob
from collections import defaultdict

if __name__=='__main__':
    # This reads all phrases.
    # paper_dict, facet_dict, entity_names_set = read_corpus_util.read_ns_entities(read_corpus_util.kCorpusDirectory, to_lower=False)
    # paper_key_phrases_dict, key_phrases_set = read_corpus_util.read_key_phrases(read_corpus_util.kCorpusDirectory, to_lower=False)
    # all_phrases = list(entity_names_set.union(key_phrases_set))
    # trie = trie_util.Trie(all_phrases)
    # for i in range(0,5000,100):
    #     # Field of study is either "Neuroscience" or "Computer Science"
    #     # 'E:/paper_corpus/cs_corpus_en_and_kp_replaced_punc_included'
    #     with open('/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_corpus_en_and_kp_replaced_with_upper_and_special_char' + str(i) + '.txt', 'w', encoding='utf8') as f:
    #         f.write(read_corpus_util.read_papers_corpus(
    #         read_corpus_util.kCorpusDirectory, field_of_study = "Computer Science", start_index = i,
    #         end_index = i + 100, trie = trie, to_lower=False, no_punctuations=True,
    #                    no_special_char=False))# This is taking a lot of memory, so do not use a variable to store it.
    #     break

    # # This only reads entity names
    # paper_dict, facet_dict, entity_names_set = read_corpus_util.read_ns_entities(read_corpus_util.kCorpusDirectory)
    # trie = trie_util.Trie(entity_names_set)
    # for i in range(1000,5000,1000):
    #     corpus = read_corpus_util.read_papers_corpus(
    #         read_corpus_util.kCorpusDirectory, field_of_study = "Neuroscience", start_index = i,
    #         end_index = i + 1000, trie = trie)
    #     with open('E:/paper_corpus/test_corpus_entity_names_replaced_' + str(i) + '.txt', 'w', encoding='utf8') as f:
    #         f.write(corpus)



    # trie = trie_util.Trie(entity_names_set)
    # 'E:/paper_corpus/neural_science_phrases.txt'
    # for key in facet_dict.keys():
    #     with open('/home/jerryli27/PycharmProjects/Active/neural_science_exhuastive_list/' + key + '_phrases.txt', 'w',
    #               encoding='utf8') as f:
    #         for phrase in facet_dict[key]:
    #             f.write(phrase.replace(' ','_'))
    #             f.write('\n')

    # This reads the corpus and ...'E:/paper_corpus/cs_corpus_en_and_kp_replaced_0.txt' '/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_split/cs_corpus_100m_aa'
    # with open('E:/paper_corpus/cs_split/cs_corpus_100m_aa' , 'r', encoding='utf8') as f:
    #     s = f.read()
    #     s_list = s.split(' ')
    #     word_pairs = [('the', 'algorithm'), ('the', 'model'), ('using', 'classification'), ('a', 'algorithm')]
    #     for word_pair in word_pairs:
    #         word1 = word_pair[0]
    #         word2 = word_pair[1]
    #         d = 5
    #         print('')
    #         co_occurrence.print_co_occurrence(s_list, word1, word2, d)
    #
    #     # phrases = ['random_forest_rf', 'hmm', 'latent_semantic_indexing_lsi', 'adaboost_ab', 'support_vector_machine_svm']
    #     # for phrase in phrases:
    #     #     print('')
    #     #     contexts = co_occurrence.get_context_around_phrase(s_list, phrase, window=5)
    #     #     for context in contexts:
    #     #         print(' '.join(s_list[context[0]:context[1] + 1]))

    # # This reads the corpus and ...'E:/paper_corpus/cs_corpus_en_and_kp_replaced_0.txt' '/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_split/cs_corpus_100m_aa'
    #
    # word_pairs = [('the', 'algorithm'), ('the', 'model'), ('using', 'classification'), ('a', 'algorithm')]
    # word_pairs_count_dictionary = {word_pair: defaultdict(int) for word_pair in word_pairs}
    # phrases = ['random_forest_rf', 'hmm', 'latent_semantic_indexing_lsi', 'adaboost_ab', 'support_vector_machine_svm']
    # context_word_count_dictionary = defaultdict(int)
    # file_names = glob.glob("E:/paper_corpus/cs_split/*")
    # bar = progressbar.ProgressBar(max_value=len(file_names))
    # for file_i, file_name in enumerate(file_names):
    #     with open(file_name, 'r', encoding='utf8') as f:
    #         s = f.read()
    #         s_list = s.split(' ')
    #         for word_pair in word_pairs:
    #             word1 = word_pair[0]
    #             word2 = word_pair[1]
    #             d = 5
    #             # print('')
    #             # co_occurrence.print_co_occurrence(s_list, word1, word2, d)
    #             co_occurrence.count_phrase_between_co_occurrence(s_list, word1, word2, d,
    #                                                              word_pairs_count_dictionary[word_pair])
    #         for phrase in phrases:
    #             co_occurrence.count_context_around_phrase(s_list, phrase, context_word_count_dictionary, window=5)
    #     bar.update(file_i)
    # del bar
    #
    # kMinimumCountThreshold = 2
    # word_pairs_count_list = {
    # word_pair: sorted([(k, v) for k, v in word_pairs_count_dictionary[word_pair].items()], key=lambda tup: tup[1], reverse=True)
    # for word_pair in word_pairs}
    #
    # with open('golden_dataset_raw.txt', 'w', encoding='utf8') as f:
    #     for word_pair in word_pairs:
    #         print('The phrases that appear between %s and %s  more than %d times are:'
    #               % (word_pair[0], word_pair[1], kMinimumCountThreshold))
    #         f.write('The phrases that appear between %s and %s  more than %d times are: \n'
    #               % (word_pair[0], word_pair[1], kMinimumCountThreshold))
    #         for word_count in word_pairs_count_list[word_pair]:
    #             if word_count[1] > kMinimumCountThreshold:
    #                 print('%s: %d' % (word_count[0], word_count[1]))
    #                 f.write('%s: %d\n' % (word_count[0], word_count[1]))
    #
    # context_word_count_list = sorted([(k, v) for k, v in context_word_count_dictionary.items()], key=lambda tup: tup[1], reverse=True)
    # with open('context_words_raw.txt', 'w', encoding='utf8') as f:
    #     print('The phrases that appear around %s more than %d times are:'
    #           % (str(phrases), kMinimumCountThreshold))
    #     f.write('The phrases that appear around %s more than %d times are:\n'
    #           % (str(phrases), kMinimumCountThreshold))
    #     for word_count in context_word_count_list:
    #         if word_count[1] > kMinimumCountThreshold:
    #             print('%s: %d' % (word_count[0], word_count[1]))
    #             f.write('%s: %d\n' % (word_count[0], word_count[1]))




    #
    # # This is for testing whether techniques_such is in the key phrase set.
    # paper_dict, facet_dict, entity_names_set = read_corpus_util.read_ns_entities(read_corpus_util.kCorpusDirectory)
    # paper_key_phrases_dict, key_phrases_set = read_corpus_util.read_key_phrases(read_corpus_util.kCorpusDirectory)
    # all_phrases = list(entity_names_set.union(key_phrases_set))
    # if 'techniques such' in all_phrases:
    #     print('techniques such is in the key phrases set')
    # else:
    #     print('techniques such is NOT in the key phrases set')
    #
    # for i, key_phrase in enumerate(key_phrases_set):
    #     print('%i %s' % (i, key_phrase))
    #     if i > 100:
    #         break
    # trie = trie_util.Trie(all_phrases)
    # joined_text = read_corpus_util.join_entity_names('ranges over a variety of techniques such as traditional or breakpointstyle debuggers event monitoring systems', trie)
    # print(joined_text)
    # #
    # # for i in range(0,5000,100):
    # #     # Field of study is either "Neuroscience" or "Computer Science"
    # #     # 'E:/paper_corpus/cs_corpus_en_and_kp_replaced_punc_included'
    # #     with open('/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_corpus_en_and_kp_replaced_punc_included' + str(i) + '.txt', 'w', encoding='utf8') as f:
    # #         f.write(read_corpus_util.read_papers_corpus(
    # #         read_corpus_util.kCorpusDirectory, field_of_study = "Computer Science", start_index = i,
    # #         end_index = i + 100, trie = trie, include_punctuations=True))# This is taking a lot of memory, so do not use a variable to store it.
    # #     break

    # TODO: collect golden data set.

    # This reads the corpus and ...'E:/paper_corpus/cs_corpus_en_and_kp_replaced_0.txt' '/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_split/cs_corpus_100m_aa'

    phrases = ['visualization techniques such as', 'string matching techniques such as',
               'signal processing techniques such as', 'face detection techniques such as',
               'virtualization techniques such as', 'optimization techniques such as',
               'cryptographic techniques such as', 'spatial reasoning techniques such as']
    context_word_count_dictionary = defaultdict(int)
    file_names = glob.glob("/media/jerryli27/1ACC040DCC03E1BD/paper_corpus/cs_split_with_upper_and_special/*")
    bar = progressbar.ProgressBar(max_value=len(file_names))
    with open('context_words_raw.txt', 'w', encoding='utf8') as f:
        for file_i, file_name in enumerate(file_names):
            with open(file_name, 'r', encoding='utf8') as f:
                s = f.read()
                s_list = s.split(' ')
                for phrase in phrases:
                    contexts = co_occurrence.get_context_around_phrase(s_list, phrase, window=8)
                    for context in contexts:
                        print(' '.join(s_list[context[0]:context[1] + 1]))
                        f.write('%s\t%s\n' % (phrase, ' '.join(s_list[context[0]:context[1] + 1])))
                # co_occurrence.count_context_around_phrase(s_list, phrase, context_word_count_dictionary, window=5)
            bar.update(file_i)
    del bar

    # context_word_count_list = sorted([(k, v) for k, v in context_word_count_dictionary.items()], key=lambda tup: tup[1],
    #                                  reverse=True)
    # with open('context_words_raw.txt', 'w', encoding='utf8') as f:
    #     print('The phrases that appear around %s more than %d times are:'
    #           % (str(phrases), kMinimumCountThreshold))
    #     f.write('The phrases that appear around %s more than %d times are:\n'
    #             % (str(phrases), kMinimumCountThreshold))
    #     for word_count in context_word_count_list:
    #         if word_count[1] > kMinimumCountThreshold:
    #             print('%s: %d' % (word_count[0], word_count[1]))
    #             f.write('%s: %d\n' % (word_count[0], word_count[1]))