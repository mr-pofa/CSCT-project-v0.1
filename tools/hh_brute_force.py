import os


if True :
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
# http-post-form
# method
ip_target = input(LIGHT_CYAN+"target ip : "+END)
url_path = input(LIGHT_CYAN+"url path : "+END)
username_variable = input(LIGHT_CYAN+"username variable : "+END)
password_variable = input(LIGHT_CYAN+"password variable : "+END)
Cookie = input(LIGHT_CYAN+"Cookie : "+END)
bad_login = input(LIGHT_CYAN+"bad login text : "+END)
wordlist = input(LIGHT_CYAN+"wordlist : "+END)
method = input(LIGHT_CYAN+"method GET or POST : "+END)
if method.lower() != "get" and method.lower() != "post" :
     print(LIGHT_RED+"eror"+END)
     exit()
if method.lower() == "get":
     method = "http-get-form"
if method.lower() == "post":
     method = "http-post-form"
user_name_ask = input(LIGHT_CYAN+"you have user name Y/n : "+END)
if user_name_ask.lower() == "y" :
     user_name = input(LIGHT_CYAN+"user name : "+END)
     os.system('hydra '+ip_target+' -l '+user_name+' -P '+wordlist+' '+method+' "'+url_path+':'+username_variable+'=^USER^&'+password_variable+'=^PASS^&Login=Login:'+bad_login+':H='+Cookie+'" ')
if user_name_ask.lower() == "n" :
     users_name_wordlist = input(LIGHT_CYAN+"users name path : "+END)
     os.system('hydra '+ip_target+' -L '+users_name_wordlist+' -P '+wordlist+' '+method+' "'+url_path+':'+username_variable+'=^USER^&'+password_variable+'=^PASS^&Login=Login:'+bad_login+':H='+Cookie+'" ')


