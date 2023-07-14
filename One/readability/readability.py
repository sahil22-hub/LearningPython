def split_paragraph(paragraph):
    sentences = []
    words = []

    # Split the paragraph into sentences based on punctuation marks (.?!)
    sentence_delimiters = (".", "?", "!")
    current_sentence = ""
    for char in paragraph:
        current_sentence += char
        if char in sentence_delimiters:
            sentences.append(current_sentence.strip())
            current_sentence = ""

    # Split each sentence into words based on whitespace
    for sentence in sentences:
        current_word = ""
        for char in sentence:
            if char.isalnum() or char == "'":
                current_word += char
            elif current_word:
                words.append(current_word)
                current_word = ""
        if current_word:
            words.append(current_word)

    return sentences, words


def getGrade(letter_count, word_count, sentence_count):
    l = letter_count/word_count * 100
    s = sentence_count/word_count * 100
    grade = 0.0588 * l - 0.296 * s - 15.8
    return grade


# Example usage
paragraph = input("The paragraph:")
sentences, words = split_paragraph(paragraph)
letter_count = 0
word_count = len(words)
sentence_count = len(sentences)

for word in words:
    letter_count += len(word)

grade = getGrade(letter_count, word_count, sentence_count)
print("garde:", round(grade))
