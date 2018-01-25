s = b'\x99\xca\xff\xff\x99'
s2 = b'\xff'
print(int.from_bytes(s2,byteorder='big'))