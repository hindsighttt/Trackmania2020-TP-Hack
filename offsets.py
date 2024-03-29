import pymem


process = pymem.Pymem('Trackmania.exe')

#base address resolving
xbase = process.base_address + 0x01FD4FA0
ybase = process.base_address + 0x01F4A380
zbase = process.base_address + 0x01F7B850

xvelbase = process.base_address + 0x01F7B850
zvelbase = process.base_address + 0x01F4A380

#address offsets
offsets_x = [0x30, 0x158, 0x58, 0x9D0, 0x38, 0x0, 0x78]
offsets_y = [0x158, 0x58, 0xA78, 0xF0, 0x38, 0x0, 0x7C]
offsets_z = [0x50, 0x130, 0x0, 0x9D0, 0x38, 0x0, 0x80]

offsets_xvel = [0x50, 0x130, 0x0, 0x78, 0x38, 0x0, 0x84]
offsets_zvel = [0x158, 0x50, 0xD00, 0x78, 0x38, 0x0, 0x8C]
