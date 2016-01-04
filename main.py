"""
Some mickmath stuff

If you want to use with another dict:
change path line 25
check the "parsing words" part (line 27)
"""

#IMPORT
import unicodedata
import time

#FUNCTION
def evalWord(word):
	ret = 1;
	for letter in word:
		ret *= ord(letter.lower()) - ord('a') + 1
	return ret


#####################
#      Main         #
#####################

start = int(input("Quelle annee voulez vous commencer le test : "))
end   = int(input("Quelle annee voulez vous terminer le test : "))
timeBegin = time.time()

#reading file
f = open("./dict.txt", 'r')
words = f.readlines()
f.close()

#parsing words
evalList = []
for word in words:
	word = word[0:-1]
	_word = unicode(word, 'utf-8')
	_word = unicodedata.normalize('NFD', _word).encode('ascii', 'ignore')
	evalList.append((word, evalWord(_word)))

#init
total = 0
max = (0, -1) #(year, number of words found in this year)
nbrOfYearWithResult = 0

#seach in evalList
for year in xrange(start, end + 1):
	count = 0
	for tuple in evalList:
		if tuple[1] == year:
			print tuple[0], '->', tuple[1]
			count +=1
	if count > 0:
		print count, "words found in", year, "\n"
		total += count
		nbrOfYearWithResult += 1
		if count > max[1]:
			max = (year,count)

#final result on stdout
print "\n", total, "words found between", start, "and", end
print nbrOfYearWithResult, "years have their words"
print max[0], "is the winner year with", max[1], "words !"
print "time : ", time.time() - timeBegin, "s"
