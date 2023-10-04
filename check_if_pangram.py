def checkIfPangram(sentence: str) -> bool:
    """A pangram is a sentence where every letter of the English alphabet appears at least once."""
    sentence_list = []
    for char in sentence.replace(" ",""):
        if char not in sentence_list:
            sentence_list.append(char)

    print(len(sentence_list)==26)

checkIfPangram("a quick brown fox jumps over the lazy dog")
checkIfPangram('leet code')            

