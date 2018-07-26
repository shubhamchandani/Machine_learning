#!/usr/bin/python3
import operator
import numpy
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import PyPDF2
def split_file():
	file = "/home/shubham/Downloads/JavaBasics-notes.pdf"
	pdf_file = open(file, 'rb')
	read_pdf = PyPDF2.PdfFileReader(pdf_file)
	number_of_pages = read_pdf.getNumPages()
	split =[]
	for i in range(number_of_pages):

		page = read_pdf.getPage(i)
		page_content = page.extractText()
		if len(split) == 0:
			split = page_content.split()
		else:
			split.append(page_content.split())
	return (split)

def extract(list1):
	count_in = 0
	count_en = 0
	count_mt = 0
	for i in list1:
		if " Inheritance" in i:
			count_in = count_im + 1
		elif  "encapsulation" in i:
			count_en = count_en+1
		elif  "multithreading" in i:
			count_mt = count_mt+1
	#print ("no of times inheritence occured = "+str(count_in))
	#print ("no of times encapsulation occured ="+str(count_en))
	#print ("no of times multithreading occured ="+str(count_mt))
	count = {'Inheritance':count_in,'encapsulation':count_en,'multithreading':count_mt}
	return (count)
def sort_dic(dic):
	sorted_d = sorted(dic.items(), key=operator.itemgetter(1))
	print (dic)
	return (dic)
def write_into_excel(dictionary):
	df = pd.DataFrame(dictionary,index=[0]) 
	writer = ExcelWriter('excel.xlsx')
	df.to_excel(writer,'Sheet1',index=False)
	writer.save()


list1 = []
list1 = split_file()
dic = extract(list1)
sort_dic(dic)
dictionary = sort_dic(dic)
write_into_excel(dictionary)


		 
