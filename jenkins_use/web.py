import glob
from bs4 import BeautifulSoup
from collections import OrderedDict
from pprint import pprint
from html_table_extractor.extractor import Extractor
import os
#import lxml
#import lxml.html
import json
jobname = 'PolyLogyx_Detection_Automation_Test_Suite'
path="/home/asm/Jenkin Builds"+jobname
os.mkdir(path)

os.system("sudo scp -i /home/asm/ASM_polylogyx.pem -r  ubuntu@13.235.153.134:/var/lib/jenkins/jobs/PolyLogyx_Detection_Automation_Test_Suite/builds/29/robot-plugin/ /home/asm/JenkinBuilds"+jobname)

#list_of_files = glob.glob('/home/asm/'+ 'log.html')
#data = max(list_of_files, key=os.path.getctime)
#html = open('/home/asm/log.html').read()
#soup = BeautifulSoup(html,'html.parser')
#print(soup)
#print(soup.prettify())
#g = open('soup.xml', 'w')
#things = soup.find_all('script', {'type':"text/javascript"})[14].string
#things = soup.find_all("/html/body/table/tbody/tr[2]/td")
#print("things")
#thing=things.split('=')
#t=thing[1]
#st= str(t)[1:-2] 
#print(type(st))
#j=json.loads(st)
#print(j[0][0].keys())
