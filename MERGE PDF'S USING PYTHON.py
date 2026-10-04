
from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []
n = int(input("How many pdfs do you want to merge?\n"))
# This is a nice way to iterate using for loops in Python 

for i in range(0, n): 
    name = input(f"Enter the name of pdf {i + 1}: ")
    pdfs.append(name)  

for pdf in pdfs:
    merger.append(pdf)

merger.write("merging by guneesh kohli4.pdf") # it is name of file in which all files are merged 
merger.close()


'''

merger = pdfwriter
pdfs=[]
enter how many files you wanna merge

i=0
for i in range(0, n):
print(f" enter the  pdf{i+1} name:   ")
pdfs.append(name)

for pdf in pdfs:


'''