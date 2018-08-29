import sys
import os
import time
os.system('clear')
def los():
    print '''
====================================
put your wordlist location Down here
====================================
             '''

def banner():
    print '\x1b[0;31;1m'+'''
================================From FD=================================================
:'######:::'#######::'##::: ##:'##::::'##::::::::::'########::'########::'##::::'##:'########:'########:
'##... ##:'##.... ##: ###:: ##: ##:::: ##:::::::::: ##.... ##: ##.... ##: ##:::: ##:... ##..:: ##.....::
 ##:::..:: ##:::: ##: ####: ##: ##:::: ##:::::::::: ##:::: ##: ##:::: ##: ##:::: ##:::: ##:::: ##:::::::
 ##::::::: ##:::: ##: ## ## ##: ##:::: ##:'#######: ########:: ########:: ##:::: ##:::: ##:::: ######:::
 ##::::::: ##:::: ##: ##. ####:. ##:: ##::........: ##.... ##: ##.. ##::: ##:::: ##:::: ##:::: ##...::::
 ##::: ##: ##:::: ##: ##:. ###::. ## ##:::::::::::: ##:::: ##: ##::. ##:: ##:::: ##:::: ##:::: ##:::::::
. ######::. #######:: ##::. ##:::. ###::::::::::::: ########:: ##:::. ##:. #######::::: ##:::: ########:
:......::::.......:::..::::..:::::...::::::::::::::........:::..:::::..:::.......::::::..:::::........::
 https://github.com/FDX100/                                                     

================================From FD=================================================
    ''''\x1b[0m'

input = raw_input
banner()
print('insert .CAP file location')
ccap = input(":- ")
print('enter name for This File')
name = input(":-")
os.system("aircrack-ng "+ccap+" -J /root/"+name)
time.sleep(3)
os.system("clear")
print '\x1b[1;32;40m'+'''
==============
your File Converted to HCCAP.

now we need more ....

(1) To Start attack without Wordlist
(2) To Start Attack with Wordlist
(3) To Start Attack with Wordlist using Aircrack-ng
(4) To Start Attack with Custom Wordlist using Aircrack-ng
==============
'''
op2 = raw_input(' :- ')


if op2=="1":
      os.system("clear")     
      print'''
  #####  #######        #     #       ######                             
 #     # #     # #    # #     #       #     # #####  #    # ##### ###### 
 #       #     # ##   # #     #       #     # #    # #    #   #   #      
 #       #     # # #  # #     # ##### ######  #    # #    #   #   #####  
 #       #     # #  # #  #   #        #     # #####  #    #   #   #      
 #     # #     # #   ##   # #         #     # #   #  #    #   #   #      
  #####  ####### #    #    #          ######  #    #  ####    #   ######
This tool is made by FD .
The one with no Wordlist
         '''
      os.system("hccap2john /root/"+name+".hccap > /root/"+name+".txt") 
      os.system("xterm -hold -e john /root/"+name+".txt")  
if op2=="2":
       os.system("hccap2john /root/"+name+".hccap > /root/"+name+".txt")
       los()
       wordl=raw_input(" :- ")
       os.system("xterm -hold -e john /root/"+name+".txt "+"--wordlist "+wordl+" --format=wpapsk")
if op2=="3":
        los()
        wordls=raw_input(" :- ")
        os.system("clear")
        banner()
        os.system("xterm -hold -e aircrack-ng "+ccap+" -w "+wordls)
        

if op2=="4":
    os.system("gunzip /usr/share/wordlists/rockyou.txt.gz") 
    os.system("clear")
    banner()
    os.system("xterm -hold -e aircrack-ng "+ccap+" -w /usr/share/wordlists/rockyou.txt")
  
     




