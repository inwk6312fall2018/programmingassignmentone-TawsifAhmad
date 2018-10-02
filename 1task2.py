"""Write a Python function to create a new configuration file that 
replaces all (sub-)interface IP addresses that start with '172.' and '192." to "10." 
and also change the security-level to "10" . """

def change_ip(file_name):
	file=open(file_name)
	list=[]
	list2=[]	#contains all ip addresses
	list3=[]	#contains list of elements in ip add
	list4=[]	#list of updated ip address  
	for line in file:
		line=line.strip()
		for word in line.split():
			list.append(word)
	for i in range(len(list)):
		if list[i-1]!='no' and list[i]=='ip' and list[i+1]=='address':
			list2.append(list[i+2])	#add all ip add in list2
	for i in list2:
		list3.append(i.split('.'))	#list of elements in ip
	for i in list3:		#remove '172' or '192' and update with '10'
		del i[0]	#del first element
		i.insert(0,'10')	#insert '10' at first location
		list4.append('.'.join(i))	#add upated ip add in list
	return list4

print(change_ip('running-config.txt'))
