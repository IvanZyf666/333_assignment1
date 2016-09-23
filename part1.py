import operator
filename = "1.txt"
cipher = [line.rstrip('\n') for line in open(filename)]
length = len(cipher)

# find key length
# j is the index, i is what you're adding each time. 
# coincidence is a counter for each iteration of the loop.

coincidence = []
for i in range (1, length//2):
    coincidence.append(0) #add counter for this iteration 
    
    for j in range(length):
        if (j + i) >= length:    
            break
        
        if cipher[j] == cipher[i+j]:
            coincidence[i-1] += 1
            
key_length = 7 # I counted it. 


# find the key
# frequency: http://fitaly.com/board/domper3/posts/136.html

count = []
char_count = dict()
total = 0

for i in range (7):
    # count frequency for each letter
    for char in cipher[i::7]:
        total += 1
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for char in char_count:
        char_count[char] = round(char_count[char]/total, 5)
          
    count.append(char_count)
    char_count = dict()
    total = 0
    

sorted_x = sorted(count[0], key=count[0].get, reverse=True)

for char in sorted_x:
    print(char, count[0][char])