data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        # if count % 1000 == 0:
        #     print(len(data))
print('All reviews are read. There are', len(data), 'reviews in total.')


#count the average length of the reviews
total_len = 0
for review in data:
    total_len += len(review)

print('The average lenth of the reviews is', total_len/len(data))

#filter for reviews shorter than 100 words
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('There are', len(new), 'reviews whose length less than 100.')
print(new[0])

#filter for reviews which contain 'good'
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('There are', len(good), 'reviews which contains "good".')
print(good[0])



#count the number of each word
wc = {} #word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('Which word do you want to search: ')
    if word == 'q':
        print('Thanks for using!')
        break
    if word in wc:
        print('The number of "', word, '" in the reviews is', wc[word])
    else:
        print('The word is not exist.')




