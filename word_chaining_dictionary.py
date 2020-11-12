import time
from chaining_dictionary import ChainingDict


def selectStopFile():
    """
    Read the stop word txt file into a stopWordDict.
    """
    stopWordDict = ChainingDict(2700)
    #stopWord = input("Please enter the file name of \"stop words\" (DO NOT include \".txt\"): ")
    stopWord = "stop_words"
    stopWordTxt = stopWord + ".txt"
    with open(stopWordTxt, "r") as stopFile:
        for line in stopFile:
            item = line.strip()
            stopWordDict[item] = []
    return stopWordDict


def selectWordFile(stopWordDict):
    """
    Read the main textual txt file. 
    Select each word excluding stop words (split by line and whitespace) and reshape each word.
    Assign each word with the lineCounter that appeared in every line.
    """
    wordConcordanceDict = ChainingDict(20000)
    #textual = input("Please enter the file name of \"main textual file\" (DO NOT include \".txt\"): ")
    textual = "WarAndPeace"
    textualTxt = textual + ".txt"
    with open(textualTxt, "r") as textualFile:
        lineCounter = 1
        for line in textualFile:
            wordList = line.split()
            for word in wordList:
                word = reshape(word)
                if not word in stopWordDict:
                    if not word in wordConcordanceDict:
                        wordConcordanceDict[word] = [lineCounter]
                    else:
                        wordConcordanceDict[word].append(lineCounter)
            lineCounter += 1
    return wordConcordanceDict


def sortDict(wordConcordanceDict, outputName):
    """
    Write the result as an output txt file.
    """
    concordanceWordList = sorted(wordConcordanceDict)
    outputTxt = outputName + ".txt"
    with open(outputTxt, "w") as outputFile:
        for word in concordanceWordList:
            outputFile.write(word + ": ")
            for line in wordConcordanceDict[word]:
                outputFile.write(str(line) + " ")
            outputFile.write("\n")
        outputFile.close()


def reshape(word):
    """
    Reshape each word with lower case and exclude any non-letter sign.
    """
    word = word.lower()
    for letter in word:
        if not letter.isalpha():
            word = word.replace(letter, "")
    return word


def main():
    start = time.perf_counter()
    stopWordDict = selectStopFile()
    wordConcordanceDict = selectWordFile(stopWordDict)
    outputName = "test6"
    sortDict(wordConcordanceDict, outputName)
    end = time.perf_counter()
    print("Time =", end - start)


if __name__ == "__main__":
    main()