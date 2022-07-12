IP = '192.168.3.1'
list_ip = IP.split('.')
ip_template = '''IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
print(ip_template.format(int(list_ip[0]), int(list_ip[1]), int(list_ip[2]), int(list_ip[3])))
