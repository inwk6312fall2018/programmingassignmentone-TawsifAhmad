

def access_list(file_name):
	file=open(file_name)
	list=[]
	for line in file:
		line=line.strip()
		for i in line.split():	#if line contains global-access or fw-management it will add that line to list
			if i=='global_access' or i=='fw-management_access_in':
				list.append(line)
	return list
print(access_list('running-config.cfg')		
