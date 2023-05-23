import text

def parse(sourceFile, destinationDict, baseFile):
    textParser = text.Text(baseFile)
    with open(sourceFile, 'r') as file:
        words = file.read().strip().split()
        for word in words:
            textParser.add(word)
      
    for oWord in textParser.traverse():
        word = oWord.getWord()
        if word in destinationDict:
            destinationDict[word].append(sourceFile)
        else:
            destinationDict.update({word : [sourceFile]})


def dictToFile(sourceDict, destFile):
    with open(destFile, 'w') as file:
        for key in sourceDict:
            line = f'{key}:{str(sourceDict[key])[1 : -1]}\n'
            print(line)
            file.write(line)

def found(openFile, word):
    for line in openFile:
        line = line.split(':')
        if word == line[0]:
            openFile.seek(0)
            return line[1]
    openFile.seek(0)
    return None


if __name__ == '__main__':
    d = {}
    parse('/home/molly/Desktop/Crawler + Indexer/1.txt', d, '/home/molly/Desktop/Crawler + Indexer/words_alpha.txt')
    parse('/home/molly/Desktop/Crawler + Indexer/2.txt', d, '/home/molly/Desktop/Crawler + Indexer/words_alpha.txt')
    dictToFile(d, 'db.txt')

    with open('/home/molly/Desktop/db.txt', 'r') as file:
        while True:
            word = input('Enter a word to search or press Enter to quit: ')
            if word == '':
                print('Bye')
                break
            res = found(file, word)
            if res:
                print(res)
            else:
                print('Word not found')