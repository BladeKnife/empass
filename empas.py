import os,sys,time,re,json,random,requests
def clear():
    os.system('clear')
def baner():
    print('''
\033[1;97m\tEMPAS CRACKER
\033[90m\t---------------

\033[1;97m{\033[1;91m•\033[1;97m}Creator:\033[1;96m FahmiApz
\033[1;97m{\033[1;91m•\033[1;97m}Youtube:\033[1;96m Knifer12
\033[1;97m{\033[1;91m•\033[1;97m}Github :\033[4;92m github.com/BladeKnife\033[00m
\033[1;94m_____________________________________''')
def load():
    for x in range(1,101):
        time.sleep(1./20)
        print(f"\r\033[1;97m[\033[1;96m•\033[1;97m]Loading\033[90m...\033[1;92m{x}\033[1;97m%", end="", flush=True)
def exit():
    sys.exit('\033[1;97m[\033[1;91m!\033[1;97m]\033[1;91mExit\033[00m')
def kembali():
    o=input("\033[1;97m\t[\033[1;93menter back to menu\033[1;97m]")
    if o == "":
       os.system("python empas.py")
    else:
       exit()
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./150)
def monton():
    time.sleep(1)
    os.system("wget https://raw.githubusercontent.com/LimitQueenProject/banner/master/empas-monton -o done")
    a=open("empas-monton","r")
    for anjayyyy in a:
        time.sleep(1)
        print("\033[1;97m[\033[1;92m√\033[1;97m]\033[1;92m",anjayyyy)
    a.close()
def empas():
    os.system("wget https://raw.githubusercontent.com/LimitQueenProject/banner/master/empas-fresh -o done")
    a=open("empas-fresh","r")
    for anjayy in a:
        time.sleep(1)
        print("\033[1;97m[\033[1;92m√\033[1;97m]\033[1;92m",anjayy)
    a.close()
def unchek():
    os.system("wget https://raw.githubusercontent.com/LimitQueenProject/banner/master/empas-uncheck -o done")
    a=open("empas-uncheck","r")
    for anjayyy in a:
        time.sleep(1)
        print("\033[1;97m[\033[1;92m√\033[1;97m]\033[1;92m",anjayyy)
    a.close()
def acak():
    os.system("wget https://raw.githubusercontent.com/LimitQueenProject/banner/master/empass -o done")
    a=open("empass","r")
    for anjay in a:
        time.sleep(1./5)
        print ("\033[1;97m[\033[1;92m√\033[1;97m]\033]1;92m",anjay)       
    a.close()
if __name__=="__main__":
     clear()
     baner()
     kata("""\033[1;97m{\33[1;95m01\033[1;97m}\033[1;96m Empas Random
\033[1;97m{\033[1;95m02\033[1;97m}\033[1;96m Empas Fresh
\033[1;97m{\033[1;95m03\033[1;97m}\033[1;96m Empas Uncheck
\033[1;97m{\033[1;95m04\033[1;97m}\033[1;96m Empas Moonton
\033[1;97m{\033[1;95m05\033[1;97m}\033[1;96m Empas Checker
\033[1;97m{\033[1;95m00\033[1;97m}\033[1;91m Exit\033[00m
\033[1;94m_____________________________________""")
     f=input('\033[1;97m[\033[1;91m?\033[1;97m]PILIH: \033[1;96m')
     if f == "01" or f == "1":
        load()
        print('\n')
        acak()
        kembali()
     elif f == "02" or f == "2":
        load()
        print('\n')
        empas()
        kembali()
     elif f == "03" or f == "3":
        load()
        print('\n')
        unchek()
        kembali()
     elif f == "04" or f == "4":
        load()
        print('\n')
        monton()
        kembali()
     elif f == "05" or f == "5":
          load()
          print('\n')
          os.system('python moonton.py')
          kembali()
     elif f == "00" or f == "0":
        exit()
     else:
        print ("\033[1;97m[\033[1;91m!\033[1;97m]Wrong Input\033[1;91m!!\033[00m")
        kembali() 

