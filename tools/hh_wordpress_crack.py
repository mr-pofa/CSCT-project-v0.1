import os
print("[1] = wordpress_users-name_scaner")
print("[2] = wordpress_password_cracker")
ask_5 = input("\n\nprint the options number : ")
url_5 = input("print URL : ")
if ask_5 == "1" :
    os.system("wpscan --url "+url_5+" -e u")
if ask_5 == "2" :
    username_5 = input("print user name : ")
    wordlist_5 = input("print wordlist PATH name : ")
    os.system("wpscan --url "+url_5+" --passwords "+wordlist_5+" -U "+username_5+" ")