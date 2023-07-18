import pymem, utility, keyboard, os, time
from offsets import *

process = pymem.Pymem('Trackmania.exe')


def GetPtr(x, y, z):

    # find which address is the pointer pointing towards
    xAddr = utility.FindDMAAddy(process.process_handle, xbase, offsets_x, 64)
    yAddr = utility.FindDMAAddy(process.process_handle, ybase, offsets_y, 64)
    zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_z, 64)

    # Write the values to the ptr
    process.write_float(xAddr, x)
    process.write_float(yAddr, y)
    process.write_float(zAddr, z)

def GetPtrLoop(x, y, z):

    # find which address is the pointer pointing towards
    xAddr = utility.FindDMAAddy(process.process_handle, xbase, offsets_x, 64)
    yAddr = utility.FindDMAAddy(process.process_handle, ybase, offsets_y, 64)
    zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_z, 64)

    # Write the values to the ptr
    while True:
        process.write_float(xAddr, x)
        process.write_float(yAddr, y)
        process.write_float(zAddr, z)

        if keyboard.is_pressed('shift + e'):
            time.sleep(1.5)
            break

def GetPtrSpeed(xvel,zvel):

    # find which address is the pointer pointing towards
    xvelAddr = utility.FindDMAAddy(process.process_handle, xvelbase, offsets_xvel, 64)
    zvelAddr = utility.FindDMAAddy(process.process_handle, zvelbase, offsets_zvel, 64)


    xvel_current = process.read_float(xvelAddr)
    xvelnew = xvel + xvel_current
    zvel_current = process.read_float(zvelAddr)
    zvelnew = zvel + zvel_current

    # Write the values to the ptr
    process.write_float(xvelAddr, xvelnew)
    process.write_float(zvelAddr, zvelnew)



while True:
    if keyboard.is_pressed('shift + a'):

        keyboard.press_and_release('esc') # pause the game

        # Gathers the cords of where the user wants to teleport
        x_value = float(input("X: "))
        y_value = float(input("Y: "))
        z_value = float(input("Z: "))

        GetPtr(x_value, y_value, z_value) # Send the values to the GetPtr function

        os.system('cls') # cls the console

        pass

    elif keyboard.is_pressed('shift + y'):
        xAddr = utility.FindDMAAddy(process.process_handle, xbase, offsets_x, 64)
        yAddr = utility.FindDMAAddy(process.process_handle, ybase, offsets_y, 64)
        zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_z, 64)

        print("X: " + str(process.read_float(xAddr)))
        print("Y: " + str(process.read_float(yAddr)))
        print("Z: " + str(process.read_float(zAddr)))
        time.sleep(0.5)
        pass

    elif keyboard.is_pressed('shift + e'):
        x_value = float(677.55078125)#float(input("X: "))
        y_value = float(106.0137939453125)#float(input("Y: "))
        z_value = float(925.1013793945312)#float(input("Z: "))
        time.sleep(0.2)
        GetPtrLoop(x_value, y_value, z_value)

        os.system('cls')
        pass

    elif keyboard.is_pressed('shift'):

        xAddr = utility.FindDMAAddy(process.process_handle, xbase, offsets_x, 64)
        zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_z, 64)
        xvelAddr = utility.FindDMAAddy(process.process_handle, xvelbase, offsets_xvel, 64)
        zvelAddr = utility.FindDMAAddy(process.process_handle, zvelbase, offsets_zvel, 64)


        xcur = process.read_float(xAddr)
        zcur = process.read_float(zAddr)

        time.sleep(0.05)

        xnew = process.read_float(xAddr)
        znew = process.read_float(zAddr)

        xdif = xnew - xcur
        zdif = znew - zcur

        if abs(xdif) > abs(zdif):
            if xdif > 0:
                GetPtrSpeed(5,0)
                pass

            else:
                GetPtrSpeed(-5,0)
                pass
            pass

        elif abs(xdif) < abs(zdif):
            if zdif > 0:
                GetPtrSpeed(0,5)
                pass
            else:
                GetPtrSpeed(0,-5)
                pass
            pass
