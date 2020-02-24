import sys
import jenkins
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import PyMongo
from flask import Flask, request, jsonify
from jenkinsapi.jenkins import Jenkins
import datetime
app = Flask(__name__)
api = Api(app)
CORS(app)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['MONGO_DBNAME'] = 'test_mine3'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/test_mine3'

mongo = PyMongo(app)
curr = mongo.db.testlog1
'''jobname = ['PolyLogyx_Detection_Automation_Test_Suite', 'PolyLogyx_Sanity_Test_Suite', 'PolyLogyx_Node_Scale_Test']
@app.route("/", methods=["GET"])
def job1():
	out=curr.find({'job':jobname[1]})
	dic={}
	for i in out:

		dic['job']=i['job']
		dic['output']=i['output']
		for j in i['output']:
			#print(j['file'])
			res = str(j['file'])[1:-1]
			dic['file']=res
		
		return jsonify(dic)
 @app.route("/job2", methods=["GET"])
 def job2():
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
	workingdirectory = '/home/asm/JenkinBuilds/'+jobname+"/"+build+"/log.html"

	command = 'google-chrome {}'.format(workingdirectory)
	process = subprocess.Popen(command,  shell=True)
	print(jobname,build)
	return ("file:/"+workingdirectory)'''

@app.route("/jobs", methods=["GET"])
def get_log1():
	ci_jenkins_url = "http://13.235.153.134:8080"
	username = "admin"
	password = "polylogyx123"
	server_stag=Jenkins(ci_jenkins_url,username,password)
	views = server_stag.views.keys()
	l=[]
	j=0
	for i in views:
		dic={}
		dic[j]=i
		j=j+1
		l.append(dic)
	return jsonify(l)

@app.route("/jobs/<view>", methods=["GET"])
def get_log(view):
	ci_jenkins_url = "http://13.235.153.134:8080"
	username = "admin"
	password = "polylogyx123"
	server_stag=Jenkins(ci_jenkins_url,username,password)
	#view=jobname
	#dic={}
	l=[]
	jobs=list(server_stag.views.__getitem__(view).keys())
	print(jobs)
	j=0
	for i in jobs:
		dic={}
		dic[j]=i
		j=j+1
		l.append(dic)
	print(l)
	return jsonify(l)

'''@app.route("/jobs/build/<jobname>", methods=["GET"])
def get_log2():
	ci_jenkins_url = "http://13.235.153.134:8080"
	username = "admin"
	password = "polylogyx123"
	server_stag=Jenkins(ci_jenkins_url,username,password)
	jobsserver_stag.get_downstream_job_names()
	job=jobname
	build_job(name, parameters=None, token=None)
	#jobs[job]=list(server_stag.views.__getitem__(job).keys())
	print(jobs)
	return jsonify(jobs)'''
@app.route("/jobs/buildnumber/<jobname>", methods=["GET"])
def get_log2(jobname):
	ci_jenkins_url = "http://13.235.153.134:8080"
	username = "admin"
	password = "polylogyx123"
	server_stag=jenkins.Jenkins(ci_jenkins_url, username=username, password=password)
	last_build_number = server_stag.get_job_info(jobname)
	dic1 = {}
	k=[]
	for i in last_build_number['builds']:
		print(type(i['number']))
		build_info = server_stag.get_build_info(jobname, i['number'])
		b = build_info['actions']
		dic1 = {}
		result = build_info['result']
		result12 = build_info['timestamp']
		result2 = build_info['duration']
		result1 = datetime.datetime.fromtimestamp(float(result12) / 1000.).strftime('%I:%M:%S')
		
		da_ti = datetime.datetime.fromtimestamp(float(result12) / 1000.).strftime('%d-%m-%Y %I:%M:%S')
		if result != 'ABORTED':
				dic1['buildnumber'] = i['number']
				for i in b:
					if 'failCount' in i:
						dic1['failCount'] = i['failCount']
						dic1['totalCount'] = i['totalCount']
						dic1['passCount'] = i['totalCount'] - i['failCount']
				dic1['date'] = da_ti
				dic1['result'] = result
				
				dic1['duration']=result12
				dic1['job']=jobname
				k.append(dic1)
	return jsonify(k)
def form_date(duration):
	seconds=(duration/1000)%60
	minutes=(duration/(1000*60))%60
	hours=(duration/(1000*60*60))%24
	
	t3=str(int(hours))+':'+str(int(minutes))+':'+str(int(seconds))
	return(t3)

@app.route("/jobs/buildnumber/<jobname>/<buildnumber>", methods=["GET"])
def get_log3(jobname,buildnumber):
	ci_jenkins_url = "http://13.235.153.134:8080"
	username = "admin"
	password = "polylogyx123"
	server_stag=jenkins.Jenkins(ci_jenkins_url, username=username, password=password)
	last_build_number = server_stag.get_job_info(jobname)
	dic1 = {}
	k=[]
	
	build_info = server_stag.get_build_info(jobname, int(buildnumber))
	b = build_info['actions']
	dic1 = {}
	result = build_info['result']
	result12 = build_info['timestamp']
	result2 = build_info['duration']
	result2=form_date(result2)
	result1 = datetime.datetime.fromtimestamp(float(result12) / 1000.).strftime('%I:%M:%S')
		
	da_ti = datetime.datetime.fromtimestamp(float(result12) / 1000.).strftime('%d-%m-%Y %I:%M:%S')
	if result != 'ABORTED':
			for i in b:
				if 'failCount' in i:
					dic1['failCount'] = i['failCount']
					dic1['totalCount'] = i['totalCount']
					dic1['passCount'] = i['totalCount'] - i['failCount']
			dic1['date'] = da_ti
			dic1['result'] = result
				
			dic1['duration']=result2
			dic1['job']=jobname
			k.append(dic1)
	return jsonify(k)

if __name__ == '__main__':
	app.run(host='127.0.0.1',port=5001,debug=True)
