import re

word_list = ["spork", "labradoodle", "fordle", "cardor", "lark", "spoooon", "labradabrador"]
patterns = ["spoon", "fork", "labrador", "poodle", "form", "car"]

prefix_word1 = "a"
suffix_word1 = "b"


for word in word_list:


    # six filter
    if len(word) == 6:
        amb_check = 0
        for prefix_word in patterns:
            for suffix_word in patterns:
                prefix = prefix_word[:3]
                suffix = suffix_word[-3:]
                if prefix in word:
                    if suffix in word:
                        amb_check += 1
                        prefix_word1 = prefix_word
                        suffix_word1 = suffix_word

        if amb_check > 1:
            print(f"ambiguous {word}, {prefix_word1}, {suffix_word1}")
        else:
            print(prefix_word1, " ", suffix_word1)




    # elif len(word) >= 6:

    else:
        print(f"none {word}")















