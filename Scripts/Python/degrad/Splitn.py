def SPLIT1(I,E,EI,ESEC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	# MODIFIED OPAL BEATY WITH ENERGY DEP# endANT SPLITTING def
	# MODEL ASSUMES CONSTANT SPLITTING def BETWEEN EI AND 10 KEV
	# : LOGARTHMIC CHANGE WITH ENERGY UP TO A CONSTANT VALUE AT
	# MINIMUM IONISING ,1 MEV , AND ABOVE 
	WPLLOW=ESPLIT[I][1]
	WPLHIGH=ESPLIT[I][2]
	if(E <= 1*10**4):
		WPL=WPLLOW
		pass
	elif(E >= 1*10**6) :
		WPL=WPLHIGH
		pass
	else:
		#  LOG INTERPOLATE AT ENERGY E 
		A=(WPLHIGH-WPLLOW)*0.21714724095
		B=-(9.21034037198*WPLHIGH-13.815510558*WPLLOW)*0.21714724095
		WPL=A*math.log(E)+B
	# endif
	R1=DRAND48(RDUM)
	ESEC=WPL*TAN(R1*ATAN((E-EI)/(2.0*WPL))) 
	ESEC=WPL*(ESEC/WPL)**0.9524
	return
	# end 
def SPLIT2(I,E,EI,ESEC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	# POSSIBLE ENERGY SPLITTING def
	return
	# end 
def SPLIT3(I,E,EI,ESEC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	# POSSIBLE ENERGY SPLITTING def
	return
	# end 
def SPLIT4(I,E,EI,ESEC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	# POSSIBLE ENERGY SPLITTING def
	return
	# end 
def SPLIT5(I,E,EI,ESEC):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	# POSSIBLE ENERGY SPLITTING def
	return
      # end 