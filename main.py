import pymem, utility, keyboard, os, time

process = pymem.Pymem('Trackmania.exe')

xbase = process.base_address + 0x01F7A890
ybase = process.base_address + 0x01F7A890
zbase = process.base_address + 0x01F7A890

offsets_x = [0x50, 0xD00, 0x368, 0x38, 0x0, 0x78]
offsets_y = [0x50, 0xD00, 0xA20, 0x28, 0x38, 0x0, 0x7C]
offsets_z = [0x50, 0x1C0, 0x20, 0x9D0, 0x38, 0x0, 0x80]

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
        yAddr = utility.FindDMAAddy(process.process_handle, ybase, offsets_y, 64)
        zAddr = utility.FindDMAAddy(process.process_handle, zbase, offsets_z, 64)

        print("X: " + str(process.read_float(xAddr)))
        print("Y: " + str(process.read_float(yAddr)))
        print("Z: " + str(process.read_float(zAddr)))
        time.sleep(0.5)
        pass

    elif keyboard.is_pressed('shift + e'):
        x_value = float(input("X: "))
        y_value = float(input("Y: "))
        z_value = float(input("Z: "))
        time.sleep(0.5)
        GetPtrLoop(x_value, y_value, z_value)

        os.system('cls')
        pass
