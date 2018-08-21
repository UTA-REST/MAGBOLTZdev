## DENSITY()
### Arguments

| Argument | Description |
|----------|-------------|
| NONE     | -           |
|          |             |

### Pseudo Code
* Initialize data arrays
* Calculate Density Correction Array `DEN[20000+1]`

```python
def DENSITY():
	#IMPLICIT #real*8 (A-H,O-Z)
	#IMPLICIT #integer*8 (I-N)
	global DEN #=[0 for x in range(20000)]
	global AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC #=[0 for x in range(6)]
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	global NGASN #=[0 for x in range[6]]
	global BET#=[0 for x in range(2000)]
	global GAM#=[0 for x in range(20000)]
	global VC,EMS
	###############################################
	DEN=conf.DEN
	AN1=conf.AN1
	AN2=conf.AN2
	AN3=conf.AN3
	AN4=conf.AN4
	AN5=conf.AN5
	AN6=conf.AN6
	AN=conf.AN
	FRAC=conf.FRAC
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
	NGASN=conf.NGASN
	BET=conf.BET
	GAM=conf.GAM
	VC=conf.VC
	EMS=conf.EMS
	###############################################
	AND=numpy.zeros(6+1)
	EIAV=numpy.zeros(80+1)
	X00=numpy.zeros(80+1)
	X11=numpy.zeros(80+1)
	AKS=numpy.zeros(80+1)
	AAA=numpy.zeros(80+1)
	JELEC=numpy.zeros(80+1)
	# DENSITY EFFECT CONSTANTS
	# EIAV ENERGY IN EV
	# JELEC NUMBER OF ELECTRONS PER ATOM OR MOLECULE
	EIAV=[0,115.0,188.0,41.8,41.8,137.0,352.0,482.0,41.7,45.4,47.1,48.3,85.0,0.0,71.6,95.0,82.0,0.0,0.0,0.0,0.0,19.2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,128.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,48.3,*36*[0.0]]
	# print(len(EIAV))
	JELEC=[0,42,18,2,2,10,36,54,10,18,26,34,22,0,10,16,14,0,0,0,0,2,0,0,0,0,0,0,0,0,70,0,0,0,0,0,0,0,0,0,0,0,0,0,34]+36*[0]
	X00=[0,1.70,1.7635,2.2017,2.2017,2.0735,1.7158,1.5630,1.6263,1.5090,1.4339,1.3788,1.6294,0.0,1.7952,1.7541,1.7378,0.0,0.0,0.0,0.0,1.8639,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.6,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.3788,*36*[0.0]]
	X11=[0,4.00,4.4855,3.6122,3.6122,4.6421,5.0748,4.7371,3.9716,3.8726,3.8011,3.7524,4.1825,0.0,4.3437,4.3213,4.1323,0.0,0.0,0.0,0.0,3.2718,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.7524,*36*[0.0]]
	AKS=[0,3.00,2.9618,5.8347,5.8347,3.5771,3.4051,2.7414,3.6257,3.6095,3.5920,3.4884,3.3227,0.0,3.5901,3.2913,3.2125,0.0,0.0,0.0,0.0,5.7273,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.4884,*36*[0.0]]
	AAA=[0,.18551,.19714,.13443,.13443,.08064,.07446,.23314,.09253,0.09627,0.09916,.10852,.11768,0.0,.08101,.11778,.15349,0.0,0.0,0.0,0.0,.14092,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,.177484,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,.10852,*36*[0.0]]
	#
	API=numpy.arccos(-1.00)                                                 
	EMS=510998.9280
	RE=2.8179403267*(10**-13)
	ALPH=137.035999074
	ABZERO=273.150                                                   
	ATMOS=760.00                                                     
	#                                                                       
	# DENSITY EFFECT CALCULATION
	AND[1]=AN1
	AND[2]=AN2
	AND[3]=AN3
	AND[4]=AN4
	AND[5]=AN5
	AND[6]=AN6
	HSUM=0.0
	SUM1=0.0
	SUMDNOM=0.0
	# print(NGAS)
	for L1 in range(1,NGAS+1):
		# print("E",EIAV[int(NGASN[L1])],NGASN[L1])
		SUM1=SUM1+FRAC[L1]*float(JELEC[int(NGASN[L1])])*math.log(EIAV[int(NGASN[L1])]) 
		SUMDNOM=SUMDNOM+FRAC[L1]*float(JELEC[int(NGASN[L1])])
		HSUM=HSUM+AND[L1]*float(JELEC[int(NGASN[L1])])  #22385
	EIBAR=math.exp(SUM1/SUMDNOM)
	# PLASMA ENERGY
	HWP1=math.sqrt(4.0*API*HSUM*RE**3)*ALPH*EMS
	#
	DELDEN=math.log(EIBAR/HWP1)
	CBAR=1.0+2.0*DELDEN
	flag=0   #SELF ADDED
	if(NGAS == 1):  #22392
 		flag=1
	# CALC X0 AND X1
	if(CBAR < 10.0):
		X0=1.6
		X1=4.0
	elif(CBAR >= 4.0 and CBAR < 10.5) :
		X0=1.7
		X1=4.0
	elif(CBAR >= 10.5 and CBAR < 11.0) :
		X0=1.8
		X1=4.0
	elif(CBAR >= 11.0 and CBAR < 11.5) :
		X0=1.9
		X1=4.0
	elif(CBAR >= 11.5 and CBAR < 12.25) :
		X0=2.0
		X1=4.0
	elif(CBAR >= 12.25 and CBAR < 13.804) :
		X0=2.0
		X1=5.0
	else: 
		X0=0.326*CBAR-1.5
		X1=5.0
	# endif
	if(flag==1):
		AKBAR=3.0
		ABAR=(CBAR-2.0*math.log(10.00)*X0)/((X1-X0)**3)
	elif(flag==0):
		AKBAR=AKS[int(NGASN[1])]
		X0=X00[int(NGASN[1])]
		X1=X11[int(NGASN[1])]
		ABAR=AAA[int(NGASN[1])]
	else:
		pass
	# CORRECT X0 AND X1 FOR DENSITY CHANGE FROM 20C AND 760 TORR
	# NB CORRECTION TO CBAR ALREADY DONE
	DCOR=0.5*math.log10(TORR*293.15/(760.0*(TEMPC+ABZERO)))
	X0=X0-DCOR
	X1=X1-DCOR
	# CALCULATE DENSITY CORRECTION FACTOR ARRAY DEN(20000)
	AFC=2.0*math.log(10.00)
	for I in range(1,20000+1):
		BG=BET[I]*GAM[I]
		X=math.log10(BG)
		if(X < X0):
			DEN[I]=0.0
		elif(X > X0 and X < X1) :
			DEN[I]=ABAR*math.exp(AKBAR*math.log(X1-X))+AFC*X-CBAR
		else: 
			DEN[I]=AFC*X-CBAR              
		# endif
		#     WRITE(6,99) DEN[I]
		#  99 print(' DENSITY CORRECTION=',D12.5)
	conf.DEN=DEN
	conf.AN1=AN1
	conf.AN2=AN2
	conf.AN3=AN3
	conf.AN4=AN4
	conf.AN5=AN5
	conf.AN6=AN6
	conf.AN=AN
	conf.FRAC=FRAC
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
	conf.NGASN=NGASN
	conf.BET=BET
	conf.GAM=GAM
	conf.VC=VC
	conf.EMS=EMS	
	return
	# end
```

```fortran
      SUBROUTINE DENSITY
      IMPLICIT REAL*8 (A-H,O-Z)
      IMPLICIT INTEGER*8 (I-N)
      COMMON/DENS/DEN(20000)
      COMMON/RATIO/AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC(6)
      COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
      COMMON/GASN/NGASN(6)
      COMMON/RLTVY/BET(20000),GAM(20000),VC,EMS
      DIMENSION AND(6),EIAV(80),X00(80),X11(80),AKS(80),AAA(80),
     /JELEC(80)
C DENSITY EFFECT CONSTANTS
C EIAV ENERGY IN EV
C JELEC NUMBER OF ELECTRONS PER ATOM OR MOLECULE
      DATA EIAV/115.0,188.0,41.8,41.8,137.0,352.0,482.0,41.7,45.4,47.1,
     /48.3,85.0,0.0,71.6,95.0,82.0,0.0,0.0,0.0,0.0,
     /19.2,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,128.0,
     /0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
     /0.0,0.0,0.0,48.3,
     /36*0.0/
      DATA JELEC/42,18,2,2,10,36,54,10,18,26,
     /34,22,0,10,16,14,0,0,0,0,
     /2,0,0,0,0,0,0,0,0,70,
     /0,0,0,0,0,0,0,0,0,0,
     /0,0,0,34,
     /36*0/
      DATA X00/1.70,1.7635,2.2017,2.2017,2.0735,1.7158,1.5630,1.6263,
     /1.5090,1.4339,
     /1.3788,1.6294,0.0,1.7952,1.7541,1.7378,0.0,0.0,0.0,0.0,
     /1.8639,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.6,
     /0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
     /0.0,0.0,0.0,1.3788,
     /36*0.0/
      DATA X11/4.00,4.4855,3.6122,3.6122,4.6421,5.0748,4.7371,3.9716,
     /3.8726,3.8011,
     /3.7524,4.1825,0.0,4.3437,4.3213,4.1323,0.0,0.0,0.0,0.0,
     /3.2718,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,4.0,
     /0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
     /0.0,0.0,0.0,3.7524,
     /36*0.0/
      DATA AKS/3.00,2.9618,5.8347,5.8347,3.5771,3.4051,2.7414,3.6257,
     /3.6095,3.5920,
     /3.4884,3.3227,0.0,3.5901,3.2913,3.2125,0.0,0.0,0.0,0.0,
     /5.7273,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,3.0,
     /0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
     /0.0,0.0,0.0,3.4884,
     /36*0.0/
      DATA AAA/.18551,.19714,.13443,.13443,.08064,.07446,.23314,.09253,
     /0.09627,0.09916,
     /.10852,.11768,0.0,.08101,.11778,.15349,0.0,0.0,0.0,0.0,
     /.14092,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,.177484,
     /0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,
     /0.0,0.0,0.0,.10852,
     /36*0.0/
C
      API=DACOS(-1.0D0)                                                 
      EMS=510998.928D0
      RE=2.8179403267D-13    
      ALPH=137.035999074
      ABZERO=273.15D0                                                   
      ATMOS=760.0D0                                                     
C                                                                       
C DENSITY EFFECT CALCULATION
      AND(1)=AN1
      AND(2)=AN2
      AND(3)=AN3
      AND(4)=AN4
      AND(5)=AN5
      AND(6)=AN6
      HSUM=0.0
      SUM1=0.0
      SUMDNOM=0.0
      DO 120 L1=1,NGAS
      SUM1=SUM1+FRAC(L1)*DFLOAT(JELEC(NGASN(L1)))*DLOG(EIAV(NGASN(L1))) 
      SUMDNOM=SUMDNOM+FRAC(L1)*DFLOAT(JELEC(NGASN(L1)))
  120 HSUM=HSUM+AND(L1)*DFLOAT(JELEC(NGASN(L1)))
      EIBAR=DEXP(SUM1/SUMDNOM)
C PLASMA ENERGY
      HWP1=DSQRT(4.0*API*HSUM*RE**3)*ALPH*EMS
C
      DELDEN=DLOG(EIBAR/HWP1)
      CBAR=1.0+2.0*DELDEN
      IF(NGAS.EQ.1) GO TO 200
C CALC X0 AND X1
      IF(CBAR.LT.10.0) THEN
      X0=1.6
      X1=4.0
      ELSE IF(CBAR.GE.4.0.AND.CBAR.LT.10.5) THEN
      X0=1.7
      X1=4.0
      ELSE IF(CBAR.GE.10.5.AND.CBAR.LT.11.0) THEN
      X0=1.8
      X1=4.0
      ELSE IF(CBAR.GE.11.0.AND.CBAR.LT.11.5) THEN
      X0=1.9
      X1=4.0
      ELSE IF(CBAR.GE.11.5.AND.CBAR.LT.12.25) THEN
      X0=2.0
      X1=4.0
      ELSE IF(CBAR.GE.12.25.AND.CBAR.LT.13.804) THEN
      X0=2.0
      X1=5.0
      ELSE 
      X0=0.326*CBAR-1.5
      X1=5.0
      ENDIF
      AKBAR=3.0
      ABAR=(CBAR-2.0*DLOG(10.0D0)*X0)/((X1-X0)**3)
      GO TO 201
  200 AKBAR=AKS(NGASN(1))
      X0=X00(NGASN(1))
      X1=X11(NGASN(1))
      ABAR=AAA(NGASN(1))
  201 CONTINUE
C CORRECT X0 AND X1 FOR DENSITY CHANGE FROM 20C AND 760 TORR
C NB CORRECTION TO CBAR ALREADY DONE
      DCOR=0.5*DLOG10(TORR*293.15/(760.0*(TEMPC+ABZERO)))
      X0=X0-DCOR
      X1=X1-DCOR
C CALCULATE DENSITY CORRECTION FACTOR ARRAY DEN(20000)
      AFC=2.0*DLOG(10.0D0)
      DO 236 I=1,20000
      BG=BET(I)*GAM(I)
      X=DLOG10(BG)
      IF(X.LT.X0) THEN   
       DEN(I)=0.0
      ELSE IF(X.GT.X0.AND.X.LT.X1) THEN
       DEN(I)=ABAR*DEXP(AKBAR*DLOG(X1-X))+AFC*X-CBAR
      ELSE 
       DEN(I)=AFC*X-CBAR              
      ENDIF
C     WRITE(6,99) DEN(I)
C  99 FORMAT(' DENSITY CORRECTION=',D12.5)
  236 CONTINUE
      RETURN
      END
```

