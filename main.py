from disease import Disease
import os

os.chdir("webpages")
directory = os.listdir()
filename = directory[0]
file = open(directory[0]).read()
disease = Disease(filename, file)
print(disease.wordBag)
print(disease.id)
print (disease.name)