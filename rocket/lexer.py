from subprocess import call

s=open("synt.lx")
syn=s.read()
s.close()
syn=syn.split("\n")
idc=0

def is_op(token):
	pass

def is_id(token):
	global mem
	pass

def is_sy(token):
	if token in syn:
		return 1
	
mem=""
rfile="file.rkt"
r=open(rfile)
cont=r.read()
r.close()
cont=cont.split("\n")
lfile=rfile+".lexed"
call(['touch',lfile])

with open(lfile,"w") as lexed:
	for j in range(len(cont)):
		rline=cont[j]
		rline=rline.split()
		i=0
		while(i<len(rline)):
			w=1
			tok,val="",""
			token=rline[i]
			if(token[:1]=="\""):
				qoute=token+" "
				while(rline[i][-1:]!="\""):
					i+=1
					qoute+=rline[i]+" "	
				tok,val="st",qoute
			elif(is_sy(token)==1):
				tok,val="sy",token
			elif(is_op(token)==1):
				tok,val="op",token
			elif(is_id(token)==1):
				tok,val="id"+str(idc),mem
			else:				
				print("Syntax error at line "+str(j+1)+":: "+"\""+token+"\"")
				w=0	
			i+=1
			if(w!=0):
				lexed.write(tok+":"+val+"\n")		
