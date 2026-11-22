with open('practice.py','r')as f: #open a file practice py
     print("initial position:",f.tell())  #check inital position start of file
     print("Read:",f.read(5))   #read the first 5 characters
     print("position after reading 5 bytes:",f.tell())  #read the first 5 characters
     f.seek(0)   #now go back to 0
     print("position after seek 0:",f.tell())   #ab tm 0 pr jaany k baad tell kro