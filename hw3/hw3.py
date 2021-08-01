from typing import Dict, Match


print("Enter the line to count most frequent words:")
userinput = input()
words = userinput.lower().split()
wordsmap = {}

for word in words:
    if word in wordsmap:
        wordsmap[word] += 1
    else:
        wordsmap[word] = 1

maxcount = max(list(wordsmap.values()))

for word in wordsmap:
    if wordsmap[word] == maxcount:
        print(maxcount, "-", word)