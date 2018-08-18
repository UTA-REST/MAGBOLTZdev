import numpy
import conf
from Abso import *
def FLDIST():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONFL/
	global NC0#(512)
	global EC0#(512)
	global NG1#(512)
	global EG1#(512)
	global NG2#(512)
	global EG2#(512)
	global WKLM#(512)
	global EFL#(512)	
	NC0=conf.NC0
	EC0=conf.EC0
	NG1=conf.NG1
	EG1=conf.EG1
	NG2=conf.NG2
	EG2=conf.EG2
	WKLM=conf.WKLM
	EFL=conf.EFL
	# print("------------------------------------------")
	# print(EFL)
	# print("------------------------------------------")
	# CALCULATE FLUORESCENCE AVERAGE ABSORPTION DISTANCE AND LOAD INTO ARRAY
	for I in range(1,512+1):
		EPH=EFL[I]
		# print("EPF=",EPH)
		if(EPH == 0.0):
			continue
		JF=3
		ABSO(JF,EPH,IDUM,KDUM,LDUM,DIST)
		EFL[I]=DIST

	conf.NC0=NC0
	conf.EC0=EC0
	conf.NG1=NG1
	conf.EG1=EG1
	conf.NG2=NG2
	conf.EG2=EG2
	conf.WKLM=WKLM
	conf.EFL=EFL
	return
	# end