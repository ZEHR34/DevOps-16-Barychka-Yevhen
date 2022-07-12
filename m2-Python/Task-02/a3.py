config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlan = [int(i) for i in config.replace(",", " ").split() if i.isnumeric()]
print(vlan)
