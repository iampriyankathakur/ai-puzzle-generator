from nltk.corpus import wordnet

def generate_clues(words):
    clues = {}
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            definition = synsets[0].definition()
            clues[word] = definition
        else:
            clues[word] = f"No clue available for {word}"
    return clues
