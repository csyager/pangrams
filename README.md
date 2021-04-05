# Pangrams
Python script for finding Pangrams of a set of letters.  Based on finding solutions for the New York Times "Spelling Bee" puzzle.

Wordlist sourced from [dwyl/english-words](https://github.com/dwyl/english-words).

The python script takes a list of arguments, which should be character inputs.  The first character input represents the letter in the center of the puzzle.  This letter must be used in any words formed.  The rest represent any other letters that can be used to form words.  The output is a JSON-formatted dictionary containing all words from the word list that 1) contain the center letter which must appear in all words and 2) contain only letters that make up the rest of the arguments.

Not all words in this list are valid inputs according to the New York Times.  Substituting the wordlist.json file with a more suitable wordlist would improve this issue.

Example usage:  `python3 main.py p n t i a c y `  
![Example of NYT Spelling Bee Puzzle](assets/example.png)