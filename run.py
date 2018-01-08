import subprocess 
import shlex
from Tkinter import *
import ttk
import time
from read import NonBlockingStreamReader as NBSR
import tkMessageBox
from check_input import check 

# makes an executable of the fortran code
p = subprocess.Popen('gfortran magboltz-11.3.f',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)

root = Tk() 

# Number of gases field
label_numGases = Label(root,text="Number of Gases:")
label_numGases.grid(row=0)
numGases = Entry(root)
numGases.grid(row=0,column=1)	

# Number of real collisions field
label_numRealcollisions = Label(root,text="Number of real collisions(multiple of 10^7):")
label_numRealcollisions.grid(row=1)
numRealcollisions = Entry(root)	
numRealcollisions.grid(row=1,column=1)

# penning effects check box
ipen = IntVar()
Ipen = Checkbutton(root,text="Include Penning Effects",variable=ipen)
Ipen.grid(row=2,columnspan=2)

# gas motion checkbox
ithrm = IntVar()
Ithrm = Checkbutton(root,text="Gas Motion Assumed To Be At O Kelvin (Static Gas)",variable=ithrm)
Ithrm.grid(row=3,columnspan=2)

# Upper limit of the electron energy field (check box + entry box)
label_EFINAL = Label(root,text="Upper Limit Of The Electron Energy [eV]")
EFINAL = Entry(root)
label_EFINAL.grid(row=4)
EFINAL.grid(row=4,column=1)
# the checkbox
efinalc = IntVar()
EFINALC = Checkbutton(root,text="Automatically Calculate The Upper Integration Energy Limit",variable=efinalc)
EFINALC.grid(row=5,columnspan=2)

# gas1
label_Gas1 = Label(root,text="Gas1:")
label_Gas1.grid(row=6)
numGas1 = Entry(root)	
numGas1.grid(row=6,column=1)

# gas2
label_Gas2 = Label(root,text="Gas2:")
label_Gas2.grid(row=7)
numGas2 = Entry(root)	
numGas2.grid(row=7,column=1)

# gas3
label_Gas3 = Label(root,text="Gas3:")
label_Gas3.grid(row=8)
numGas3 = Entry(root)	
numGas3.grid(row=8,column=1)

# gas4
label_Gas4 = Label(root,text="Gas4:")
label_Gas4.grid(row=9)
numGas4 = Entry(root)	
numGas4.grid(row=9,column=1)

# gas5
label_Gas5 = Label(root,text="Gas5:")
label_Gas5.grid(row=10)
numGas5 = Entry(root)	
numGas5.grid(row=10,column=1)

# gas6
label_Gas6 = Label(root,text="Gas6:")
label_Gas6.grid(row=11)
numGas6 = Entry(root)	
numGas6.grid(row=11,column=1)

note= Label(root, text="use the Database.txt file to fill in the above entry boxes")
note.grid(row=12,columnspan=2)

# fraction fields
label_fGas1 = Label(root,text="Fraction of Gas1:")
label_fGas1.grid(row=13)
numfGas1 = Entry(root)	
numfGas1.grid(row=13,column=1)

label_fGas2 = Label(root,text="Fraction of Gas2:")
label_fGas2.grid(row=14)
numfGas2 = Entry(root)	
numfGas2.grid(row=14,column=1)

label_fGas3 = Label(root,text="Fraction of Gas3:")
label_fGas3.grid(row=15)
numfGas3 = Entry(root)	
numfGas3.grid(row=15,column=1)

label_fGas4 = Label(root,text="Fraction of Gas4:")
label_fGas4.grid(row=16)
numfGas4 = Entry(root)	
numfGas4.grid(row=16,column=1)

label_fGas5 = Label(root,text="Fraction of Gas5:")
label_fGas5.grid(row=17)
numfGas5 = Entry(root)	
numfGas5.grid(row=17,column=1)

label_fGas6 = Label(root,text="Fraction of Gas6:")
label_fGas6.grid(row=18)
numfGas6 = Entry(root)	
numfGas6.grid(row=18,column=1)

# temp field 
label_temp = Label(root,text="Tempreture in Centigrades:")
label_temp.grid(row=19)
temp = Entry(root)	
temp.grid(row=19,column=1)

# pressure field
label_press = Label(root,text="Pressure In torr:")
label_press.grid(row=20)
press = Entry(root)	
press.grid(row=20,column=1)

# electric field
label_EF = Label(root,text="Electric Field In VOLTS/ CM:")
label_EF.grid(row=21)
EF = Entry(root)	
EF.grid(row=21,column=1)

# magnetic field
label_BF = Label(root,text="Magnetic Field In Kilagauss:")
label_BF.grid(row=22)
BF = Entry(root)	
BF.grid(row=22,column=1)

# degree field
label_theta = Label(root,text="Angle Between The Electric AND Magnetic Fields In Degrees:")
label_theta.grid(row=23)
theta = Entry(root)	
theta.grid(row=23,column=1)


progress_var = DoubleVar()
progressbar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progressbar.grid(row=24,columnspan=2)

v = StringVar()
label_progress = Label(root, textvariable=v)
label_progress.grid(row=25)

def runn():

	# stores the input into one string
	s=""
	ngass = numGases.get()
	s=s+ngass+'\n'
	nmax = numRealcollisions.get()
	s=s+nmax+'\n'	
	iipen = ipen.get()
	s=s+str(iipen)+'\n'	
	iithrm =ithrm.get()
	s=s+str(iithrm)+'\n'	
	eefinalc = efinalc.get()
	
	if eefinalc!=0:
		efinal=r"0.0" 
	else:
		efinal= EFINAL.get()
	s=s+efinal+'\n'	
	ngas = ["","","","","","",""]
	ngas[0]= numGas1.get()	
	ngas[1]= numGas2.get()
	ngas[2]= numGas3.get()
	ngas[3]= numGas4.get()
	ngas[4]= numGas5.get()
	ngas[5]= numGas6.get()
	s=s+ngas[0]+'\n'+ngas[1]+'\n'+ngas[2]+'\n'+ngas[3]+'\n'+ngas[4]+'\n'+ngas[5]+'\n'
	fgas=["","","","","","",""]
	fgas[0]= numfGas1.get()
	fgas[1]= numfGas2.get()
	fgas[2]= numfGas3.get()
	fgas[3]= numfGas4.get()
	fgas[4]= numfGas5.get()
	fgas[5]= numfGas6.get()
	s=s+fgas[0]+'\n'+fgas[1]+'\n'+fgas[2]+'\n'+fgas[3]+'\n'+fgas[4]+'\n'+fgas[5]+'\n'
	tempv = temp.get()
	s=s+tempv+'\n'	
	pressv=press.get()
	s=s+pressv+'\n'
	ef= EF.get()
	s=s+ef+'\n'
	bf= BF.get()
	s=s+bf+'\n'
	ang=theta.get()
	s=s+ang+'\n'
	if check(s):
		# runs magboltz in the background
		ps = subprocess.Popen('./a.out',shell=False, stdin = subprocess.PIPE,stdout=subprocess.PIPE)
		nbsr = NBSR(ps.stdout)
		ps.stdin.write(s)
		result=""
		processnum = 0
		v.set("Initializing RM48...")
		root.update()
		# sends the input, and reads the output to and from magboltz.	
		numofe = 0
		x=0
		while True:	
			output = nbsr.readline(0.1)
	 		result+=output
			time.sleep(0.1)
			if numofe==40:
				progress_var.set(100)
				v.set("Done!")
				processnum=0
				s='0\n'+'0\n'+'0\n'+'0\n'+'0\n'
				ps.stdin.write(s)
				break
	  		elif output[0:16]==" RM48 INITIALIZE" and processnum==0:
				progress_var.set(12)
				v.set("Finding the decorrelation length...")
				processnum+=1
				root.update_idletasks()
	  		elif output[0:25]==" LONG DECORRELATION LENGT" :
				progress_var.set(24)
				v.set("Finding the Velocity/Energy/Diffusion table...")
				root.update_idletasks()
			elif output[0:6]=="   VEL":
				progress_var.set(36)
				v.set("Finding the diffusion values...")
				root.update_idletasks()
			elif output[0:17]=="  DIFFUSION TENSO":
				progress_var.set(48)
				v.set("Finding the number of collisions in the final energy bin...")
				root.update_idletasks()
			elif output[0:29]==" NUMBER OF COLLISIONS IN FINA" :
				progress_var.set(60)
				v.set("Finding the normalized energy distribution...")
				root.update_idletasks()
			elif output[0:8]=="      E=":
				numofe+=1

	
		# opens a file to store the output	
		fo = open("Output.txt", "w")
		fo.write(str(result))
		fo.close()
		

# submit button
button_submit = Button(root,text ="Run",command=runn)
button_submit.grid(row=26,columnspan=2)
root.mainloop()
