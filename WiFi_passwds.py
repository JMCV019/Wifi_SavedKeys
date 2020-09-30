#WiFi_passwds.py
#__JMCV__
import subprocess
opc=3
while opc!=0:
    #Clean screen
    subprocess.Popen("cls", shell=True).communicate()
    print(" /===================================================================================================\ ")
    print("|                                  Keys for saved network profiles                                    |")
    print("|                                              By_JMCV                                                |")
    print(" \===================================================================================================/ ")
    print("- Show all storaged keys ..................[1]")
    print("- Show key for one network in particular ..[2]")
    print("- Exit ....................................[0]")
    opc = int(input("\nOpcion escogida: "))
    
    #Show all
    if opc==1:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        #Clean screen
        subprocess.Popen("cls", shell=True).communicate()
        for i in sorted(profiles):
            try:
                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
                try:
                    print ("{:<30}|  {:<}".format(i, results[0]))
                except IndexError:
                    print ("{:<30}|  {:<}".format(i, ""))
            except subprocess.CalledProcessError:
                print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))
        input("\n\nPress <ENTER> to continue...")
        
    #Show a key
    elif opc==2:
        #Clean screen
        subprocess.Popen("cls", shell=True).communicate()
        print("Available networks:")
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
        profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
        for profile in sorted(profiles):
            print(profile)
        profile = str(input("\nNetwork profile: "))
        #Clean screen
        subprocess.Popen("cls", shell=True).communicate()
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print ("{:<30}|  {:<}".format(profile, results[0]))
            except IndexError:
                print ("{:<30}|  {:<}".format(profile, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(profile, "ENCODING ERROR"))
        input("\n\nPress <ENTER> to continue...")