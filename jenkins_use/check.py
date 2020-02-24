#import os
#jobname = ['PolyLogyx_Detection_Automation_Test_Suite', 'PolyLogyx_Sanity_Test_Suite', 'PolyLogyx_Node_Scale_Test']
# define the name of the directory to be created
#l=[10,20]
#for job in jobname:
#	path = "/home/asm/JenkinBuilds/"+job+"/"+str(l[1])
#
	# define the access rights
	#access_rights = 0o755
#
#	try:
#   		os.mkdir(path)
#	except OSError:
#    		print ("Creation of the directory %s failed" % path)
#	else:
#   	 	print ("Successfully created the directory %s" % path)
#	
#	os.system("sshpass -p 'asm123' scp -i /home/asm/ASM_polylogyx.pem -pr ubuntu@13.235.153.134:~/var/lib/jenkins/jobs/"+
#		job+"/builds/"+str(l[1])+"/robot-plugin/ /home/asm/JenkinBuilds/PolyLogyx_Detection_Automation_Test_Suite/")

from bs4 import BeautifulSoup
import time
from selenium import webdriver

url = "http://13.235.153.134:8080/job/PolyLogyx_Sanity_Test_Suite/157/robot/report/report.html"
browser = webdriver.Chrome("/home/asm/jenkins_use/chromedriver_linux64/chromedriver_linux64 (1)/chromedriver")

browser.get(url,username='admin',password='polylogyx123')
time.sleep(3)
html = browser.page_source
soup = BeautifulSoup(html, "lxml")

print(len(soup.find_all("table")))
print(soup.find("table", {"id": "expanded_standings"}))

browser.close()
browser.quit()
