def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    for char in text:
        if char.lower() in characters:
            characters[char.lower()] += 1
        else:
            characters[char.lower()] = 1
    return characters

def sort_on(characters):
    return characters["num"]

def sort_characters(characters):
    characters.sort(reverse=True, key=sort_on)

            