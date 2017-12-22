import subprocess 
from Tkinter import *

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

# call back function to the event of clicking the button
def runn():
	# stores the input into one string
	s=""
	ngas = numGases.get()
	s=s+ngas+'\n'
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
	ngas1= numGas1.get()	
	ngas2= numGas2.get()
	ngas3= numGas3.get()
	ngas4= numGas4.get()
	ngas5= numGas5.get()
	ngas6= numGas6.get()
	s=s+ngas1+'\n'+ngas2+'\n'+ngas3+'\n'+ngas4+'\n'+ngas5+'\n'+ngas6+'\n'
	fgas1= numfGas1.get()
	fgas2= numfGas2.get()
	fgas3= numfGas3.get()
	fgas4= numfGas4.get()
	fgas5= numfGas5.get()
	fgas6= numfGas6.get()
	s=s+fgas1+'\n'+fgas2+'\n'+fgas3+'\n'+fgas4+'\n'+fgas5+'\n'+fgas6+'\n'
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
	s=s+'0'+'\n'	
	# runs magboltz in the background
	ps = subprocess.Popen('./a.out',shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	# sends the input, and reads the output to and from magboltz.	
	result = ps.communicate(s)
	# opens a file to store the output	
	fo = open("Output.txt", "w")
	fo.write(str(result[0]))
	fo.close()


# submit button
button_submit = Button(root,text ="Run",command=runn)
button_submit.grid(row=24,columnspan=2)
root.mainloop()
