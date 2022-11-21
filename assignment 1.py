#Luke Schroeder
#assignment 1
#CPSC 3400 02
import string
from collections import deque
import collections
from copy import copy

def fillDic(inFile):
    dictionary = {}
    count = 0;
    adj = list()
    
    with open (inFile) as file:
        for line in file:
            key = line.rstrip()
            dictionary[str(key)] = adj
    return dictionary

def findWordLadder(start, end, dictionary):
    #error handle
    if start == end:
        print (start + " " + end)
        return 0
    if start not in dictionary:
        print(start + " is not in the dictionary")
        return 0
    
    if end not in dictionary:
        print(end + " is not in the dictionary")
        return 0
    
    queue = deque()
    queue.append([start])
    
    print("word ladder from: " + start + " to " + end)
    check = 0
    # checking to make sure the end has an adjacency
    for char in range(0, len(end)): 
        for letter in string.ascii_lowercase:
                newWord = end[:char] + letter + end[char+1:]
                if(newWord in dictionary and newWord != end):
                    check += 1
    if(check == 0):
        print ("no Word Ladder")
        return 0

    visited = []
    while queue:
        currLadder = queue.popleft()
        origLadder = copy(currLadder)
        word = str(currLadder[-1])
        for char in range(0, len(word)): 
            for letter in string.ascii_lowercase:
                newWord = word[:char] + letter + word[char+1:]
            
                if  newWord == end:
                    currLadder.append(newWord)
                    return currLadder
                
                if newWord in dictionary and newWord != word and newWord not in visited:
                    currLadder.append(newWord)
                    visited.append(newWord)
                    if str(currLadder) not in dictionary:
                        dictionary[str(currLadder)] = 1
                        queue.append(currLadder)
                        currLadder = copy(origLadder)
        
    print("No word ladder found")
    return 0


def main():
    d = fillDic("words.txt")

    #my own word list based on the video
    words = {"car":0,"cat":0,"cot":0,"cur":0,"cut":0,"hot":0,"tar":0}
    
    print(findWordLadder("aah", "aal", d))
    print(findWordLadder("car","hot",words))
    print(findWordLadder("cat","hot",d))
    print(findWordLadder("aces", "reef", d))
    print(findWordLadder("awed", "pest", d))
    print(findWordLadder("abed", "expo", d))
    print(findWordLadder("yak", "zyz",d))
    print(findWordLadder("clash", "plumb", d))
    
    print(findWordLadder("gloves", "topper", d))

if __name__ == "__main__":
    main()
