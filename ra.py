import json
data=b'\r\nRule Name: test_rule\r\n----------------------------------------------------------------------\r\nDescription: \r\nEnabled: Yes\r\nDirection: In\r\nProfiles: Domain,Private,Public\r\nGrouping: test\r\nLocalIP: Any\r\nRemoteIP: Any\r\nProtocol: Any\r\nEdge traversal: No\r\nProgram: C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\r\nInterfaceTypes: Any\r\nSecurity: NotRequired\r\nRule source: Local Setting\r\nAction: Block\r\nOk.\r\n\r\n'
data1=json.loads(data.decode('utf-8'))
#data.decode()
#line = data1.replace('\r', '')
#data1=str(line.split('\n'))
print(data1)
#data1=json.loads(str(data1))
data1=data1[4:-4]
	
print(data1)
	

