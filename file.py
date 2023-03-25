import os, platform

try:

        import requests

except:

        os.system('pip2 install requests')



import requests

bit = platform.architecture()[0]

if bit == "64bit":

        from ultra64 import main_menu

        main_menu()



elif bit == "32bit":

        from ultra import main_menu


        main_menu()
