from text import Text

text = Text()

file = open('/home/molly/Desktop/Crawler + Indexer/lorem.txt', 'r')
readf = file.read().split()
for word in readf:
    text.add(word)