END = "\033[0m"
LIGHT_CYAN = "\033[1;36m"
import os
os.system("chmod +x tools/* ; chmod +x CSCT ; mv tools /home/kali/Documents ; mv CSCT /bin")
os.system("chmod +x chip ; mv chip /bin;rm *")
print(LIGHT_CYAN+"done"+END)