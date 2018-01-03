from urllib.request import urlopen
with open("Registracije/registracije1.csvreg","r",encoding="utf-8") as f:
    with open("Registracije/registracije1.csv","w",encoding="utf-8") as g:
        a = f.read()
        b = a.split("\n")
        ozs = urlopen("http://www.orientacijska-zveza.si/registracija-ski-o.html")
        stran=ozs.read().decode("utf-8")
        s = ""
        for i in b:
            stri=""
            c = i.split(";")
            k = 0
            if len(c)>1:
                if not ((c[1]+" "+c[2]+"<sup>") in stran) or c[1] in ["Mariya"]:
                    while k < 5:
                        stri += c[k]+";"
                        k += 1
                    stri = stri[:-1] + ";\n"
                    s += stri
                else:
                    print(c)
        if len(c)>1:
            if not (c[1]+" "+c[2]+"<sup>" in stran):
                g.write(s)
            else:
                print(s)
