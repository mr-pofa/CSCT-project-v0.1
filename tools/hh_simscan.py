import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--my_text", help="Enter your text here")
args = parser.parse_args()
url = args.my_text
if args.my_text:
    os.system("gobuster dir -u "+url+" -w /usr/share/wordlists/dirb/common.txt -x tar,php,txt,cgi,old,dev")  
else : 
    url = input("print url : ")
    os.system("gobuster dir -u "+url+" -w /usr/share/wordlists/dirb/common.txt -x tar,php,txt,cgi,old,dev")  
