#!/home/connor/anaconda3/bin/python3

"""
Purpose: Open resources for studying
"""

import webbrowser
import os

websites = {'Python Bootcamp' : "https://www.udemy.com/complete-python-bootcamp/",
            'Tomato Timer' : "https://tomato-timer.com/",
            'One Note' : "https://jabil-my.sharepoint.com/personal/connor_hamm_jabil_com/_layouts/15/WopiFrame.aspx?sourcedoc={395547fd-b437-4c4c-b385-752e4eafb2f2}&action=edit&wd=target%28Classes.one%7Ca49583cb-bba5-41a2-b5b2-66125086bafc%2F%5BUdemy%5D%20Python%20Bootcamp%7Cc47c1968-6e3c-495f-bcc2-73ac2ee93678%2F%29"
            }

def open_websites():
    for key, value in websites.items():
        print("Opening - {}".format(key))
        webbrowser.open(value)

def open_apps(): 
    os.system("nohup spotify &")
    os.system("nohup anaconda-navigator &")

def update_repo():
    update = input("Update Repository? (y/n)")
    if update == 'y':
        os.chdir('/home/connor/Classes/Complete-Python-3-Bootcamp')
        os.system("git fetch --all")
        os.system("git reset --hard origin/master")
        os.chdir('/home/')
    else:
        print("Update Aborted")

update_repo()
open_websites()
open_apps()

