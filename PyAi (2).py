import os,sys,sysconfig,webbrowser,time,datetime as dt,random
# updating this file in startup folder
# a = open(sys.argv[0])
# b = open("C:\\Users\\{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\etask2.py".format(os.getlogin()), "w")
# c= open("C:\\Users\\{}\\Desktop\\PyAi.py".format(os.getlogin()),"w")
# b.write(a.read())
# c.write(a.read())
def style(x,y):
    #where x is the sring and y is fastness to print
    sys.stdout.write("\r")
    for a in x:
        sys.stdout.write(a.upper())
        sys.stdout.flush()
        time.sleep(y)
    global var2
    var2=len(x)
tm=""
hr =int(str(dt.datetime.fromtimestamp(time.time()))[11:13])
if hr > 0 and hr < 10:
    tm = "morning"
if hr >10 and hr < 17:
    tm = "afternoon"
if hr >17 and hr < 20:
    tm = "evening"
if hr >20:
    tm ="night"
greeting = "good  {}  sir".format(tm)
style(greeting,0.02)
time.sleep(2)
sent1="what you wanna do sir"
style(sent1+" "*(var2-len(sent1)),0.07)
sent2="give me a task "
style(sent2+"-"*(var2-len(sent2))+">",0.02)
var1 =input()
inp=var1.lower()
while True:
    if "open" in inp:
        inp = inp.replace("open ", "")
    if "google" in inp:
        webbrowser.open_new_tab("www.google.com")
    if ".com" in inp:
        webbrowser.open_new_tab("http:\www."+inp)
    if "music" in inp or "song" in inp or "songs" in inp:
        os.startfile("C:\\Users\\krishna\\Desktop\\gaane\\{}".format(os.listdir("C:\\Users\\krishna\\Desktop\\gaane")[random.randrange(0,len(os.listdir("C:\\Users\\krishna\\Desktop\\gaane")))]))
    inp=input("anything else:")
    if inp == "no" or inp =="na":
        break

        
sent3 = "my service is that only but it is in working"
style(sent3+" "*(var2-len(sent3)),0.01)
time.sleep(2)
try:
    pass
finally:
    print()
    print()
    sent4='bye'
    style(sent4+" "*(var2-len(sent4)),0)
    print()
    time.sleep(2)


