input_list = ['all', 'this', 'happened', 'more', 'or', 'less']
#
def find_bigrams(input_list):
	bigram_list = []
	for i in range(len(input_list)-1):
		print i
		bigram_list.append((input_list[i], input_list[i+1]))
	return bigram_list
#
bigrams = find_bigrams(input_list)
print bigrams
# will output:
#0
#1
#2
#3
#4
#[('all', 'this'), ('this', 'happened'), ('happened', 'more'), ('more', 'or'), ('or', 'less')]