#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
print(proto)
print(proto[1])
proto.append('dns')
print(proto)
proto2 = [22, 80, 443, 53]
proto.extend(proto2)
print(proto)
proto.append(proto2)
print(proto)
#remove all added items
proto.remove(proto2)
proto.remove(22)
proto.remove(53)
proto.remove(443)
proto.remove(80)
print(proto)
# reorder list as it appears when printed
proto.sort()
# add port numbers adjacent to protocol
proto.insert(1, 53)
proto.insert(3, 80)
proto.insert(5, 443)
proto.insert(7, 22)
print(proto)
