# sort frequencies
filename = "frequency.txt"
freq = [line.rstrip('\n') for line in open(filename)]
freqParsed = []
for f in freq:
	item = f.split(' ')
	#convert decimal to hex
	item[0] = hex(int(item[0]))
	#remove bracket and % sign
	item[-1] = item[-1][0:-2]
	#remove another bracket
	if '(' in item:
		item.remove('(')
	#change % to decimal
	item[-1] = round(float(item[-1])/100, 5)
	freqParsed.append(item)


def sort_ascii_list():
	freqParsed.sort(key=lambda x: float(x[-1]), reverse=True)
	for sortedItem in freqParsed:
		print (sortedItem)


