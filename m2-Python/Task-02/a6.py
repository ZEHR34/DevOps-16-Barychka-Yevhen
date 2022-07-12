ospf_route = 'OSPF    10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

list_ospf = ospf_route.strip().split()
list_ospf.remove('via')
list2_ospf = [element.strip('[').strip(']') for element in list_ospf]
print (list2_ospf)

keys = ['Protocol', 'Prefix', 'AD/Metric', 'Next-Hop', 'Last update', 'Outbound Interface']

for i in range(len(keys)):
   print('{:<20} {}'.format(keys[i],list_ospf[i].strip(',')))