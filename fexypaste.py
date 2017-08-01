#-*- coding: utf-8 -*-
__author__="Fexyler"
import urllib2
import urllib
import sys

print """

| __| __\ \/ /\ \ / / _ \/_\ / __|_   _| __|    /  \       /  \      / |
| _|| _| >  <  \ V /|  _/ _ \\__ \ | | | _|     | () |  _  | () |  _  | |
|_| |___/_/\_\  |_| |_|/_/ \_\___/ |_| |___|    \__/  (_)  \__/  (_) |_|

 """.strip()

URL = "http://dpaste.com"
files=sys.argv[1:]
if len(files)==0:
    print "Usage = 'dpaster.py file1.txt file2.txt.'"
    sys.exit()
    

for  dosya in files:
    try:
        content=open(dosya,'r').read()
    except Exception as err:
        print "|>| Error:",err
        continue
    

data = {'content': content}
data = urllib.urlencode(data)

request = urllib2.Request(URL, data=data)

resp = urllib2.urlopen(request).url + ".txt"

print resp
print "İşlem tamamdır, iyi günler."
