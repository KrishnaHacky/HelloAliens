import os

b=os.listdir("C:/Users")
path="C:/Users"
while True:
    c = []
    for x in range(len(b)):
        c.append("{} -- {}".format(str(x), b[x]))
        print(c[x])
    a=int(input("choose the directory you wanna go with == ".upper()))

    path = os.path.join(path, b[a])

    def oldpath(path):
        p = list(path)
        p.reverse()
        for x in range(len(p)):
            if p[0] == "\\":
                break
            else:
                p.remove(p[0])
        p.remove(p[0])
        p.reverse()
        o = ""
        for x in range(len(p)):
            o = o + p[x]
        return o

    if os.path.isfile(path):
        os.startfile(path)
        path=oldpath(path)
    else:
        b = os.listdir(path)
