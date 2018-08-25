'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
	dictionary = {}
	for list_ in string:
		for word in list_:
			if word in dictionary.keys():
				dictionary[word] = dictionary[word] + 1

			else:
				dictionary[word] = 1
	return dictionary
            
def main():
	string = []
	no_of_lines = int(input())
	for _ in range(no_of_lines):
		string.append(input().split())
	print(tokenize(string))


if __name__ == '__main__':
    main()
