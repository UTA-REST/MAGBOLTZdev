from PyQt5 import QtCore,QtGui,QtWidgets,uic
from subprocess import call
from os import system

input_values=[
'nGASLineEdit','nDELTALineEdit','iMIPLineEdit','nDVECLineEdit','nSEEDLineEdit','eSTARTLineEdit','eTHRMLineEdit','eCUTLineEdit','nGAS1LineEdit','nGAS2LineEdit','nGAS3LineEdit','nGAS4LineEdit','nGAS5LineEdit','nGAS6LineEdit','fRAC1LineEdit','fRAC2LineEdit','fRAC3LineEdit','fRAC4LineEdit','fRAC5LineEdit','fRAC6LineEdit','tEMPLineEdit','tORRLineEdit','eFIELDLineEdit','bMAGLineEdit','bTHETALineEdit','iWRITELineEdit','iPENLineEdit','dETEFFLineEdit','eXCWGHTLineEdit','kGASLineEdit','lGASLineEdit','lCMPLineEdit','lRAYLineEdit','lPAPLineEdit','lBRMLineEdit','iECASCLineEdit'
]

input_variables=[
'NGAS','NDELTA','IMIP','NDVEC','NSEED','ESTART','ETHRM','ECUT','NGAS1',' NGAS2',' NGAS3 ',' NGAS4 ',' NGAS5 ',' NGAS6','FRAC1','FRAC2','FRAC3','FRAC4','FRAC5','FRAC6','TEMP','TORR','EFIELD','BMAG','BTHETA','IWRITE','IPEN','DETEFF','EXCWGHT','KGAS','LGAS','LCMP','LRAY','LPAP','LBRM','IECASC'
]

default_0_values=[
2,100,5,1,0,1.0,1.5,2.0,
2 , 12 , 0 , 0 , 0 , 0,
80.000,20.000,0.0,0.0,0.0,0.0,20.000,760.000,   
2.000,3.000,30.000,0,0,
50.0,0.55,2,1,1,1,1,1,1
]

class Window(QtWidgets.QMainWindow):
	def __init__(self):
		super(Window,self).__init__()
		uic.loadUi('main.ui',self)
		self.pushButton_2.clicked.connect(lambda: self.reset())
		self.pushButton.clicked.connect(lambda: self.submit())		
		self.pushButton_3.clicked.connect(self.close)


	def reset(self):
		global input_values
		global default_0_values
		for le,val in zip(input_values,default_0_values):
			getattr(self,le).setText(str(val))
	
	def submit(self):
		global default_0_values
		input_degrad=[]
		for le in input_values:
			input_degrad.append(str(getattr(self,le).text()))
		system("rm input_degrad.txt")
		input_file=open('input_degrad.txt',"w")
		count=1
		card=1
		for i in input_degrad:
			
			if(card==1 and count==8):
				input_file.write(i+'\n')
				count=1
				card=card+1
			elif(card==1 and count<8):
				input_file.write(i+',')
				count=count+1
			elif(card==2 and count==6):
				input_file.write(i+'\n')
				count=1
				card=card+1
			elif(card==2 and count<6):
				input_file.write(i+',')
				count=count+1
			elif(card==3 and count==8):
				input_file.write(i+'\n')
				count=1
				card=card+1
			elif(card==3 and count<8):
				input_file.write(i+',')
				count=count+1
			elif(card==4 and count==5):
				input_file.write(i+'\n')
				count=1
				card=card+1
			elif(card==4 and count<5):
				input_file.write(i+',')
				count=count+1
			elif(card==5 and count==9):
				input_file.write(i+'\n')
				count=1
				card=card+1
			elif(card==5 and count<9):
				input_file.write(i+',')
				count=count+1
		input_file.write('0\n')
		input_file.close()
		system("cat input_degrad.txt")
		system("gfortran -o degrad.out degrad-3.3.f")
		system("./degrad.out < input_degrad.txt")

	
		

if __name__=='__main__':
	import sys
	print("started")
	app=QtWidgets.QApplication(sys.argv)
	window=Window()
	window.show()
	sys.exit(app.exec())
