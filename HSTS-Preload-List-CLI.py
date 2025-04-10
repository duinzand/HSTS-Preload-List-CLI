import requests
import json
import sys

class colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    ERROR = '\033[91m'
    ENDC = '\033[0m'

domain = str(sys.argv[1])

statusURL = 'https://hstspreload.org/api/v2/status?domain=' + domain

preloadableURL = 'https://hstspreload.org/api/v2/preloadable?domain=' + domain

statusJSON = requests.get(statusURL)

preloadableJSON = requests.get(preloadableURL)

statusDict = json.loads(statusJSON.text)

preloadableDict  = json.loads(preloadableJSON.text)

print(colors.BLUE+'[+] General Information:'+colors.ENDC)

print ('    '+'Name: \t\t'+str(statusDict["name"]))

if (str(statusDict["status"])=='preloaded'):
    print('    '+'Status: \t\t'+colors.GREEN+str(statusDict["status"])+colors.ENDC)
else:
    print('    '+'Status: \t\t'+colors.WARNING+str(statusDict["status"])+colors.ENDC)

print('    '+'Bulk: \t\t'+str(statusDict["bulk"]))

print('    '+'Preloaded Domain: \t'+str(statusDict["preloadedDomain"])+'\n')

print(colors.ERROR+'[+] Errors found: '+colors.ENDC+str(len(preloadableDict["errors"]))+'\n')

for error in preloadableDict["errors"]:
    print(colors.ERROR+'[-] '+colors.ENDC+'code: '+error['code'])
    print('    '+'summary: '+error['summary'])
    print('    '+'message: '+error['message']+'\n')

print(colors.WARNING+'[+] Warnings found: '+colors.ENDC+str(len(preloadableDict["warnings"]))+'\n')

for warning in preloadableDict["warnings"]:
    print(colors.WARNING+'[-] '+colors.ENDC+'code: '+warning['code'])
    print('    '+'summary: '+warning['summary'])
    print('    '+'message: '+warning['message']+'\n')
