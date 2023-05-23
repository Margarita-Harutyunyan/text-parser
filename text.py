class Word:
    def __init__(self):
        self.__word = None

    def getWord(self):
        return self.__word
    
    def setWord(self, word):
        self.__word = word
    
    def removeSpecial(self):
        self.__word = ''.join((c for c in self.__word if c.isalnum()))

    def lowerCase(self):
        self.__word = self.__word.lower()
    
    def __eq__(self, other):
        return self.__word == other.__word
    
    def __str__(self):
        return self.__word

        
class Text:
    def __init__(self, dictPath = ''):
        self.__collection = []
        self.__dictPath = dictPath

    def traverse(self):
        return self.__collection

    def viewCollection(self):
        if self.__collection:
            for i in range(len(self.__collection) - 1):
                print(self.__collection[i], end = ', ')
            print(self.__collection[-1])
    
    def add(self, word):
        oWord = Word()
        oWord.setWord(word)
        self.__normalize(oWord)
        if oWord.getWord():
            duplicate = False
            for wordOb in self.__collection:
                if oWord == wordOb:
                    duplicate = True
            if not duplicate:
                self.__collection.append(oWord)

    def __normalize(self, word):
        word.removeSpecial()
        word.lowerCase()

        if self.__foundInDict(word):
            return

        if len(word.getWord()) > 1 and word.getWord()[-1] == 's':
            sWord = word.getWord()[:-1]
            tmp = Word()
            tmp.setWord(sWord)
            if self.__foundInDict(tmp):
                word.setWord(sWord)
                return
        
        if len(word.getWord()) > 2 and word.getWord()[-2:] == 'es':
            sWord = word.getWord()[:-2]
            tmp = Word()
            tmp.setWord(sWord)
            if self.__foundInDict(tmp):
                word.setWord(sWord)
                return
        
        word.setWord('')
            
        
            
    def __foundInDict(self, word):
        if self.__dictPath == '':
            return True
        
        with open(self.__dictPath, 'r') as dictionary:
            for dword in dictionary:
                dword = dword.strip()
                if word.getWord() == dword:
                    return True
