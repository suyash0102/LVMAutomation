import os

os.system("tput setaf 3")
os.system('figlet WELCOME TO LVM AUTOMATION USING PYTHON')

os.system("tput setaf 7")
print("\t \t \t \t --------------------")

print('\n\n\n')
print("\t \t Let's see the devices attached to this system.")
print('\n\n\n')

os.system('fdisk -l')
print('\n\n\n')

noOfDevices = int(input("Kindly enter the no. of devices you want to create: "))

while True :

        print('''
        1.  Create Physical Volumes(PV)
        2.  Show Physical Volumes
        3.  Delete Physical Volume
        4.  Create Volume Group (VG)
        5.  Show Volume Groups (VGs)
        6.  Delete Volume Group
        7.  Create Logical Volume (LV)
        8.  Delete Logical Volume
        9.  Format Logical Volume
        10. Mount Logical Volume
	11. Unmount Logical Volume
        12. Increase the size of Logical Volume
        13. Format the Modified Volume 
        14. To exit
        ''')

        user_input = int(input("Kindly choose an option from below Choices: "))

        if user_input == 1:
            for i in range(noOfDevices):
                device_name = input("Kindly enter the name of device: ")
                os.system("pvcreate"+ ' ' + device_name)

        elif user_input == 2:
            os.system("pvdisplay")

        elif user_input == 3:
            deviceName = input("Kindly enter the name of device that you want to delete: ")
            os.system("pvremove {}".format(deviceName))

        elif user_input == 4:
            vgName = input("Kindly enter the name of Volume Group: ")
            device_names=[]
            for i in range(noOfDevices):
                device_name = input ("Kindly enter the name of device: ")
                device_names.append(device_name)
            os.system("vgcreate {}".format(vgName) + ' ' + ' '.join(device_names))

        elif user_input == 5:
            os.system("vgdisplay")

        elif user_input == 6:
            vgName = input("Kindly enter the name of Volume Group that you want to delete: ")
            os.system("vgremove {}".format(vgName))

        elif user_input == 7:
            lvSize = int(input("Kindly enter the size of volume you want to create in GB: "))
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")

            os.system("lvcreate --size {}G --name {} {}".format(lvSize,lvName,vgName))
        elif user_input == 8:
            lvName = input("Kindly enter the name of Logical volume that you want to delete: ")
            vgName = input("Kindly enter the name of Volume Group in which LV resides: ")
            os.system("lvremove /dev/{}/{}".format(vgName,lvName))
            
        elif user_input == 9:
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")
            os.system("mkfs.ext4 /dev/{}/{}".format(vgName,lvName))
            
        elif user_input ==10:
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")
            dirName = input("Kindly enter the name of the Directory where you want to mount the volume: ")
            os.system("mkdir /{}".format(dirName))
            os.system("mount /dev/{}/{} /{}".format(vgName,lvName,dirName))
            os.system("df -h")
            print("Yay! Volume has been mounted successfully.")

        elif user_input ==11:
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")
            os.system("umount /dev/{}/{}".format(vgName,lvName))
            os.system("df -h")
            print("Yay! Volume has been unmounted successfully.")

        elif user_input == 12:
            changeInSize = int(input("Kindly enter the size by which you want to increase the volume: "))
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")
            os.system("lvextend --size +{} /dev/{}/{}".format(changeInSize,vgName,lvName))
                
        elif user_input == 13:
            lvName = input("Kindly enter a name for the Logical Volume:")
            vgName = input("Kindly enter the name of Volume Group: ")
            os.system("resize2fs /dev/{}/{}".format(vgName,lvName))
            os.system("df -h")
            print("Yay! Size of your LVM has been modified successfully.")

        elif user_input == 14:
            exit()
