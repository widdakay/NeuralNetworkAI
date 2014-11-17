import operator

test = open("/Users/erimeik/Desktop/test.txt", "r")
words = {}
for word in test.read().split():
	words[word.lower()] = words.get(word.lower(), 0) + 1

words = sorted(words.items(), key=operator.itemgetter(1))
words.reverse()

for i in words:
	print i[0]+","+str(i[1])