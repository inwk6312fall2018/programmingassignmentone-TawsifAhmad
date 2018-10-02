""" THIS IS THE FUNCTION WHICH WILL RETURN A LIST OF INTERFACE NAME,nameif- VALUE"""
def int_and_int_name(file_name):
	file=open(file_name)
	list1=[]
	list2=[]	#INTERFACE 
	list3=[]	#INTERFACE NAME
	list4=[]	#TUPLE (interface,interface name)
	for line in file:
		line=line.strip()
		for word in line.split():
			list1.append(word)	# WILL MAKE A LIST OF ALL WORDS
	for i in range(len(list1)):
		if list1[i]=='interface':
			list2.append(list1[i+1])	#MAKE LIST OF INTERFACE
		elif list1[i]=='nameif' or (list1[i]=='no' and list1[i+1]=='nameif'):
			#MAKE LIST OF INTERFACE NAME AS WELL
			if list1[i]=='no' and list1[i+1]=='nameif':
				list3.append('no name')
			elif list1[i-1]!='no' and list1[i]=='nameif':
				list3.append(list1[i+1])
	for i in range(len(list2)):			#CREATE LIST OF TUPLE(INTERFACE,INTERFACE NAME)
		list4.append((list2[i],list3[i]))
	return list4

"""THIS FUNCTION CHANGE THE CONFIGURATION AND RETURN A DICTIONARY CONTAINING interfacce AS A KEY and NAMEIF,VLAN,IPADDRESS,SUBNET MASK
 LIST AS THE CORRESPONDING VALUES""""

def list_ifname_ip(file_name):
	file=open(file_name)
	list1=[]
	list2=[]	#INTERFACE LIST
	list3=[]	#NAME OF INTERFACE
	list4=[]	#VLAN ID
	lst5=[]	# IP ADDRESS
	lst6=[]	#SUBNETMASK
	lst7=[]	#LIST OF INTERFACE NAME,VLANID,IP ADDRESS,SUBNETMASK
	dict={}	#DICTIONARY
	for line in file:
		line=line.strip()
		for word in line.split():
			list1.append(word)
	for i in range(len(list1)):
		if list1[i]=='interface':
			list2.append(list1[i+1])  #MAKING LIST OF INTERFACE
		elif list1[i]=='nameif' or (list1[i]=='no' and list1[i+1]=='nameif'):
			#MAKING A LIST OF INTERFACE NAME
			if list1[i]=='no' and list1[i+1]=='nameif':
				list3.append('no name')
				list4.append('no vlan')	#FOR THE INTERFACE WHICH HAS NO NAME , NO IP ADDRESS AND NO SUBNETMASK
				lst5.append('no ip address')
				lst6.append('no netmask')
			elif list1[i-1]!='no' and list1[i]=='nameif':
				list3.append(list1[i+1])
				lst5.append(list1[i+6])
				lst6.append(list1[i+7])
				if list1[i-1]=='management-only':	# MANAGEMENT NETWORK CAS
					list4.append('no vlan')
				else:
					list4.append(list1[i-2]+list1[i-1])
	for i in range(len(list2)):
		lst7=[]
		lst7.append(list3[i])
		lst7.append(list4[i])
		lst7.append(lst5[i])
		lst7.append(lst6[i])
		dict[list2[i]]=lst7	#add list of nameif,ip,netMask as value in dict
	return dict


print('List contain tuple interface (interfacename,"nameif"- value) is:\n',int_and_int_name('running-config.cfg'))
print('dictionary that contains the "interfacename" as the key and "nameif,VLAN,IPaddress,NetMask" list as the value is :\n',list_ifname_ip('running-config.cfg'))
