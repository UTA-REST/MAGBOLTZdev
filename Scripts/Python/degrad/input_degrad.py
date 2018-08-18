#--------------------------------------------------------------- 
#   INPUT CARDS :                                                       
#-------------------------------------------------------------------   
#  FIRST CARD: 5I10,3F10.5 : NGAS,NDELTA,IMIP,NDVEC,NSEED,
#                                    ESTART,ETHRM,ECUT
#  NGAS   = NUMBER OF GASES IN MIXTURE                                
#  NDELTA = NUMBER OF DELTA ELECTRONS (CONVERTED X-RAYS) OR MIPS  
#           MAXIMUM NUMBER OF MIPS   = 100000   
#           MAXIMUM NUMBER OF GAMMAS =  10000
#           MAXIMUM NUMBER OF BETAS  =  10000
#           MAXIMUM NUMBER OF E-BEAM =  10000
#
#  IMIP   = 1 MIPS SIMULATION  (DE/DX, CLUSTERS)
#  IMIP   = 2 ELECTRON BEAM  (TOTAL ABSORPTION)
#  IMIP   = 3 X-RAY
#  IMIP   = 4 BETA DECAY
#  IMIP   = 5 DOUBLE BETA DECAY
#
#  NOTE THE DOUBLE BETA DECAY EVENTS ARE SPLIT IN TWO THE FIRST
#  BETA IS OUTPUT AS A SEPARATE EVENT FROM THE SECOND BETA WHICH
#  ARE AT 180 DEGREES TO EACH OTHER (USE EVEN NUMBER OF TOTAL EVENTS
#  IN ORDER TO HAVE FULL TWO BETA EVENTS)   
# 
#  NDVEC  = 2 MIP X-RAY OR BETA IN RANDOM DIRECTION
#  NDVEC  = 1 MIP X-RAY OR BETA DIRECTION PARALLEL TO E-FIELD (Z) 
#  NDVEC  =-1 MIP X-RAY OR BETA DIRECTION ANTI PARALLEL TO E-FIELD (-Z) 
#  NDVEC  = 0 MIP X-RAY OR BETA IN RANDOM DIRECTION IN X-Y PLANE
#         
#  NOTE :   ELECTRON BEAM WITH NDVEC =0 GIVES DIRECTION ALONG X-AXIS
#           THIS ALLOWS TRACK PARALLEL TO BFIELD WHEN THE B-FIELD IS
#           AT 90 DEGREES TO E-FIELD
#  NSEED  = 0 USES STANDARD SEED VALUE = 54217137
#  NSEED != 0 USES VALUE OF NSEED AS SEED VALUE 
#
#  ESTART = MIP,ELECTRON,BETA DECAY OR X-RAY ENERGY IN EV.
#           NOTE DOUBLE BETA DECAY ENERGY IS TO BE ENTERED AS
#           THE ENERGY OF EACH BETA (0.5 TIMES TOTAL DECAY ENERGY)
#            (IF X-RAY MAX ENERGY=2.0MEV)
#            
#  ETHRM  = ELECTRONS TRACKED UNTIL THEY FALL TO THIS ENERGY EV.
#           FOR FAST CALCULATION THE THERMALISATION ENERGY SHOULD BE 
#          SET TO THE LOWEST IONISATION POTENTIAL IN THE GAS MIXTURE.
#          FOR MORE ACCURATE THERMALISATION RANGE THE THERMALISATION
#          ENERGY SHOULD BE SET TO THE LOWEST EXCITATION ENERGY IN 
#          PURE NOBLE GASES OR TO 2.0EV FOR MIXTURES WITH MOLECULAR
#          GAS
#  ECUT   = FOR MIPS ONLY.  APPLIES ENERGY CUT IN EV TO GIVE THE 
#           MAXIMUM ALLOWED PRIMARY CLUSTER ENERGY ( SHOULD BE SET
#           TO LESS THAN 10000. EV TO GIVE MAXIMUM PRIMARY CLUSTER SIZE
#           OF TYPICALLY 400 ELECTRONS
#------------------------------------------------------------------
#  SECOND CARD : 6I5   : NGAS1 , NGAS2, NGAS3 , NGAS4 , NGAS5 , NGAS6
#       NGAS1,ETC :  GAS NUMBER IDENTIFIERS (BETWEEN 1 AND 80)
#                   SEE GAS LIST BELOW FOR IDENTIFYING NUMBERS.
#                                                                      
#-------------------------------------------------------------          
# THIRD CARD: 8F10.4  : FRAC1,FRAC2,FRAC3,FRAC4,FRAC5,FRAC6,TEMP,TORR   
#  FRAC1,ETC : PERCENTAGE FRACTION OF GAS1,ETC                          
#  TEMP : TEMPERATURE OF GAS IN CENTIGRADE                              
#  TORR :  PRESSURE OF GAS IN TORR                                      
# ------------------------------------------------------------          
# FOURTH CARD :  3F10.3,2I5  : EFIELD,BMAG,BTHETA,IWRITE,IPEN             
#  EFIELD : ELECTRIC FIELD IN VOLTS/ CM.                                
#   BMAG  : MAGNITUDE OF THE MAGNETIC FIELD IN KILOGAUSS
#  BTHETA : ANGLE BETWEEN THE ELECTRIC AND MAGNETIC FIELDS IN DEGREES. 
#
#  IWRITE : =0                STANDARD OUTPUT
#  IWRITE : =1    
#   LINE1   OUTPUT NO OF ELECTRONS AND NO OF EXCITATIONS FOR EACH EVENT
#   LINE2   OUTPUTS X,Y,Z AND T FOR EACH THERMALISED ELECTRON
#  IWRITE : =2
#   LINE1   OUTPUT NO OF ELECTRONS AND NO OF EXCITATIONS FOR EACH EVENT
#   LINE2   OUTPUTS X,Y,Z AND T FOR EACH THERMALISED ELECTRON
#   LINE3   OUTPUTS X,Y,Z AND T FOR EACH EXCITATION
#   
#   IPEN :  =0 NO PENNING TRANSFERS
#           =1  PENNING TRANSFERS ALLOWED
#            ( MODIFY GAS def TO CHANGE PENNING FRACTIONS)
# -----------------------------------------------------------------
# FIFTH CARD : 2F10.3,7I5 : 
#          DETEFF,EXCWGHT,KGAS,LGAS,LCMP,LRAY,LPAP,LBRM,IECASC
#  DETEFF: DETECTION EFFICIENCY OF PHOTONS. USED FOR CALCULATION OF
#          FANO FACTORS FOR COMBINED ELECTRON AND PHOTON DETECTION 
#          IN PURE NOBLE GASES  :  
#          USE BETWEEN 0.0  -  100.0  DETECTION EFFICIENCY
# EXCWGHT: WEIGHT GIVEN TO EXCITATION EVENTS IN FANO CALCULATION
#          WITH RESPECT TO IONISATION. TYPICALLY 0.5 TO 0.6
#          USE WEIGHT GIVEN BY SQRT(Fele/Fexc)  
#          WHERE Fele= ELECTRON FANO FACTOR
#                Fexc= EXCITATION FANO FACTOR
#  KGAS:   GAS IDENTIFIER FOR WHICH GAS IN MIXTURE HAS BETA DECAYED
#          IDENTIFIER NUMBERS : NGAS1 etc   
#  LGAS:   IF MOLECULAR GAS : LGAS IDENTIFIES THE COMPONENT ATOM
#          IN THE MOLECULE WHICH HAS BETA DECAYED:
#          E.G. IN CO2  1 = CARBON  2 = OXYGEN
#               IN CF4  1 = CARBON  2 = FLUORINE
#  LCMP:   = 0 NO COMPTON SCATTERING
#          = 1 INCLUDE COMPTON SCATTERING
#  LRAY:   = 0 NO RAYLEIGH SCATTERING
#          = 1 INCLUDE RAYLEIGH SCATTERING
#  LPAP:   = 0 NO PAIR PRODUCTION
#          = 1 INCLUDE PAIR PRODUCTION                  
#  LBRM;   = 0 NO BREMSSTRAHLUNG
#          = 1 INCLUDE BREMSSTRAHLUNG
#
# IECASC   = 0 USE PARAMETERISED CASCADE FOR 2ND TO NTH GENERATION OF
#               ELECTRON IONISING COLLISIONS
#          = 1 USE EXACT CASCADE FOR 2ND TO NTH GENERATION OF ELECTRON
#               IONISING COLLISIONS
#-----------------------------------------------------------------------
# CARD 4*N+1 USES NGAS=0 TO TERMINATE CORRECTLY                         
#-------------------------------------------------------------------- 
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QToolTip,QPushButton,QApplication,QMessageBox,QHBoxLayout,QVBoxLayout,QLabel, QLineEdit,QTextEdit, QGridLayout
from PyQt5.QtGui import QIcon,QFont
#first card
NGAS=2
NDELTA=100
IMIP=5
NDVEC=1
NSEED=0
ESTART=1.0
ETHRM=1.5
ECUT=2.0
#second card
NGAS1=2
NGAS2=12
NGAS3=0
NGAS4=0
NGAS5=0
NGAS6=0
#third card
FRAC1=80.0
FRAC2=20.0
FRAC3=0.0
FRAC4=0.0
FRAC5=0.0
FRAC6=0.0
TEMP=20.0
TORR=760.0
#fourth card
EFIELD=2.0
BMAG=3.0
BTHETA=30.0
IWRITE=0
IPEN=0
#fifth card
DETEFF=50.0
EXCWGHT=0.55
KGAS=2
LGAS=1
LCMP=1
LRAY=1
LPAP=1
LBRM=1
IECASC=1
'''
'NGAS','NDELTA','IMIP','NDVEC','NSEED','ESTART','ETHRM','ECUT'
'NGAS1',' NGAS2',' NGAS3 ',' NGAS4 ',' NGAS5 ',' NGAS6'
'FRAC1','FRAC2','FRAC3','FRAC4','FRAC5','FRAC6','TEMP','TORR'
'EFIELD','BMAG','BTHETA','IWRITE','IPEN'
'DETEFF','EXCWGHT','KGAS','LGAS','LCMP','LRAY','LPAP','LBRM','IECASC'

input_card=NGAS,',',NDELTA,',',IMIP,',',NDVEC,',',NSEED,',',ESTART,',',ETHRM,',',ECUT,'\n',NGAS1,',', NGAS2,',', NGAS3 ,',', NGAS4 ,',', NGAS5 ,',', NGAS6,'\n',FRAC1,',',FRAC2,',',FRAC3,',',FRAC4,',',FRAC5,',',FRAC6,',',TEMP,',',TORR,'\n',EFIELD,',',BMAG,',',BTHETA,',',IWRITE,',',IPEN,'\n',DETEFF,',',EXCWGHT,',',KGAS,',',LGAS,',',LCMP,',',LRAY,',',LPAP,',',LBRM,',',IECASC,'\n'

class Window(QMainWindow):
	def __init__(self):
		super().__init__()

		self.title="input degrad"
		self.top=100
		self.left=100
		self.width=680
		self.height =500

	def initWindow(self):
		self.setWindowTitle(self.title)
		self.setGeometry(self.top,self.left,self.width,self.height)
		self.show()
		self.initWindow()
app=QApplication(sys.argv)
window=Window()

b=QtGui.QLabel(w)
b.setText("NGAS,NDELTA,IMIP,NDVEC,NSEED,ESTART,ETHRM,ECUT")
w.setGeometry(100,100,200,50)	
b.move(50,20)
w.show()

sys.exit(app.exec_())

'''
class Window(QWidget):
	def __init__(self):
		super().__init__()
		self.initUI()

	def initUI(self):
		QToolTip.setFont(QFont('SansSerif',10))
		self.setToolTip('Input interface for degrad')
		# card 1 
		## labels
		ngas=QLabel('NGAS')
		ndelta=QLabel('NDELTA')
		imip=QLabel('IMIP')
		ndvec=QLabel('NDVEC')
		nseed=QLabel('NSEED')
		estart=QLabel('ESTART')
		ethrm=QLabel('ETHRM')
		ecut=QLabel('ECUT')
		## lines
		ngasedit=QLineEdit()
		ndeltaedit=QLineEdit()
		imipedit=QLineEdit()
		ndvecedit=QLineEdit()
		nseededit=QLineEdit()
		estartedit=QLineEdit()
		ethrmedit=QLineEdit()
		ecutedit=QLineEdit()
		#grid setup
		grid=QGridLayout()
		grid.setSpacing(10)

		grid.addWidget( ngas , 0 ,0)
		grid.addWidget( ngasedit, 0 ,1)
		grid.addWidget( ndelta , 1 ,0)
		grid.addWidget( ndeltaedit, 1 ,1)
		grid.addWidget( imip , 2 ,0)
		grid.addWidget( imipedit, 2 ,1)
		grid.addWidget( ndvec , 3 ,0)
		grid.addWidget( ndvecedit, 3 ,1)
		grid.addWidget( nseed , 4 ,0)
		grid.addWidget( nseededit, 4 ,1)
		grid.addWidget( estart , 5 ,0)
		grid.addWidget( estartedit, 5 ,1)
		grid.addWidget( ethrm , 6 ,0)
		grid.addWidget( ethrmedit, 6 ,1)
		grid.addWidget( ecut , 7 ,0)
		grid.addWidget( ecutedit, 7 ,1)


		#self.setLayout(grid)


		#Submit button
		submit_btn=QPushButton('Submit',self)
		submit_btn.setToolTip('Submit')
		submit_btn.resize(submit_btn.sizeHint())
		# quit button
		quit_btn=QPushButton('Quit',self)
		quit_btn.clicked.connect(QApplication.instance().quit)
		#hbox
		'''
		hbox=QHBoxLayout()
		hbox.addStretch(1)
		hbox.addWidget(submit_btn)
		hbox.addWidget(quit_btn)
		#vbox
		vbox = QVBoxLayout()
		vbox.addStretch(1)
		vbox.addLayout(hbox)
		'''
		#set layout
		grid.addWidget(submit_btn,8,0)
		grid.addWidget(quit_btn,8,1)
		self.setLayout(grid)
		#status bar - QMainWindow
		#self.statusBar().showMessage('Ready')
		#formation
		self.setGeometry(300,300,300,220)
		self.setWindowTitle("Input Degrad")
		self.show() 

	def closeEvent(self, event):
        
		reply = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
		    event.accept()
		else:
		    event.ignore() 
if __name__ == '__main__':
    
    app = QApplication(sys.argv)

    w=Window()
    sys.exit(app.exec_())