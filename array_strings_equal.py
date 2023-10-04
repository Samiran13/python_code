def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    s1 = ""
    s2 = ""
    for element in word1:
        s1+=element
    for ele in word2:
        s2+=ele
    print(s1 == s2)

arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"])            

