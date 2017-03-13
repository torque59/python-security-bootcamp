import sys
from zipfile import ZipFile

with open("dict.txt") as stream:
	data = stream.readlines()

for passw in data:
	try:
		with ZipFile('secret.zip') as zf:
			if zf.extractall(pwd=passw.strip("\n")) == None:
				print "[+] Succesfully Extracted the file using password: "+passw
				#sys.exit(0)
	except RuntimeError:
		pass
