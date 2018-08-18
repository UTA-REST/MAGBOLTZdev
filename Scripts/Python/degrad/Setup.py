import numpy
import math
import sys
import conf
#COMMONINPT
# NGAS=conf.NGAS
# NSTEP=conf.NSTEP
# NANISO=conf.NANISO
# EFINAL=conf.EFINAL
# ESTEP=conf.ESTEP
# AKT=conf.AKT
# ARY=conf.ARY
# TEMPC=conf.TEMPC
# TORR=conf.TORR
# IPEN=conf.IPEN
# #COMMONCNSTS
# ECHARG=conf.ECHARG
# EMASS=conf.EMASS
# AMU=conf.AMU
# PIR2=conf.PIR2
# #COMMONINPT2
# KGAS=conf.KGAS
# LGAS=conf.LGAS
# DETEFF=conf.DETEFF
# EXCWGHT=conf.EXCWGHT
# #COMMONINPT1
# NDVEC=conf.NDVEC
# #COMMONCNSTS1
# CONST1=conf.CONST1
# CONST2=conf.CONST2
# CONST3=conf.CONST3
# CONST4=conf.CONST4
# CONST5=conf.CONST5
# #COMMONRATIO
# AN1=conf.AN1
# AN2=conf.AN2
# AN3=conf.AN3
# AN4=conf.AN4
# AN5=conf.AN5
# AN6=conf.AN6
# AN=conf.AN
# FRAC=conf.FRAC
# #COMMONGASN
# NGASN=conf.NGASN
# #COMMONSETP
# TMAX=conf.TMAX
# SMALL=conf.SMALL
# API=conf.API
# ESTART=conf.ESTART
# THETA=conf.THETA
# PHI=conf.PHI
# TCFMAX=conf.TCFMAX
# TCFMAX1=conf.TCFMAX1

# RSTART=conf.RSTART
# EFIELD=conf.EFIELD
# ETHRM=conf.ETHRM
# ECUT=conf.ECUT
# NEVENT=conf.NEVENT
# IMIP=conf.IMIP
# IWRITE=conf.IWRITE
# #COMMONSET2
# DRXINIT=conf.DRXINIT
# DRYINIT=conf.DRYINIT
# DRZINIT=conf.DRZINIT
# #COMMONBFLD
# EOVB=conf.EOVB
# WB=conf.WB
# BTHETA=conf.BTHETA
# BMAG=conf.BMAG
# #COMMONIONC
# DOUBLE=conf.DOUBLE
# CMINIXSC=conf.CMINIXSC
# CMINEXSC=conf.CMINEXSC
# ECLOSS=conf.ECLOSS

# WPLN=conf.WPLN
# ICOUNT=conf.ICOUNT
# AVPFRAC=conf.AVPFRAC
# #COMMONMRATIO
# VAN1=conf.VAN1
# VAN2=conf.VAN2
# VAN3=conf.VAN3
# VAN4=conf.VAN4
# VAN5=conf.VAN5
# VAN6=conf.VAN6
# VAN=conf.VAN
# #COMMONOUTPT
# ICOLL=conf.ICOLL
# NETOT=conf.NETOT
# NPRIME=conf.NPRIME
# TMAX1=conf.TMAX1
# TIME=conf.TIME
# NNULL=conf.NNULL

# NITOT=conf.NITOT
# ICOLN=conf.ICOLN
# ICOLNN=conf.ICOLNN
# NREAL=conf.NREAL
# NEXCTOT=conf.NEXCTOT
# #COMMONPRIM3
# MSUM=conf.MSUM
# MCOMP=conf.MCOMP
# MRAYL=conf.MRAYL
# MPAIR=conf.MPAIR

# MPHOT=conf.MPHOT
# MVAC=conf.MVAC
# #COMMONRLTVY
# BET=conf.BET
# GAM=conf.GAM
# VC=conf.VC
# EMS=conf.EMS
# #COMMONCOMP
# ICMP=conf.ICMP
# ICFLG=conf.ICFLG
# IRAY=conf.IRAY
# IRFLG=conf.IRFLG
# IPAP=conf.IPAP
# IPFLG=conf.IPFLG
# IBRM=conf.IBRM
# IBFLG=conf.IBFLG
# LPEFLG=conf.LPEFLG
# #COMMONMIX2
# E=conf.E
# EROOT=conf.EROOT
# QTOT=conf.QTOT
# QREL=conf.QREL

# QINEL=conf.QINEL
# QEL=conf.QEL
# #COMMONPLOT
# NXPL10=conf.NXPL10
# NYPL10=conf.NYPL10
# NZPL10=conf.NZPL10
# NXPL40=conf.NXPL40

# NYPL40=conf.NYPL40
# NZPL40=conf.NZPL40
# NXPL100=conf.NXPL100
# NYPL100=conf.NYPL100
# NZPL100=conf.NZPL100

# NXPL400=conf.NXPL400
# NYPL400=conf.NYPL400
# NZPL400=conf.NZPL400
# NXPL1000=conf.NXPL1000
# NYPL1000=conf.NYPL1000

# NZPL1000=conf.NZPL1000
# NXPL2=conf.NXPL2
# NYPL2=conf.NYPL2
# NZPL2=conf.NZPL2
# NXPL4000=conf.NXPL4000

# NYPL4000=conf.NYPL4000
# NZPL4000=conf.NZPL4000
# NXPL10000=conf.NXPL10000
# NYPL10000=conf.NYPL10000

# NZPL10000=conf.NZPL10000
# NXPL40000=conf.NXPL40000
# NYPL40000=conf.NYPL40000
# NZPL40000=conf.NZPL40000

# NXPL100000=conf.NXPL100000
# NYPL100000=conf.NYPL100000
# NZPL100000=conf.NZPL100000
# NRPL2=conf.NRPL2
# NRPL10=conf.NRPL10

# NRPL40=conf.NRPL40
# NRPL100=conf.NRPL100
# NRPL400=conf.NRPL400
# NRPL1000=conf.NRPL1000
# NRPL4000=conf.NRPL4000

# NRPL10000=conf.NRPL10000
# NRPL40000=conf.NRPL40000
# NRPL100000=conf.NRPL100000
# NEPL1=conf.NEPL1

# NEPL10=conf.NEPL10
# NEPL100=conf.NEPL100
# MELEC=conf.MELEC
# MELEC3=conf.MELEC3
# MELEC10=conf.MELEC10

# MELEC30=conf.MELEC30
# MELEC100=conf.MELEC100
# MELEC300=conf.MELEC300
# #COMMONBREMG
# EBRGAM=conf.EBRGAM
# BRDCOSX=conf.BRDCOSX
# BRDCOSY=conf.BRDCOSY
# BRDCOSZ=conf.BRDCOSZ

# BRX=conf.BRX
# BRY=conf.BRY
# BRZ=conf.BRZ
# BRT=conf.BRT
# EBRTOT=conf.EBRTOT
# NBREM=conf.NBREM
# #COMMONCLUS
# XAV=conf.XAV
# YAV=conf.YAV
# ZAV=conf.ZAV
# TAV=conf.TAV

# XYAV=conf.XYAV
# XYZAV=conf.XYZAV
# DX=conf.DX
# DY=conf.DY
# DZ=conf.DZ

# DT=conf.DT
# DXY=conf.DXY
# DXYZ=conf.DXYZ
# NCL=conf.NCL
# FARX1=conf.FARX1
# FARY1=conf.FARY1
# FARZ1=conf.FARZ1
# FARXY1=conf.FARXY1
# RMAX1=conf.RMAX1

# TSUM=conf.TSUM
# XNEG=conf.XNEG
 
# YNEG=conf.YNEG
# ZNEG=conf.ZNEG
# EDELTA=conf.EDELTA
# EDELTA2=conf.EDELTA2

# NCLEXC=conf.NCLEXC
# #COMMONKSEED
# NSEED=conf.NSEED
# #COMMONECASC
# NEGAS=conf.NEGAS
# LEGAS=conf.LEGAS
# IESHELL=conf.IESHELL
# IECASC=conf.IECASC

def SETUP(LAST):
	def GOTO999():
		# print("in GOTO999")
		print(conf.NGASN,conf.FRAC)
		print(' ERROR IN GAS INPUT : NGAS=',conf.NGAS,'\n')
		for J in range(1,6+1):
			# print(J)
			print(' N=',J,' NGAS=',conf.NGASN[J],' FRAC=',conf.FRAC[J])
		LAST=1                                                            
		return LAST
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
	conf.API=numpy.arccos(-1.00)                                                 
	conf.ARY=13.605692530                                              
	conf.PIR2=8.7973554297*(10**-17)
	conf.ECHARG=1.602176565*(10**-19)                                         
	conf.EMASS=9.10938291*(10**-31)                     
	conf.EMS=510998.9280
	conf.VC=299792458.00                       
	conf.AMU=1.660538921*(10**-27)                                             
	BOLTZ=8.6173324*(10**-5)    
	BOLTZJ=1.3806488*(10**-23)                                              
	AWB=1.758820088*(10**10)                                             
	ALOSCH=2.6867805*(10**19)     
	RE=2.8179403267*(10**-13)    
	ALPH=137.035999074
	HBAR=6.58211928*(10**-16)                                     
	EOVM=math.sqrt(2.00*conf.ECHARG/conf.EMASS)*100.00                            
	ABZERO=273.150                                                   
	ATMOS=760.00                                                     
	conf.CONST1=AWB/2.00*1.0*(10**-19)                                          
	conf.CONST2=conf.CONST1*1.0*(10**-2)                                             
	conf.CONST3=math.sqrt(0.20*AWB)*1.0*(10**-9)                                   
	conf.CONST4=conf.CONST3*ALOSCH*1.0*(10**-15)                                      
	conf.CONST5=conf.CONST3/2.00
	TWOPI=2.00*conf.API
	conf.NANISO=2
	conf.NBREM=numpy.zeros(7)  # negotiated for extra element 
	conf.EBRTOT=numpy.zeros(7)   # negotiated for extra element 

	conf.ICFLG=0
	conf.IRFLG=0
	conf.IPFLG=0
	conf.IBFLG=0
	conf.LPEFLG=0
	#  --------------------------------------------       
	#                                                                       
	#      READ IN OUTPUT CONTROL AND INTEGRATION DATA                      
	#                
	conf.NGAS,conf.NEVENT,conf.IMIP,conf.NDVEC,conf.NSEED,conf.ESTART,conf.ETHRM,conf.ECUT=2,100,5,1,0,1.0,1.5,2.0

	# NGAS,NEVENT,IMIP,NDVEC,NSEED,ESTART,ETHRM,ECUT=input("Input Card 1 ").split()
	conf.NGAS=int(conf.NGAS)#input('NGAS'))
	conf.NEVENT=int(conf.NEVENT)#input('NEVENT'))
	conf.IMIP=int(conf.IMIP)#input('IMIP'))
	conf.NDVEC=int(conf.NDVEC)#input('NDVEC'))
	conf.NSEED=int(conf.NSEED)#input('NSEED'))
	conf.ESTART=float(conf.ESTART)#input('ESTART'))
	conf.ETHRM=float(conf.ETHRM)#input('ETHRM'))
	conf.ECUT=float(conf.ECUT)#input('ECUT'))
	conf.ICOUNT=0

	if(conf.IMIP == 1):
		conf.ICOUNT=1 
	if(conf.NGAS == 0):
		LAST=1
		return LAST
	if(conf.ESTART > 3.0*(10**6) and conf.IMIP == 3):
		print(' SUBROUTINE STOPPED: X-RAY ENERGY=','%.3f' % conf.ESTART,'EV. MAXIMUM ENERGY 3.0MEV')
		sys.exit() 
	# endif
	if(conf.IMIP != 1 and conf.NEVENT > 10000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',conf.NEVENT,' LARGER THAN ARRAY LIMIT OF 10000')
		sys.exit()
	# endif
	if(conf.IMIP == 1 and conf.NEVENT > 100000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',conf.NEVENT,' LARGER THAN ARRAY LIMIT OF 100000')
		sys.exit()
	# endif
	# 
	#   GAS IDENTIFIERS 
	#
	conf.NGASN=numpy.zeros(7)
	card2=[2 , 12 , 0 , 0 , 0 , 0]
	# card2=input("Input Card 2 ").split()
	for i in range(6):
		conf.NGASN[i+1]=card2[i]
	#      
	#      GAS PARAMETERS
	#
	conf.FRAC=numpy.zeros(7)
	card3=[80.000,20.000,0.0,0.0,0.0,0.0,20.000,760.000]
	# card3=input("Input Card 3 ").split()
	for i in range(6):
		conf.FRAC[i+1]=float(card3[i])
	conf.TEMPC=round(float(card3[6]),4)  				#print(8'%.4f' %)      
	conf.TORR=round(float(card3[7]),4)                  	#print(8'%.4f' %)      

       
	#print(8'%.4f' %)      
	#                                                  
	#      FIELD VALUES                                                    
	#   
	conf.EFIELD,conf.BMAG,conf.BTHETA,conf.IWRITE,conf.IPEN=2.000,3.000,30.000,0,0
	# EFIELD,BMAG,BTHETA,IWRITE,IPEN=input("Input Card 4 ").split()                                                                    
	conf.EFIELD=round(float(conf.EFIELD),3)  			#print(3'%.3f' % ,2I5)
	conf.BMAG=round(float(conf.BMAG),3)			#print(3'%.3f' % ,2I5)
	conf.BTHETA=round(float(conf.BTHETA),3)			#print(3'%.3f' % ,2I5)
	conf.IWRITE=int(conf.IWRITE)			#print(3'%.3f' % ,2I5)
	conf.IPEN=int(conf.IPEN)                    			#print(3'%.3f' % ,2I5)     
	
	conf.DETEFF,conf.EXCWGHT,conf.KGAS,conf.LGAS,conf.ICMP,conf.IRAY,conf.IPAP,conf.IBRM,conf.IECASC=50.0,0.55,2,1,1,1,1,1,1
	# DETEFF,EXCWGHT,KGAS,LGAS,ICMP,IRAY,IPAP,IBRM,IECASC=input("Input Card 5 ").split()
	conf.DETEFF=round(float(conf.DETEFF),3)      	# print(2'%.3f' % ,7I5)
	conf.EXCWGHT=round(float(conf.EXCWGHT),3)		# print(2'%.3f' % ,7I5)			
	conf.KGAS=int(conf.KGAS)						# print(2'%.3f' % ,7I5)
	conf.LGAS=int(conf.LGAS)						# print(2'%.3f' % ,7I5)
	conf.ICMP=int(conf.ICMP)						# print(2'%.3f' % ,7I5)
	conf.IRAY=int(conf.IRAY)						# print(2'%.3f' % ,7I5)
	conf.IPAP=int(conf.IPAP)						# print(2'%.3f' % ,7I5)
	conf.IBRM=int(conf.IBRM)						# print(2'%.3f' % ,7I5)
	conf.IECASC =int(conf.IECASC)					# print(2'%.3f' % ,7I5)
	#     WRITE(6,656) IWRITE
	# 656 print(' IWRITE=',I3)  
	if(conf.IMIP != 0):
		outputfile=open("DEGRAD.OUT","w")
	# CALCULATE EFINAL FOR DELTAS OR XRAYS 
	# INCREASED EFINAL CAUSED BY ELECTRIC FIELD 
	EBIG=0.05*conf.ESTART/1000. 
	conf.EFINAL=conf.ESTART*1.0001+760.0*EBIG/conf.TORR*(conf.TEMPC+ABZERO)/293.15*conf.EFIELD
	if(conf.EFINAL < (1.01*conf.ESTART)):
		conf.EFINAL=1.01*conf.ESTART 
	#   CHECK INPUT
	TOTFRAC=0.00
	if(conf.NGAS == 0 or conf.NGAS > 6):
			GOTO999()
	for J in range(1,conf.NGAS+1):
		# 	print('J',J)
		if(conf.NGASN[J]== 0 or conf.FRAC[J] == 0.00):
			GOTO999()
		TOTFRAC=TOTFRAC+conf.FRAC[J]

	if(abs(TOTFRAC-100.00)> 1*(10**-6)):
		print(TOTFRAC)
		GOTO999()
	LAST=0
	conf.TMAX=100.00  
	NOUT=10  
	conf.NSTEP=20000
	# INITIAL ANGLES
	if(conf.NDVEC): #22594
		conf.PHI=0
		conf.THETA=0
	elif(conf.NDVEC==-1):
		conf.PHI=0
		conf.THETA=numpy.arccos(-1)
	elif(conf.NDVEC==0):
		conf.PHI=0.0
		conf.THETA=conf.API/2.0
	elif(conf.NDVEC==2):
		R3=DRAND48(0.0,1.0)
		conf.PHI=TWOPI*R3
		R4=DRAND48(1.5, 1.9)
		conf.THETA=numpy.arccos(1.0-2.0*R4)
	else :
		print('DIRECTION OF BEAM NOT DEFINED NDVEC =',conf.NDVEC)
		sys.exit()

	# INITIAL DIRECTION COSINES FOR CASCADE CALCULATION
	conf.DRZINIT= numpy.cos(conf.THETA)
	conf.DRXINIT= numpy.sin(conf.THETA)*numpy.cos(conf.PHI)
	conf.DRYINIT=numpy.sin(conf.THETA)*numpy.sin(conf.PHI)
	# ZERO COMMON BLOCKS OF OUTPUT RESULTS
	conf.MSUM=numpy.zeros(10001,dtype=int)
	conf.MCOMP=numpy.zeros(10001,dtype=int)
	conf.MRAYL=numpy.zeros(10001,dtype=int)
	conf.MPAIR=numpy.zeros(10001,dtype=int)
	conf.MPHOT=numpy.zeros(10001,dtype=int)
	conf.MVAC=numpy.zeros(10001,dtype=int)

	# for J in range(1,300):
	conf.TIME=numpy.zeros(301,dtype=int)
	# for K in range(1,30):
	conf.ICOLL=numpy.zeros(31,dtype=int)
	# for K in range(1,512):
	conf.ICOLN=numpy.zeros(513,dtype=int)
	# for K in range(1,60):
	conf.ICOLNN=numpy.zeros(61,dtype=int)
	# for K in range(1,10):
	conf.TCFMAX=numpy.zeros(11)
	# ZERO PLOT ARRAYS
	conf.NXPL2=numpy.zeros(32,dtype=int)
	conf.NYPL2=numpy.zeros(32,dtype=int)
	conf.NZPL2=numpy.zeros(32,dtype=int)
	conf.NXPL10=numpy.zeros(32,dtype=int)
	conf.NYPL10=numpy.zeros(32,dtype=int)
	conf.NZPL10=numpy.zeros(32,dtype=int)
	conf.NXPL40=numpy.zeros(32,dtype=int)
	conf.NYPL40=numpy.zeros(32,dtype=int)
	conf.NZPL40=numpy.zeros(32,dtype=int)
	conf.NXPL100=numpy.zeros(32,dtype=int)
	conf.NYPL100=numpy.zeros(32,dtype=int)
	conf.NZPL100=numpy.zeros(32,dtype=int)
	conf.NXPL400=numpy.zeros(32,dtype=int)
	conf.NYPL400=numpy.zeros(32,dtype=int)
	conf.NZPL400=numpy.zeros(32,dtype=int)
	conf.NXPL1000=numpy.zeros(32,dtype=int)
	conf.NYPL1000=numpy.zeros(32,dtype=int)
	conf.NZPL1000=numpy.zeros(32,dtype=int)
	conf.NXPL4000=numpy.zeros(32,dtype=int)
	conf.NYPL4000=numpy.zeros(32,dtype=int)
	conf.NZPL4000=numpy.zeros(32,dtype=int)
	conf.NXPL10000=numpy.zeros(32,dtype=int)
	conf.NYPL10000=numpy.zeros(32,dtype=int)
	conf.NZPL10000=numpy.zeros(32,dtype=int)
	conf.NXPL40000=numpy.zeros(32,dtype=int)
	conf.NYPL40000=numpy.zeros(32,dtype=int)
	conf.NZPL40000=numpy.zeros(32,dtype=int)
	conf.NXPL100000=numpy.zeros(32,dtype=int)
	conf.NYPL100000=numpy.zeros(32,dtype=int)
	conf.NZPL100000=numpy.zeros(32,dtype=int)
	conf.NRPL2=numpy.zeros(32,dtype=int)
	conf.NRPL10=numpy.zeros(32,dtype=int)
	conf.NRPL40=numpy.zeros(32,dtype=int)
	conf.NRPL100=numpy.zeros(32,dtype=int)
	conf.NRPL400=numpy.zeros(32,dtype=int)
	conf.NRPL1000=numpy.zeros(32,dtype=int)
	conf.NRPL4000=numpy.zeros(32,dtype=int)
	conf.NRPL10000=numpy.zeros(32,dtype=int)
	conf.NRPL40000=numpy.zeros(32,dtype=int)
	conf.NRPL100000=numpy.zeros(32,dtype=int) #22678
	conf.NEPL1=numpy.zeros(101,dtype=int)
	conf.NEPL10=numpy.zeros(101,dtype=int)
	conf.NEPL100=numpy.zeros(101,dtype=int)
	conf.MELEC=numpy.zeros(1001,dtype=int)
	conf.MELEC3=numpy.zeros(1001,dtype=int)
	conf.MELEC10=numpy.zeros(1001,dtype=int)
	conf.MELEC30=numpy.zeros(1001,dtype=int)
	conf.MELEC100=numpy.zeros(1001,dtype=int)
	conf.MELEC300=numpy.zeros(1001,dtype=int) #22689
	# C ZERO ARRAYS
	conf.XAV=numpy.zeros(100001)
	conf.YAV=numpy.zeros(100001)
	conf.ZAV=numpy.zeros(100001)
	conf.TAV=numpy.zeros(100001)
	conf.XYAV=numpy.zeros(100001)
	conf.XYZAV=numpy.zeros(100001)
	conf.DX=numpy.zeros(100001)
	conf.DY=numpy.zeros(100001)
	conf.DZ=numpy.zeros(100001)
	conf.DT=numpy.zeros(100001)
	conf.DXY=numpy.zeros(100001)
	conf.DXYZ=numpy.zeros(100001)
	conf.FARX1=numpy.zeros(100001)
	conf.FARY1=numpy.zeros(100001)
	conf.FARZ1=numpy.zeros(100001)
	conf.FARXY1=numpy.zeros(100001)
	conf.RMAX1=numpy.zeros(100001)
	conf.TSUM=numpy.zeros(100001)
	conf.XNEG=numpy.zeros(100001)
	conf.YNEG=numpy.zeros(100001)
	conf.ZNEG=numpy.zeros(100001)
	conf.EDELTA=numpy.zeros(100001)
	conf.EDELTA2=numpy.zeros(100001)
	conf.NCL=numpy.zeros(100001)
	conf.NCLEXC=numpy.zeros(100001) ##22716 #22915
	# ----------------------------------------------------  
	# if NSEED = 0 : USE STANDARD SEED VALUE =54217137
	if(conf.NSEED != 0):
		RM48(conf.NSEED,0,0)                           
	#-----------------------------------------------      
	#
	CORR=ABZERO*conf.TORR/(ATMOS*(ABZERO+conf.TEMPC)*100.00)                    #check precision
	conf.AKT=(ABZERO+conf.TEMPC)*BOLTZ
	conf.AN1=conf.FRAC[1]*CORR*ALOSCH                                           
	conf.AN2=conf.FRAC[2]*CORR*ALOSCH                                           
	conf.AN3=conf.FRAC[3]*CORR*ALOSCH                                           
	conf.AN4=conf.FRAC[4]*CORR*ALOSCH
	conf.AN5=conf.FRAC[5]*CORR*ALOSCH
	conf.AN6=conf.FRAC[6]*CORR*ALOSCH                                           
	conf.AN=float(100.00*CORR*ALOSCH)
	conf.AN=100.00*CORR*ALOSCH                                            
	#VAN1=FRAC[1]*CORR*CONST4*1.0D15                                   
	#VAN2=FRAC[2]*CORR*CONST4*1.0D15                                   
	#VAN3=FRAC(3)*CORR*CONST4*1.0D15                                   
	#VAN4=FRAC[4]*CORR*CONST4*1.0D15
	#VAN5=FRAC[5]*CORR*CONST4*1.0D15
	#VAN6=FRAC[6]*CORR*CONST4*1.0D15                                   
	#VAN=100.00*CORR*CONST4*1.0D15
	conf.VAN1=conf.FRAC[1]*CORR*ALOSCH*conf.VC                                   
	conf.VAN2=conf.FRAC[2]*CORR*ALOSCH*conf.VC                                   
	conf.VAN3=conf.FRAC[3]*CORR*ALOSCH*conf.VC                                  
	conf.VAN4=conf.FRAC[4]*CORR*ALOSCH*conf.VC
	conf.VAN5=conf.FRAC[5]*CORR*ALOSCH*conf.VC
	conf.VAN6=conf.FRAC[6]*CORR*ALOSCH*conf.VC                                  
	conf.VAN=float(100.00*CORR*ALOSCH*conf.VC)    #22745 #22945
	# CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
	E=numpy.zeros(20001)
	conf.GAM=numpy.zeros(20001)
	conf.BET=numpy.zeros(20001)
	if(conf.EFINAL <= 20000.0):
		conf.ESTEP=float(conf.EFINAL/float(conf.NSTEP))
		EHALF=float(conf.ESTEP/2.00)
		conf.E[1]=EHALF
		conf.GAM[1]=(conf.EMS+conf.E[1])/conf.EMS
		conf.BET[1]=math.sqrt(1.00-1.00/(conf.GAM[1]*conf.GAM[1]))  #ifcontinues
		for I in range(2,20000+1):                      #ifcontinues
			AJ=float(I-1)
			conf.E[I]=EHALF+conf.ESTEP*AJ
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))
	elif(conf.EFINAL > 20000.0 and conf.EFINAL <= 140000.) :
		conf.ESTEP=1.0
		EHALF=0.5
		conf.E[1]=EHALF
		conf.GAM[1]=(conf.EMS+conf.E[1])/conf.EMS
		conf.BET[1]=math.sqrt(1.00-1.00/(conf.GAM[1]*conf.GAM[1]))
		for i in range(2,16000+1):
			AJ=float(I-1)
			conf.E[I]=EHALF+conf.ESTEP*AJ
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))   #22768 #22968  
		ESTEP1=(conf.EFINAL-16000.0)/float(4000)
		for I in range(16001,2000+1):
			AJ=float(I-16000)
			conf.E[I]=16000.0+AJ*ESTEP1
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))
	else:
		conf.ESTEP=1.0
		EHALF=0.5
		conf.E[1]=EHALF
		conf.GAM[1]=(conf.EMS+conf.E[1])/conf.EMS
		conf.BET[1]=math.sqrt(1.00-1.00/(conf.GAM[1]*conf.GAM[1]))
		for I in range(2,12000+1):
			AJ=float(I-1)
			conf.E[I]=EHALF+conf.ESTEP*AJ
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))
		ESTEP1=20.0
		for I in range(12001,16000+1):
			AJ=float(I-12000)
			conf.E[I]=12000.0+AJ*ESTEP1
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))
		ESTEP2=(conf.EFINAL-92000.0)/float(4000)
		for I in range(16001,20000+1):
			AJ=float(I-16000)
			conf.E[I]=92000.0+AJ*ESTEP2
			conf.GAM[I]=(conf.EMS+conf.E[I])/conf.EMS
			conf.BET[I]=math.sqrt(1.00-1.00/(conf.GAM[I]*conf.GAM[I]))
	# endif
	#  RADIANS PER PICOSECOND                                        
	conf.WB=AWB*conf.BMAG*1.0*(10**-12 )
	#   METRES PER PICOSECOND

	if(conf.BMAG == 0.00):
		return LAST
	conf.EOVB=conf.EFIELD*1*(10**-9)/conf.BMAG
	return LAST
	
	GOTO999()                                                            
	# end                                                               

# SETUP(0)