import requests,json

base_url="https://13.127.198.209:5000/services/api/v0/"
def get_token():
	
	data={
		"username":"admin",
		"password":"admin"
	}
	r = requests.post(base_url+"login",data=json.dumps(data),verify=False)
	
	#print(r.text)
	r=json.loads(r.text)
	#print(r["token"])
	return(r["token"])

def nodes_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+"nodes",headers=q,verify=False)
	return(r)


def query_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+"quaries",headers=q,verify=False)
	return(r)



def packs_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	r = requests.get(base_url+"packs",headers=q,verify=False)
	return(r)


def tags_post():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#return(q)
	data={  "host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253",
		"tags":"dhanya"
	}
	r = requests.post(base_url+"tags/add",data=json.dumps(data),headers=q,verify=False)
	return(r)

def carves_post():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253"
	}
	r = requests.post(base_url+"carves",data=data,headers=q,verify=False)
	return(r)

def hunt_post():
	q={}
	r=get_token()
	q["x-access-token"]=r
	#f_md = open("/home/asm/Dhanya/doc_com.md5","rb")
	data={
		
		"file" : open("/home/asm/Dhanya/sample.md5","r+"),
		"type" : "md5"
	}
	r = requests.post(base_url+"hunt-upload",files=data,data=data,headers=q,verify=False)
	#texts = json.loads(r.text)
	return (r)
def carves_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"host_identifier":"4C4C4544-004B-4D10-804E-CAC04F354253"
	}
	r = requests.get(base_url+"carves/download/OE5R2J1MZT",data=data,headers=q,verify=False)
	return(r)


def change_pass():
	q={}
	r=get_token()
	q["x-access-token"]=r
	data={
		"old_password":"admin",
		"new_password":"admin123",
		"confirm_new_password":"admin123"
	}
	r = requests.post(base_url+"changepw",data=data,headers=q,verify=False)
	return(r)
def log_out():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.post(base_url+"logout",headers=q,verify=False)
	return(r)

def api_keys_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"apikeys",headers=q,verify=False)
	return(r)

def certi():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"certificate",headers=q,verify=False)
	with open('/home/asm/sim.txt', 'wb') as f:
		f.write(r.content)
	with open('/home/asm/sim.txt','r') as f:
		lines = f.readlines()
	return(lines)
def cpt_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"cpt/ubuntu",headers=q,verify=False)
	with open('/home/asm/sim1.txt', 'wb') as f:
		f.write(r.content)
	with open('/home/asm/sim1.txt', 'r') as f:
		lines = f.readlines()
	return(lines)

def car_get():
	q={}
	r=get_token()
	q["x-access-token"]=r
	r = requests.get(base_url+"carves/download/XMB0UD1HGC",headers=q,verify=False)
	
	return(r)



n=nodes_get()
#print('nodes information', n.text)
r=query_get()
#print("query information",r.text)
p=packs_get()
#print("packs information",p.text)
t=tags_post()
#print("tags information" ,t.text)
c=carves_post()
#print("carves information" ,c.text)
h=hunt_post()
#print("Hunt information" ,h.text)
c=carves_get()
#print("carves information" ,c.text)
#passw=change_pass()
#print("password ",passw)

#l=log_out()
#print("logout",l)
A=api_keys_get()
A=json.loads(A.text)
#print("file",A)

cer=certi()
#for data in cer:
#	print(data)
cer=cpt_get()
#for data in cer:
#	print(data)
car=car_get()
print(car)
	

