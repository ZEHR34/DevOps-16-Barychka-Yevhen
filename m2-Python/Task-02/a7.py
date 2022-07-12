MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(':', '')
print(str(bin(int(MAC, 16)))[2:])
