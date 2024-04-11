# poem.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurance.
word_stats={}
with open("E:/Programming/Crash Course of Python by Google/Exercisess/read_write_exercise/poem.txt","r") as f:
    for line in f:
        words=line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word]=1

print(word_stats)
word_occurances = list(word_stats.values())
print(word_occurances)
max_count=max(word_occurances)
print('Max occurances of any word is: ', max_count)
print("Words with max occurances are: ")
for word,count in word_stats.items():
    if count==max_count:
        print(word)