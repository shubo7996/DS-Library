import time
from datetime import datetime as dt

tempHost = "hosts"
pathVar = "C:\Windows\System32\drivers\etc"
host = "127.0.0.1"
webList = ["www.facebook.com" , "www.Pornhub.com", "www.xnxx.com"]

def checktime(pathVar):
	while True:
		if dt(dt.now().year,dt.now().month,dt.now().day,15) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,19):
			handleFileWhenBlocked(pathVar)
			break
		else:
			handleFileWhenNotBlocked(pathVar)
			print ("lets roll")
			time.sleep(5)


def handleFileWhenBlocked(pathVar):
	with open(pathVar, "r+") as file:
		content = file.read()
		print(content)
		for website in webList:
			if website in content:
				pass
			else:
				file.write(host + "" + website + "\n")

def handleFileWhenNotBlocked(pathVar):
	with open(pathVar, "r+") as file:
		content = file.readlines()
		file.seek(0)
		for line in content:
			if not any (website in line for website in webList):
				file.write(line)
		file.truncate()


checktime(pathVar)