#Programme : B.Tech CSE
#Name : Gohil Hiren Ashvinbhai
#EnrollMent No. : 202103103510017

#------------------------------------------------------------------------------------
with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile:
	
	for line in firstfile:
			
			secondfile.write(line)

#------------------------------------------------------------------------------------
