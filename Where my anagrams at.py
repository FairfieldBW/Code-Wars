'''
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. 
'''

def anagrams(word, words):
	word = list(word)
	word.sort()
	anagrams = []


	for listWord in words:
		listListWord = list(listWord.replace(" ", ""))
		listListWord.sort()
		print(listListWord)
		if listListWord == word:
			anagrams.append(listWord.replace(" ", ""))

	return anagrams

print(anagrams('abba', ['a    abb', 'abcd', 'bbaa', 'dada']))