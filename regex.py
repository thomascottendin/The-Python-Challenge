#Regex

#One small letter, surrounded by EXACTLY three big bodyguards on each of its sides

#Source code:
#<!--
#kAewtloYgcFQaJNhHVGxXDiQmzjfcpYbzxlWrVcqsmUbCunkfxZWDZjUZMiGqhRRiUvGmYmvnJIHEmbT
#MUKLECKdCthezSYBpIElRnZugFAxDRtQPpyeCBgBfaRVvvguRXLvkAdLOeCKxsDUvBBCwdpMMWmuELeG
#ENihrpCLhujoBqPRDPvfzcwadMMMbkmkzCCzoTPfbRlzBqMblmxTxNniNoCufprWXxgHZpldkoLCrHJq
#...

#une lettre minuscule entourée par 3 lettres majuscules

import urllib.request
import re

#load raw html source coding using urllib.request
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()

#extract the comment blocks in html. Note that by default dot does not match \n, so we need to use re .DOTALL flag
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]

print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))

#Result: linkedlist