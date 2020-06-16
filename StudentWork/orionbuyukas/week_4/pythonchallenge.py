codededtext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
decodetext = ""

for i in range(0, len(codededtext)-1):
    codededtext = codededtext.upper()
    c = codededtext[i]
    if c != " ":
        decode = ord(c) + 2
        encode = chr(decode)
        decodetext += encode

print decodetext


codededtext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp."
decodetext = ""

for i in range(0, len(codededtext)-1):
    codededtext = codededtext.upper()
    encode = codededtext[i]
    if encode == "M":
		encode = "K"
    elif encode == "Q":
        encode = "O"
    elif encode == "G":
        encode ="E"
    decodetext += encode

print decodetext
print codededtext
