import pymem, utility, keyboard, os, time

process = pymem.Pymem('Trackmania.exe')

xbase = process.base_address + 0x01F37AC8
ybase = process.base_address + 0x01F37AB8
zbase = process.base_address + 0x01F37AB8

offsets_x = [0x158, 0x50, 0x1D0, 0x48, 0x180, 0xCBC, 0x2C]
offsets_y = [0x158, 0x50, 0x1D0, 0x48, 0x180, 0xCBC, 0x30]
offsets_z = [0x158, 0x50, 0x1C8, 0x1F8, 0x30, 0xD20, 0x34]

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
        yAddr = utility.FindDMAAddy(process.process_handle, ybase, offsets_x, 64)
        zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_x, 64)

        print("X: " + str(process.read_float(xAddr)))
        print("Y: " + str(process.read_float(yAddr)))
        print("Z: " + str(process.read_float(zAddr)))
        time.sleep(0.5)
        pass

    elif keyboard.is_pressed('shift + e'):
        x_value = float(input("X: "))
        y_value = float(input("Y: "))
        z_value = float(input("Z: "))

        GetPtrLoop(x_value, y_value, z_value)
