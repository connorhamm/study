#!/home/connor/anaconda3/bin/python3

"""
Purpose: Open resources for studying
"""

import webbrowser
import os

def update_repo(system):
    update = input("Update repo? (y/n)")
    pp = input("push or pull?")
    if update == 'y':
        if system == 'w':
            os.chdir('C:/Users/100042090/OneDrive - Jabil/Personal/MyCode/Complete-Python-3-Bootcamp')
            os.system("git " + pp)
        elif system == 'l':
            os.chdir('/home/connor/Personal/Classes/Complete-Python-3-Bootcamp')
            os.system("git " + pp)
        else:
            print("OS not support")

# update_repo()
system = input("(w)indows or (l)inux? ")
update_repo(system)

if system == 'w':
    # Open Websites
    webbrowser.open("https://www.udemy.com/complete-python-bootcamp/")
    webbrowser.open("https://tomato-timer.com/")

    os.system("jupyter notebook")

elif system == 'l':
    # Open Websites
    webbrowser.open("https://www.udemy.com/complete-python-bootcamp/")     
    webbrowser.open("https://tomato-timer.com/")
    webbrowser.open("https://jabil-my.sharepoint.com/personal/connor_hamm_jabil_com/_layouts/15/WopiFrame.aspx?sourcedoc={08cac105-607b-47dd-bf80-3c3b340083bf}&action=edit&wd=target%28Python%20Bootcamp.one%7Cefb8316c-cf80-435c-8542-3357a94efb69%2F8%5C%2F26%5C%2F2019%7C69ac5842-a14f-4771-a2b0-eab3ab2ad26c%2F%29")

    # Open Apps
    os.system("nohup spotify &")     
    os.system("jupyter notebook")

else:
    print("OS not supported")
