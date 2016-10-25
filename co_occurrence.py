def str_or_list_to_list(s):
    if isinstance(s,str):
        s_list = s.split(' ')
    elif isinstance(s,list):
        s_list = s
    else:
        raise TypeError
    return s_list

# Given a space-separated string or a list of words and two words, return a list of (word1,word2) indices where two
# words co-occur around each other within distance d.
def co_occurrence(s,word1,word2,d):
    s_list = str_or_list_to_list(s)
    word1_indices = [i for i, x in enumerate(s_list) if x == word1]
    word2_indices = [i for i, x in enumerate(s_list) if x == word2]
    return find_close_indices(word1_indices, word2_indices, d)

# Given two sorted lists of indices, return pairs of indices (i1,i2) where i1 is in the first list, i2 is in the second
# list, and abs(i1,i2) < d
def find_close_indices(index_list_1, index_list_2, d):
    l1 = len(index_list_1)
    l2 = len(index_list_2)
    i1 = 0
    i2_start = 0
    i2_end = 0
    ret = []
    while i1 < l1:
        # Move i2_start until the element in list 2 is greater than the element in list 1 - d.
        while  i2_start < l2 and index_list_1[i1] - d > index_list_2[i2_start]:
            i2_start += 1
        # Move i2_end until the element in list 2 is the smallest one that is greater than the element in list 1 + d.
        while i2_end < l2 and index_list_1[i1] + d >= index_list_2[i2_end]:
            i2_end += 1
        for i2 in range(i2_start, i2_end):
            ret.append((index_list_1[i1],index_list_2[i2]))
        i1 += 1
    return ret

# Given a space-separated string or a list of words and two words, print a list of short snippets in which two
# words co-occur around each other within distance d.
def print_co_occurrence(s,word1,word2,d, num_words_around_to_show = 5):
    s_list = str_or_list_to_list(s)
    l = len(s_list)
    co_occurrence_indices = co_occurrence(s_list,word1,word2,d)
    for (i1, i2) in co_occurrence_indices:
        start = max(0, min(i1,i2) - num_words_around_to_show)
        end = min(l, max(i1,i2) + num_words_around_to_show)
        print(' '.join(s_list[start:end]))

# Given a space-separated string or a list of words and two words, modify the default dictionary containing the count of
# phrases between where two words co-occur around each other within distance d.
def count_phrase_between_co_occurrence(s,word1,word2,d, count_dict):
    s_list = str_or_list_to_list(s)
    l = len(s_list)
    co_occurrence_indices = co_occurrence(s_list,word1,word2,d)
    for (i1, i2) in co_occurrence_indices:
        if i1 < i2 - 1:
            count_dict[' '.join(s_list[i1 + 1:i2])] += 1

# For patterns such as: x word y, or x phrase y, return the index of x and y.
def get_context_around_phrase(s, phrase, window = 1):
    # The most naive way
    s_list = str_or_list_to_list(s)
    phrase_list = str_or_list_to_list(phrase)
    l = len(s_list)
    ret = []
    # We must have at least one word in front and at the back
    for i in range(window, l - len(phrase_list) - window):
        success = True
        for word_i, word in enumerate(phrase_list):
            if s_list[i + word_i] != word:
                success = False
                break
        if success:
            ret.append((i-window, i + len(phrase_list) + window - 1))
    return ret


# Given a space-separated string or a list of words and two words, modify the default dictionary containing the count of
# phrases between where two words co-occur around each other within distance d.
def count_context_around_phrase(s, phrase, count_dict,  window = 1):
    s_list = str_or_list_to_list(s)
    phrase_list = str_or_list_to_list(phrase)
    l = len(s_list)
    # We must have at least 'window' number of word in front and at the back
    for i in range(window, l - len(phrase_list) - window):
        success = True
        for word_i, word in enumerate(phrase_list):
            if s_list[i + word_i] != word:
                success = False
                break
        if success:
            for j in range(i-window, i):
                count_dict[s_list[j]] += 1
            for j in range(i + len(phrase_list), i + len(phrase_list) + window):
                count_dict[s_list[j]] += 1