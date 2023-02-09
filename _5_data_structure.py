from collections import OrderedDict

d = OrderedDict()
d['x'] = 100
d['y'] = 200
d['z'] = 300
d['l'] = 400

for k, v in d.items():
    print(k, v)

