#Level 1

# Decrypt:
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
#indice: K -> M ; O -> M ; E -> G

#Alphabetical substitution

raw = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

table = str.maketrans(
    "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
)

result = raw.translate(table)

print(result)

#i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

#URL before: http://www.pythonchallenge.com/pc/def/map.html

raw = "map"

result = raw.translate(table)

print(result)

#URL after: http://www.pythonchallenge.com/pc/def/ocr.html