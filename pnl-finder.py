#! /usr/bin/env python
#find pnl for a given essid from a kismet nettxt

import sys

try:
        f=sys.argv[1]
        file = open(f,'r')
        results = file.read().split("Network ")
        results.pop(0)
except:
        print "\nProvide Kismet .nettxt file as an argument\n"
        sys.exit()

dict = {}
searchresults = []

searchterm = raw_input('\nEnter the case-sensitive ESSID: ')

for item in results:
        ssids = []

        try:
                a= item.split("Client") #split based on client number
                b= a[1].split("\n")
                c= b[0].split(" ")
                clientMac= c[3] #mac of client probing for ssid
                for i in b:
                        if "SSID       :" in i and "loaked" not in i: #not a hidden net
                                ssid= i.split(":")[1][1:]
                                ssids.append(ssid)
                dict[clientMac] = ssids
        except Exception,e:
                #print str(e)
                pass

for mac in dict:
        if searchterm in dict[mac]:
                searchresults.append(mac)
print '\nThe following MAC addresses probed for ' + searchterm + ':'
print(", ".join(searchresults))
print '\nThese MAC addresses who probed for ' +searchterm+ ' also probed for:'
l=set()
for mac in searchresults:
        if len(dict[mac]) >1:
                print mac + ' :: ' + str(dict[mac])
                a =(dict[mac])
                for i in a:
                        l.add(i)
#print l #[:4:-2]
print "\nProbe list: " + ", ".join(sorted(l))
