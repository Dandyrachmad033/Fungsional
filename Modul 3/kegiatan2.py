data1 = ["21 hari 20 jam 9 menit 20 detik", "19 hari 14 jam 0 menit 13 detik", "1 hari 1 jam 1 menit 1 detik"]


m = list(map(lambda x: x.replace('hari','').replace('jam','').replace('menit','').replace('detik', ''), data1))

def konversi(h=0):
    def jam(j=0):
        def menit(m=0):
            def detik(d=0):
                return ((((h*24)+ j)*60)+m)*60 +d
            return detik
        return menit
    return jam

def listAppend(nameList, nameFunction):
    a = []
    for i in nameList:
        hari, jam, menit, detik = i.split('  ')
        konvert = nameFunction(int(hari))(int(jam))(int(menit))(int(detik))
        a.append(konvert)
    return a

print(listAppend(m, konversi))
input("masuk")

