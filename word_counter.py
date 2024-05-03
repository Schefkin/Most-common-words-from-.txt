import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Add more words as needed
ignore_words = ['die', 'der', 'und', 'zu', 'in', 'das', 'ist', 'daãÿ', 'nicht', 'es', 'sie', 'sich', 'von', 'eine', 'den', 'ein',
                'als', 'wird', 'oder', 'des', 'fã¼r', 'wir', 'mit', 'sind', 'werden', 'auf', 'man', 'aber', 'wenn', 'system', 'diese',
                'durch', 'er', 'haben', 'nur', 'einer', 'hat', 'kann', 'um', 'im', 'wie', 'dem', 'sein', 'ihre', 'e', 'so', 'auch',
                'wã¼rde', 'ã¼ber', 'nach', 'dann', 'an', 'damit', 'al', 'kã¶nnen', 'weil', 'viele', 'andere', 'einem', 'aus', 'â§',
                'macht', 'en', 'keine', 'wã¤re', 'dieser', 'seine', 'muãÿ', 'zum', 'kã¶nnte', 'noch', 'bei', 'was', 'unter', 'eines', 
                'dafã¼r', 'uns', 'dies', 'ohne', 'unserer', 'ihnen', 'wã¼rden', 'zur', 'immer', 'ihrer', 'bedã¼rfnisse', 'jeder', 'mã¼ssen', 
                'revolutionã¤re', 'unsere', 'sehr', 'hier', 'sol', 'war', 'denn', 'zeit', 'verã¤nderung', 'ihren', 'usw', 'vom', 'alle', 'ihm',
                'bis', 'verã¤nderungen', 'ihn', 'diesem', 'diesen', 'gegenã¼ber', 't', 'kleinen', 'kleine', 'am', 'abhã¤ngig', 'fã¼hren', 'bevã¶lkerung', 'wã¤hrend',
                'kein', 'groãÿen', 'vgl', 'te', 'stã¤rker', 'prozeãÿ', 's', 'seiner', 'verã¤ndert', 'keinen', 'natã¼rlich', 'seinen', 'darã¼ber', 'wã¤ren', 'mã¶glich', '„',
                'nichts', 'ã¼berangepaãÿte', 'bedã¼rfnissen', 'lã¤ãÿt', 'gefã¼hle', 'lã¶sen', 'jeden', 'vielen', 'fã¼hrt', 'unmã¶glich', 'hã¤tte']  

# Read the text from a file
with open('file.txt', 'r') as file:
    text = file.read()

# Remove punctuation and lowercase the text
text = text.translate(str.maketrans('', '', string.punctuation)).lower()

# Tokenize the text into words
words = word_tokenize(text)

# Filter out the ignore words
filtered_words = [word for word in words if word not in ignore_words]

# Count the frequency of each word
word_freq = Counter(filtered_words)

# Ask the user for the output file name
output_filename = input("Enter the name of the output file: ")

# Open a file to write the results
with open(output_filename + '.txt', 'w') as output_file:
    # Write the most common words to the file
    for word, freq in word_freq.most_common(400): # Change 10 to however many top words you want to write
        output_file.write(f"{word}: {freq} times\n")