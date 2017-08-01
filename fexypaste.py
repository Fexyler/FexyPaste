#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

__author__="Fexyler"

import sys
import urllib
import urllib2

print """
 _____ _______  ____   ______   _    ____ _____ _____    ___   ___   _ 
|  ___| ____\ \/ /\ \ / /  _ \ / \  / ___|_   _| ____|  / _ \ / _ \ / |
| |_  |  _|  \  /  \ V /| |_) / _ \ \___ \ | | |  _|   | | | | | | || |
|  _| | |___ /  \   | | |  __/ ___ \ ___) || | | |___  | |_| | |_| || |
|_|   |_____/_/\_\  |_| |_| /_/   \_\____/ |_| |_____|  \___(_)___(_)_|

"""

URL = "http://dpaste.com"
files = sys.argv[1:]

if len(files)==0:
    print "Usage = 'dpaster.py file1.txt file2.txt.'"
    sys.exit()

for dosya in files:
    try:
        content = open(dosya,'r').read()
    except Exception as err:
        print "|>| Error:",err
        continue
    

    data = {'content': content}
    data = urllib.urlencode(data)

    request = urllib2.Request(URL, data=data)

    resp = urllib2.urlopen(request).url + ".txt"

    print dosya, "\t: ", resp

    print "\nİşlem tamamdır, iyi günler."
