"""
Project #7:
name: Chenghui Zhu

This program process a textual data file to generate a word concordance 
with line numbers for each main word (exclude the "stop words")
"""

def selectStopFile():
    """
    Read the stop word txt file into a stopWordDict.
    """
    stopWordDict = {}
    stopWord = input("Please enter the file name of \"stop words\" (DO NOT include \".txt\"): ")
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
    wordConcordanceDict = {}
    textual = input("Please enter the file name of \"main textual file\" (DO NOT include \".txt\"): ")
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
    stopWordDict = selectStopFile()
    wordConcordanceDict = selectWordFile(stopWordDict)
    outputName = input("Please enter the file name of \"output file\" (DO NOT include \".txt\"): ")
    sortDict(wordConcordanceDict, outputName)


if __name__ == "__main__":
    main()