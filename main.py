import json
import sys
import re

with open('wordlist.json') as json_file:
    word_dict = json.load(json_file)

if __name__ == "__main__":
    center = sys.argv[1]
    for elem in list(word_dict):
        if center not in elem or len(elem) < 4:
            word_dict.pop(elem)
    char_string = center
    for c in sys.argv[2:]:
        char_string += c

    regex_str = f"^[{char_string}]*$"
    regex = re.compile(regex_str)

    for elem in list(word_dict):
        if regex.search(elem) == None:
            word_dict.pop(elem)

    print(json.dumps(word_dict))