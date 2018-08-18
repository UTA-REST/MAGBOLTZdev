import numpy
import conf
import math
def ABSO(JF,EPH,ISHELL,KGAS,LGAS,DIST):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	def get_globals():
		#COMMON/RATIO/
		AN1=conf.AN1
		AN2=conf.AN2
		AN3=conf.AN3
		AN4=conf.AN4
		AN5=conf.AN5
		AN6=conf.AN6
		AN=conf.AN
		FRAC=conf.FRAC#(6)  
		#COMMON/COMP/=conf.#COMMON/COMP/
		LCMP=conf.LCMP
		LCFLG=conf.LCFLG
		LRAY=conf.LRAY
		LRFLG=conf.LRFLG
		LPAP=conf.LPAP
		LPFLG=conf.LPFLG
		LBRM=conf.LBRM
		LBFLG=conf.LBFLG
		LPEFLG=conf.LPEFLG
		#COMMON/ABBS/=conf.#COMMON/ABBS/
		ABSXRAY=conf.ABSXRAY             
		#COMMON/INPT/=conf.#COMMON/INPT/
		NGAS=conf.NGAS
		NSTEP=conf.NSTEP
		NANISO=conf.NANISO
		EFINAL=conf.EFINAL
		ESTEP=conf.ESTEP
		AKT=conf.AKT
		ARY=conf.ARY
		TEMPC=conf.TEMPC
		TORR=conf.TORR
		IPEN=conf.IPEN
		#COMMON/MIXC/=conf.#COMMON/MIXC/
		PRS=conf.PRSH#(6,3,17,17)
		ESH=conf.ESH#(6,3,17)
		AUG17=conf.AUG#(6,3,17,17,17)
		RAD=conf.RAD#(6,3,17,17)
		PRSHBT=conf.PRSHBT#(6,3,17)
		IZ=conf.IZ#(6,3)
		INIOCC=conf.INIOCC#(6,3,17)
		ISHLMX=conf.ISHLMX#(6,3)
		AMZ=conf.AMZ#(6,3)
		#COMMON/MIXPE/=conf.#COMMON/MIXPE/
		XPE=conf.XPE#(6,3,17,60)
		YPE=conf.YPE#(6,3,17,60)
		#COMMON/MIXCN/=conf.#COMMON/MIXCN/
		XEN=conf.XEN#(6,3,54)
		YRY=conf.YRY#(6,3,54)
		YCP=conf.YCP#(6,3,54)
		YPP=conf.YPP#(6,3,54)
		globals().update(locals())
	get_globals()
	# DIMENSION 
	XSEC=numpy.zeros((306+1))
	XSECC=numpy.zeros((18+1))
	XSECR=numpy.zeros((18+1))
	XSECP=numpy.zeros((18+1))
	ANGAS=numpy.zeros((6+1))
	ABSL=numpy.zeros((306+1))
	ABSLC=numpy.zeros((18+1))
	ABSLR=numpy.zeros((18+1))
	ABSLP=numpy.zeros((18+1))
	XSUM=numpy.zeros((360+1))
	def update_globals():
		conf.AN1=AN1
		conf.AN2=AN2
		conf.AN3=AN3
		conf.AN4=AN4
		conf.AN5=AN5
		conf.AN6=AN6
		conf.AN=AN
		conf.FRAC=FRAC
		conf.LCMP=LCMP
		conf.LCFLG=LCFLG
		conf.LRAY=LRAY
		conf.LRFLG=LRFLG
		conf.LPAP=LPAP
		conf.LPFLG=LPFLG
		conf.LBRM=LBRM
		conf.LBFLG=LBFLG
		conf.LPEFLG=LPEFLG
		conf.ABSXRAY=ABSXRAY
		conf.NGAS=NGAS
		conf.NSTEP=NSTEP
		conf.NANISO=NANISO
		conf.EFINAL=EFINAL
		conf.ESTEP=ESTEP
		conf.AKT=AKT
		conf.ARY=ARY
		conf.TEMPC=TEMPC
		conf.TORR=TORR
		conf.IPEN=IPEN
		conf.PRSH=PRS
		conf.ESH=ESH
		conf.AUG=AUG17
		conf.RAD=RAD
		conf.PRSHBT=PRSHBT
		conf.IZ=IZ
		conf.INIOCC=INIOCC
		conf.ISHLMX=ISHLMX
		conf.AMZ=AMZ
		conf.XPE=XPE
		conf.YPE=YPE
		conf.XEN=XEN
		conf.YRY=YRY
		conf.YCP=YCP
		conf.YPP=YPP
	#******************************************************************
	# FOR PHOTON ENERGY EPH CALCULATES INTERACTION DISTANCE WITH
	#  GAS IDENTITY,KGAS . IF MOLECULAR GAS ALSO IDENTIFIES THE 
	#  ATOMIC COMPONENT OF THE MOLECULE  LGAS. 
	#  IF PHOTOELECTRIC ABSORPTION CALCULATES ABSORPTION SHELL, ISHELL
	# AND SETS PHOTOELECTRIC FLAG,LPEFLG=1. 
	# IF COMPTON RAYLEIGH OR PAIR PRODUCTION ALLOWED : CALCULATES
	# KGAS , LGAS AND SETS COMPTON RAYLEIGH OR PAIR PRODUCTION FLAGS.
	#****************************************************************** 
	ANGAS[1]=AN1
	ANGAS[2]=AN2
	ANGAS[3]=AN3
	ANGAS[4]=AN4
	ANGAS[5]=AN5
	ANGAS[6]=AN6
	LCFLG=0
	LRFLG=0
	LPFLG=0
	LPEFLG=0
	# CALCULATE PE X-SECTION FOR EACH GAS AND FIND ABS LENGTH 
	EPHLG=math.log(EPH)
	IPT=0
	for I in range(1,NGAS+1):
		for J1 in range(1,3+1):
			for J in range(1,17+1):
				IPT=IPT+1
				XSEC[IPT]=0.0
				ABSL[IPT]=0.0
				if(J > ISHLMX(I,J1)):
					# GO TO 1
					continue
				if(EPHLG < XPE[I][J1][J][1]):
					# GO TO 1
					continue
				for K in range(2,60+1):
					if(EPHLG <= XPE[I][J1][J][K]) :
						A=(YPE[I][J1][J][K]-YPE[I][J1][J][K-1])/(XPE[I][J1][J][K]-XPE[I][J1][J][K-1])
						B=(XPE[I][J1][J][K-1]*YPE[I][J1][J][K]-XPE[I][J1][J][K]*YPE[I][J1][J][K-1])/(XPE[I][J1][J][K-1]-XPE[I][J1][J][K])
						XSEC[IPT]=math.exp(A*EPHLG+B)
						ABSL[IPT]=XSEC[IPT]*ANGAS[I]
						break
					# endif
	# CALCULATE COMPTON X-SECTION FOR EACH GAS AND FIND ABS LENGTH
	IPT=0
	for I in range(1,NGAS+1):
		for J1 in range(1,3+1):
			IPT=IPT+1
			XSECC[IPT]=0.0
			ABSLC[IPT]=0.0
			# USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
			if(JF == 3 or JF == 2):
				# GO TO 30
				continue
			# ONLY USE PE X-SECTION
			if(LCMP != 1):
				# GO TO 30
				continue
			if(EPHLG < XEN[I][J1][1]):
				# GO TO 30
				continue
			for K in range(2,54+1):
				if(EPHLG <= XEN[I][J1][K]) :
					A=(YCP[I][J1][K]-YCP[I][J1][K-1])/(XEN[I][J1][K]-XEN[I][J1][K-1])
					B=(XEN[I][J1][K-1]*YCP[I][J1][K]-XEN[I][J1][K]*YCP[I][J1][K-1])/(XEN[I][J1][K-1]-XEN[I][J1][K])
					XSECC[IPT]=math.exp(A*EPHLG+B)
					ABSLC[IPT]=XSECC[IPT]*ANGAS[I]
					# GO TO 30 
					break
				# endif
			# 30 CONTINUE
	# CALCULATE RAYLEIGH X-SECTION FOR EACH GAS AND FIND ABS LENGTH
	IPT=0
	for I in range(1,NGAS+1):
		for J1 in range(1,3+1):
			IPT=IPT+1
			XSECR[IPT]=0.0
			ABSLR[IPT]=0.0
			# USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
			if(JF == 3 or JF == 2):
				# GO TO 40
				continue
			if(LRAY != 1):
				# GO TO 40
				continue
			if(EPHLG < XEN[I][J1][1]):
				# GO TO 40
				continue
			for K in range(2,54+1):
				if(EPHLG <= XEN[I][J1][K]) :
					A=(YRY[I][J1][K]-YRY[I][J1][K-1])/(XEN[I][J1][K]-XEN[I][J1][K-1])
					B=(XEN[I][J1][K-1]*YRY[I][J1][K]-XEN[I][J1][K]*YRY[I][J1][K-1])/(XEN[I][J1][K-1]-XEN[I][J1][K])
					XSECR[IPT]=math.exp(A*EPHLG+B)
					ABSLR[IPT]=XSECR[IPT]*ANGAS[I]
					# GO TO 40
					break
				# endif
			# 40 CONTINUE   
	# CALCULATE PAIR PRODUCTION X-SECTION FOR EACH GAS AND FIND ABS LENGTH 
	IPT=0
	for I in range(1,NGAS+1):
		for J1 in range(1,3+1):
			IPT=IPT+1
			XSECP[IPT]=0.0
			ABSLP[IPT]=0.0
			# USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
			if(JF == 3 or JF == 2):
				# GO TO 50
				continue
			if(LPAP != 1):
				# GO TO 50
				continue
			if(EPHLG < XEN[I][J1][1]):
				# GO TO 50
				continue
			for K in range(2,54+1):
				if(EPHLG <= XEN[I][J1][K]) :
					A=(YPP[I][J1][K]-YPP[I][J1][K-1])/(XEN[I][J1][K]-XEN[I][J1][K-1])
					B=(XEN[I][J1][K-1]*YPP[I][J1][K]-XEN[I][J1][K]*YPP[I][J1][K-1])/(XEN[I][J1][K-1]-XEN[I][J1][K])
					XSECP[IPT]=math.exp(A*EPHLG+B)
					ABSLP[IPT]=XSECP[IPT]*ANGAS[I]
					# GO TO 50
					break
				# endif
				# 49 CONTINUE
			# 50 CONTINUE   
	# FORM CUMULATIVE SUMS 
	IFIN=NGAS*17*3
	for J in range(2,IFIN+1):
		XSEC[J]=XSEC[J]+XSEC[J-1]
		ABSL[J]=ABSL[J]+ABSL[J-1]
	IFINR=NGAS*3
	for J in range(2,IFINR+1):
		XSECC[J]=XSECC[J]+XSECC[J-1]
		ABSLC[J]=ABSLC[J]+ABSLC[J-1]
		XSECR[J]=XSECR[J]+XSECR[J-1]
		ABSLR[J]=ABSLR[J]+ABSLR[J-1]
		XSECP[J]=XSECP[J]+XSECP[J-1]
		ABSLP[J]=ABSLP[J]+ABSLP[J-1]
	# TOTAL X-SECTION
	XSECT=XSEC[IFIN]+XSECC[IFINR]+XSECR[IFINR]+XSECP[IFINR]
	# TOTAL ABS LENGTH
	ABSTOT=ABSL[IFIN]+ABSLR[IFINR]+ABSLC[IFINR]+ABSLP[IFINR]
	# CALCULATE ABSORPTION DISTANCE IN METRES AND RETURN
	if(JF == 3):
		DIST=1.0/(ABSTOT*100.0)
		return
	# endif
	# CALCULATE ABSORPTION DISTANCE IN MICRONS
	if(JF == -1):
		if(ABSTOT > 0.0):
			ABSXRAY=1.0e4/ABSTOT
		if(ABSTOT == 0.0):
			ABSXRAY=1.0e15
		return
	# endif
	if(ABSTOT == 0.0):
		# PHOTON TOO LOW ENERGY TO IONISE SET ISHELL=-1
		ISHELL=-1
		return
	# endif
	# NORMALISE TO 1 
	for J in range(1,IFIN+1):
		XSEC[J]=XSEC[J]/XSECT
	for J in range(1,IFINR+1):
		XSECC[J]=XSECC[J]/XSECT
		XSECR[J]=XSECR[J]/XSECT
		XSECP[J]=XSECP[J]/XSECT
	# FORM SUM X-SECTION FOR SAMPLING ARRAY 
	# P.E.
	for J in range(1,IFIN+1):
		XSUM[J]=XSEC[J]
	IEND=IFIN
	if(LCMP != 1):
		# GO TO 145 
		pass
	else:
		# COMPTON
		ISTART=IFIN+1
		IEND=IFIN+IFINR
		for J in range(ISTART,IEND+1):
			XSUM[J]=XSUM[ISTART-1]+XSECC[J-ISTART+1] 
	# 145 
	if(LRAY != 1):
		# GO TO 155
		pass
	else:
		# RAYLEIGH
		if(LCMP == 0):
			ISTART=IFIN+1
			IEND=IFIN+IFINR
		elif(LCMP == 1) :
			ISTART=IFIN+IFINR+1
			IEND=IFIN+IFINR+IFINR
		# endif
		for J in range(ISTART,IEND+1):
			XSUM[J]=XSUM[ISTART-1]+XSECR[J-ISTART+1]
	# 155 
	if(LPAP != 1):
		# GO TO 165
		pass
	else:
		# PAIR PRODUCTION
		if(LCMP == 0 and LRAY == 0):
			ISTART=IFIN+1
			IEND=IFIN+IFINR
		elif(LCMP == 0 and LRAY == 1) :
			ISTART=IFIN+IFINR+1
			IEND=IFIN+IFINR+IFINR
		elif(LCMP == 1 and LRAY == 0) :
			ISTART=IFIN+IFINR+1
			IEND=IFIN+IFINR+IFINR
		elif(LCMP == 1 and LRAY == 1) :
			ISTART=IFIN+IFINR+IFINR+1
			IEND=ISTART+IFINR+IFINR+IFINR
		else: 
			print(' ERROR IN FUNCTION ABSO FLAG NOT CORRECT')
			sys.exit()
		# endif
		for J in range(ISTART,IEND+1):
			XSUM[J]=XSUM[ISTART-1]+XSECP[J-ISTART+1]
	# 165 CONTINUE 
	# FIND GAS AND SHELL
	R1=DRAND48(RDUM)
	for J in range(1,IEND+1):
		if(XSUM[J]< R1):
			# GO TO 4
			continue
		ID=J
		# GO TO 5
		break
	# 4 CONTINUE
	# LOCATE GAS AND SHELL
	# 5 
	flag200=0
	IPET=NGAS*3*17
	if(ID > IPET):
		# GO TO 22
		pass
	else:
		# PHOTO ELECTRIC
		LPEFLG=1
		if(ID <= 51):
			KGAS=1
			if(ID <= 17):
				LGAS=1
				ISHELL=ID
			elif(ID <= 34) :
				LGAS=2
				ISHELL=ID-17
			else:
				LGAS=3
				ISHELL=ID-34
			# endif
			# GO TO 12		
		elif(ID <= 102) :
			KGAS=2
			if(ID <= 68):
				LGAS=1
				ISHELL=ID-51
			elif(ID <= 85) :
				LGAS=2
				ISHELL=ID-68
			else:
				LGAS=3
				ISHELL=ID-85
			# endif
			# GO TO 12
		elif(ID <= 153) :
			KGAS=3
			if(ID <= 119):
				LGAS=1
				ISHELL=ID-102
			elif(ID <= 136) :
				LGAS=2
				ISHELL=ID-119
			else:
				LGAS=3
				ISHELL=ID-136
			# endif
			# GO TO 12
		elif(ID <= 204) :
			KGAS=4
			if(ID <= 170):
				LGAS=1
				ISHELL=ID-153
			elif(ID <= 187) :
				LGAS=2
				ISHELL=ID-170
			else:
				LGAS=3
				ISHELL=ID-187
			# endif
			# GO TO 12
		elif(ID <= 255) :
			KGAS=5
			if(ID <= 221):
				LGAS=1
				ISHELL=ID-204
			elif(ID <= 238) :
				LGAS=2
				ISHELL=ID-221
			else:
				LGAS=3
				ISHELL=ID-238
			# endif
			# GO TO 12
		else: 
			KGAS=6
			if(ID <= 272):
				LGAS=1
				ISHELL=ID-255
			elif(ID <= 289) :
				LGAS=2
				ISHELL=ID-272
			else:
				LGAS=3
				ISHELL=ID-289
			# endif
		# endif
		# 12 CONTINUE
		flag200=1
		# COMPTON RAYLEIGH OR PAIR PRODUCTION
	# 22 
	if(flag200):
		pass
	else:
		ISHELL=0
		if(ID <= (IPET+IFINR)) :
			# COMPTON RAYLEIGH OR PAIR PRODUCTION.   SET :  FLAG KGAS LGAS
			if(LCMP == 1):
				LCFLG=1
			if(LCMP == 0 and LRAY == 1):
				LRFLG=1
			if(LCMP == 0 and LRAY == 0):
				LPFLG=1
			if(ID <= IPET+3):
				KGAS=1
				LGAS=ID-IPET
			elif(ID <= IPET+6) :
				KGAS=2
				LGAS=ID-IPET-3
			elif(ID <= IPET+9) : 
				KGAS=3
				LGAS=ID-IPET-6 
			elif(ID <= IPET+12) :
				KGAS=4
				LGAS=ID-IPET-9
			elif(ID <= IPET+15) :
				KGAS=5
				LGAS=ID-IPET-12
			else:
				KGAS=6
				LGAS=ID-IPET-15
		# endif
		elif (ID <= IPET+2*IFINR) :
			if(LRAY == 1):
				LRFLG=1
			if(LRAY == 0 and LPAP == 1):
				LPFLG=1
			if(ID <= IPET+IFINR+3):
				KGAS=1
				LGAS=ID-IPET-IFINR
			elif(ID <= IPET+IFINR+6) :
				KGAS=2
				LGAS=ID-IPET-IFINR-3
			elif(ID <= IPET+IFINR+9) : 
				KGAS=3
				LGAS=ID-IPET-IFINR-6
			elif(ID <= IPET+IFINR+12) :
				KGAS=4
				LGAS=ID-IPET-IFINR-9
			elif(ID <= IPET+IFINR+15) :
				KGAS=5
				LGAS=ID-IPET-IFINR-12
			else:
				KGAS=6
				LGAS=ID-IPET-IFINR-15
			# endif
		else: 
			LPFLG=1
			if(ID <= IPET+3*IFINR):
				KGAS=1
				LGAS=ID-IPET-IFINR-IFINR
			elif(ID <= IPET+IFINR+IFINR+6) :
				KGAS=2
				LGAS=ID-IPET-IFINR-IFINR-3
			elif(ID <= IPET+IFINR+IFINR+9) : 
				KGAS=3
				LGAS=ID-IPET-IFINR-IFINR-6
			elif(ID <= IPET+IFINR+IFINR+12) :
				KGAS=4
				LGAS=ID-IPET-IFINR-IFINR-9
			elif(ID <= IPET+IFINR+IFINR+15) :
				KGAS=5
				LGAS=ID-IPET-IFINR-IFINR-12
			else:
				KGAS=6
				LGAS=ID-IPET-IFINR-IFINR-15
			# endif
		# endif
		if(ID > (IPET+54)) :
			print(' IDENTifIER IN FUNCTION ABSO IS GT LIMIT ID=',ID,'\n    def STOPPED:')
			sys.exit()
		# endif
	# 200 CONTINUE
	# CALCULATE ABSORPTION DISTANCE PER EVENT IN METRES
	R1=DRAND48(RDUM)  
	DIST=-math.log(R1)/(ABSTOT*100.0)
	return
	# end