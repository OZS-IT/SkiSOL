from os import path
from re import *
for j in range(1,7):
    if not path.isfile("SSOL"+str(j)+"a.csv"):
        break
    with open("./Registracije/registracija1.txt","r", encoding = "UTF-8") as s:
        n = s.read()
    with open("SSOL"+str(j)+"a.csv","r", encoding = "UTF-8") as f:
        with open("SSOL"+str(j)+".csv","w", encoding = "UTF-8") as g:
            a = f.read()
            lines = a.split("\n")
            for i in lines:
                b = lines.split(";")
                if len(b)>2:
                    for k in n.split("\n"):
                        l = k.split(";")
                        if l[0] == b[2] and (l[3] in kategorije[b[18]]):
                            #rep = b[18]
                            re.sub(r";[A,B,C];",";"+l[3]+";", b)
                            g.write(b)
