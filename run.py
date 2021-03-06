from src import levenshtein_ratio_and_distance, Dictionary

# loading the dictionary
dictionary = Dictionary()

# input from user
inputs = [
    "giraff is an animl",
    "honesy is the best polic",
]

print("\n\n")
print("-------------------------------------------------------")
print("| Original Word |\t Dictionary Word \t|\t Ratio \t |")
print("-------------------------------------------------------")

for string in inputs:
    for word in string.split():
        most_matching, max_ratio = word, 0

        for dict_word in dictionary.words()[word[0]]:
            ratio = levenshtein_ratio_and_distance(word, dict_word, ratio_calc=True)

            if ratio >= max_ratio:
                max_ratio, most_matching = ratio, dict_word

        print(f"| {word: <20}  {most_matching: <20}  {round(max_ratio, 3): <8}  ")
        print("-------------------------------------------------------")

