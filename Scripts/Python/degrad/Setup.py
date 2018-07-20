import numpy
import math
import sys
def SETUP(LAST):
	def GOTO999():
		print("in GOTO999")
		print(NGASN,FRAC)
		print(' ERROR IN GAS INPUT : NGAS=',NGAS,'\n')
		for J in range(1,6+1):
			# print(J)
			print(' N=',J,' NGAS=',NGASN[J],' FRAC=',FRAC[J])
		LAST=1                                                            
		return
	#IMPLICIT #real*8 (A-H,O-Z) 
	#IMPLICIT #integer*8 (I-N) 
	#integer*4 NSEED                                       
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	global ECHARG,EMASS,AMU,PIR2
	global KGAS,LGAS,DETEFF,EXCWGHT
	global NDVEC,CONST1,CONST2,CONST3,CONST4,CONST5                  
	global AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC #=[0 for x in range[6]]               
	global NGASN #=[0 for x in range[6]]                                 
	global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX #=[0 for x in range(10)]
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE
	global DRXINIT,DRYINIT,DRZINIT
	global EOVB,WB,BTHETA,BMAG 
	global DOUBLE #=[[0 for x in range[6]] for y in range(20000)]
	global AVPFRAC #=[[0 for x in range(3)] for y in range(6)]
	global CMINIXSC #=[0 for x in range[6]]
	global CMINEXSC #=[0 for x in range[6]]
	global ECLOSS #=[0 for x in range[6]]
	global WPLN #=[0 for x in range[6]]
	global ICOUNT
	global OVAN1,VAN2,VAN3,VAN4,VAN5,VAN6,VAN
	global ICOLL#=[0 for x in range(30)]
	global NETOT,NPRIME,TMAX1
	global TIME #=[0 for x in range(300)]
	global NNULL,NITOT
	global ICOLN #=[0 for x i range(512)]
	global ICOLNN#=[0 for x in range(60)]
	global NREAL,NEXCTOT
	global MSUM#=[0 for x in range(10000)]
	global MCOMP#=[0 for x in range(10000)]
	global MRAYL#=[0 for x in range(10000)]
	global MPAIR#=[0 for x in range(10000)]
	global MPHOT#=[0 for x in range(10000)]
	global MVAC#=[0 for x in range(10000)]
	global BET#=[0 for x in range(2000)]
	global GAM#=[0 for x in range(20000)]
	global VC,EMS 
	global ICMP,ICFLG,IRAY,IRFLG,IPAP,IPFLG,IBRM,IBFLG,LPEFLG 
	global E #=[0 for x in range(20000)]
	global EROOT #=[0 for x in range(20000)]
	global QTOT #=[0 for x in range(20000)]
	global QREL #=[0 for x in range(20000)]
	global QINEL #=[0 for x in range(20000)]
	global QEL #=[0 for x in range(20000)]
	global NXPL10#=[0 for x in range(31)]
	global NYPL10#=[0 for x in range(31)]
	global NZPL10#=[0 for x in range(31)]
	global NXPL40#=[0 for x in range(31)]
	global NYPL40#=[0 for x in range(31)]
	global NZPL40#=[0 for x in range(31)]
	global NXPL100#=[0 for x in range(31)]
	global NYPL100#=[0 for x in range(31)]
	global NZPL100#=[0 for x in range(31)]
	global NXPL400#=[0 for x in range(31)]
	global NYPL400#=[0 for x in range(31)]
	global NZPL400#=[0 for x in range(31)]
	global NXPL1000#=[0 for x in range(31)]
	global NYPL1000#=[0 for x in range(31)]
	global NZPL1000#=[0 for x in range(31)]
	global NXPL2#=[0 for x in range(31)]
	global NYPL2#=[0 for x in range(31)]
	global NZPL2#=[0 for x in range(31)]
	global NXPL4000#=[0 for x in range(31)]
	global NYPL4000#=[0 for x in range(31)]
	global NZPL4000#=[0 for x in range(31)]
	global NXPL10000#=[0 for x in range(31)]
	global NYPL10000#=[0 for x in range(31)]
	global NZPL10000#=[0 for x in range(31)]
	global NXPL40000#=[0 for x in range(31)]
	global NYPL40000#=[0 for x in range(31)]
	global NZPL40000#=[0 for x in range(31)]
	global NXPL100000#=[0 for x in range(31)]
	global NYPL100000#=[0 for x in range(31)]
	global NZPL100000#=[0 for x in range(31)]
	global NRPL2#=[0 for x in range(31)]
	global NRPL10#=[0 for x in range(31)]
	global NRPL40#=[0 for x in range(31)]
	global NRPL100#=[0 for x in range(31)]
	global NRPL400#=[0 for x in range(31)]
	global NRPL1000#=[0 for x in range(31)]
	global NRPL4000#=[0 for x in range(31)]
	global NRPL10000#=[0 for x in range(31)]
	global NRPL40000#=[0 for x in range(31)]
	global NRPL100000#=[0 for x in range(31)]
	global NEPL1#=[0 for x in range(100)]
	global NEPL10#=[0 for x in range(100)]
	global NEPL100#=[0 for x in range(100)]
	global MELEC#=[0 for x in range(1000)]
	global MELEC3#=[0 for x in range(1000)]
	global MELEC10#=[0 for x in range(1000)]
	global MELEC30#=[0 for x in range(1000)]
	global MELEC100#=[0 for x in range(1000)]
	global MELEC300#=[0 for x in range(1000)]
	global EBRGAM#=[0 for x in range(10)]
	global BRDCOSX# =[0 for x in range(10)]
	global BRDCOSY# =[0 for x in range(10)]
	global BRDCOSZ# =[0 for x in range(10)]
	global BRX#=[0 for x in range(10)]
	global BRY#=[0 for x in range(10)]
	global BRZ#=[0 for x in range(10)]
	global BRT#=[0 for x in range(10)]
	global EBRTOT#=[0 for x in range[6]]
	global NBREM#=[0 for x in range[6]]
	global XAV#=[0 for x in range(100000)]
	global YAV#=[0 for x in range(100000)]
	global ZAV#=[0 for x in range(100000)]
	global TAV#=[0 for x in range(100000)]
	global XYAV#=[0 for x in range(100000)]
	global XYZAV#=[0 for x in range(100000)]
	global DX#=[0 for x in range(100000)]
	global DY#=[0 for x in range(100000)] 
	global DZ#=[0 for x in range(100000)]
	global DT#=[0 for x in range(100000)]
	global DXY#=[0 for x in range(100000)]
	global DXYZ#=[0 for x in range(100000)]
	global NCL#=[0 for x in range(100000)]
	global FARX1#=[0 for x in range(100000)]
	global FARY1#=[0 for x in range(100000)]
	global FARZ1#=[0 for x in range(100000)]
	global FARXY1#=[0 for x in range(100000)]
	global RMAX1#=[0 for x in range(100000)]
	global TSUM#=[0 for x in range(100000)]
	global XNEG#=[0 for x in range(100000)]
	global YNEG#=[0 for x in range(100000)]
	global ZNEG#=[0 for x in range(100000)]
	global EDELTA#[100000]
	global EDELTA2#=[0 for x in range(100000)]
	global NCLEXC#=[0 for x in range(100000)]
	global NSEED
	global NEGAS#=[0 for x in range(512)]
	global LEGAS#=[0 for x in range(512)]
	global IESHELL#=[0 for x in range(512)]
	global IECASC
	#                                                                       
	#   NEW UPDATE OF CONSTANTS 2010
	#
	API=numpy.arccos(-1.00)                                                 
	ARY=13.605692530                                              
	PIR2=8.7973554297*(10**-17)
	ECHARG=1.602176565*(10**-19)                                         
	EMASS=9.10938291*(10**-31)                     
	EMS=510998.9280
	VC=299792458.00                       
	AMU=1.660538921*(10**-27)                                             
	BOLTZ=8.6173324*(10**-5)    
	BOLTZJ=1.3806488*(10**-23)                                              
	AWB=1.758820088*(10**10)                                             
	ALOSCH=2.6867805*(10**19)     
	RE=2.8179403267*(10**-13)    
	ALPH=137.035999074
	HBAR=6.58211928*(10**-16)                                     
	EOVM=math.sqrt(2.00*ECHARG/EMASS)*100.00                            
	ABZERO=273.150                                                   
	ATMOS=760.00                                                     
	CONST1=AWB/2.00*1.0*(10**-19)                                          
	CONST2=CONST1*1.0*(10**-2)                                             
	CONST3=math.sqrt(0.20*AWB)*1.0*(10**-9)                                   
	CONST4=CONST3*ALOSCH*1.0*(10**-15)                                      
	CONST5=CONST3/2.00
	TWOPI=2.00*API
	NANISO=2
	NBREM=numpy.zeros(7)  # negotiated for extra element 
	EBRTOT=numpy.zeros(7)   # negotiated for extra element 

	ICFLG=0
	IRFLG=0
	IPFLG=0
	IBFLG=0
	LPEFLG=0
	#  --------------------------------------------       
	#                                                                       
	#      READ IN OUTPUT CONTROL AND INTEGRATION DATA                      
	#                
	NGAS,NEVENT,IMIP,NDVEC,NSEED,ESTART,ETHRM,ECUT=2,100,5,1,0,1.0,1.5,2.0
	# NGAS,NEVENT,IMIP,NDVEC,NSEED,ESTART,ETHRM,ECUT=input("Input Card 1 ").split()
	NGAS=int(NGAS)#input('NGAS'))
	NEVENT=int(NEVENT)#input('NEVENT'))
	IMIP=int(IMIP)#input('IMIP'))
	NDVEC=int(NDVEC)#input('NDVEC'))
	NSEED=int(NSEED)#input('NSEED'))
	ESTART=float(ESTART)#input('ESTART'))
	ETHRM=float(ETHRM)#input('ETHRM'))
	ECUT=float(ECUT)#input('ECUT'))
	ICOUNT=0
	if(IMIP == 1):
		ICOUNT=1 
	if(NGAS == 0):
		LAST=1
		return  
	if(ESTART > 3.0*(10**6) and IMIP == 3):
		print(' SUBROUTINE STOPPED: X-RAY ENERGY=','%.3f' % ESTART,'EV. MAXIMUM ENERGY 3.0MEV')
		sys.exit() 
	# endif
	if(IMIP != 1 and NEVENT > 10000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',NEVENT,' LARGER THAN ARRAY LIMIT OF 10000')
		sys.exit()
	# endif
	if(IMIP == 1 and NEVENT > 100000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',NEVENT,' LARGER THAN ARRAY LIMIT OF 100000')
		sys.exit()
	# endif
	# 
	#   GAS IDENTIFIERS 
	#
	NGASN=numpy.zeros(7)
	card2=[2 , 12 , 0 , 0 , 0 , 0]
	# card2=input("Input Card 2 ").split()
	for i in range(6):
		NGASN[i+1]=card2[i]
	#      
	#      GAS PARAMETERS
	#
	FRAC=numpy.zeros(7)
	card3=[80.000,20.000,0.0,0.0,0.0,0.0,20.000,760.000]
	# card3=input("Input Card 3 ").split()
	for i in range(6):
		FRAC[i+1]=float(card3[i])
	TEMPC=round(float(card3[6]),4)  					#print(8'%.4f' %)      
	TORR=round(float(card3[7]),4)                  	#print(8'%.4f' %)      

       
	#print(8'%.4f' %)      
	#                                                  
	#      FIELD VALUES                                                    
	#   
	EFIELD,BMAG,BTHETA,IWRITE,IPEN=2.000,3.000,30.000,0,0
	# EFIELD,BMAG,BTHETA,IWRITE,IPEN=input("Input Card 4 ").split()                                                                    
	EFIELD=round(float(EFIELD),3)  			#print(3'%.3f' % ,2I5)
	BMAG=round(float(BMAG),3)			#print(3'%.3f' % ,2I5)
	BTHETA=round(float(BTHETA),3)			#print(3'%.3f' % ,2I5)
	IWRITE=int(IWRITE)			#print(3'%.3f' % ,2I5)
	IPEN=int(IPEN)                    			#print(3'%.3f' % ,2I5)     
	
	DETEFF,EXCWGHT,KGAS,LGAS,ICMP,IRAY,IPAP,IBRM,IECASC=50.0,0.55,2,1,1,1,1,1,1
	# DETEFF,EXCWGHT,KGAS,LGAS,ICMP,IRAY,IPAP,IBRM,IECASC=input("Input Card 5 ").split()
	DETEFF=round(float(DETEFF),3)      	# print(2'%.3f' % ,7I5)
	EXCWGHT=round(float(EXCWGHT),3)			# print(2'%.3f' % ,7I5)			
	KGAS=int(KGAS)						# print(2'%.3f' % ,7I5)
	LGAS=int(LGAS)						# print(2'%.3f' % ,7I5)
	ICMP=int(ICMP)						# print(2'%.3f' % ,7I5)
	IRAY=int(IRAY)						# print(2'%.3f' % ,7I5)
	IPAP=int(IPAP)						# print(2'%.3f' % ,7I5)
	IBRM=int(IBRM)						# print(2'%.3f' % ,7I5)
	IECASC =int(IECASC)					# print(2'%.3f' % ,7I5)
	#     WRITE(6,656) IWRITE
	# 656 print(' IWRITE=',I3)  
	if(IWRITE != 0):
		outputfile=open("DEGRAD.OUT","w")
	# CALCULATE EFINAL FOR DELTAS OR XRAYS 
	# INCREASED EFINAL CAUSED BY ELECTRIC FIELD 
	EBIG=0.05*ESTART/1000. 
	EFINAL=ESTART*1.0001+760.0*EBIG/TORR*(TEMPC+ABZERO)/293.15*EFIELD
	if(EFINAL < (1.01*ESTART)):
		EFINAL=1.01*ESTART 
	#   CHECK INPUT
	TOTFRAC=0.00
	if(NGAS == 0 or NGAS > 6):
			GOTO999()
	for J in range(1,NGAS+1):
		# 	print('J',J)
		if(NGASN[J]== 0 or FRAC[J] == 0.00):
			GOTO999()
		TOTFRAC=TOTFRAC+FRAC[J]

	if(abs(TOTFRAC-100.00)> 1*(10**-6)):
		print(TOTFRAC)
		GOTO999()
	LAST=0
	TMAX=100.00  
	NOUT=10  
	NSTEP=20000
	# INITIAL ANGLES
	if(NDVEC): #22594
		PHI=0
		THETA=0
	elif(NDVEC==-1):
		PHI=0
		THETA=numpy.arccos(-1)
	elif(NDVEC==0):
		PHI=0.0
		THETA=API/2.0
	elif(NDVEC==2):
		R3=DRAND48(0.0,1.0)
		PHI=TWOPI*R3
		R4=DRAND48(1.5, 1.9)
		THETA=numpy.arccos(1.0-2.0*R4)
	else :
		print('DIRECTION OF BEAM NOT DEFINED NDVEC =',NDVEC)
		sys.exit()

	# INITIAL DIRECTION COSINES FOR CASCADE CALCULATION
	DRZINIT= numpy.cos(THETA)
	DRXINIT= numpy.sin(THETA)*numpy.cos(PHI)
	DRYINIT=numpy.sin(THETA)*numpy.sin(PHI)
	# ZERO COMMON BLOCKS OF OUTPUT RESULTS
	MSUM=numpy.zeros(10001,dtype=int)
	MCOMP=numpy.zeros(10001,dtype=int)
	MRAYL=numpy.zeros(10001,dtype=int)
	MPAIR=numpy.zeros(10001,dtype=int)
	MPHOT=numpy.zeros(10001,dtype=int)
	MVAC=numpy.zeros(10001,dtype=int)

	# for J in range(1,300):
	TIME=numpy.zeros(301,dtype=int)
	# for K in range(1,30):
	ICOLL=numpy.zeros(31,dtype=int)
	# for K in range(1,512):
	ICOLN=numpy.zeros(513,dtype=int)
	# for K in range(1,60):
	ICOLNN=numpy.zeros(61,dtype=int)
	# for K in range(1,10):
	TCFMAX=numpy.zeros(11)
	# ZERO PLOT ARRAYS
	NXPL2=numpy.zeros(32,dtype=int)
	NYPL2=numpy.zeros(32,dtype=int)
	NZPL2=numpy.zeros(32,dtype=int)
	NXPL10=numpy.zeros(32,dtype=int)
	NYPL10=numpy.zeros(32,dtype=int)
	NZPL10=numpy.zeros(32,dtype=int)
	NXPL40=numpy.zeros(32,dtype=int)
	NYPL40=numpy.zeros(32,dtype=int)
	NZPL40=numpy.zeros(32,dtype=int)
	NXPL100=numpy.zeros(32,dtype=int)
	NYPL100=numpy.zeros(32,dtype=int)
	NZPL100=numpy.zeros(32,dtype=int)
	NXPL400=numpy.zeros(32,dtype=int)
	NYPL400=numpy.zeros(32,dtype=int)
	NZPL400=numpy.zeros(32,dtype=int)
	NXPL1000=numpy.zeros(32,dtype=int)
	NYPL1000=numpy.zeros(32,dtype=int)
	NZPL1000=numpy.zeros(32,dtype=int)
	NXPL4000=numpy.zeros(32,dtype=int)
	NYPL4000=numpy.zeros(32,dtype=int)
	NZPL4000=numpy.zeros(32,dtype=int)
	NXPL10000=numpy.zeros(32,dtype=int)
	NYPL10000=numpy.zeros(32,dtype=int)
	NZPL10000=numpy.zeros(32,dtype=int)
	NXPL40000=numpy.zeros(32,dtype=int)
	NYPL40000=numpy.zeros(32,dtype=int)
	NZPL40000=numpy.zeros(32,dtype=int)
	NXPL100000=numpy.zeros(32,dtype=int)
	NYPL100000=numpy.zeros(32,dtype=int)
	NZPL100000=numpy.zeros(32,dtype=int)
	NRPL2=numpy.zeros(32,dtype=int)
	NRPL10=numpy.zeros(32,dtype=int)
	NRPL40=numpy.zeros(32,dtype=int)
	NRPL100=numpy.zeros(32,dtype=int)
	NRPL400=numpy.zeros(32,dtype=int)
	NRPL1000=numpy.zeros(32,dtype=int)
	NRPL4000=numpy.zeros(32,dtype=int)
	NRPL10000=numpy.zeros(32,dtype=int)
	NRPL40000=numpy.zeros(32,dtype=int)
	NRPL100000=numpy.zeros(32,dtype=int) #22678
	NEPL1=numpy.zeros(101,dtype=int)
	NEPL10=numpy.zeros(101,dtype=int)
	NEPL100=numpy.zeros(101,dtype=int)
	MELEC=numpy.zeros(1001,dtype=int)
	MELEC3=numpy.zeros(1001,dtype=int)
	MELEC10=numpy.zeros(1001,dtype=int)
	MELEC30=numpy.zeros(1001,dtype=int)
	MELEC100=numpy.zeros(1001,dtype=int)
	MELEC300=numpy.zeros(1001,dtype=int) #22689
	# C ZERO ARRAYS
	XAV=numpy.zeros(100001)
	YAV=numpy.zeros(100001)
	ZAV=numpy.zeros(100001)
	TAV=numpy.zeros(100001)
	XYAV=numpy.zeros(100001)
	XYZAV=numpy.zeros(100001)
	DX=numpy.zeros(100001)
	DY=numpy.zeros(100001)
	DZ=numpy.zeros(100001)
	DT=numpy.zeros(100001)
	DXY=numpy.zeros(100001)
	DXYZ=numpy.zeros(100001)
	FARX1=numpy.zeros(100001)
	FARY1=numpy.zeros(100001)
	FARZ1=numpy.zeros(100001)
	FARXY1=numpy.zeros(100001)
	RMAX1=numpy.zeros(100001)
	TSUM=numpy.zeros(100001)
	XNEG=numpy.zeros(100001)
	YNEG=numpy.zeros(100001)
	ZNEG=numpy.zeros(100001)
	EDELTA=numpy.zeros(100001)
	EDELTA2=numpy.zeros(100001)
	NCL=numpy.zeros(100001)
	NCLEXC=numpy.zeros(100001) ##22716 #22915
	# ----------------------------------------------------  
	# if NSEED = 0 : USE STANDARD SEED VALUE =54217137
	if(NSEED != 0):
		RM48(NSEED,0,0)                           
	#-----------------------------------------------      
	#
	CORR=ABZERO*TORR/(ATMOS*(ABZERO+TEMPC)*100.00)                    #check precision
	AKT=(ABZERO+TEMPC)*BOLTZ
	AN1=FRAC[1]*CORR*ALOSCH                                           
	AN2=FRAC[2]*CORR*ALOSCH                                           
	AN3=FRAC[3]*CORR*ALOSCH                                           
	AN4=FRAC[4]*CORR*ALOSCH
	AN5=FRAC[5]*CORR*ALOSCH
	AN6=FRAC[6]*CORR*ALOSCH                                           
	AN=float(100.00*CORR*ALOSCH)
	AN=100.00*CORR*ALOSCH                                            
	#VAN1=FRAC[1]*CORR*CONST4*1.0D15                                   
	#VAN2=FRAC[2]*CORR*CONST4*1.0D15                                   
	#VAN3=FRAC(3)*CORR*CONST4*1.0D15                                   
	#VAN4=FRAC[4]*CORR*CONST4*1.0D15
	#VAN5=FRAC[5]*CORR*CONST4*1.0D15
	#VAN6=FRAC[6]*CORR*CONST4*1.0D15                                   
	#VAN=100.00*CORR*CONST4*1.0D15
	VAN1=FRAC[1]*CORR*ALOSCH*VC                                   
	VAN2=FRAC[2]*CORR*ALOSCH*VC                                   
	VAN3=FRAC[3]*CORR*ALOSCH*VC                                  
	VAN4=FRAC[4]*CORR*ALOSCH*VC
	VAN5=FRAC[5]*CORR*ALOSCH*VC
	VAN6=FRAC[6]*CORR*ALOSCH*VC                                  
	VAN=float(100.00*CORR*ALOSCH*VC)    #22745 #22945
	# CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
	E=numpy.zeros(20001)
	GAM=numpy.zeros(20001)
	BET=numpy.zeros(20001)
	if(EFINAL <= 20000.0):
		ESTEP=float(EFINAL/float(NSTEP))
		EHALF=float(ESTEP/2.00)
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))  #ifcontinues
		for I in range(2,20000+1):                      #ifcontinues
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	elif(EFINAL > 20000.0 and EFINAL <= 140000.) :
		ESTEP=1.0
		EHALF=0.5
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for i in range(2,16000+1):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))   #22768 #22968  
		ESTEP1=(EFINAL-16000.0)/float(4000)
		for I in range(16001,2000+1):
			AJ=float(I-16000)
			E[I]=16000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	else:
		ESTEP=1.0
		EHALF=0.5
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for I in range(2,12000+1):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
		ESTEP1=20.0
		for I in range(12001,16000+1):
			AJ=float(I-12000)
			E[I]=12000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
		ESTEP2=(EFINAL-92000.0)/float(4000)
		for I in range(16001,20000+1):
			AJ=float(I-16000)
			E[I]=92000.0+AJ*ESTEP2
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	# endif
	#  RADIANS PER PICOSECOND                                        
	WB=AWB*BMAG*1.0*(10**-12 )
	#   METRES PER PICOSECOND
	if(BMAG == 0.00):
		return
	EOVB=EFIELD*1*(10**-9)/BMAG
	return
	
	GOTO999()                                                            
	# end                                                               

# SETUP(0)