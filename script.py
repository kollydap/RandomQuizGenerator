import os
import shelve
shelfFile = shelve.open('yes')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats
shelfFile.close()
fileObject = open('C:\\Users\\kollydap\\desktop\\scripts\\hello.txt','a')
fileObject.write("happy boy")
fileObject.close()
fileObject = open('C:\\Users\\kollydap\\desktop\\scripts\\hello.txt')
file_content = fileObject.readline()
print(file_content)