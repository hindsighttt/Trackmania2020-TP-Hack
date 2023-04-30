import pymem, utility, keyboard, os, time

process = pymem.Pymem('Trackmania.exe')

xbase = process.base_address + 0x01F2E2C8
ybase = process.base_address + 0x01F5E028
zbase = process.base_address + 0x01F2E2D8

def GetPtr(x, y, z):

    # find which address is the pointer pointing towards
    xAddr = utility.FindDMAAddy(process.process_handle, xbase, [0x158, 0x58, 0xC8, 0x28, 0x38, 0x0, 0x80], 64)
    yAddr = utility.FindDMAAddy(process.process_handle, ybase, [0x48, 0xD00, 0x908, 0x1E8, 0x38, 0, 0x78], 64)
    zAddr = utility.FindDMAAddy(process.process_handle, zbase, [0x158, 0x58, 0x9D0, 0x38, 0x0, 0x7C], 64)

    # Write the values to the ptr
    process.write_float(xAddr, x)
    process.write_float(yAddr, y)
    process.write_float(zAddr, z)
#    print(xAddr)
#    print(yAddr)
#    print(zAddr)

while True:
    if keyboard.is_pressed('shift + t'):

        keyboard.press_and_release('esc') # pause the game

        # Gathers the cords of where the user wants to teleport
        x_value = float(input("X: "))
        y_value = float(input("Y: "))
        z_value = float(input("Z: "))

        GetPtr(x_value, y_value, z_value) # Send the values to the GetPtr function

        os.system('cls') # cls the console

        pass

    elif keyboard.is_pressed('shift + y'):
        xAddr = utility.FindDMAAddy(process.process_handle, xbase, [0x158, 0x58, 0xC8, 0x28, 0x38, 0x0, 0x80], 64)
        yAddr = utility.FindDMAAddy(process.process_handle, ybase, [0x48, 0xD00, 0x908, 0x1E8, 0x38, 0, 0x78], 64)
        zAddr = utility.FindDMAAddy(process.process_handle, zbase, [0x158, 0x58, 0x9D0, 0x38, 0x0, 0x7C], 64)

        print("X: " + str(process.read_float(xAddr)))
        print("Y: " + str(process.read_float(yAddr)))
        print("Z: " + str(process.read_float(zAddr)))
        time.sleep(0.5)
        pass