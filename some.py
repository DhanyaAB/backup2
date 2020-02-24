from jenkinsapi.jenkins import Jenkins
import subprocess
import sys
import os
import requests
import json
import jenkins
ci_jenkins_url = "http://13.235.153.134:8080"
username = "admin"
password = "polylogyx123"
server_stag=jenkins.Jenkins(ci_jenkins_url, username=username, password=password)
dic={}
job={}
#myjob=server_stag.get_job('PolyLogyx_Sanity_Test_Suite')
#print(myjob)
#complete=myjob.get_last_good_build()

#print(complete)
#
#j=server_stag.get_job_info('PolyLogyx_Sanity_Test_Suite')

last_build_number = server_stag.get_job_info('PolyLogyx_Sanity_Test_Suite')
dic1 = {}
l=[]
j=0
for i in last_build_number['builds']:
	print(i['number'])
	#build_info =server_stag.get_build_info(job, i['number'])
	dic[j]=i['number']
	j=j+1
	l.append(dic)
print(l)

