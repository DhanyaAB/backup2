from jenkinsapi.jenkins import Jenkins
import jenkins
import json
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import PyMongo
from flask import jsonify
import datetime
import glob
import os
import subprocess,shlex
#import xmltodict

app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MONGO_DBNAME'] = 'test_mine4'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_mine4'
mongo = PyMongo(app)
curr = mongo.db.testing_data
username = 'admin'
password = 'polylogyx123'
url = 'http://13.235.153.134:8080'
jobname = ['PolyLogyx_Detection_Automation_Test_Suite', 'PolyLogyx_Sanity_Test_Suite', 'PolyLogyx_Node_Scale_Test']


def all_jobs(url=url, jobname=jobname, username=username, password=password):
	J = jenkins.Jenkins(url, username=username, password=password)
	print(len(jobname))
	for job in jobname:
		k = []
		out = curr.find({'job': job})
		l = [i for i in out]
		l1 = [i['output'] for i in l]
		if len(l1) == 0:
			print('if loop')
			last_build_number = J.get_job_info(job)
			dic1 = {}
			for i in last_build_number['builds']:
				build_info = J.get_build_info(job, i['number'])
				b = build_info['actions']
				dic1 = {}
				result = build_info['result']
				result1 = build_info['timestamp']
				
				path = "/home/asm/JenkinBuilds/"+job

				# define the access rights
				#access_rights = 0o755
				try:
					os.mkdir(path)
				except OSError:
    					print ("Creation of the directory %s failed" % path)
				try:
					
					os.system("sshpass -p 'asm123' scp -i /home/asm/ASM_polylogyx.pem -r ubuntu@13.235.153.134:/var/lib/jenkins/jobs/"+job+"/builds/"+str(i['number'])+"/robot-plugin/ /home/asm/JenkinBuilds/"+job+"/"+str(i['number'])+"/")
				except OSError:
    					print ("Creation of the directory %s failed" % path)
				else:
    					print ("Successfully created the directory %s" % path)
				
				da_ti = datetime.datetime.fromtimestamp(float(result1) / 1000.).strftime('%d-%m-%Y %I:%M:%S')
				for i in b:
					if 'buildsByBranchName' in i:
						dic = str(i['buildsByBranchName']['refs/remotes/origin/jenkins_test']['buildNumber'])
						dic1['buildNumber'] = dic
						break
				for i in b:
					if 'failCount' in i:
						dic1['failCount'] = i['failCount']
						dic1['totalCount'] = i['totalCount']
						dic1['passCount'] = i['totalCount'] - i['failCount']
				dic1['date'] = da_ti
				dic1['result'] = result
				k.append(dic1)
			curr.insert_one({'job': job, 'output': k})
		else:
			print('else loop')
			last_build_number = J.get_job_info(job)['lastCompletedBuild']['number']
			for i in l:
				print(i['output'][0]['buildNumber'])
				if int(last_build_number) > int(i['output'][0]['buildNumber']):
					print("hello")
					build_info = J.get_build_info(job, last_build_number)
					b = build_info['actions']
					dic2 = {}
					result = build_info['result']
					result1 = build_info['timestamp']
					da_ti = datetime.datetime.fromtimestamp(float(result1) / 1000.).strftime('%d-%m-%Y %I:%M:%S')
					for i in b:
						if 'buildsByBranchName' in i:
							dic = str(i['buildsByBranchName']['refs/remotes/origin/jenkins_test']['buildNumber'])
							dic2['buildNumber'] = dic
							break
					for i in b:
						if 'failCount' in i:
							dic2['failCount'] = i['failCount']
							dic2['totalCount'] = i['totalCount']
							dic2['passCount'] = i['totalCount'] - i['failCount']
					dic2['date'] = da_ti
					dic2['result'] = result

					curr.update_one({'job': job}, {'$push': {'output': {'$each': [dic2], '$position': 0}}})


all_jobs()
@app.route("/", methods=["GET"])
def job1(url=url, username=username, password=password):
	out=curr.find({'job':jobname[1]})
	dic={}
	for i in out:
		dic['job']=i['job']
		dic['output']=i['output']
		return jsonify(dic)
@app.route("/job2", methods=["GET"])
def job2(url=url, username=username, password=password):
	out=curr.find({'job':jobname[0]})
	dic={}
	for i in out:
		dic['job']=i['job']
		dic['output']=i['output']
		return jsonify(dic)
@app.route("/job3", methods=["GET"])
def job3():
	out=curr.find({'job':jobname[2]})
	dic={}
	for i in out:
		dic['job']=i['job']
		dic['output']=i['output']
		return jsonify(dic)

@app.route("/<jobname>/<build>", methods=["GET"])
def get_log(jobname,build):
	workingdirectory = '/home/asm/jenkinsBuilds/'+jobname+"/"+build+"/log.html"
	command = 'google-chrome {}'.format(workingdirectory)

	try:
    		process = subprocess.Popen(command, stdout=subprocess.PIPE,
			stderr=subprocess.PIPE, shell=True, cwd=workingdirectory)

    		stdout, stderr = process.communicate()

     		if stderr.decode('utf-8') == "":
         		print(stdout.decode('utf-8'))
     		else:
         		print(stderr.decode('utf-8'))
