#!/home/connor/anaconda3/bin/python3

"""
Purpose: Open resources for studying
"""

import webbrowser
import os

def open_websites(website):
        webbrowser.open(website)

def open_apps(): 
    os.system("nohup spotify &")
    os.system("nohup anaconda-navigator &")

def update_repo(system):
    update = input("Update Repository? (y/n)")
    if update == 'y':
        if system == 'w':
            os.chdir('C:/Users/100042090/OneDrive - Jabil/Personal/MyCode/Complete-Python-3-Bootcamp')
            os.system("git push")
        elif system == 'l':
            os.chdir('/home/connor/Classes/Complete-Python-3-Bootcamp')
            os.system("git push")
        else:
            print("OS not support")

# update_repo()
system = input("(w)indows or (l)inux? ")
update_repo(system)

if system == 'w':
    # Open Websites
    webbrowser.open("https://www.udemy.com/complete-python-bootcamp/")
    webbrowser.open("https://tomato-timer.com/")

elif system == 'l':
    # Open Websites
    webbrowser.open("https://www.udemy.com/complete-python-bootcamp/")     
    webbrowser.open("https://tomato-timer.com/")
    webbrowser.open("https://jabil-my.sharepoint.com/personal/connor_hamm_jabil_com/_layouts/15/WopiFrame.aspx?sourcedoc={395547fd-b437-4c4c-b385-752e4eafb2f2}&action=edit&wd=target%28Classes.one%7Ca49583cb-bba5-41a2-b5b2-66125086bafc%2F%5BUdemy%5D%20Python%20Bootcamp%7Cc47c1968-6e3c-495f-bcc2-73ac2ee93678%2F%29")

    # Open Apps
    os.system("nohup spotify &")     
    os.system("nohup anaconda-navigator &")

else:
    print("OS not supported")
