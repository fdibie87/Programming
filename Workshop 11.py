#Part 1
# This program generates 10 random integers between 1 and 100, writes them to a file, and then calculates the average of those integers.
import random
f = open('integers.txt',"w")
for count in range(10):
    number = random.randint(1,100)
    f.write(str(number)+'\n')
f.close()

with open('integers.txt','r') as infile:
    num = [int(line.strip()) for line in infile]
    average = sum(num)/ len(num)
    print(average)
with open('result.txt','w') as outfile:
    outfile.write(f'The average value is {average}')

#Part 2
# This program prompts the user to enter 5 words, writes them to a file, and then counts the number of words in that file.
f = open('mywords.txt',"w")
for i in range(5):
    five_words = input(f'Enter word no{1+i}:')
    f.write(five_words + '\n')
f.close()
#Part 3
# Reads the words file and counts total words 
f = open('mywords.txt','r')
text = f.read()
words = len(text.split())
print(f'There are {words} words in the file.')

