import re

#create function to capitalize the sentence
def capitalize_sentences(text):
  sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|!)\s', text)
  capitalized_sentences = [s.capitalize() for s in sentences]
  return " ".join(capitalized_sentences)

#build the dictionary from the file with all words
dictionary = { }
with open("top_english_words_lower_50000.txt","r") as file: 
    for line in file:
        #print(line)
        line = line.strip()
        characters = list(line)
        first_char=characters[0]
        last_char=characters[len(characters)-1]
        characters = characters[1:(len(characters)-1)]
        #print('middle chars: ', characters)
        characters.sort()
        key = first_char+"".join(characters)+last_char
        #print('key', key.lower())

        dictionary[key.lower()] = line.lower()
        
#print(dictionary);

#read the file for sentence with words scrambled letters
str_array = ''.strip().split()
with open("randoletter-input.txt","r") as file: 
    first_line_processed = False
    for line in file:
        if first_line_processed == False:
            str_array = line.strip().split()
            first_line_processed = True

# print(str_array)

#process all the words whose length is > 3. Create the word key based on the rules supplied and 
# find the matching word from the dictionary.
str_corrected = ""
for str in str_array:
    if len(str) > 3:
        random = str
        characters = list(random)
        first_char=characters[0]
        last_char=characters[len(characters)-1]
        characters = characters[1:(len(characters)-1)]
        characters.sort()
        key = first_char+"".join(characters)+last_char
        #print('key', key.lower())
        str_corrected = str_corrected +' ' + dictionary[key.lower()]
    else:
        str_corrected = str_corrected + ' '+str

#print(capitalize_sentences(str_corrected))

file = open("randomword-output.txt","w")
file.write(capitalize_sentences(str_corrected))
file.close()