import os
from xml.dom import minidom


folder = "Annotations/"

def check_freq(freq_min_tol, freq_max_tol):
	#I want to get all audios whose annotations is such that
	#the range of freq_min and freq_max is in the range 
	#of (freq_min_tol, freq_max_tol)
	
	#Get names of the file in folder
	files = os.listdir(folder)
	
	#List which contains the name of all file that satisfy 
	#what I want
	annotations = []
	for f in files:
		#get file name
		file_name = os.path.basename(f)
		path_file = folder+file_name
		#print(path_file)
		
		#Parse the file select
		dom = minidom.parse(path_file)
		#Get root element 
		#root = dom.documentElement
		#Gte elements
		items = dom.getElementsByTagName("point")
		#Get 
		boolean = False
		for item in items:
			value = float(item.getAttribute("value"))#freq_min
			extent = float(item.getAttribute("extent"))#freq_max_freq_min
			
			#I want freq_max, freq_min in (1000, 9000)
			if value >= freq_min_tol and extent <= freq_max_tol:
				boolean = True
			else:
				boolean = False
		
		#if boolean is true, all frequence in file
		#satisfy freq_max, freq_min in (1000, 9000)
		if boolean:
			annotations.append(file_name)
	return annotations
		
		#print(attributs)
		
freq_min_tol, freq_max_tol = 1000.0, 9000.0


annotations = check_freq(freq_min_tol, freq_max_tol)

#print(annotations)

print(f"Number of files with frequency ranges {freq_min_tol, freq_max_tol} : {len(annotations)}")


#os.syste("mkdir annotaions")


#**********************************************
#Copy all file well annoted in my folder
#for file_name in annotations:
#	#print(path)
#	os.system("cp "+folder+file_name+" annotations")
#**********************************************
#

#Get file names 
with open("DataFiles/TrainingFiles.txt", "r") as f1:
	lines_f1 = [line.strip() for line in f1.readlines()]

with open("DataFiles/TestingFiles.txt", "r") as f2:
	lines_f2 = [line.strip() for line in f2.readlines()]

print("Creating TrainingFiles.txt ...")

f3 =  open("datafiles/TrainingFiles.txt", "a")


print("Creating TestingFiles.txt ...")

f4 =  open("datafiles/TestingFiles.txt", "a")


i = 0
j = 0
for file_name in annotations:
	fname = file_name.split('.')[0]
	if fname in lines_f1:
		f3.write(fname+"\n")
		i += 1
	elif fname in lines_f2:
		f4.write(fname+"\n")
		j +=1


f2.close()

f4.close()


print(f"{i} testing files and {j} testing files")
print("Done")






	
