## ABSO()

### Arguments
| Argument |                    Description                    |
|----------|---------------------------------------------------|
| JF       |                                                   |
| EPH      | For photon energy calculates interaction distance |
|          | with Gas identity, KGAS.                          |
|          | If compton rayleigh or pair production allowed    |
|          | then calculates KGAS, LGAS                        |
| ISHELL   | Absorption Shell                                  |
| KGAS     | Gas Identity                                      |
| LGAS     |                                                   |
| DIST     | Absorption distance per event in metres           |
|          |                                                   |

### Pseudo Code

```python
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
```

```fortran
      SUBROUTINE ABSO(JF,EPH,ISHELL,KGAS,LGAS,DIST)
      IMPLICIT REAL*8 (A-H,O-Z)
      IMPLICIT INTEGER*8 (I-N)
      COMMON/RATIO/AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC(6)  
      COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
      COMMON/ABBS/ABSXRAY             
      COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
      COMMON/MIXC/PRSH(6,3,17,17),ESH(6,3,17),AUG(6,3,17,17,17),
     /RAD(6,3,17,17),PRSHBT(6,3,17),IZ(6,3),INIOCC(6,3,17),ISHLMX(6,3),
     /AMZ(6,3)
      COMMON/MIXPE/XPE(6,3,17,60),YPE(6,3,17,60)
      COMMON/MIXCN/XEN(6,3,54),YRY(6,3,54),YCP(6,3,54),YPP(6,3,54)
      DIMENSION XSEC(306),XSECC(18),XSECR(18),XSECP(18),
     /ANGAS(6),ABSL(306),ABSLC(18),ABSLR(18),ABSLP(18),XSUM(360)
C******************************************************************
C FOR PHOTON ENERGY EPH CALCULATES INTERACTION DISTANCE WITH
C  GAS IDENTITY,KGAS . IF MOLECULAR GAS ALSO IDENTIFIES THE 
C  ATOMIC COMPONENT OF THE MOLECULE  LGAS. 
C  IF PHOTOELECTRIC ABSORPTION CALCULATES ABSORPTION SHELL, ISHELL
C AND SETS PHOTOELECTRIC FLAG,LPEFLG=1. 
C IF COMPTON RAYLEIGH OR PAIR PRODUCTION ALLOWED THEN CALCULATES
C KGAS , LGAS AND SETS COMPTON RAYLEIGH OR PAIR PRODUCTION FLAGS.
C****************************************************************** 
      ANGAS(1)=AN1
      ANGAS(2)=AN2
      ANGAS(3)=AN3
      ANGAS(4)=AN4
      ANGAS(5)=AN5
      ANGAS(6)=AN6
      LCFLG=0
      LRFLG=0
      LPFLG=0
      LPEFLG=0
C CALCULATE PE X-SECTION FOR EACH GAS AND FIND ABS LENGTH 
      EPHLG=DLOG(EPH)
      IPT=0
      DO 1 I=1,NGAS
      DO 1 J1=1,3
      DO 1 J=1,17
      IPT=IPT+1
      XSEC(IPT)=0.0
      ABSL(IPT)=0.0
      IF(J.GT.ISHLMX(I,J1)) GO TO 1
      IF(EPHLG.LT.XPE(I,J1,J,1)) GO TO 1
      DO 11 K=2,60 
      IF(EPHLG.LE.XPE(I,J1,J,K)) THEN
       A=(YPE(I,J1,J,K)-YPE(I,J1,J,K-1))/(XPE(I,J1,J,K)-XPE(I,J1,J,K-1))
       B=(XPE(I,J1,J,K-1)*YPE(I,J1,J,K)-XPE(I,J1,J,K)*YPE(I,J1,J,K-1))/
     /(XPE(I,J1,J,K-1)-XPE(I,J1,J,K))
       XSEC(IPT)=DEXP(A*EPHLG+B)
       ABSL(IPT)=XSEC(IPT)*ANGAS(I)
       GO TO 1
      ENDIF
   11 CONTINUE
    1 CONTINUE
C CALCULATE COMPTON X-SECTION FOR EACH GAS AND FIND ABS LENGTH
      IPT=0
      DO 30 I=1,NGAS
      DO 30 J1=1,3   
      IPT=IPT+1
      XSECC(IPT)=0.0
      ABSLC(IPT)=0.0
C USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
      IF(JF.EQ.3.OR.JF.EQ.2) GO TO 30
C ONLY USE PE X-SECTION
      IF(LCMP.NE.1) GO TO 30
      IF(EPHLG.LT.XEN(I,J1,1)) GO TO 30
      DO 29 K=2,54
      IF(EPHLG.LE.XEN(I,J1,K)) THEN
       A=(YCP(I,J1,K)-YCP(I,J1,K-1))/(XEN(I,J1,K)-XEN(I,J1,K-1))
       B=(XEN(I,J1,K-1)*YCP(I,J1,K)-XEN(I,J1,K)*YCP(I,J1,K-1))/
     /(XEN(I,J1,K-1)-XEN(I,J1,K))
       XSECC(IPT)=DEXP(A*EPHLG+B)
       ABSLC(IPT)=XSECC(IPT)*ANGAS(I)
       GO TO 30 
      ENDIF
   29 CONTINUE
   30 CONTINUE
C CALCULATE RAYLEIGH X-SECTION FOR EACH GAS AND FIND ABS LENGTH
      IPT=0
      DO 40 I=1,NGAS
      DO 40 J1=1,3   
      IPT=IPT+1
      XSECR(IPT)=0.0
      ABSLR(IPT)=0.0
C USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
      IF(JF.EQ.3.OR.JF.EQ.2) GO TO 40
      IF(LRAY.NE.1) GO TO 40
      IF(EPHLG.LT.XEN(I,J1,1)) GO TO 40
      DO 39 K=2,54
      IF(EPHLG.LE.XEN(I,J1,K)) THEN
       A=(YRY(I,J1,K)-YRY(I,J1,K-1))/(XEN(I,J1,K)-XEN(I,J1,K-1))
       B=(XEN(I,J1,K-1)*YRY(I,J1,K)-XEN(I,J1,K)*YRY(I,J1,K-1))/
     /(XEN(I,J1,K-1)-XEN(I,J1,K))
       XSECR(IPT)=DEXP(A*EPHLG+B)
       ABSLR(IPT)=XSECR(IPT)*ANGAS(I)
       GO TO 40
      ENDIF
   39 CONTINUE
   40 CONTINUE   
C CALCULATE PAIR PRODUCTION X-SECTION FOR EACH GAS AND FIND ABS LENGTH 
      IPT=0
      DO 50 I=1,NGAS
      DO 50 J1=1,3
      IPT=IPT+1
      XSECP(IPT)=0.0
      ABSLP(IPT)=0.0
C USE ONLY PE X-SECTION FOR SECOND STAGE FLUORESCENCE 
      IF(JF.EQ.3.OR.JF.EQ.2) GO TO 50
      IF(LPAP.NE.1) GO TO 50
      IF(EPHLG.LT.XEN(I,J1,1)) GO TO 50
      DO 49 K=2,54
      IF(EPHLG.LE.XEN(I,J1,K)) THEN
       A=(YPP(I,J1,K)-YPP(I,J1,K-1))/(XEN(I,J1,K)-XEN(I,J1,K-1))
       B=(XEN(I,J1,K-1)*YPP(I,J1,K)-XEN(I,J1,K)*YPP(I,J1,K-1))/
     /(XEN(I,J1,K-1)-XEN(I,J1,K))
       XSECP(IPT)=DEXP(A*EPHLG+B)
       ABSLP(IPT)=XSECP(IPT)*ANGAS(I)
       GO TO 50
      ENDIF
   49 CONTINUE
   50 CONTINUE   
C FORM CUMULATIVE SUMS 
      IFIN=NGAS*17*3
      DO 2 J=2,IFIN
      XSEC(J)=XSEC(J)+XSEC(J-1)
      ABSL(J)=ABSL(J)+ABSL(J-1)
    2 CONTINUE 
      IFINR=NGAS*3
      DO 110 J=2,IFINR
      XSECC(J)=XSECC(J)+XSECC(J-1)
      ABSLC(J)=ABSLC(J)+ABSLC(J-1)
      XSECR(J)=XSECR(J)+XSECR(J-1)
      ABSLR(J)=ABSLR(J)+ABSLR(J-1)
      XSECP(J)=XSECP(J)+XSECP(J-1)
      ABSLP(J)=ABSLP(J)+ABSLP(J-1)
  110 CONTINUE 
C TOTAL X-SECTION
      XSECT=XSEC(IFIN)+XSECC(IFINR)+XSECR(IFINR)+XSECP(IFINR)
C TOTAL ABS LENGTH
      ABSTOT=ABSL(IFIN)+ABSLR(IFINR)+ABSLC(IFINR)+ABSLP(IFINR)
C CALCULATE ABSORPTION DISTANCE IN METRES AND RETURN
      IF(JF.EQ.3) THEN
       DIST=1.0/(ABSTOT*100.0)
       RETURN
      ENDIF
C CALCULATE ABSORPTION DISTANCE IN MICRONS
      IF(JF.EQ.-1) THEN 
       IF(ABSTOT.GT.0.0) ABSXRAY=1.0D4/ABSTOT
       IF(ABSTOT.EQ.0.0) ABSXRAY=1.0D15
       RETURN
      ENDIF
      IF(ABSTOT.EQ.0.0) THEN
C PHOTON TOO LOW ENERGY TO IONISE SET ISHELL=-1
       ISHELL=-1
       RETURN
      ENDIF
C NORMALISE TO 1 
      DO 3 J=1,IFIN
      XSEC(J)=XSEC(J)/XSECT
    3 CONTINUE
      DO 120 J=1,IFINR
      XSECC(J)=XSECC(J)/XSECT
      XSECR(J)=XSECR(J)/XSECT
      XSECP(J)=XSECP(J)/XSECT
  120 CONTINUE
C FORM SUM X-SECTION FOR SAMPLING ARRAY 
C P.E.
      DO 130 J=1,IFIN
      XSUM(J)=XSEC(J)
  130 CONTINUE
      IEND=IFIN
      IF(LCMP.NE.1) GO TO 145 
C COMPTON
      ISTART=IFIN+1
      IEND=IFIN+IFINR
      DO 140 J=ISTART,IEND
      XSUM(J)=XSUM(ISTART-1)+XSECC(J-ISTART+1) 
  140 CONTINUE
  145 IF(LRAY.NE.1) GO TO 155
C RAYLEIGH
      IF(LCMP.EQ.0) THEN 
       ISTART=IFIN+1
       IEND=IFIN+IFINR
       ELSE IF(LCMP.EQ.1) THEN
       ISTART=IFIN+IFINR+1
       IEND=IFIN+IFINR+IFINR
      ENDIF
      DO 150 J=ISTART,IEND
      XSUM(J)=XSUM(ISTART-1)+XSECR(J-ISTART+1)
  150 CONTINUE
  155 IF(LPAP.NE.1) GO TO 165
C PAIR PRODUCTION
      IF(LCMP.EQ.0.AND.LRAY.EQ.0) THEN
       ISTART=IFIN+1
       IEND=IFIN+IFINR
      ELSE IF(LCMP.EQ.0.AND.LRAY.EQ.1) THEN
       ISTART=IFIN+IFINR+1
       IEND=IFIN+IFINR+IFINR
      ELSE IF(LCMP.EQ.1.AND.LRAY.EQ.0) THEN
       ISTART=IFIN+IFINR+1
       IEND=IFIN+IFINR+IFINR
      ELSE IF(LCMP.EQ.1.AND.LRAY.EQ.1) THEN
       ISTART=IFIN+IFINR+IFINR+1
       IEND=ISTART+IFINR+IFINR+IFINR
      ELSE 
       WRITE(6,998)
  998  FORMAT(' ERROR IN SUBROUTINE ABSO FLAG NOT CORRECT')
       STOP
      ENDIF
      DO 160 J=ISTART,IEND
      XSUM(J)=XSUM(ISTART-1)+XSECP(J-ISTART+1)
  160 CONTINUE
  165 CONTINUE 
C FIND GAS AND SHELL
      R1=drand48(RDUM)
      DO 4 J=1,IEND
      IF(XSUM(J).LT.R1) GO TO 4
       ID=J
       GO TO 5
    4 CONTINUE
C LOCATE GAS AND SHELL
    5 IPET=NGAS*3*17
      IF(ID.GT.IPET) GO TO 22
C PHOTO ELECTRIC
      LPEFLG=1
      IF(ID.LE.51) THEN
       KGAS=1
       IF(ID.LE.17) THEN
        LGAS=1
        ISHELL=ID
       ELSE IF(ID.LE.34) THEN
        LGAS=2
        ISHELL=ID-17
       ELSE
        LGAS=3
        ISHELL=ID-34
       ENDIF
       GO TO 12
      ELSE IF(ID.LE.102) THEN
       KGAS=2
       IF(ID.LE.68) THEN
        LGAS=1
        ISHELL=ID-51
       ELSE IF(ID.LE.85) THEN
        LGAS=2
        ISHELL=ID-68
       ELSE
        LGAS=3
        ISHELL=ID-85
       ENDIF
       GO TO 12
      ELSE IF(ID.LE.153) THEN
       KGAS=3
       IF(ID.LE.119) THEN
        LGAS=1
        ISHELL=ID-102
       ELSE IF(ID.LE.136) THEN
        LGAS=2
        ISHELL=ID-119
       ELSE
        LGAS=3
        ISHELL=ID-136
       ENDIF
       GO TO 12
      ELSE IF(ID.LE.204) THEN
       KGAS=4
       IF(ID.LE.170) THEN
        LGAS=1
        ISHELL=ID-153
       ELSE IF(ID.LE.187) THEN
        LGAS=2
        ISHELL=ID-170
       ELSE
        LGAS=3
        ISHELL=ID-187
       ENDIF
       GO TO 12
      ELSE IF(ID.LE.255) THEN
       KGAS=5
       IF(ID.LE.221) THEN
        LGAS=1
        ISHELL=ID-204
       ELSE IF(ID.LE.238) THEN
        LGAS=2
        ISHELL=ID-221
       ELSE
        LGAS=3
        ISHELL=ID-238
       ENDIF
       GO TO 12
      ELSE 
       KGAS=6
       IF(ID.LE.272) THEN
        LGAS=1
        ISHELL=ID-255
       ELSE IF(ID.LE.289) THEN
        LGAS=2
        ISHELL=ID-272
       ELSE
        LGAS=3
        ISHELL=ID-289
       ENDIF
      ENDIF
   12 CONTINUE
      GO TO 200
C COMPTON RAYLEIGH OR PAIR PRODUCTION
   22 ISHELL=0
      IF(ID.LE.(IPET+IFINR)) THEN
C COMPTON RAYLEIGH OR PAIR PRODUCTION.   SET :  FLAG KGAS LGAS
       IF(LCMP.EQ.1) LCFLG=1
       IF(LCMP.EQ.0.AND.LRAY.EQ.1) LRFLG=1
       IF(LCMP.EQ.0.AND.LRAY.EQ.0) LPFLG=1
       IF(ID.LE.IPET+3) THEN
        KGAS=1
        LGAS=ID-IPET
       ELSE IF(ID.LE.IPET+6) THEN
        KGAS=2
        LGAS=ID-IPET-3
       ELSE IF(ID.LE.IPET+9) THEN 
        KGAS=3
        LGAS=ID-IPET-6 
       ELSE IF(ID.LE.IPET+12) THEN
        KGAS=4
        LGAS=ID-IPET-9
       ELSE IF(ID.LE.IPET+15) THEN
        KGAS=5
        LGAS=ID-IPET-12
       ELSE
        KGAS=6
        LGAS=ID-IPET-15
       ENDIF
      ELSE IF (ID.LE.IPET+2*IFINR) THEN
       IF(LRAY.EQ.1) LRFLG=1
       IF(LRAY.EQ.0.AND.LPAP.EQ.1) LPFLG=1
       IF(ID.LE.IPET+IFINR+3) THEN
        KGAS=1
        LGAS=ID-IPET-IFINR
       ELSE IF(ID.LE.IPET+IFINR+6) THEN
        KGAS=2
        LGAS=ID-IPET-IFINR-3
       ELSE IF(ID.LE.IPET+IFINR+9) THEN 
        KGAS=3
        LGAS=ID-IPET-IFINR-6
       ELSE IF(ID.LE.IPET+IFINR+12) THEN
        KGAS=4
        LGAS=ID-IPET-IFINR-9
       ELSE IF(ID.LE.IPET+IFINR+15) THEN
        KGAS=5
        LGAS=ID-IPET-IFINR-12
       ELSE
        KGAS=6
        LGAS=ID-IPET-IFINR-15
       ENDIF
      ELSE 
       LPFLG=1
       IF(ID.LE.IPET+3*IFINR) THEN
        KGAS=1
        LGAS=ID-IPET-IFINR-IFINR
       ELSE IF(ID.LE.IPET+IFINR+IFINR+6) THEN
        KGAS=2
        LGAS=ID-IPET-IFINR-IFINR-3
       ELSE IF(ID.LE.IPET+IFINR+IFINR+9) THEN 
        KGAS=3
        LGAS=ID-IPET-IFINR-IFINR-6
       ELSE IF(ID.LE.IPET+IFINR+IFINR+12) THEN
        KGAS=4
        LGAS=ID-IPET-IFINR-IFINR-9
       ELSE IF(ID.LE.IPET+IFINR+IFINR+15) THEN
        KGAS=5
        LGAS=ID-IPET-IFINR-IFINR-12
       ELSE
        KGAS=6
        LGAS=ID-IPET-IFINR-IFINR-15
       ENDIF
      ENDIF
      IF(ID.GT.(IPET+54)) THEN
       WRITE(6,999) ID
  999 FORMAT(' IDENTIFIER IN SUBROUTINE ABSO IS GT LIMIT ID=',I5,/,'    
     /PROGRAM STOPPED')
       STOP
      ENDIF
  200 CONTINUE
C CALCULATE ABSORPTION DISTANCE PER EVENT IN METRES
      R1=drand48(RDUM)  
      DIST=-DLOG(R1)/(ABSTOT*100.0)
      RETURN
      END
```

