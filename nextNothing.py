#Click on the image, you would see

#    and the next nothing is 44827

#And the url changed to http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345

#Change the url with the new number and another number will be given.

from urllib.request import urlopen
import re

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

num = "12345"
#num = str(16044/2)

pattern = re.compile("and the next nothing is (\d+)")

while True:
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

 #Result: peak.html