try:
    import os, pyfiglet
except ImportError as error:
    os.system("pip install pyfiglet")
    import os, pyfiglet


def main():
    banner = pyfiglet.figlet_format('POCO F1 Tools by Karma')
    print(banner)
    print('''
    1)  Check device [ADB/FASTBOOT]         6)  Flash recovery [FASTBOOT]
    2)  Push files [ADB]                    7)  Reboot to system [FASTBOOT]
    3)  Reboot [ADB]                        8)  Exit
    4)  Boot TWRP recovery [FASTBOOT]                                
    5)  Backup Stock recovery [#ADB]      
    ''')

    while True:
        choice = int(input('Enter your choice: '))

        if choice == 1:  # Check device
            print("")
            print('''    [1] ADB    [2] FASTBOOT            ''')
            print("")
            chk_dev_choice = int(input("Enter your option: "))
            if chk_dev_choice == 1:
                os.system("platform-tools\\adb.exe devices")
            if chk_dev_choice == 2:
                os.system("platform-tools\\fastboot.exe devices")
            print("")

        if choice == 2:  # Push files
            print("")
            print("Pushing DisableForceEncryption_Treble.zip [/sdcard/TWRP/] (1/3)")
            os.system(
                "platform-tools\\adb.exe push ./latest/DisableForceEncryption_Treble.zip /sdcard/TWRP/DisableForceEncryption_Treble.zip")
            print("")
            print("Pushing Magisk.zip [/sdcard/TWRP/] (2/3)")
            os.system("platform-tools\\adb.exe push ./latest/Magisk.zip /sdcard/TWRP/Magisk.zip")
            print("")
            print("Pushing safetynet-fix-v1.1.0.zip [/sdcard/TWRP/] (3/3)")
            os.system(
                "platform-tools\\adb.exe push ./latest/safetynet-fix-v1.1.0.zip /sdcard/TWRP/safetynet-fix-v1.1.0.zip")
            print("")

        if choice == 3:  # Reboot
            print("")
            print('''    [1] RECOVERY    [2] FASTBOOT            ''')
            print("")
            rbt_choice = int(input("Enter your option: "))
            print("")
            if rbt_choice == 1:
                print("Rebooting to recovery...")
                os.system("platform-tools\\adb.exe reboot recovery")
            if rbt_choice == 2:
                print("Rebooting to fastboot...")
                os.system("platform-tools\\adb.exe reboot fastboot")
            print("")

        if choice == 4:  # Boot TWRP recovery
            print("")
            print("Booting latest/twrp_recovery.img...")
            os.system("platform-tools\\fastboot.exe boot ./latest/twrp_recovery.img")
            print("")

        if choice == 5:  # Backup Stock recovery
            print("")
            print("Warning:- TWRP recovery required in boot mode or ADB Root required!")
            print("")
            confirmation = str(input('Are you sure you want to continue? (y/n): '))
            if confirmation == 'y':
                print("Creating stock recovery...")
                os.system("platform-tools\\adb.exe shell dd if=/dev/block/sda19 of=/sdcard/TWRP/stock_recovery.img")
                print("")
                print("Pulling stock recovery...")
                os.system("platform-tools\\adb.exe pull /sdcard/TWRP/stock_recovery.img backup/")
                print("")
            elif confirmation == 'n':
                pass
            print("")

        if choice == 6:
            print("")
            print("Warning:- Current recovery will be removed from device!")
            print("")
            print('''    [1] TWRP    [2] STOCK            ''')
            print("")
            recovery_choice = int(input("Enter your option: "))
            print("")
            if recovery_choice == 1:
                confirmation = str(input('Are you sure you want to flash twrp_recovery.img? (y/n): '))
                if confirmation == 'y':
                    print("Flashing twrp_recovery.img...")
                    os.system("platform-tools\\fastboot.exe flash recovery ./latest/twrp_recovery.img")
                elif confirmation == 'n':
                    pass
            elif recovery_choice == 2:
                print("*Notice*:- Stock recovery required in backup folder!")
                print("")
                confirmation = input('Are you sure you want to flash stock_recovery.img? (y/n): ')
                if confirmation == 'y':
                    print("Flashing stock_recovery.img...")
                    os.system("platform-tools\\fastboot.exe flash recovery ./backup/stock_recovery.img")
                elif confirmation == 'n':
                    pass
            print("")

        if choice == 7:
            print("Rebooting to system...")
            os.system("platform-tools\\fastboot.exe continue")

        if choice == 8:
            confirmation = input('Are you sure you want exit? (y/n): ')
            if confirmation == 'y':
                os.system("platform-tools\\adb.exe kill-server")
                break
            elif confirmation == 'n':
                pass


if __name__ == '__main__':
    main()
