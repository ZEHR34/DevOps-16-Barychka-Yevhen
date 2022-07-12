command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

command1 = [int(i) for i in command1.replace(",", " ").split() if i.isnumeric()]
command2 = [int(i) for i in command2.replace(",", " ").split() if i.isnumeric()]

command1 = set(command1)
command2 = set(command2)

vlan = list(command1 & command2)
print(vlan)
