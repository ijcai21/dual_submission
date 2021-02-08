import pdftotext
import os
import re
import csv
from collections import Counter

def cleanWord(word):
    regex = re.compile('[,\.!?\(\)0-9]')
    out = regex.sub('', word)
    out=out.lower()
    return out

for file in os.listdir('pdfs/'):
    if (file.endswith(".pdf")):

        words = [];
        with open('pdfs/' + file, "rb") as f:
            pdf = pdftotext.PDF(f)
            for page in pdf:
                words = words + page.split()


        histogram={}
        abstract_reached = False
        for word in words:
            if (word == "Abstract"):
                abstract_reached= True
                continue
            if (abstract_reached):
                word = cleanWord(word)
                if len(word) < 5:
                    continue
                if word in histogram:
                    histogram[word] += 1
                else:
                    histogram[word] = 1

        histogram_sorted = (sorted(histogram.items(), key=lambda x:x[1], reverse = True))
        freq_words = (list(filter(lambda x: x[1] > 1, histogram_sorted)))
        fileout = file + ".csv"
        with open(fileout, 'w', newline='') as outfile:
            wr = csv.writer(outfile, quoting=csv.QUOTE_ALL)
            for words in freq_words:
                wr.writerow(words)