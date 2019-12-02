from collections import Counter

m = 6
n = 5

magazine = ["two", "times", "three", "is", "not", "four"]
note = ["two", "times", "two", "is", "four"]

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # print("length of magazine, m:", m, "length of note, n:", n)
    # print("magazine", magazine)
    # print("note", note)

    # create hashtable of lookup words O(1)
    word_counts = Counter(magazine)
    
    for word in note:
        print(word_counts[word])
        if word_counts[word] > 0:
            word_counts[word] -= 1
        else:
            return False
    return True

answer = checkMagazine(magazine, note)
if(answer):
    print("Yes")
else:
    print("No")

