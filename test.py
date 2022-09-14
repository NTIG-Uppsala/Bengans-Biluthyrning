import re

x = re.compile("Dag:\s+10-16")
y = "Dag:  i   10-16"

if (not x.match(y)):
    raise NameError("thing")