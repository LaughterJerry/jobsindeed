import json
from collections import OrderedDict

curfile = json.loads(open("keywords.json", "r").read())

od = list(OrderedDict(sorted(curfile.items(), key=lambda t: t[1], reverse=True)).items())

#thingus = dict(sorted(curfile.items(), reverse=True), key=lambda item: item[1])

print(od)

output = open("result.txt", "a")
for x in od:
	if x[1] > 20:
		output.write("%s: %d\n" % (x[0], x[1]))
	else:
		break
