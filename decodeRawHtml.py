#Decode raw html and use regex to find comment

#recognize the characters. maybe they are in the book,
#but MAYBE they are in the page source.

#Source code:
#<!--
#find rare characters in the mess below:
#-->

#<!--
#%%$@_$^__#)^)&!_+]!*@&^}@[@%]()%+$&[(_@%+%$*^@$^!+]!&_#)_*}{}}!}_]$[%}@[{_@#_^{*
#@##&{#&{&)*%(]{{([*}@[@&]+!!*{)!}{%+{))])[!^})+)$]#{*+^((@^@}$[**$&^{$!@#$%)!@(&
#+^!{%_$&@^!}$_${)$_#)!({@!)(^}!*^&!$%_&&}&_#&@{)]{+)%*{&*%*&@%$+]!*__(#!*){%&@++
#!_)^$&&%#+)}!@!)&^}**#!_$([$!$}#*^}$

import urllib.request
import re

#load raw html source coding using urllib.request
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()

#extract the comment blocks in html. Note that by default dot does not match \n, so we need to use re .DOTALL flag
comments = re.findall("<!--(.*?)-->", html, re.DOTALL)
#Alternatively we can use this: comments = re.findall("<!--([\w\n]*?)-->", html)

#The pattern <!--(.*)--> will capture all blocks inside <!-- and -->. We only care about the last part, so
data = comments[-1]

#unique char only appear once
print("".join(re.findall("[A-Za-z]", data)))

#Result: equality