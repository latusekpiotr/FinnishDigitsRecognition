import os

# Constants declarations
PATH = "/home/latusek/Speech Recognition Laboratory/"
IN_FILE = os.path.join(PATH, "labels.txt")
MLF_TRAIN_FILE = os.path.join(PATH, "train.mlf")
MLF_TEST_FILE = os.path.join(PATH, "test.mlf")
SCP_TRAIN_FILE = os.path.join(PATH, "train.scp")
SCP_TEST_FILE = os.path.join(PATH, "test.scp")

digits = {"nolla": "NOLLA",
	  "yksi": "YKSI",
	  "kaksi": "KAKSI",
	  "kolme": "KOLME",
	  "neljä": "NELJA",
	  "viisi": "VIISI",
	  "kuusi": "KUUSI",
	  "seitsemän": "SEITSEMAN",
	  "kahdeksan": "KAHDEKSAN",
	  "yhdeksän": "YHDEKSAN"}

# Opening files
inFile = open(IN_FILE, "rb")
mlfTrainFile = open(MLF_TRAIN_FILE, "wb")
mlfTestFile = open(MLF_TEST_FILE, "wb")
scpTrainFile = open(SCP_TRAIN_FILE, "wb")
scpTestFile = open(SCP_TEST_FILE, "wb")

# Generating training files
mlfTrainFile.write("#!MLF!#\n")
for i in range(0, 2500):
	entry = inFile.readline()
	words = entry.split(' ')
	file = words[0]
	file = file.replace('/share/', '/opt/local/')
	digit = words[2].strip('\r\n')

	mlfTrainFile.write('"')
	mlfTrainFile.write(file)
	mlfTrainFile.write('"\n')
	mlfTrainFile.write(digits.get(digit))
	mlfTrainFile.write("\n.\n")

	scpTrainFile.write(file.replace('FIAFIO', 'MFC_Z').replace('.fio', '.mfc'))
	scpTrainFile.write("\n")

# Generating test files
mlfTestFile.write("#!MLF!#\n")
for i in range(2500, 3000):
	entry = inFile.readline()
	words = entry.split(' ')
	file = words[0]
	file = file.replace('/share/', '/opt/local/')
	digit = words[2].strip('\r\n')

	mlfTestFile.write('"')
	mlfTestFile.write(file)
	mlfTestFile.write('"\n')
	mlfTestFile.write(digits.get(digit))
	mlfTestFile.write("\n.\n")

	scpTestFile.write(file.replace('FIAFIO', 'MFC_Z').replace('.fio', '.mfc'))
	scpTestFile.write("\n")

# Closing files
inFile.close()
mlfTrainFile.close()
mlfTestFile.close()
scpTrainFile.close()
scpTestFile.close()
