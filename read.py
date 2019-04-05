data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))

print('All reviews are read. There are', len(data), 'reviews in total.')

#count the average length of the reviews
total_len = 0
for review in data:
    total_len += len(review)

print('The average lenth of the reviews is', total_len/len(data))


