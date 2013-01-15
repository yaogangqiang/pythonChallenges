def translate(string):
    translated_string = '' 
    for i in string:
        if ord(i) >= ord('a') and ord(i) <= ('z'):
            if i == 'y': i = 'a'
            elif i == 'z': i = 'b'
            else:
                i = chr(ord(i) + 2)
        translated_string += i
    return translated_string

                
string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
print translate(string)
