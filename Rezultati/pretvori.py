from os import path
from re import sub
def skrajsaj(string):
    if string:
        return string[1:-1]
    return string
kategorije = {1:{"A" : ["M17", "M20", "M21E", "M40", "Ž21E", "MB", "Ž14", "ŽB","M14", "Ž17"],
                 "B" : []},
              2 : {"A" : ["M20", "M21E"],
                   "B" : ["Ž21E", "M40", "M17"],
                   "C" : ["M14", "MB", "Ž14", "Ž17", "ŽB"]}}
for j in range(1,3):
    if not path.isfile("SSOL"+str(j)+"a.csv"):
        break
    with open("../Registracije/registracije1.csv","r", encoding = "UTF-8") as s:
        n = s.read()
    with open("SSOL"+str(j)+"a.csv","r", encoding = "UTF-8") as f:
        with open("SSOL"+str(j)+".csv","w", encoding = "UTF-8") as g:
            a = f.read()
            lines = a.split("\n")
            z = 0
            for i in lines:
                z+=1
                if z > 2:
                    b = i.split(";")
                    for k in n.split("\n"):
                        l = k.split(";")
                        #print(b[3],b[4])
                        if  (l[4] in kategorije[j][skrajsaj(b[18])])and l[1] == skrajsaj(b[4]) and skrajsaj(b[3]) == l[2] :
                            gz=sub(r";\"[A-C]\";",";"+l[4]+";", i)
                            g.write(gz+"\n")
                else:
                    g.write(i+"\n")
