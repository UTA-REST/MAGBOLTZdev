import tkMessageBox
def check(s):
	i = 0
	ngass = 0 
	fgass = 0
	fsum = 0.0
	flag =1
	errormessage = ""
	for line in s.splitlines(): 
		if i==0:	
			if line!="":
				line =float(line)	
				x = int(line)
				if x<=0  or x>6 or x!=line:
					errormessage+= "* The number of gases should be an integer in the range of 1-6"+'\n'
				else:
					ngass = x 	
					fgass = x
			else:
				errormessage+= "* make sure to put a number for the amout of gases used" + '\n'					
		if i==1 and line=="":
			errormessage+= "* make sure to fill number of real collisions"+'\n'
		if i==4 and line=="":
			errormessage+= "* make sure to fill the Upper Limit Of The Electron Energy or check the underneath box"+'\n'
		if i>=5 and i<=10:
			if ngass>=1:
				ngass-=1
				if line=="" or line=="0" or int(line)!=float(line):
					errormessage+= "* make sure to fill the right values for the gases used"+'\n'				
			else:
				if line=="":
					errormessage+= "* make sure to put a 0 for unused gases" + '\n'
		if i>=11 and i<=16:
			if fgass>=1:
				fgass-=1
				if line=="":
					errormessage+= "* make sure to fill the right values for the gases used"+'\n'					
				else:				
					fsum += float(line)
			else:
				if line=="":
					errormessage+= "* make sure to put a 0 for unused gases" + '\n'
		if i>=17 and i<=21 and flag==1:
			if line=="":
					errormessage+= "* make sure to fill out all the necessary boxes" + '\n'
					flag =0
		i+=1
	if errormessage =="":
		return 1
	else:
		tkMessageBox.showinfo("Input error", errormessage)
		return 0
