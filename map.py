#0
#http://www.pythonchallenge.com/pc/def/0.html
print(2**38)
print('http://www.pythonchallenge.com/pc/def/{}.html'.format(2**38))

#1
#http://www.pythonchallenge.com/pc/def/map.html
k1 = ord('M')-ord('K')
k2 = ord('Q')-ord('O')
k3 = ord('G')-ord('E')
print('k1 = {},k2={},k3={}'.format(k1,k2,k3))
str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def map(str,k):
    newStr=''
    for c in str:
        if c=='.' or c==' ' or c=="'":
            newStr += c
        else:
            c1 = ord(c)+k
            if c1 in range(64,91) or c1 in range(97,122):
                newStr += chr(c1)
            else:
                newStr += chr(c1-26)
       
    return newStr
s2 = map(str,k1)
print(str)
print(s2)

# string.maketrans
intab = "abcdefghijklmnopqrstuvwxyz"
outtab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outtab)
print (str.translate(trantab))
print ('http://www.pythonchallenge.com/pc/def/{}.html'.format('map'.translate(trantab)))

#2
#http://www.pythonchallenge.com/pc/def/ocr.html

f = open(r"ocr.txt")
str = f.read()
for x in str:
    if x.isalpha():
        print(x)
# equality