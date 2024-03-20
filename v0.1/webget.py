import os

def shellXecute(cmd,pcmd):
	if cmd == "" and not(pcmd == ""):
		os.system(f"""
		 if pip show {pcmd} -q
		 then
		 else
		   pip install {pcmd} || pip2 install {pcmd}
		 fi
		""")
	elif pcmd == "" and not(cmd == ""):
		os.system(f"""
		 if command -v {cmd} > log
		 then
		   rm -rf log
		  else
		   rm -rf log
		   pkg install {cmd} || sudo apt install {cmd}
		 fi
		""")
	elif cmd != "" and pcmd != "":
		os.system(f"""
		 if pip show {pcmd} -q && command -v {cmd} > log
		 then
		   rm -rf log
		 else
		   rm -rf log
		   pkg install {cmd} || sudo apt install {cmd}
		   pip install {pcmd} || pip2 install {pcmd}
		 fi
		""")
def pull(u,w):
	try:
		os.system(f"{u}")
	except:
		os.system(f"{w}")
		

shellXecute("wget","requests")
shellXecute("curl","")

from os.path import exists
from time import sleep
import requests


def fileHundler():
	link = input("link: ")
	file = input("filename: ")

	r = requests.get(link)
	with open(f"{file}","wb") as f:
		f.write(r.content)
		if r == r:
			if exists(file):
				print("...Done")
			elif exists(file) == False:
				os.system(f"wget {link}")
				if exists(file):
					print("...Done")
				if exists(file):
					os.system(f"curl -o {file} {link}")
					if exists(file):
						print("..Done")
					else:
						pass
				else:
					pass
			else:
				pass
		else:
			pass
						
while True:
	fileHundler()