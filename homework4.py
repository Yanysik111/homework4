immutable_var = (1, 'door', [1,3,5],133)
print(immutable_var)
mutable_list = ['window', 'door', 'wool', 'floor']
mutable_list.append('chair')
print(mutable_list)
mutable_list[2] = 'lamp'
print(mutable_list)
mutable_list.extend(['closed'])
print(mutable_list)
mutable_list.remove('closed')
print(mutable_list)