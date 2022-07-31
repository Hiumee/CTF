import zlib

crcs = {}

for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_{}":
    crcs[zlib.crc32(bytes(character, encoding="utf-8"))] = character

for i in range(22):
    data = open(f'{i}.zip', 'rb').read()
    crc = int.from_bytes(data[14:18], byteorder='little')
    print(crcs[crc], end="")