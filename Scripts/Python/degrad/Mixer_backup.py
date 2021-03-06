import numpy
import time
import math
import sys
import conf
from Gasmix import *
def MIXER():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)                                         
	# CHARACTER*25 NAMEG,
	NAME1=' '*(25+1)
	NAME2=' '*(25+1)
	NAME3=' '*(25+1)
	NAME4=' '*(25+1)
	NAME5=' '*(25+1)
	NAME6=' '*(25+1)
	global AN1,AN2,AN3,AN4,AN5,AN6,AN
	AN1=conf.AN1
	AN2=conf.AN2
	AN3=conf.AN3
	AN4=conf.AN4
	AN5=conf.AN5
	AN6=conf.AN6
	AN=conf.AN
	global FRAC#[6] 
	FRAC=conf.FRAC 
	# not global             
	# CHARACTER*50 
	# DSCRPT=numpy.zeros((50+1),dtype=str)
	SCRP1=numpy.chararray((300+1),itemsize=50+1)
	SCRP2=numpy.chararray((300+1),itemsize=50+1)
	SCRP3=numpy.chararray((300+1),itemsize=50+1)
	SCRP4=numpy.chararray((300+1),itemsize=50+1)
	SCRP5=numpy.chararray((300+1),itemsize=50+1)
	SCRP6=numpy.chararray((300+1),itemsize=50+1)
	# CHARACTER*50 
	# DSCRPTN=numpy.zeros((50+1),dtype=str)
	SCRPN1=numpy.chararray((10+1),itemsize=50+1)
	SCRPN2=numpy.chararray((10+1),itemsize=50+1)
	SCRPN3=numpy.chararray((10+1),itemsize=50+1)
	SCRPN4=numpy.chararray((10+1),itemsize=50+1)
	SCRPN5=numpy.chararray((10+1),itemsize=50+1)
	SCRPN6=numpy.chararray((10+1),itemsize=50+1)                          
	global NGASN#[6] 
	NGASN=conf.NGASN
	global QELM#(20000)
	global QSUM#(20000)
	global QION#(6,20000)
	global QIN1#(250,20000)
	global QIN2#(250,20000)
	global QIN3#(250,20000)
	global QIN4#(250,20000)
	global QIN5#(250,20000)
	global QIN6#(250,20000)
	global QSATT#(20000)             
	global E#(20000)
	global EROOT#(20000)
	global QTOT#(20000)
	global QREL#(20000)
	global QINEL#(20000)
	global QEL#(20000)
	global NIN1,NIN2,NIN3,NIN4,NIN5,NIN6
	global LION#[6]
	global LIN1#(250)
	global LIN2#(250)
	global LIN3#(250)
	global LIN4#(250)
	global LIN5#(250)
	global LIN6#(250),
	global ALION#[6]
	global ALIN1#(250)
	global ALIN2#(250)
	global ALIN3#(250)
	global ALIN4#(250)
	global ALIN5#(250)
	global ALIN6#(250)
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	global CONST1,CONST2,CONST3,CONST4,CONST5                  
	global TMAX,SMALL,API,ESTART,THETA,PHI
	global TCFMAX#(10)
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE,NPLAST
	global CF#(20000,512)
	global EIN#(512)
	global TCF#(20000)
	global IARRY#(512)
	global RGAS#(512)
	global IPN#(512)
	global WPL#(512)
	global IZBR#(512)
	global IPLAST
	global PENFRA#[3,512]  
	global CFN#(20000,60)''',
	global TCFN#(20000)
	global SCLENUL#(60)    
	global PSCT#(20000,512)
	global ANGCT#(20000,512)
	global INDEX#(512)
	global NISO
	global FCION#(20000)
	global FCATT#(20000)
	global NEGAS#(512)
	global LEGAS#(512)
	global IESHELL#(512)            
	global VAN1,VAN2,VAN3,VAN4,VAN5,VAN6,VAN,IECASC
	global DOUBLE#(6,20000)
	global CMINIXSC#[6]
	global CMINEXSC#[6]
	global ECLOSS#[6]
	global WPLN#[6]
	global ICOUNT
	global AVPFRAC#(3,6)
	global NC0#(512)
	global EC0#(512)
	global NG1#(512)
	global EG1#(512)
	global NG2#(512)
	global EG2#(512)
	global WKLM#(512)
	global EFL#(512)
	global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	global NAMEG#[6]
	global NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6      
	global DSCRPT#(512)
	global DSCRPTN#(60)
	global ESPLIT#(512,20)
	global IONMODEL#(512)
	global BET#[2000]
	global GAM#(20000)
	global VC,EMS                        
	QELM=conf.QELM
	QSUM=conf.QSUM
	QION=conf.QION
	QIN1=conf.QIN1
	QIN2=conf.QIN2
	QIN3=conf.QIN3
	QIN4=conf.QIN4
	QIN5=conf.QIN5
	QIN6=conf.QIN6
	QSATT=conf.QSATT
	E=conf.E
	EROOT=conf.EROOT
	QTOT=conf.QTOT
	QREL=conf.QREL
	QINEL=conf.QINEL
	QEL=conf.QEL
	NIN1=conf.NIN1
	NIN2=conf.NIN2
	NIN3=conf.NIN3
	NIN4=conf.NIN4
	NIN5=conf.NIN5
	NIN6=conf.NIN6
	LION=conf.LION
	LIN1=conf.LIN1
	LIN2=conf.LIN2
	LIN3=conf.LIN3
	LIN4=conf.LIN4
	LIN5=conf.LIN5
	LIN6=conf.LIN6
	ALION=conf.ALION
	ALIN1=conf.ALIN1
	ALIN2=conf.ALIN2
	ALIN3=conf.ALIN3
	ALIN4=conf.ALIN4
	ALIN5=conf.ALIN5
	ALIN6=conf.ALIN6
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
	CONST1=conf.CONST1	
	CONST2=conf.CONST2	
	CONST3=conf.CONST3	
	CONST4=conf.CONST4	
	CONST5=conf.CONST5                  
	TMAX=conf.TMAX
	SMALL=conf.SMALL
	API=conf.API
	ESTART=conf.ESTART
	THETA=conf.THETA
	PHI=conf.PHI
	TCFMAX=conf.TCFMAX
	TCFMAX1=conf.TCFMAX1
	RSTART=conf.RSTART
	EFIELD=conf.EFIELD
	ETHRM=conf.ETHRM
	ECUT=conf.ECUT
	NDELTA=conf.NDELTA
	IMIP=conf.IMIP
	IWRITE=conf.IWRITE
	NPLAST=conf.NPLAST
	CF=conf.CF
	EIN=conf.EIN
	TCF=conf.TCF
	IARRY=conf.IARRY
	RGAS=conf.RGAS
	IPN=conf.IPN
	WPL=conf.WPL
	IZBR=conf.IZBR
	IPLAST=conf.IPLAST
	PENFRA=conf.PENFRA
	CFN=conf.CFN
	TCFN=conf.TCFN
	SCLENUL=conf.SCLENUL
	PSCT=conf.PSCT
	ANGCT=conf.ANGCT
	INDEX=conf.INDEX
	NISO=conf.NISO
	FCION=conf.FCION
	FCATT=conf.FCATT
	NEGAS=conf.NEGAS
	LEGAS=conf.LEGAS
	IESHELL=conf.IESHELL
	VAN1=conf.VAN1
	VAN2=conf.VAN2
	VAN3=conf.VAN3
	VAN4=conf.VAN4
	VAN5=conf.VAN5
	VAN6=conf.VAN6
	VAN=conf.VAN
	IECASC=conf.IECASC
	DOUBLE=conf.DOUBLE
	CMINIXSC=conf.CMINIXSC
	CMINEXSC=conf.CMINEXSC
	ECLOSS=conf.ECLOSS
	WPLN=conf.WPLN
	ICOUNT=conf.ICOUNT
	AVPFRAC=conf.AVPFRAC
	NC0=conf.NC0
	EC0=conf.EC0
	NG1=conf.NG1
	EG1=conf.EG1
	NG2=conf.NG2
	EG2=conf.EG2
	WKLM=conf.WKLM
	EFL=conf.EFL
	LCMP=conf.LCMP
	LCFLG=conf.LCFLG
	LRAY=conf.LRAY
	LRFLG=conf.LRFLG
	LPAP=conf.LPAP
	LPFLG=conf.LPFLG
	LBRM=conf.LBRM
	LBFLG=conf.LBFLG
	LPEFLG=conf.LPEFLG
	NAMEG=conf.NAMEG
	NGEXC1=conf.NGEXC1
	NGEXC2=conf.NGEXC2
	NGEXC3=conf.NGEXC3
	NGEXC4=conf.NGEXC4
	NGEXC5=conf.NGEXC5
	NGEXC6=conf.NGEXC6
	IDG1=conf.IDG1
	IDG2=conf.IDG2
	IDG3=conf.IDG3
	IDG4=conf.IDG4
	IDG5=conf.IDG5
	IDG6=conf.IDG6      
	DSCRPT=conf.DSCRPT
	DSCRPTN=conf.DSCRPTN
	ESPLIT=conf.ESPLIT
	IONMODEL=conf.IONMODEL
	BET=conf.BET
	GAM=conf.GAM
	VC=conf.VC
	EMS=conf.EMS
	Q1=numpy.zeros((6+1,20000+1))
	Q2=numpy.zeros((6+1,20000+1))
	Q3=numpy.zeros((6+1,20000+1))
	Q4=numpy.zeros((6+1,20000+1))
	Q5=numpy.zeros((6+1,20000+1))
	Q6=numpy.zeros((6+1,20000+1))
	E1=numpy.zeros((6+1))
	E2=numpy.zeros((6+1))
	E3=numpy.zeros((6+1))
	E4=numpy.zeros((6+1))
	E5=numpy.zeros((6+1))
	E6=numpy.zeros((6+1))
	EI1=numpy.zeros((250+1))
	EI2=numpy.zeros((250+1))
	EI3=numpy.zeros((250+1))
	EI4=numpy.zeros((250+1))
	EI5=numpy.zeros((250+1))
	EI6=numpy.zeros((250+1))
	QATT=numpy.zeros((6+1,20000+1))
	EION=numpy.zeros((6+1))
	PEQEL1=numpy.zeros((6+1,20000+1))
	PEQEL2=numpy.zeros((6+1,20000+1))
	PEQEL3=numpy.zeros((6+1,20000+1))
	PEQEL4=numpy.zeros((6+1,20000+1))
	PEQEL5=numpy.zeros((6+1,20000+1))
	PEQEL6=numpy.zeros((6+1,20000+1))
	PEQIN1=numpy.zeros((250+1,20000+1))
	PEQIN2=numpy.zeros((250+1,20000+1))
	PEQIN3=numpy.zeros((250+1,20000+1))
	PEQIN4=numpy.zeros((250+1,20000+1))
	PEQIN5=numpy.zeros((250+1,20000+1))
	PEQIN6=numpy.zeros((250+1,20000+1))
	PENFRA1=numpy.zeros((3+1,250+1))
	PENFRA2=numpy.zeros((3+1,250+1))
	PENFRA3=numpy.zeros((3+1,250+1))
	PENFRA4=numpy.zeros((3+1,250+1))
	PENFRA5=numpy.zeros((3+1,250+1))
	PENFRA6=numpy.zeros((3+1,250+1))
	KIN1=numpy.zeros((250+1))
	KIN2=numpy.zeros((250+1))
	KIN3=numpy.zeros((250+1))
	KIN4=numpy.zeros((250+1))
	KIN5=numpy.zeros((250+1))
	KIN6=numpy.zeros((250+1))
	KEL1=numpy.zeros((6+1))
	KEL2=numpy.zeros((6+1))
	KEL3=numpy.zeros((6+1))
	KEL4=numpy.zeros((6+1))
	KEL5=numpy.zeros((6+1))
	KEL6=numpy.zeros((6+1))
	EION1=numpy.zeros((30+1))
	EION2=numpy.zeros((30+1))
	EION3=numpy.zeros((30+1))
	EION4=numpy.zeros((30+1))
	EION5=numpy.zeros((30+1))
	EION6=numpy.zeros((30+1))
	QION1=numpy.zeros((30+1,20000+1))
	QION2=numpy.zeros((30+1,20000+1))
	QION3=numpy.zeros((30+1,20000+1))
	QION4=numpy.zeros((30+1,20000+1))
	QION5=numpy.zeros((30+1,20000+1))
	QION6=numpy.zeros((30+1,20000+1))
	PEQION1=numpy.zeros((30+1,20000+1))
	PEQION2=numpy.zeros((30+1,20000+1))
	PEQION3=numpy.zeros((30+1,20000+1))
	PEQION4=numpy.zeros((30+1,20000+1))
	PEQION5=numpy.zeros((30+1,20000+1))
	PEQION6=numpy.zeros((30+1,20000+1))
	LEGAS1=numpy.zeros((30+1))
	LEGAS2=numpy.zeros((30+1))
	LEGAS3=numpy.zeros((30+1))
	LEGAS4=numpy.zeros((30+1))
	LEGAS5=numpy.zeros((30+1))
	LEGAS6=numpy.zeros((30+1))
	IESHEL1=numpy.zeros((30+1))
	IESHEL2=numpy.zeros((30+1))
	IESHEL3=numpy.zeros((30+1))
	IESHEL4=numpy.zeros((30+1))
	IESHEL5=numpy.zeros((30+1))
	IESHEL6=numpy.zeros((30+1))
	EB1=numpy.zeros((30+1))
	EB2=numpy.zeros((30+1))
	EB3=numpy.zeros((30+1))
	EB4=numpy.zeros((30+1))
	EB5=numpy.zeros((30+1))
	EB6=numpy.zeros((30+1))
	NC01=numpy.zeros((30+1))
	NC02=numpy.zeros((30+1))
	NC03=numpy.zeros((30+1))
	NC04=numpy.zeros((30+1))
	NC05=numpy.zeros((30+1))
	NC06=numpy.zeros((30+1))
	EC01=numpy.zeros((30+1))
	EC02=numpy.zeros((30+1))
	EC03=numpy.zeros((30+1))
	EC04=numpy.zeros((30+1))
	EC05=numpy.zeros((30+1))
	EC06=numpy.zeros((30+1))
	NG11=numpy.zeros((30+1))
	NG12=numpy.zeros((30+1))
	NG13=numpy.zeros((30+1))
	NG14=numpy.zeros((30+1))
	NG15=numpy.zeros((30+1))
	NG16=numpy.zeros((30+1))
	EG11=numpy.zeros((30+1))
	EG12=numpy.zeros((30+1))
	EG13=numpy.zeros((30+1))
	EG14=numpy.zeros((30+1))
	EG15=numpy.zeros((30+1))
	EG16=numpy.zeros((30+1))
	NG21=numpy.zeros((30+1))
	NG22=numpy.zeros((30+1))
	NG23=numpy.zeros((30+1))
	NG24=numpy.zeros((30+1))
	NG25=numpy.zeros((30+1))
	NG26=numpy.zeros((30+1))
	EG21=numpy.zeros((30+1))
	EG22=numpy.zeros((30+1))
	EG23=numpy.zeros((30+1))
	EG24=numpy.zeros((30+1))
	EG25=numpy.zeros((30+1))
	EG26=numpy.zeros((30+1))
	WK1=numpy.zeros((30+1))
	WK2=numpy.zeros((30+1))
	WK3=numpy.zeros((30+1))
	WK4=numpy.zeros((30+1))
	WK5=numpy.zeros((30+1))
	WK6=numpy.zeros((30+1))
	EFL1=numpy.zeros((30+1))
	EFL2=numpy.zeros((30+1))
	EFL3=numpy.zeros((30+1))
	EFL4=numpy.zeros((30+1))
	EFL5=numpy.zeros((30+1))
	EFL6=numpy.zeros((30+1))
	IZBR1=numpy.zeros((250+1))
	IZBR2=numpy.zeros((250+1))
	IZBR3=numpy.zeros((250+1))
	IZBR4=numpy.zeros((250+1))
	IZBR5=numpy.zeros((250+1))
	IZBR6=numpy.zeros((250+1))
	QATT1=numpy.zeros((8+1,20000+1))
	QATT2=numpy.zeros((8+1,20000+1))
	QATT3=numpy.zeros((8+1,20000+1))
	QATT4=numpy.zeros((8+1,20000+1))
	QATT5=numpy.zeros((8+1,20000+1))
	QATT6=numpy.zeros((8+1,20000+1))
	QNUL1=numpy.zeros((10+1,20000+1))
	QNUL2=numpy.zeros((10+1,20000+1))
	QNUL3=numpy.zeros((10+1,20000+1))
	QNUL4=numpy.zeros((10+1,20000+1))
	QNUL5=numpy.zeros((10+1,20000+1))
	QNUL6=numpy.zeros((10+1,20000+1))
	SCLN1=numpy.zeros((10+1))
	SCLN2=numpy.zeros((10+1))
	SCLN3=numpy.zeros((10+1))
	SCLN4=numpy.zeros((10+1))
	SCLN5=numpy.zeros((10+1))
	SCLN6=numpy.zeros((10+1))
	ESPLIT1=numpy.zeros((5+1,20+1))
	ESPLIT2=numpy.zeros((5+1,20+1))
	ESPLIT3=numpy.zeros((5+1,20+1))
	ESPLIT4=numpy.zeros((5+1,20+1))
	ESPLIT5=numpy.zeros((5+1,20+1))
	ESPLIT6=numpy.zeros((5+1,20+1))
	#                                                                       
	#  ---------------------------------------------------------------------
	#                                                                       
	#     SUBROUTINE MIXER FILLS ARRAYS OF COLLISION FREQUENCY              
	#     CAN HAVE A MIXTURE OF UP TO 6 GASES                               
	#                                                                       
	#     MOD: STORE COUNTING IONISATION X-SECTION IN ARRAY CMINIXSC[6]
	#          AT MINIMUM IONISING ENERGY                                 
	#  ---------------------------------------------------------------------
	#                                                             
	NISO=0
	NIN1=0                                                            
	NIN2=0                                                            
	NIN3=0                                                            
	NIN4=0
	NIN5=0
	NIN6=0
	NION1=0
	NION2=0
	NION3=0
	NION4=0
	NION5=0
	NION6=0
	NATT1=0
	NATT2=0
	NATT3=0
	NATT4=0
	NATT5=0
	NATT6=0
	NUL1=0
	NUL2=0
	NUL3=0
	NUL4=0
	NUL5=0
	NUL6=0
	for J in range(1,6+1):
		NAMEG[J]='-------------------------'                              
		KEL1[J]=0
		KEL2[J]=0
		KEL3[J]=0
		KEL4[J]=0
		KEL5[J]=0
		KEL6[J]=0                       
		for I in range(1,20000+1):
			Q1[J][I]=0.00                                                     
			Q2[J][I]=0.00                                                     
			Q3[J][I]=0.00                                                     
			Q4[J][I]=0.00
			Q5[J][I]=0.00
			Q6[J][I]=0.00
			DOUBLE[J][I]=0.00    
		E1[J]=0.00                                                       
		E2[J]=0.00                                                       
		E3[J]=0.00                                                       
		E4[J]=0.00 
		E5[J]=0.00
		E6[J]=0.00
	for J in range(1,30+1):
		IESHEL1[J]=0
		IESHEL2[J]=0
		IESHEL3[J]=0
		IESHEL4[J]=0
		IESHEL5[J]=0
		IESHEL6[J]=0
		LEGAS1[J]=0
		LEGAS2[J]=0
		LEGAS3[J]=0
		LEGAS4[J]=0
		LEGAS5[J]=0
		LEGAS6[J]=0
		EION1[J]=0.00
		EION2[J]=0.00
		EION3[J]=0.00
		EION4[J]=0.00
		EION5[J]=0.00
		EION6[J]=0.00
		EB1[J]=0.00
		EB2[J]=0.00
		EB3[J]=0.00
		EB4[J]=0.00
		EB5[J]=0.00
		EB6[J]=0.00
		EC01[J]=0.00
		EC02[J]=0.00
		EC03[J]=0.00
		EC04[J]=0.00
		EC05[J]=0.00
		EC06[J]=0.00
		EG11[J]=0.00
		EG12[J]=0.00
		EG13[J]=0.00
		EG14[J]=0.00
		EG15[J]=0.00
		EG16[J]=0.00
		EG21[J]=0.00
		EG22[J]=0.00
		EG23[J]=0.00
		EG24[J]=0.00
		EG25[J]=0.00
		EG26[J]=0.00
		WK1[J]=0.00
		WK2[J]=0.00
		WK3[J]=0.00
		WK4[J]=0.00
		WK5[J]=0.00
		WK6[J]=0.00
		EFL1[J]=0.00
		EFL2[J]=0.00
		EFL3[J]=0.00
		EFL4[J]=0.00
		EFL5[J]=0.00
		EFL6[J]=0.00
		NC01[J]=0
		NC02[J]=0
		NC03[J]=0
		NC04[J]=0
		NC05[J]=0
		NC06[J]=0
		NG11[J]=0
		NG12[J]=0
		NG13[J]=0
		NG14[J]=0
		NG15[J]=0
		NG16[J]=0
		NG21[J]=0
		NG22[J]=0
		NG23[J]=0
		NG24[J]=0
		NG25[J]=0
		NG26[J]=0
		for I in range(1,20000+1):
			QION1[J][I]=0.00
			QION2[J][I]=0.00
			QION3[J][I]=0.00
			QION4[J][I]=0.00
			QION5[J][I]=0.00
			QION6[J][I]=0.00
	for K in range(1,8+1):
		for I in range(1,20000+1):
			QATT1[K][I]=0.0
			QATT2[K][I]=0.0
			QATT3[K][I]=0.0
			QATT4[K][I]=0.0
			QATT5[K][I]=0.0
			QATT6[K][I]=0.0
	for K in range(1,10+1):
		for I in range(1,20000+1):
			QNUL1[K][I]=0.0
			QNUL2[K][I]=0.0
			QNUL3[K][I]=0.0
			QNUL4[K][I]=0.0
			QNUL5[K][I]=0.0
			QNUL6[K][I]=0.0
	for I in range(1,512+1):
		IONMODEL[I]=0
		for K in range(1,20+1):
			ESPLIT[I][K]=0.0
	# CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
	if(EFINAL <= 20000.0):
		ESTEP=EFINAL/float(NSTEP)
		EHALF=ESTEP/2.00
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for I in range(2,20000+1):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
			EROOT[I]=math.sqrt(E[I])
		EROOT[1]=math.sqrt(EHALF)     
	elif(EFINAL > 20000.0 and EFINAL <= 140000.0) :
		ESTEP=1.0
		EHALF=0.5
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for I in range(2,16000+1):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
			EROOT[I]=math.sqrt(E[I])
		EROOT[1]=math.sqrt(EHALF)
		ESTEP1=(EFINAL-16000.0)/float(4000)
		for I in range(16001,20000+1):
			AJ=float(I-16000)
			E[I]=16000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
			EROOT[I]=math.sqrt(E[I])
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
			EROOT[I]=math.sqrt(E[I])
		EROOT[1]=math.sqrt(EHALF)
		ESTEP1=20.0
		for I in range(12001,16000+1):
			AJ=float(I-12000)
			E[I]=12000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
			EROOT[I]=math.sqrt(E[I])
		ESTEP2=(EFINAL-92000.0)/float(4000)
		for I in range(16001,20000+1):
			AJ=float(I-16000)
			E[I]=92000.0+AJ*ESTEP2
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
			EROOT[I]=math.sqrt(E[I])
	# endif
	#
	for I in range(1,250+1):
		IZBR1[I]=0
		IZBR2[I]=0
		IZBR3[I]=0
		IZBR4[I]=0
		IZBR5[I]=0
		IZBR6[I]=0
		KIN1[I]=0
		KIN2[I]=0
		KIN3[I]=0
		KIN4[I]=0
		KIN5[I]=0
		KIN6[I]=0
	for I in range(1,512+1):
		INDEX[I]=0                                               
	#                                                                       
	#   CALL GAS CROSS-SECTIONS 
	VIRIAL1=0
	VIRIAL2=0
	VIRIAL3=0
	VIRIAL4=0
	VIRIAL5=0
	VIRIAL6=0
	IONMODL1=0
	IONMODL2=0
	IONMODL3=0
	IONMODL4=0
	IONMODL5=0
	IONMODL6=0
	GASMIX(NGASN[1],Q1,QIN1,NIN1,E1,EI1,NAME1,VIRIAL1,EB1,PEQEL1,PEQIN1,PENFRA1,KEL1,KIN1,QION1,PEQION1,EION1,NION1,QATT1,NATT1,QNUL1,NUL1,SCLN1,NC01,EC01,WK1,EFL1,NG11,EG11,NG21,EG21,IZBR1,LEGAS1,IESHEL1,IONMODL1,ESPLIT1,SCRP1,SCRPN1) 
	if(1):
		QELM=conf.QELM
		QSUM=conf.QSUM
		QION=conf.QION
		QIN1=conf.QIN1
		QIN2=conf.QIN2
		QIN3=conf.QIN3
		QIN4=conf.QIN4
		QIN5=conf.QIN5
		QIN6=conf.QIN6
		QSATT=conf.QSATT
		E=conf.E
		EROOT=conf.EROOT
		QTOT=conf.QTOT
		QREL=conf.QREL
		QINEL=conf.QINEL
		QEL=conf.QEL
		NIN1=conf.NIN1
		NIN2=conf.NIN2
		NIN3=conf.NIN3
		NIN4=conf.NIN4
		NIN5=conf.NIN5
		NIN6=conf.NIN6
		LION=conf.LION
		LIN1=conf.LIN1
		LIN2=conf.LIN2
		LIN3=conf.LIN3
		LIN4=conf.LIN4
		LIN5=conf.LIN5
		LIN6=conf.LIN6
		ALION=conf.ALION
		ALIN1=conf.ALIN1
		ALIN2=conf.ALIN2
		ALIN3=conf.ALIN3
		ALIN4=conf.ALIN4
		ALIN5=conf.ALIN5
		ALIN6=conf.ALIN6
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
		CONST1=conf.CONST1	
		CONST2=conf.CONST2	
		CONST3=conf.CONST3	
		CONST4=conf.CONST4	
		CONST5=conf.CONST5                  
		TMAX=conf.TMAX
		SMALL=conf.SMALL
		API=conf.API
		ESTART=conf.ESTART
		THETA=conf.THETA
		PHI=conf.PHI
		TCFMAX=conf.TCFMAX
		TCFMAX1=conf.TCFMAX1
		RSTART=conf.RSTART
		EFIELD=conf.EFIELD
		ETHRM=conf.ETHRM
		ECUT=conf.ECUT
		NDELTA=conf.NDELTA
		IMIP=conf.IMIP
		IWRITE=conf.IWRITE
		NPLAST=conf.NPLAST
		CF=conf.CF
		EIN=conf.EIN
		TCF=conf.TCF
		IARRY=conf.IARRY
		RGAS=conf.RGAS
		IPN=conf.IPN
		WPL=conf.WPL
		IZBR=conf.IZBR
		IPLAST=conf.IPLAST
		PENFRA=conf.PENFRA
		CFN=conf.CFN
		TCFN=conf.TCFN
		SCLENUL=conf.SCLENUL
		PSCT=conf.PSCT
		ANGCT=conf.ANGCT
		INDEX=conf.INDEX
		NISO=conf.NISO
		FCION=conf.FCION
		FCATT=conf.FCATT
		NEGAS=conf.NEGAS
		LEGAS=conf.LEGAS
		IESHELL=conf.IESHELL
		VAN1=conf.VAN1
		VAN2=conf.VAN2
		VAN3=conf.VAN3
		VAN4=conf.VAN4
		VAN5=conf.VAN5
		VAN6=conf.VAN6
		VAN=conf.VAN
		IECASC=conf.IECASC
		DOUBLE=conf.DOUBLE
		CMINIXSC=conf.CMINIXSC
		CMINEXSC=conf.CMINEXSC
		ECLOSS=conf.ECLOSS
		WPLN=conf.WPLN
		ICOUNT=conf.ICOUNT
		AVPFRAC=conf.AVPFRAC
		NC0=conf.NC0
		EC0=conf.EC0
		NG1=conf.NG1
		EG1=conf.EG1
		NG2=conf.NG2
		EG2=conf.EG2
		WKLM=conf.WKLM
		EFL=conf.EFL
		LCMP=conf.LCMP
		LCFLG=conf.LCFLG
		LRAY=conf.LRAY
		LRFLG=conf.LRFLG
		LPAP=conf.LPAP
		LPFLG=conf.LPFLG
		LBRM=conf.LBRM
		LBFLG=conf.LBFLG
		LPEFLG=conf.LPEFLG
		NAMEG=conf.NAMEG
		NGEXC1=conf.NGEXC1
		NGEXC2=conf.NGEXC2
		NGEXC3=conf.NGEXC3
		NGEXC4=conf.NGEXC4
		NGEXC5=conf.NGEXC5
		NGEXC6=conf.NGEXC6
		IDG1=conf.IDG1
		IDG2=conf.IDG2
		IDG3=conf.IDG3
		IDG4=conf.IDG4
		IDG5=conf.IDG5
		IDG6=conf.IDG6      
		DSCRPT=conf.DSCRPT
		DSCRPTN=conf.DSCRPTN
		ESPLIT=conf.ESPLIT
		IONMODEL=conf.IONMODEL
		BET=conf.BET
		GAM=conf.GAM
		VC=conf.VC
		EMS=conf.EMS
	if(NGAS == 1):
		pass
	else: 
		GASMIX(NGASN[2],Q2,QIN2,NIN2,E2,EI2,NAME2,VIRIAL2,EB2,PEQEL2,PEQIN2,PENFRA2,KEL2,KIN2,QION2,PEQION2,EION2,NION2,QATT2,NATT2,QNUL2,NUL2,SCLN2,NC02,EC02,WK2,EFL2,NG12,EG12,NG22,EG22,IZBR2,LEGAS2,IESHEL2,IONMODL2,ESPLIT2,SCRP2,SCRPN2) 
		if(1):
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMS
	if(NGAS == 2):
		pass
	else: 
		GASMIX(NGASN[3],Q3,QIN3,NIN3,E3,EI3,NAME3,VIRIAL3,EB3,PEQEL3,PEQIN3,PENFRA3,KEL3,KIN3,QION3,PEQION3,EION3,NION3,QATT3,NATT3,QNUL3,NUL3,SCLN3,NC03,EC03,WK3,EFL3,NG13,EG13,NG23,EG23,IZBR3,LEGAS3,IESHEL3,IONMODL3,ESPLIT3,SCRP3,SCRPN3) 
		if(1):
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMS
	if(NGAS == 3):
		pass
	else: 
		GASMIX(NGASN[4],Q4,QIN4,NIN4,E4,EI4,NAME4,VIRIAL4,EB4,PEQEL4,PEQIN4,PENFRA4,KEL4,KIN4,QION4,PEQION4,EION4,NION4,QATT4,NATT4,QNUL4,NUL4,SCLN4,NC04,EC04,WK4,EFL4,NG14,EG14,NG24,EG24,IZBR4,LEGAS4,IESHEL4,IONMODL4,ESPLIT4,SCRP4,SCRPN4)
		if(1):
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMSR=conf.TORR
			IPEN=conf.IPEN
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMS
	if(NGAS == 4):
		pass
	else: 
		GASMIX(NGASN[5],Q5,QIN5,NIN5,E5,EI5,NAME5,VIRIAL5,EB5,PEQEL5,PEQIN5,PENFRA5,KEL5,KIN5,QION5,PEQION5,EION5,NION5,QATT5,NATT5,QNUL5,NUL5,SCLN5,NC05,EC05,WK5,EFL5,NG15,EG15,NG25,EG25,IZBR5,LEGAS5,IESHEL5,IONMODL5,ESPLIT5,SCRP5,SCRPN5)
		if(1):
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMS
	if(NGAS == 5):
		pass
	else: 
		GASMIX(NGASN[6],Q6,QIN6,NIN6,E6,EI6,NAME6,VIRIAL6,EB6,PEQEL6,PEQIN6,PENFRA6,KEL6,KIN6,QION6,PEQION6,EION6,NION6,QATT6,NATT6,QNUL6,NUL6,SCLN6,NC06,EC06,WK6,EFL6,NG16,EG16,NG26,EG26,IZBR6,LEGAS6,IESHEL6,IONMODL6,ESPLIT6,SCRP6,SCRPN6)  
		if(1):
			QELM=conf.QELM
			QSUM=conf.QSUM
			QION=conf.QION
			QIN1=conf.QIN1
			QIN2=conf.QIN2
			QIN3=conf.QIN3
			QIN4=conf.QIN4
			QIN5=conf.QIN5
			QIN6=conf.QIN6
			QSATT=conf.QSATT
			E=conf.E
			EROOT=conf.EROOT
			QTOT=conf.QTOT
			QREL=conf.QREL
			QINEL=conf.QINEL
			QEL=conf.QEL
			NIN1=conf.NIN1
			NIN2=conf.NIN2
			NIN3=conf.NIN3
			NIN4=conf.NIN4
			NIN5=conf.NIN5
			NIN6=conf.NIN6
			LION=conf.LION
			LIN1=conf.LIN1
			LIN2=conf.LIN2
			LIN3=conf.LIN3
			LIN4=conf.LIN4
			LIN5=conf.LIN5
			LIN6=conf.LIN6
			ALION=conf.ALION
			ALIN1=conf.ALIN1
			ALIN2=conf.ALIN2
			ALIN3=conf.ALIN3
			ALIN4=conf.ALIN4
			ALIN5=conf.ALIN5
			ALIN6=conf.ALIN6
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
			CONST1=conf.CONST1	
			CONST2=conf.CONST2	
			CONST3=conf.CONST3	
			CONST4=conf.CONST4	
			CONST5=conf.CONST5                  
			TMAX=conf.TMAX
			SMALL=conf.SMALL
			API=conf.API
			ESTART=conf.ESTART
			THETA=conf.THETA
			PHI=conf.PHI
			TCFMAX=conf.TCFMAX
			TCFMAX1=conf.TCFMAX1
			RSTART=conf.RSTART
			EFIELD=conf.EFIELD
			ETHRM=conf.ETHRM
			ECUT=conf.ECUT
			NDELTA=conf.NDELTA
			IMIP=conf.IMIP
			IWRITE=conf.IWRITE
			NPLAST=conf.NPLAST
			CF=conf.CF
			EIN=conf.EIN
			TCF=conf.TCF
			IARRY=conf.IARRY
			RGAS=conf.RGAS
			IPN=conf.IPN
			WPL=conf.WPL
			IZBR=conf.IZBR
			IPLAST=conf.IPLAST
			PENFRA=conf.PENFRA
			CFN=conf.CFN
			TCFN=conf.TCFN
			SCLENUL=conf.SCLENUL
			PSCT=conf.PSCT
			ANGCT=conf.ANGCT
			INDEX=conf.INDEX
			NISO=conf.NISO
			FCION=conf.FCION
			FCATT=conf.FCATT
			NEGAS=conf.NEGAS
			LEGAS=conf.LEGAS
			IESHELL=conf.IESHELL
			VAN1=conf.VAN1
			VAN2=conf.VAN2
			VAN3=conf.VAN3
			VAN4=conf.VAN4
			VAN5=conf.VAN5
			VAN6=conf.VAN6
			VAN=conf.VAN
			IECASC=conf.IECASC
			DOUBLE=conf.DOUBLE
			CMINIXSC=conf.CMINIXSC
			CMINEXSC=conf.CMINEXSC
			ECLOSS=conf.ECLOSS
			WPLN=conf.WPLN
			ICOUNT=conf.ICOUNT
			AVPFRAC=conf.AVPFRAC
			NC0=conf.NC0
			EC0=conf.EC0
			NG1=conf.NG1
			EG1=conf.EG1
			NG2=conf.NG2
			EG2=conf.EG2
			WKLM=conf.WKLM
			EFL=conf.EFL
			LCMP=conf.LCMP
			LCFLG=conf.LCFLG
			LRAY=conf.LRAY
			LRFLG=conf.LRFLG
			LPAP=conf.LPAP
			LPFLG=conf.LPFLG
			LBRM=conf.LBRM
			LBFLG=conf.LBFLG
			LPEFLG=conf.LPEFLG
			NAMEG=conf.NAMEG
			NGEXC1=conf.NGEXC1
			NGEXC2=conf.NGEXC2
			NGEXC3=conf.NGEXC3
			NGEXC4=conf.NGEXC4
			NGEXC5=conf.NGEXC5
			NGEXC6=conf.NGEXC6
			IDG1=conf.IDG1
			IDG2=conf.IDG2
			IDG3=conf.IDG3
			IDG4=conf.IDG4
			IDG5=conf.IDG5
			IDG6=conf.IDG6      
			DSCRPT=conf.DSCRPT
			DSCRPTN=conf.DSCRPTN
			ESPLIT=conf.ESPLIT
			IONMODEL=conf.IONMODEL
			BET=conf.BET
			GAM=conf.GAM
			VC=conf.VC
			EMS=conf.EMS
	# ---------------------------------------------------------------                                                         
	#  CORRECTION OF NUMBER DENSITY DUE TO VIRIAL COEFFICIENT               
	#  CAN BE defMED HERE NOT YET IMPLEMENTED.                          
	#-----------------------------------------------------------------      
	#-----------------------------------------------------------------      
	#     CALCULATION OF COLLISION FREQUENCIES FOR AN ARRAY OF              
	#     ELECTRON ENERGIES IN THE RANGE ZERO TO EFINAL        
	#                                                                     
	#     L=5*N-4    ELASTIC NTH GAS                                        
	#     L=5*N-3    IONISATION NTH GAS                               
	#     L=5*N-2    ATTACHMENT NTH GAS                                  
	#     L=5*N-1    INELASTIC NTH GAS    
	#     L=5*N      SUPERELASTIC NTH GAS                    
	#---------------------------------------------------------------   
	def GOTO600(NP):                                                         
		IPLAST=NP  
		# ----------------------------------------------------------------      
		#   CAN INCREASE ARRAY SIZE UP TO 1740 if MORE COMPLEX MIXTURES USED.
		#   1740 = 6 * 290 ( 6 = MAX NO OF GASES. 290 = MAX NO OF LEVELS )    
		# ------------------------------------------------------------------    
		if(IPLAST > 512):
			print('WARNING TOO MANY LEVELS IN CALCULATION. CAN INCREASE THE ARRAY SIZES FROM 512 UP TO 1740 MAXIMUM\n')                 

		if(IPLAST > 512):
		  	sys.exit()                                            
		# --------------------------------------------------------------------  
		#     CALCULATION OF TOTAL COLLISION FREQUENCY                          
		# --------------------------------------------------------------------- 
		TCF[IE]=0.00              #2380                                       
		for IL in range(1,IPLAST+1):
			print("MIXER 736 TCF[%d]=%f,CF[%d][%d]=%f"%(IE,TCF[IE],IE,IL,CF[IE][IL]))
			time.sleep(1)
			TCF[IE]=TCF[IE]+CF[IE][IL]
			if(CF[IE][IL]< 0.00):
				#WRITE(6,776) CF[IE][IL],IE,IL,IARRY(IL),EIN(IL),E[IE] 
				print(' WARNING NEGATIVE COLLISION FREQUENCY =',CF[IE][IL],' IE =',IE,' IL =',IL,' IARRY=',IARRY[IL],' EIN=',EIN[IL],' ENERGY=',E[IE])
		for IL in range(1,IPLAST+1):
			if(TCF[IE]== 0.00):
				CF[IE][IL]=0.00  #2390
			else:                                    
				CF[IE][IL]=CF[IE][IL]/TCF[IE]                                                                                          
		for IL in range(2,IPLAST+1):
			CF[IE][IL]=CF[IE][IL]+CF[IE][IL-1]                                   
		# FIX ROUNDING ERRORS AT HIGHEST VALUE
		CF[IE][IPLAST]=1.00
		#
		#     FCATT[IE]=FCATT[IE]*EROOT[IE]
		#     FCION[IE]=FCION[IE]*EROOT[IE]                                     
		#     TCF[IE]=TCF[IE]*EROOT[IE]   
		FCATT[IE]=FCATT[IE]*1.0e-10  
		FCION[IE]=FCION[IE]*1.0e-10                                       
		TCF[IE]=TCF[IE]*1.0e-10   
		# CALCULATION OF NULL COLLISION FREQUENCIES
		NP=0
		NPLAST=0
		if((NUL1+NUL2+NUL3+NUL4+NUL5+NUL6)== 0):
			# GO TO 699
			pass
		else:
			if(NUL1 > 0):
				for J in range(1,NUL1+1):
					NP=NP+1
					SCLENUL[NP]=SCLN1[J]
					DSCRPTN[NP]=SCRPN1[J]
					CFN[IE][NP]=QNUL1[J][IE]*VAN1*SCLENUL[NP]*BET[IE]
			# endif
			if(NUL2 > 0):
				for J in range(1,NUL2+1):
					NP=NP+1
					SCLENUL[NP]=SCLN2[J]
					DSCRPTN[NP]=SCRPN2[J]
					CFN[IE][NP]=QNUL2[J][IE]*VAN2*SCLENUL[NP]*BET[IE]
			# endif
			if(NUL3 > 0):
				for J in range(1,NUL3+1):
					NP=NP+1
					SCLENUL[NP]=SCLN3[J]
					DSCRPTN[NP]=SCRPN3[J]
					CFN[IE][NP]=QNUL3[J][IE]*VAN3*SCLENUL[NP]*BET[IE]
			# endif
			if(NUL4 > 0):
				for J in range(1,NUL4+1):
					NP=NP+1
					SCLENUL[NP]=SCLN4[J]
					DSCRPTN[NP]=SCRPN4[J]
					CFN[IE][NP]=QNUL4[J][IE]*VAN4*SCLENUL[NP]*BET[IE]
			# endif
			if(NUL5 > 0):
				for J in range(1,NUL5+1):
					NP=NP+1
					SCLENUL[NP]=SCLN5[J]
					DSCRPTN[NP]=SCRPN5[J]
					CFN[IE][NP]=QNUL5[J][IE]*VAN5*SCLENUL[NP]*BET[IE]
			# endif
			if(NUL6 > 0):
				for J in range(1,NUL6+1):
					NP=NP+1
					SCLENUL[NP]=SCLN6[J]
					DSCRPTN[NP]=SCRPN6[J]
					CFN[IE][NP]=QNUL6[J][IE]*VAN6*SCLENUL[NP]*BET[IE]
			# endif
			NPLAST=NP
			# SUM NULL COLLISIONS
			TCFN[IE]=0.0
			for IL in range(1,NPLAST+1):  # call 640  #2455
				TCFN[IE]=TCFN[IE]+CFN[IE][IL]
				if(CFN[IE][IL]< 0.0):
				#print(6,779) CFN[IE][IL],IE,IL
					print(' WARNING NEGATIVE NULL COLLISION REQUENCY =',CFN[IE][IL],' IE =',IE,' IL =',IL)
			for IL in range(1,NPLAST+1):
			  if(TCFN[IE]== 0.00):
			  	CFN[IE][IL]=0.00
			  else:
			  	CFN[IE][IL]=CFN[IE][IL]/TCFN[IE]
			TCFN[IE]=TCFN[IE]*1.0*(10**-10) #2467
			if(NPLAST == 1):
			  	pass
			else:
				for IL in range(2,NPLAST+1):
				    CFN[IE][IL]=CFN[IE][IL]+CFN[IE][IL-1]
				# FIX ROUNDING ERRORS AT HIGHEST VALUE
				CFN[IE][NPLAST]=1.00 
		#699
		#700
		globals().update(locals())
	# def GOTO260(NP):
		print("MIXER inside 260")
		def GOTO330(NP): 
			print("MIXER inside 330")
			def GOTO340(NP):
				print("MIXER inside 340")
				def GOTO430(NP):
					print("MIXER inside 430")
					def GOTO530(NP): 
						if(EFINAL < E6[4]):
							# GO TO 540                  
							pass
						else:
							if(NATT6 > 1):
								# 590 
								for JJ in range(1,NATT6+1):
									NP=NP+1
									IDG6=NP
									CF[IE][NP]=QATT6[JJ][IE]*VAN6*BET[IE]
									FCATT[IE]=FCATT[IE]+CF[IE][NP]
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									if(IE > 1):
										break
									else:    # did a swap here 

										NEGAS[NP]=6
										LEGAS[NP]=0
										IESHELL[NP]=0
										INDEX[NP]=0
										RGAS[NP]=RGAS6
										EIN[NP]=0.00
										IPN[NP]=-1
										L=28
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP6[2+NION6+JJ]
										PENFRA[1][NP]=0.0
										PENFRA[2][NP]=0.0
										PENFRA[3][NP]=0.0
										IONMODEL[NP]=IONMODL6
										for K in range(1,20+1):
											ESPLIT[NP][K]=ESPLIT6[IONMODL6][K]
							else:                   
								NP=NP+1
								IDG6=NP                                                           
								CF[IE][NP]=Q6[4][IE]*VAN6*BET[IE] 
								FCATT[IE]=FCATT[IE]+CF[IE][NP]
								PSCT[IE][NP]=0.5
								ANGCT[IE][NP]=1.0
								if(IE > 1):
									pass 
								else:
									NEGAS[NP]=6
									LEGAS[NP]=0
									IESHELL[NP]=0       
									INDEX[NP]=0                            
									RGAS[NP]=RGAS6                                                    
									EIN[NP]=0.00                                                     
									IPN[NP]=-1
									L=28                                                          
									IARRY[NP]=L
									IZBR[NP]=0  
									DSCRPT[NP]=SCRP6[3+NION6]
									PENFRA[1][NP]=0.0  
									PENFRA[2][NP]=0.0
									PENFRA[3][NP]=0.0        
						# 540	
						if(NIN6 == 0):
							pass          
						else:                                 
							for J in range(1,NIN6+1):
								NP=NP+1
								IDG6=NP      
								NEGAS[NP]=6
								LEGAS[NP]=0
								IESHELL[NP]=0                                                     
								CF[IE][NP]=QIN6[J][IE]*VAN6*BET[IE]
								# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
								if(IZBR6[J]!= 0 and LBRM == 0):
									CF[IE][NP]=0.0
								PSCT[IE][NP]=0.5
								ANGCT[IE][NP]=1.0
								INDEX[NP]=0 
								#
								if(KIN6[J]== 1) :
									PSCT1=PEQIN6[J][IE]
									ANGCUT(PSCT1,ANGC,PSCT2)
									ANGCT[IE][NP]=ANGC
									PSCT[IE][NP]=PSCT2
									INDEX[NP]=1
								# endif
								if(KIN6[J]== 2) :
									PSCT[IE][NP]=PEQIN6[J][IE]
									INDEX[NP]=2
								# endif
								#
								if(IE > 1):
									pass          
								else:
									RGAS[NP]=RGAS6                                                    
									EIN[NP]=EI6[J]/RGAS6
									L=29
									if(EI6[J]< 0.00):
										L=30                                          
										IPN[NP]=0         
										IARRY[NP]=L
										IZBR[NP]=IZBR6[J]  
										DSCRPT[NP]=SCRP6[4+NION6+NATT6+J]
										PENFRA[1][NP]=PENFRA6[1][J]
										PENFRA[2][NP]=PENFRA6[2][J]*1*(10**-6)/math.sqrt(3.00)
										PENFRA[3][NP]=PENFRA6[3][J]
										if(PENFRA[1][NP] > AVPFRAC[1][6]):
											AVPFRAC[1][6]=PENFRA[1][NP]
											AVPFRAC[2][6]=PENFRA[2][NP]
											AVPFRAC[3][6]=PENFRA[3][NP]
									# endif
									if(J == NIN6):
										CMINEXSC[6]=CMINEXSC[6]*AVPFRAC[1][6]  #2363
						# 560 CONTINUE     
						# 
						globals().update(locals())
						GOTO600(NP)                                                                      
					
					if(EFINAL < E5[4]):
						pass
					else:
						if(NATT5 > 1):
							for JJ in range(1,NATT5+1):
								NP=NP+1
								IDG5=NP
								CF[IE][NP]=QATT5[JJ,IE]*VAN5*BET[IE]
								FCATT[IE]=FCATT[IE]+CF[IE][NP]
								PSCT[IE][NP]=0.5
								ANGCT[IE][NP]=1.0
								if(IE > 1):
									pass
								else:
									NEGAS[NP]=5
									LEGAS[NP]=0
									IESHELL[NP]=0
									INDEX[NP]=0
									RGAS[NP]=RGAS5
									EIN[NP]=0.00
									IPN[NP]=-1
									L=23
									IARRY[NP]=L
									IZBR[NP]=0
									DSCRPT[NP]=SCRP5[2+NION5+JJ]
									PENFRA[1][NP]=0.0
									PENFRA[2][NP]=0.0
									PENFRA[3][NP]=0.0
						else:                    
							NP=NP+1
							IDG5=NP                                                           
							CF[IE][NP]=Q5[4][IE]*VAN5*BET[IE]
							FCATT[IE]=FCATT[IE]+CF[IE][NP]
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							if(IE > 1):
								pass
							else:
								NEGAS[NP]=5
								LEGAS[NP]=0
								IESHELL[NP]=0
								INDEX[NP]=0                                     
								RGAS[NP]=RGAS5                                                    
								EIN[NP]=0.00                                                     
								IPN[NP]=-1             
								L=23                                            
								IARRY[NP]=L
								IZBR[NP]=0
								DSCRPT[NP]=SCRP5[3+NION5]
								PENFRA[1][NP]=0.0  
								PENFRA[2][NP]=0.0 
								PENFRA[3][NP]=0.0        
								pass
					
					if(NIN5 == 0):
						pass
					else:
						for J in range(1,NIN5 +1):
							NP=NP+1
							IDG5=NP      
							NEGAS[NP]=5
							LEGAS[NP]=0
							IESHELL[NP]=0                                                     
							CF[IE][NP]=QIN5[J][IE]*VAN5*BET[IE] 
							# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
							if(IZBR5[J]!= 0 and LBRM == 0):
								CF[IE][NP]=0.0
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							INDEX[NP]=0
							#
							if(KIN5[J]== 1) :
								PSCT1=PEQIN5[J][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1
							# endif
							if(KIN5[J]== 2) :
								PSCT[IE][NP]=PEQIN5[J][IE]
								INDEX[NP]=2
							# endif  
							#        
							if(IE > 1):
								pass
							else:
								RGAS[NP]=RGAS5                                                    
								EIN[NP]=EI5[J]/RGAS5
								L=24
								if(EI5[J]< 0.00):
									L=25                                          
								IPN[NP]=0         
								IARRY[NP]=L
								IZBR[NP]=IZBR5[J]
								DSCRPT[NP]=SCRP5[4+NION5+NATT5+J]
								PENFRA[1][NP]=PENFRA5[1][J]
								PENFRA[2][NP]=PENFRA5[2][J]*1*(10**-6)/math.sqrt(3.00)
								PENFRA[3][NP]=PENFRA5[3][J]
								if(PENFRA[1][NP] > AVPFRAC[1][5]) : 
									AVPFRAC[1][5]=PENFRA[1][NP]
									AVPFRAC[2][5]=PENFRA[2][NP]
									AVPFRAC[3][5]=PENFRA[3][NP]
								# endif
								if(J == NIN5):
									CMINEXSC[5]=CMINEXSC[5]*AVPFRAC[1][5]  #2108
					#                                           
					# 460 
					if(NGAS == 5):
						GOTO600(NP)
					NP=NP+1
					IDG6=NP      
					NEGAS[NP]=6
					LEGAS[NP]=0
					IESHELL[NP]=0                                                     
					CF[IE][NP]=Q6[2][IE]*VAN6*BET[IE]
					PSCT[IE][NP]=0.5
					ANGCT[IE][NP]=1.0
					INDEX[NP]=0 
					#
					if(KEL6[2]== 1) :
						PSCT1=PEQEL6[2][IE]
						ANGCUT(PSCT1,ANGC,PSCT2)
						ANGCT[IE][NP]=ANGC
						PSCT[IE][NP]=PSCT2
						INDEX[NP]=1
					# endif
					if(KEL6[2]== 2) :
						PSCT[IE][NP]=PEQEL6[2][IE]
						INDEX[NP]=2
					# endif
					#  
					if(IE > 1):
						pass
					else:
						RGAS6=1.00+E6[2]/2.00                                           
						RGAS[NP]=RGAS6                                                    
						EIN[NP]=0.00                                                     
						IPN[NP]=0
						L=26                                                          
						IARRY[NP]=L
						IZBR[NP]=0  
						DSCRPT[NP]=SCRP6[2] 
						NAMEG[6]=NAME6  
						PENFRA[1][NP]=0.0
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0
						AVPFRAC[1][6]=0.0
						AVPFRAC[2][6]=0.0
						AVPFRAC[3][6]=0.0
						CMINEXSC[6]=E6[4]*AN6                                       
						CMINIXSC[6]=E6[5]*AN6
						ECLOSS[6]=E6[3]
						WPLN[6]=E6[6]
					# 462 
					if(EFINAL < E6[3]):
						GOTO530(NP)      
					if(NION6 > 1):
						# GO TO 470                               
						GOTO470(NP)
					else:
						NP=NP+1 
						IDG6=NP 
						# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
						if(ICOUNT==1):
							CF[IE][NP]=Q6[5][IE]*VAN6*BET[IE]
							FCION[IE]=FCION[IE]+CF[IE][NP]
							DOUBLE[6][IE]=Q6[3][IE]/Q6[5][IE]-1.00
						else:                                                         
							CF[IE][NP]=Q6[3][IE]*VAN6*BET[IE]
							FCION[IE]=FCION[IE]+CF[IE][NP]
						# endif
						NEGAS[NP]=6
						LEGAS[NP]=0
						IESHELL[NP]=0
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						#
						if(ICOUNT == 1):
							if(KEL6[5]== 1) :
								PSCT1=PEQEL6[5][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1      
						# endif
							if(KEL6[5]== 2) :
								PSCT[IE][NP]=PEQEL6[5][IE]
								INDEX[NP]=2
						# endif
						else:
							if(KEL6[3]== 1) :
								PSCT1=PEQEL6[3][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1      
							# endif
							if(KEL6[3]== 2) :
								PSCT[IE][NP]=PEQEL6[3][IE]
								INDEX[NP]=2
						# endif
						# endif
						#
						WPL[NP]=EB6[1]
						NC0[NP]=NC06[1]
						EC0[NP]=EC06[1]
						NG1[NP]=NG16[1]
						EG1[NP]=EG16[1]
						NG2[NP]=NG26[1]
						EG2[NP]=EG26[1]
						WKLM[NP]=WK6[1]
						EFL[NP]=EFL6[1]
						if(IE > 1):
							GOTO530(NP)
						RGAS[NP]=RGAS6                                                    
						EIN[NP]=E6[3]/RGAS6 
						IPN[NP]=1             
						L=27                                             
						IARRY[NP]=L
						IZBR[NP]=0  
						DSCRPT[NP]=SCRP6[3]
						PENFRA[1][NP]=0.0  
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0    
						GOTO530(NP)
					# 470 
					for KION in range(1,NION6+1):
						NP=NP+1
						IDG6=NP  
						# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
						CF[IE][NP]=QION6[KION][IE]*VAN6*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						NEGAS[NP]=6
						LEGAS[NP]=LEGAS6[KION]
						IESHELL[NP]=IESHEL6[KION]
						#
						if(KEL6[3]== 1) :
							PSCT1=PEQION6[KION][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1      
						# endif
						if(KEL6[3]== 2):
							PSCT[IE,NP]=PEQION6[KION,IE]
							INDEX[NP]=2
						# endif
						#
						WPL[NP]=EB6[KION]
						NC0[NP]=NC06[KION]
						EC0[NP]=EC06[KION]
						NG1[NP]=NG16[KION]
						EG1[NP]=EG16[KION]
						NG2[NP]=NG26[KION]
						EG2[NP]=EG26[KION]
						WKLM[NP]=WK6[KION]
						EFL[NP]=EFL6[KION]
						if(IE > 1):
							pass
						else:                                     
							RGAS[NP]=RGAS6                                                    
							EIN[NP]=EION6[KION]/RGAS6 
							IPN[NP]=1             
							L=27                                             
							IARRY[NP]=L
							IZBR[NP]=0  
							DSCRPT[NP]=SCRP6(2+KION)
							PENFRA[1][NP]=0.0  
							PENFRA[2][NP]=0.0
							PENFRA[3][NP]=0.0    
							IONMODEL[NP]=IONMODL6
							for K in range(1,20+1):
								ESPLIT[NP][K]=ESPLIT6[IONMODL6][K] 
					globals().update(locals())
					
					GOTO530(NP)
				if(NIN4 == 0):
					pass
				else:
					for J in range(1,NIN4+1):
						NP=NP+1
						IDG4=NP
						NEGAS[NP]=4
						LEGAS[NP]=0
						IESHELL[NP]=0
						CF[IE][NP]=QIN4[J][IE]*VAN4*BET[IE]
						# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
						if(IZBR4[J]!= 0 and LBRM == 0):
							CF[IE][NP]=0.0
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						#
						if(KIN4[J]== 1) :
							PSCT1=PEQIN4[J][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KIN4[J]== 2) :
							PSCT[IE][NP]=PEQIN4[J][IE]
							INDEX[NP]=2
						# endif
						#
						if(IE > 1):
							pass 
						else:      
							RGAS[NP]=RGAS4                                                    
							EIN[NP]=EI4[J]/RGAS4
							L=19
							if(EI4[J]< 0.00):
								L=20                                          
							IPN[NP]=0         
							IARRY[NP]=L
							IZBR[NP]=IZBR4[J]
							DSCRPT[NP]=SCRP4[4+NION4+NATT4+J]
							PENFRA[1][NP]=PENFRA4[1][J]
							PENFRA[2][NP]=PENFRA4[2][J]*1*(10**-6)/math.sqrt(3.00)
							PENFRA[3][NP]=PENFRA4[3][J]
							if(PENFRA[1][NP] > AVPFRAC[1][4]) : 
								AVPFRAC[1][4]=PENFRA[1][NP]
								AVPFRAC[2][4]=PENFRA[2][NP]
								AVPFRAC[3][4]=PENFRA[3][NP]
							# endif
							if(J == NIN4):
								CMINEXSC[4]=CMINEXSC[4]*AVPFRAC[1][4]
				#                                           
				if(NGAS == 4):
					GOTO600(NP)
				NP=NP+1
				IDG5=NP      
				NEGAS[NP]=5
				LEGAS[NP]=0
				IESHELL[NP]=0                                                     
				CF[IE][NP]=Q5[2][IE]*VAN5*BET[IE] 
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				INDEX[NP]=0
				#
				if(KEL5[2]== 1) : 
					PSCT1=PEQEL5[2][IE]
					ANGCUT(PSCT1,ANGC,PSCT2)
					ANGCT[IE][NP]=ANGC
					PSCT[IE][NP]=PSCT2
					INDEX[NP]=1
				# endif
				if(KEL5[2]== 2) :
					PSCT[IE][NP]=PEQEL5[2][IE]
					INDEX[NP]=2
				# endif
				# 
				if(IE > 1):
					pass
				else:                                    
					RGAS5=1.00+E5[2]/2.00                                           
					RGAS[NP]=RGAS5                                                    
					EIN[NP]=0.00                                                     
					IPN[NP]=0
					L=21                                                          
					IARRY[NP]=L
					IZBR[NP]=0
					DSCRPT[NP]=SCRP5[2] 
					NAMEG[5]=NAME5    
					PENFRA[1][NP]=0.0
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0
					AVPFRAC[1][5]=0.0
					AVPFRAC[2][5]=0.0
					AVPFRAC[3][5]=0.0
					CMINEXSC[5]=E5[4]*AN5                                    
					CMINIXSC[5]=E5[5]*AN5
					ECLOSS[5]=E5[3]
					WPLN[5]=E5[6]  #1897
				if(EFINAL < E5[3]):
					GOTO430(NP)  #yet to be 
				if(NION5 > 1):
						# GO TO 370             #yet to be                       
						pass
				else:
					NP=NP+1
					IDG5=NP  
					# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
					if(ICOUNT == 1):
						CF[IE][NP]=Q5[5][IE]*VAN5*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
						DOUBLE[5][IE]=Q5[3][IE]/Q5[5][IE]-1.00
					else:                                                         
						CF[IE][NP]=Q5[3][IE]*VAN5*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
					# endif
					NEGAS[NP]=5
					LEGAS[NP]=0
					IESHELL[NP]=0
					PSCT[IE][NP]=0.5
					ANGCT[IE][NP]=1.0
					INDEX[NP]=0 
					#
					if(ICOUNT == 1):
						if(KEL5[5]== 1) :
							PSCT1=PEQEL5[5][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KEL5[5]== 2) :
							PSCT[IE][NP]=PEQEL5[5][IE]
							INDEX[NP]=2
						# endif
					else:
						if(KEL5[3]== 1) :
							PSCT1=PEQEL5[3][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KEL5[3]== 2) :
							PSCT[IE][NP]=PEQEL5[3][IE]
							INDEX[NP]=2
						# endif
					# endif
					# 
					WPL[NP]=EB5[1]     
					NC0[NP]=NC05[1]
					EC0[NP]=EC05[1]
					NG1[NP]=NG15[1]
					EG1[NP]=EG15[1]
					NG2[NP]=NG25[1]
					EG2[NP]=EG25[1]
					WKLM[NP]=WK5[1]
					EFL[NP]=EFL5[1]
					if(IE > 1):
						GOTO430(NP)    #yet to be                                
					RGAS[NP]=RGAS5                                                    
					EIN[NP]=E5[3]/RGAS5 
					IPN[NP]=1
					L=22                                                          
					IARRY[NP]=L
					IZBR[NP]=0
					DSCRPT[NP]=SCRP5[3]  
					PENFRA[1][NP]=0.0  
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0 
					IONMODEL[NP]=IONMODL5
					for K in range(1,20+1):
						ESPLIT[NP][K]=ESPLIT5[IONMODL5][K] 
					GOTO430(NP)       #yet to be
				# 370 
				for KION in range(1,NION5+1):
					NP=NP+1
					IDG5=NP  
					# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
					CF[IE,NP]=QION5[KION][IE]*VAN5*BET[IE]
					FCION[IE]=FCION[IE]+CF[IE,NP]
					PSCT[IE,NP]=0.5
					ANGCT[IE,NP]=1.0
					INDEX[NP]=0 
					NEGAS[NP]=5
					LEGAS[NP]=LEGAS5[KION]
					IESHELL[NP]=IESHEL5[KION]
					#
					if(KEL5[3]== 1) :
						PSCT1=PEQION5[KION][IE]
						ANGCUT(PSCT1,ANGC,PSCT2)
						ANGCT[IE][NP]=ANGC
						PSCT[IE][NP]=PSCT2
						INDEX[NP]=1
					# endif
					if(KEL5[3]== 2) :
						PSCT[IE][NP]=PEQION5[KION][IE]
						INDEX[NP]=2
					# endif
					#
					WPL[NP]=EB5[KION]
					NC0[NP]=NC05[KION]
					EC0[NP]=EC05[KION]
					NG1[NP]=NG15[KION]
					EG1[NP]=EG15[KION]
					NG2[NP]=NG25[KION]
					EG2[NP]=EG25[KION]
					WKLM[NP]=WK5[KION]
					EFL[NP]=EFL5[KION]
					if(IE > 1):
						pass                                    
					else:
						RGAS[NP]=RGAS5                                                    
						EIN[NP]=EION5[KION]/RGAS5
						# 
						IPN[NP]=1
						L=22                                                          
						IARRY[NP]=L
						IZBR[NP]=0
						DSCRPT[NP]=SCRP5[2+KION]
						PENFRA[1][NP]=0.0  
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0 
						IONMODEL[NP]=IONMODL5
						for K in range(1,20+1):
							ESPLIT[NP][K]=ESPLIT5[IONMODL5][K]
				globals().update(locals())
				
				GOTO430(NP)
			if(EFINAL < E4[4]):
				GOTO340(NP)          
			if(NATT4 > 1):
				pass
			else:
				NP=NP+1
				IDG4=NP                                                           
				CF[IE][NP]=Q4[4][IE]*VAN4*BET[IE]
				FCATT[IE]=FCATT[IE]+CF[IE][NP]
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				if(IE > 1):
					GOTO340(NP)  
				NEGAS[NP]=4
				LEGAS[NP]=0
				IESHELL[NP]=0      
				INDEX[NP]=0                             
				RGAS[NP]=RGAS4                                                    
				EIN[NP]=0.00                                                     
				IPN[NP]=-1 
				L=18                                                        
				IARRY[NP]=L
				IZBR[NP]=0
				DSCRPT[NP]=SCRP4[3+NION4]
				PENFRA[1][NP]=0.0  
				PENFRA[2][NP]=0.0
				PENFRA[3][NP]=0.0        
				GOTO340(NP)
			#581 
			for JJ in range(1,NATT4+1):
				NP=NP+1
				IDG4=NP
				CF[IE][NP]=QATT4[JJ][IE]*VAN4*BET[IE]
				FCATT[IE]=FCATT[IE]+CF[IE][NP] 
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				if(IE > 1):
					pass
				else:
					NEGAS[NP]=4
					LEGAS[NP]=0
					IESHELL[NP]=0
					INDEX[NP]=0
					RGAS[NP]=RGAS4
					EIN[NP]=0.00
					IPN[NP]=-1
					L=18
					IARRY[NP]=L
					IZBR[NP]=0
					DSCRPT[NP]=SCRP4[2+NION4+JJ]
					PENFRA[1][NP]=0.0
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0
			globals().update(locals())
			
			GOTO340(NP)
		if(NGAS == 3):
			GOTO600(NP)
		NP=NP+1
		IDG4=NP      
		NEGAS[NP]=4
		LEGAS[NP]=0
		IESHELL[NP]=0                                                     
		CF[IE][NP]=Q4[2][IE]*VAN4*BET[IE] 
		PSCT[IE][NP]=0.5
		ANGCT[IE][NP]=1.0
		INDEX[NP]=0
		#
		if(KEL4[2]== 1) :
			PSCT1=PEQEL4[2][IE]
			ANGCUT(PSCT1,ANGC,PSCT2)
			ANGCT[IE][NP]=ANGC
			PSCT[IE][NP]=PSCT2
			INDEX[NP]=1  
		# endif
		if(KEL4[2]== 2) :
			PSCT[IE][NP]=PEQEL4[2][IE]
			INDEX[NP]=2
		# endif 
		#
		if(IE > 1):
			pass  
		else:                                  
			RGAS4=1.00+E4[2]/2.00                                           
			RGAS[NP]=RGAS4                                                    
			EIN[NP]=0.00                                                     
			IPN[NP]=0
			L=16                                                          
			IARRY[NP]=L
			IZBR[NP]=0
			DSCRPT[NP]=SCRP4[2]
			NAMEG[4]=NAME4 
			PENFRA[1][NP]=0.0
			PENFRA[2][NP]=0.0
			PENFRA[3][NP]=0.0
			AVPFRAC[1][4]=0.0 
			AVPFRAC[2][4]=0.0
			AVPFRAC[3][4]=0.0
			CMINEXSC[4]=E4[4]*AN4                                       
			CMINIXSC[4]=E4[5]*AN4
			ECLOSS[4]=E4[3]
			WPLN[4]=E4[6]
		if(EFINAL < E4[3]):
			GOTO330(NP)
		if(NION4 > 1):
			GOTO270(NP)                                   
		NP=NP+1
		IDG4=NP  
		# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
		if(ICOUNT == 1):
			CF[IE][NP]=Q4[5][IE]*VAN4*BET[IE]
			FCION[IE]=FCION[IE]+CF[IE][NP]
			DOUBLE[4][IE]=Q4[3][IE]/Q4[5][IE]-1.00
		else:                                                         
			CF[IE][NP]=Q4[3][IE]*VAN4*BET[IE]
			FCION[IE]=FCION[IE]+CF[IE][NP]
		# endif
		NEGAS[NP]=4
		LEGAS[NP]=0
		IESHELL[NP]=0
		PSCT[IE][NP]=0.5
		ANGCT[IE][NP]=1.0
		INDEX[NP]=0  
		#
		if(ICOUNT == 1):
			if(KEL4[5]== 1) :
				PSCT1=PEQEL4[5][IE]
				ANGCUT(PSCT1,ANGC,PSCT2)
				ANGCT[IE][NP]=ANGC
				PSCT[IE][NP]=PSCT2
				INDEX[NP]=1
			# endif
			if(KEL4[5]== 2) :
				PSCT[IE][NP]=PEQEL4[5][IE]
				INDEX[NP]=2
			# endif
		else:
			if(KEL4[3]== 1) :
				PSCT1=PEQEL4[3][IE]
				ANGCUT(PSCT1,ANGC,PSCT2)
				ANGCT[IE][NP]=ANGC
				PSCT[IE][NP]=PSCT2
				INDEX[NP]=1
			# endif
			if(KEL4[3]== 2) :
				PSCT[IE][NP]=PEQEL4[3][IE]
				INDEX[NP]=2
			# endif
		# endif
		#
		WPL[NP]=EB4[1]
		NC0[NP]=NC04[1]
		EC0[NP]=EC04[1]
		NG1[NP]=NG14[1]
		EG1[NP]=EG14[1]
		NG2[NP]=NG24[1]
		EG2[NP]=EG24[1]
		WKLM[NP]=WK4[1]
		EFL[NP]=EFL4[1]
		if(IE > 1):
			GOTO330(NP)
		RGAS[NP]=RGAS4                                                    
		EIN[NP]=E4[3]/RGAS4 
		IPN[NP]=1  
		L=17                                                        
		IARRY[NP]=L
		IZBR[NP]=0
		DSCRPT[NP]=SCRP4[3]   
		PENFRA[1][NP]=0.0  
		PENFRA[2][NP]=0.0 
		PENFRA[3][NP]=0.0  
		IONMODEL[NP]=IONMODL4
		for K in range(1,20+1):
			ESPLIT[NP][K]=ESPLIT4[IONMODL4][K] 
		GOTO330(NP)
		globals().update(locals())
		def GOTO270(NP):
			for KION in range(1,NION4+1):
				NP=NP+1
				IDG4=NP
				# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
				CF[IE][NP]=QION4[KION][IE]*VAN4*BET[IE]
				FCION[IE]=FCION[IE]+CF[IE][NP]
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				INDEX[NP]=0  
				NEGAS[NP]=4
				LEGAS[NP]=LEGAS4[KION]
				IESHELL[NP]=IESHEL4[KION]
				#
				if(KEL4[3]== 1):
					PSCT1=PEQION4[KION][IE]
					ANGCUT(PSCT1,ANGC,PSCT2)
					ANGCT[IE][NP]=ANGC
					PSCT[IE][NP]=PSCT2
					INDEX[NP]=1
				# endif
				if(KEL4[3]== 2):
					PSCT[IE][NP]=PEQION4[KION][IE]
					INDEX[NP]=2
				# endif
				# 
				WPL[NP]=EB4[KION]
				NC0[NP]=NC04[KION]
				EC0[NP]=EC04[KION]
				NG1[NP]=NG14[KION]
				EG1[NP]=EG14[KION]
				NG2[NP]=NG24[KION]
				EG2[NP]=EG24[KION]
				WKLM[NP]=WK4[KION]
				EFL[NP]=EFL4[KION]
				if(IE > 1):
					pass
				else:
					RGAS[NP]=RGAS4                                                    
					EIN[NP]=EION4[KION]/RGAS4
					# 
					IPN[NP]=1
					L=17                                                        
					IARRY[NP]=L
					IZBR[NP]=0
					DSCRPT[NP]=SCRP4[2+KION]
					PENFRA[1][NP]=0.0  
					PENFRA[2][NP]=0.0 
					PENFRA[3][NP]=0.0  
					IONMODEL[NP]=IONMODL4
					for K in range(1,20+1):
						ESPLIT[NP][K]=ESPLIT4[IONMODL4][K] 
			globals().update(locals())
			GOTO330(NP)

	def GOTO30(NP):
			print("MIXER inside 30")
			globals().update(locals())
			def GOTO40(NP):
				print("MIXER inside 40")
				globals().update(locals())
				def GOTO130(NP):
					print("MIXER inside 130")
					def GOTO230(NP):
						print("MIXER inside 230")
						def GOTO260(NP):
							print("MIXER inside 260")
							def GOTO330(NP): 
								print("MIXER inside 330")
								def GOTO340(NP):
									print("MIXER inside 340")
									def GOTO430(NP):
										print("MIXER inside 430")
										def GOTO530(NP): 
											if(EFINAL < E6[4]):
												# GO TO 540                  
												pass
											else:
												if(NATT6 > 1):
													# 590 
													for JJ in range(1,NATT6+1):
														NP=NP+1
														IDG6=NP
														CF[IE][NP]=QATT6[JJ][IE]*VAN6*BET[IE]
														FCATT[IE]=FCATT[IE]+CF[IE][NP]
														PSCT[IE][NP]=0.5
														ANGCT[IE][NP]=1.0
														if(IE > 1):
															break
														else:    # did a swap here 

															NEGAS[NP]=6
															LEGAS[NP]=0
															IESHELL[NP]=0
															INDEX[NP]=0
															RGAS[NP]=RGAS6
															EIN[NP]=0.00
															IPN[NP]=-1
															L=28
															IARRY[NP]=L
															IZBR[NP]=0
															DSCRPT[NP]=SCRP6[2+NION6+JJ]
															PENFRA[1][NP]=0.0
															PENFRA[2][NP]=0.0
															PENFRA[3][NP]=0.0
															IONMODEL[NP]=IONMODL6
															for K in range(1,20+1):
																ESPLIT[NP][K]=ESPLIT6[IONMODL6][K]
												else:                   
													NP=NP+1
													IDG6=NP                                                           
													CF[IE][NP]=Q6[4][IE]*VAN6*BET[IE] 
													FCATT[IE]=FCATT[IE]+CF[IE][NP]
													PSCT[IE][NP]=0.5
													ANGCT[IE][NP]=1.0
													if(IE > 1):
														pass 
													else:
														NEGAS[NP]=6
														LEGAS[NP]=0
														IESHELL[NP]=0       
														INDEX[NP]=0                            
														RGAS[NP]=RGAS6                                                    
														EIN[NP]=0.00                                                     
														IPN[NP]=-1
														L=28                                                          
														IARRY[NP]=L
														IZBR[NP]=0  
														DSCRPT[NP]=SCRP6[3+NION6]
														PENFRA[1][NP]=0.0  
														PENFRA[2][NP]=0.0
														PENFRA[3][NP]=0.0        
											# 540	
											if(NIN6 == 0):
												pass          
											else:                                 
												for J in range(1,NIN6+1):
													NP=NP+1
													IDG6=NP      
													NEGAS[NP]=6
													LEGAS[NP]=0
													IESHELL[NP]=0                                                     
													CF[IE][NP]=QIN6[J][IE]*VAN6*BET[IE]
													# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
													if(IZBR6[J]!= 0 and LBRM == 0):
														CF[IE][NP]=0.0
													PSCT[IE][NP]=0.5
													ANGCT[IE][NP]=1.0
													INDEX[NP]=0 
													#
													if(KIN6[J]== 1) :
														PSCT1=PEQIN6[J][IE]
														ANGCUT(PSCT1,ANGC,PSCT2)
														ANGCT[IE][NP]=ANGC
														PSCT[IE][NP]=PSCT2
														INDEX[NP]=1
													# endif
													if(KIN6[J]== 2) :
														PSCT[IE][NP]=PEQIN6[J][IE]
														INDEX[NP]=2
													# endif
													#
													if(IE > 1):
														pass          
													else:
														RGAS[NP]=RGAS6                                                    
														EIN[NP]=EI6[J]/RGAS6
														L=29
														if(EI6[J]< 0.00):
															L=30                                          
															IPN[NP]=0         
															IARRY[NP]=L
															IZBR[NP]=IZBR6[J]  
															DSCRPT[NP]=SCRP6[4+NION6+NATT6+J]
															PENFRA[1][NP]=PENFRA6[1][J]
															PENFRA[2][NP]=PENFRA6[2][J]*1*(10**-6)/math.sqrt(3.00)
															PENFRA[3][NP]=PENFRA6[3][J]
															if(PENFRA[1][NP] > AVPFRAC[1][6]):
																AVPFRAC[1][6]=PENFRA[1][NP]
																AVPFRAC[2][6]=PENFRA[2][NP]
																AVPFRAC[3][6]=PENFRA[3][NP]
														# endif
														if(J == NIN6):
															CMINEXSC[6]=CMINEXSC[6]*AVPFRAC[1][6]  #2363
											# 560 CONTINUE     
											# 
											globals().update(locals())
											GOTO600(NP)                                                                      

										if(EFINAL < E5[4]):
											pass
										else:
											if(NATT5 > 1):
												for JJ in range(1,NATT5+1):
													NP=NP+1
													IDG5=NP
													CF[IE][NP]=QATT5[JJ,IE]*VAN5*BET[IE]
													FCATT[IE]=FCATT[IE]+CF[IE][NP]
													PSCT[IE][NP]=0.5
													ANGCT[IE][NP]=1.0
													if(IE > 1):
														pass
													else:
														NEGAS[NP]=5
														LEGAS[NP]=0
														IESHELL[NP]=0
														INDEX[NP]=0
														RGAS[NP]=RGAS5
														EIN[NP]=0.00
														IPN[NP]=-1
														L=23
														IARRY[NP]=L
														IZBR[NP]=0
														DSCRPT[NP]=SCRP5[2+NION5+JJ]
														PENFRA[1][NP]=0.0
														PENFRA[2][NP]=0.0
														PENFRA[3][NP]=0.0
											else:                    
												NP=NP+1
												IDG5=NP                                                           
												CF[IE][NP]=Q5[4][IE]*VAN5*BET[IE]
												FCATT[IE]=FCATT[IE]+CF[IE][NP]
												PSCT[IE][NP]=0.5
												ANGCT[IE][NP]=1.0
												if(IE > 1):
													pass
												else:
													NEGAS[NP]=5
													LEGAS[NP]=0
													IESHELL[NP]=0
													INDEX[NP]=0                                     
													RGAS[NP]=RGAS5                                                    
													EIN[NP]=0.00                                                     
													IPN[NP]=-1             
													L=23                                            
													IARRY[NP]=L
													IZBR[NP]=0
													DSCRPT[NP]=SCRP5[3+NION5]
													PENFRA[1][NP]=0.0  
													PENFRA[2][NP]=0.0 
													PENFRA[3][NP]=0.0        
													pass
										
										if(NIN5 == 0):
											pass
										else:
											for J in range(1,NIN5 +1):
												NP=NP+1
												IDG5=NP      
												NEGAS[NP]=5
												LEGAS[NP]=0
												IESHELL[NP]=0                                                     
												CF[IE][NP]=QIN5[J][IE]*VAN5*BET[IE] 
												# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
												if(IZBR5[J]!= 0 and LBRM == 0):
													CF[IE][NP]=0.0
												PSCT[IE][NP]=0.5
												ANGCT[IE][NP]=1.0
												INDEX[NP]=0
												#
												if(KIN5[J]== 1) :
													PSCT1=PEQIN5[J][IE]
													ANGCUT(PSCT1,ANGC,PSCT2)
													ANGCT[IE][NP]=ANGC
													PSCT[IE][NP]=PSCT2
													INDEX[NP]=1
												# endif
												if(KIN5[J]== 2) :
													PSCT[IE][NP]=PEQIN5[J][IE]
													INDEX[NP]=2
												# endif  
												#        
												if(IE > 1):
													pass
												else:
													RGAS[NP]=RGAS5                                                    
													EIN[NP]=EI5[J]/RGAS5
													L=24
													if(EI5[J]< 0.00):
														L=25                                          
													IPN[NP]=0         
													IARRY[NP]=L
													IZBR[NP]=IZBR5[J]
													DSCRPT[NP]=SCRP5[4+NION5+NATT5+J]
													PENFRA[1][NP]=PENFRA5[1][J]
													PENFRA[2][NP]=PENFRA5[2][J]*1*(10**-6)/math.sqrt(3.00)
													PENFRA[3][NP]=PENFRA5[3][J]
													if(PENFRA[1][NP] > AVPFRAC[1][5]) : 
														AVPFRAC[1][5]=PENFRA[1][NP]
														AVPFRAC[2][5]=PENFRA[2][NP]
														AVPFRAC[3][5]=PENFRA[3][NP]
													# endif
													if(J == NIN5):
														CMINEXSC[5]=CMINEXSC[5]*AVPFRAC[1][5]  #2108
										#                                           
										# 460 
										if(NGAS == 5):
											GOTO600(NP)
										NP=NP+1
										IDG6=NP      
										NEGAS[NP]=6
										LEGAS[NP]=0
										IESHELL[NP]=0                                                     
										CF[IE][NP]=Q6[2][IE]*VAN6*BET[IE]
										PSCT[IE][NP]=0.5
										ANGCT[IE][NP]=1.0
										INDEX[NP]=0 
										#
										if(KEL6[2]== 1) :
											PSCT1=PEQEL6[2][IE]
											ANGCUT(PSCT1,ANGC,PSCT2)
											ANGCT[IE][NP]=ANGC
											PSCT[IE][NP]=PSCT2
											INDEX[NP]=1
										# endif
										if(KEL6[2]== 2) :
											PSCT[IE][NP]=PEQEL6[2][IE]
											INDEX[NP]=2
										# endif
										#  
										if(IE > 1):
											pass
										else:
											RGAS6=1.00+E6[2]/2.00                                           
											RGAS[NP]=RGAS6                                                    
											EIN[NP]=0.00                                                     
											IPN[NP]=0
											L=26                                                          
											IARRY[NP]=L
											IZBR[NP]=0  
											DSCRPT[NP]=SCRP6[2] 
											NAMEG[6]=NAME6  
											PENFRA[1][NP]=0.0
											PENFRA[2][NP]=0.0
											PENFRA[3][NP]=0.0
											AVPFRAC[1][6]=0.0
											AVPFRAC[2][6]=0.0
											AVPFRAC[3][6]=0.0
											CMINEXSC[6]=E6[4]*AN6                                       
											CMINIXSC[6]=E6[5]*AN6
											ECLOSS[6]=E6[3]
											WPLN[6]=E6[6]
										# 462 
										if(EFINAL < E6[3]):
											GOTO530(NP)      
										if(NION6 > 1):
											# GO TO 470                               
											GOTO470(NP)
										else:
											NP=NP+1 
											IDG6=NP 
											# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
											if(ICOUNT==1):
												CF[IE][NP]=Q6[5][IE]*VAN6*BET[IE]
												FCION[IE]=FCION[IE]+CF[IE][NP]
												DOUBLE[6][IE]=Q6[3][IE]/Q6[5][IE]-1.00
											else:                                                         
												CF[IE][NP]=Q6[3][IE]*VAN6*BET[IE]
												FCION[IE]=FCION[IE]+CF[IE][NP]
											# endif
											NEGAS[NP]=6
											LEGAS[NP]=0
											IESHELL[NP]=0
											PSCT[IE][NP]=0.5
											ANGCT[IE][NP]=1.0
											INDEX[NP]=0
											#
											if(ICOUNT == 1):
												if(KEL6[5]== 1) :
													PSCT1=PEQEL6[5][IE]
													ANGCUT(PSCT1,ANGC,PSCT2)
													ANGCT[IE][NP]=ANGC
													PSCT[IE][NP]=PSCT2
													INDEX[NP]=1      
											# endif
												if(KEL6[5]== 2) :
													PSCT[IE][NP]=PEQEL6[5][IE]
													INDEX[NP]=2
											# endif
											else:
												if(KEL6[3]== 1) :
													PSCT1=PEQEL6[3][IE]
													ANGCUT(PSCT1,ANGC,PSCT2)
													ANGCT[IE][NP]=ANGC
													PSCT[IE][NP]=PSCT2
													INDEX[NP]=1      
												# endif
												if(KEL6[3]== 2) :
													PSCT[IE][NP]=PEQEL6[3][IE]
													INDEX[NP]=2
											# endif
											# endif
											#
											WPL[NP]=EB6[1]
											NC0[NP]=NC06[1]
											EC0[NP]=EC06[1]
											NG1[NP]=NG16[1]
											EG1[NP]=EG16[1]
											NG2[NP]=NG26[1]
											EG2[NP]=EG26[1]
											WKLM[NP]=WK6[1]
											EFL[NP]=EFL6[1]
											if(IE > 1):
												GOTO530(NP)
											RGAS[NP]=RGAS6                                                    
											EIN[NP]=E6[3]/RGAS6 
											IPN[NP]=1             
											L=27                                             
											IARRY[NP]=L
											IZBR[NP]=0  
											DSCRPT[NP]=SCRP6[3]
											PENFRA[1][NP]=0.0  
											PENFRA[2][NP]=0.0
											PENFRA[3][NP]=0.0    
											GOTO530(NP)
										# 470 
										for KION in range(1,NION6+1):
											NP=NP+1
											IDG6=NP  
											# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
											CF[IE][NP]=QION6[KION][IE]*VAN6*BET[IE]
											FCION[IE]=FCION[IE]+CF[IE][NP]
											PSCT[IE][NP]=0.5
											ANGCT[IE][NP]=1.0
											INDEX[NP]=0
											NEGAS[NP]=6
											LEGAS[NP]=LEGAS6[KION]
											IESHELL[NP]=IESHEL6[KION]
											#
											if(KEL6[3]== 1) :
												PSCT1=PEQION6[KION][IE]
												ANGCUT(PSCT1,ANGC,PSCT2)
												ANGCT[IE][NP]=ANGC
												PSCT[IE][NP]=PSCT2
												INDEX[NP]=1      
											# endif
											if(KEL6[3]== 2):
												PSCT[IE,NP]=PEQION6[KION,IE]
												INDEX[NP]=2
											# endif
											#
											WPL[NP]=EB6[KION]
											NC0[NP]=NC06[KION]
											EC0[NP]=EC06[KION]
											NG1[NP]=NG16[KION]
											EG1[NP]=EG16[KION]
											NG2[NP]=NG26[KION]
											EG2[NP]=EG26[KION]
											WKLM[NP]=WK6[KION]
											EFL[NP]=EFL6[KION]
											if(IE > 1):
												pass
											else:                                     
												RGAS[NP]=RGAS6                                                    
												EIN[NP]=EION6[KION]/RGAS6 
												IPN[NP]=1             
												L=27                                             
												IARRY[NP]=L
												IZBR[NP]=0  
												DSCRPT[NP]=SCRP6(2+KION)
												PENFRA[1][NP]=0.0  
												PENFRA[2][NP]=0.0
												PENFRA[3][NP]=0.0    
												IONMODEL[NP]=IONMODL6
												for K in range(1,20+1):
													ESPLIT[NP][K]=ESPLIT6[IONMODL6][K] 
										globals().update(locals())
										
										GOTO530(NP)
									if(NIN4 == 0):
										pass
									else:
										for J in range(1,NIN4+1):
											NP=NP+1
											IDG4=NP
											NEGAS[NP]=4
											LEGAS[NP]=0
											IESHELL[NP]=0
											CF[IE][NP]=QIN4[J][IE]*VAN4*BET[IE]
											# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
											if(IZBR4[J]!= 0 and LBRM == 0):
												CF[IE][NP]=0.0
											PSCT[IE][NP]=0.5
											ANGCT[IE][NP]=1.0
											INDEX[NP]=0
											#
											if(KIN4[J]== 1) :
												PSCT1=PEQIN4[J][IE]
												ANGCUT(PSCT1,ANGC,PSCT2)
												ANGCT[IE][NP]=ANGC
												PSCT[IE][NP]=PSCT2
												INDEX[NP]=1
											# endif
											if(KIN4[J]== 2) :
												PSCT[IE][NP]=PEQIN4[J][IE]
												INDEX[NP]=2
											# endif
											#
											if(IE > 1):
												pass 
											else:      
												RGAS[NP]=RGAS4                                                    
												EIN[NP]=EI4[J]/RGAS4
												L=19
												if(EI4[J]< 0.00):
													L=20                                          
												IPN[NP]=0         
												IARRY[NP]=L
												IZBR[NP]=IZBR4[J]
												DSCRPT[NP]=SCRP4[4+NION4+NATT4+J]
												PENFRA[1][NP]=PENFRA4[1][J]
												PENFRA[2][NP]=PENFRA4[2][J]*1*(10**-6)/math.sqrt(3.00)
												PENFRA[3][NP]=PENFRA4[3][J]
												if(PENFRA[1][NP] > AVPFRAC[1][4]) : 
													AVPFRAC[1][4]=PENFRA[1][NP]
													AVPFRAC[2][4]=PENFRA[2][NP]
													AVPFRAC[3][4]=PENFRA[3][NP]
												# endif
												if(J == NIN4):
													CMINEXSC[4]=CMINEXSC[4]*AVPFRAC[1][4]
									#                                           
									if(NGAS == 4):
										GOTO600(NP)
									NP=NP+1
									IDG5=NP      
									NEGAS[NP]=5
									LEGAS[NP]=0
									IESHELL[NP]=0                                                     
									CF[IE][NP]=Q5[2][IE]*VAN5*BET[IE] 
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									INDEX[NP]=0
									#
									if(KEL5[2]== 1) : 
										PSCT1=PEQEL5[2][IE]
										ANGCUT(PSCT1,ANGC,PSCT2)
										ANGCT[IE][NP]=ANGC
										PSCT[IE][NP]=PSCT2
										INDEX[NP]=1
									# endif
									if(KEL5[2]== 2) :
										PSCT[IE][NP]=PEQEL5[2][IE]
										INDEX[NP]=2
									# endif
									# 
									if(IE > 1):
										pass
									else:                                    
										RGAS5=1.00+E5[2]/2.00                                           
										RGAS[NP]=RGAS5                                                    
										EIN[NP]=0.00                                                     
										IPN[NP]=0
										L=21                                                          
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP5[2] 
										NAMEG[5]=NAME5    
										PENFRA[1][NP]=0.0
										PENFRA[2][NP]=0.0
										PENFRA[3][NP]=0.0
										AVPFRAC[1][5]=0.0
										AVPFRAC[2][5]=0.0
										AVPFRAC[3][5]=0.0
										CMINEXSC[5]=E5[4]*AN5                                    
										CMINIXSC[5]=E5[5]*AN5
										ECLOSS[5]=E5[3]
										WPLN[5]=E5[6]  #1897
									if(EFINAL < E5[3]):
										GOTO430(NP)  #yet to be 
									if(NION5 > 1):
											# GO TO 370             #yet to be                       
											pass
									else:
										NP=NP+1
										IDG5=NP  
										# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
										if(ICOUNT == 1):
											CF[IE][NP]=Q5[5][IE]*VAN5*BET[IE]
											FCION[IE]=FCION[IE]+CF[IE][NP]
											DOUBLE[5][IE]=Q5[3][IE]/Q5[5][IE]-1.00
										else:                                                         
											CF[IE][NP]=Q5[3][IE]*VAN5*BET[IE]
											FCION[IE]=FCION[IE]+CF[IE][NP]
										# endif
										NEGAS[NP]=5
										LEGAS[NP]=0
										IESHELL[NP]=0
										PSCT[IE][NP]=0.5
										ANGCT[IE][NP]=1.0
										INDEX[NP]=0 
										#
										if(ICOUNT == 1):
											if(KEL5[5]== 1) :
												PSCT1=PEQEL5[5][IE]
												ANGCUT(PSCT1,ANGC,PSCT2)
												ANGCT[IE][NP]=ANGC
												PSCT[IE][NP]=PSCT2
												INDEX[NP]=1
											# endif
											if(KEL5[5]== 2) :
												PSCT[IE][NP]=PEQEL5[5][IE]
												INDEX[NP]=2
											# endif
										else:
											if(KEL5[3]== 1) :
												PSCT1=PEQEL5[3][IE]
												ANGCUT(PSCT1,ANGC,PSCT2)
												ANGCT[IE][NP]=ANGC
												PSCT[IE][NP]=PSCT2
												INDEX[NP]=1
											# endif
											if(KEL5[3]== 2) :
												PSCT[IE][NP]=PEQEL5[3][IE]
												INDEX[NP]=2
											# endif
										# endif
										# 
										WPL[NP]=EB5[1]     
										NC0[NP]=NC05[1]
										EC0[NP]=EC05[1]
										NG1[NP]=NG15[1]
										EG1[NP]=EG15[1]
										NG2[NP]=NG25[1]
										EG2[NP]=EG25[1]
										WKLM[NP]=WK5[1]
										EFL[NP]=EFL5[1]
										if(IE > 1):
											GOTO430(NP)    #yet to be                                
										RGAS[NP]=RGAS5                                                    
										EIN[NP]=E5[3]/RGAS5 
										IPN[NP]=1
										L=22                                                          
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP5[3]  
										PENFRA[1][NP]=0.0  
										PENFRA[2][NP]=0.0
										PENFRA[3][NP]=0.0 
										IONMODEL[NP]=IONMODL5
										for K in range(1,20+1):
											ESPLIT[NP][K]=ESPLIT5[IONMODL5][K] 
										GOTO430(NP)       #yet to be
									# 370 
									for KION in range(1,NION5+1):
										NP=NP+1
										IDG5=NP  
										# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
										CF[IE,NP]=QION5[KION][IE]*VAN5*BET[IE]
										FCION[IE]=FCION[IE]+CF[IE,NP]
										PSCT[IE,NP]=0.5
										ANGCT[IE,NP]=1.0
										INDEX[NP]=0 
										NEGAS[NP]=5
										LEGAS[NP]=LEGAS5[KION]
										IESHELL[NP]=IESHEL5[KION]
										#
										if(KEL5[3]== 1) :
											PSCT1=PEQION5[KION][IE]
											ANGCUT(PSCT1,ANGC,PSCT2)
											ANGCT[IE][NP]=ANGC
											PSCT[IE][NP]=PSCT2
											INDEX[NP]=1
										# endif
										if(KEL5[3]== 2) :
											PSCT[IE][NP]=PEQION5[KION][IE]
											INDEX[NP]=2
										# endif
										#
										WPL[NP]=EB5[KION]
										NC0[NP]=NC05[KION]
										EC0[NP]=EC05[KION]
										NG1[NP]=NG15[KION]
										EG1[NP]=EG15[KION]
										NG2[NP]=NG25[KION]
										EG2[NP]=EG25[KION]
										WKLM[NP]=WK5[KION]
										EFL[NP]=EFL5[KION]
										if(IE > 1):
											pass                                    
										else:
											RGAS[NP]=RGAS5                                                    
											EIN[NP]=EION5[KION]/RGAS5
											# 
											IPN[NP]=1
											L=22                                                          
											IARRY[NP]=L
											IZBR[NP]=0
											DSCRPT[NP]=SCRP5[2+KION]
											PENFRA[1][NP]=0.0  
											PENFRA[2][NP]=0.0
											PENFRA[3][NP]=0.0 
											IONMODEL[NP]=IONMODL5
											for K in range(1,20+1):
												ESPLIT[NP][K]=ESPLIT5[IONMODL5][K]
									globals().update(locals())
									
									GOTO430(NP)
								if(EFINAL < E4[4]):
									GOTO340(NP)          
								if(NATT4 > 1):
									pass
								else:
									NP=NP+1
									IDG4=NP                                                           
									CF[IE][NP]=Q4[4][IE]*VAN4*BET[IE]
									FCATT[IE]=FCATT[IE]+CF[IE][NP]
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									if(IE > 1):
										GOTO340(NP)  
									NEGAS[NP]=4
									LEGAS[NP]=0
									IESHELL[NP]=0      
									INDEX[NP]=0                             
									RGAS[NP]=RGAS4                                                    
									EIN[NP]=0.00                                                     
									IPN[NP]=-1 
									L=18                                                        
									IARRY[NP]=L
									IZBR[NP]=0
									DSCRPT[NP]=SCRP4[3+NION4]
									PENFRA[1][NP]=0.0  
									PENFRA[2][NP]=0.0
									PENFRA[3][NP]=0.0        
									GOTO340(NP)
								#581 
								for JJ in range(1,NATT4+1):
									NP=NP+1
									IDG4=NP
									CF[IE][NP]=QATT4[JJ][IE]*VAN4*BET[IE]
									FCATT[IE]=FCATT[IE]+CF[IE][NP] 
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									if(IE > 1):
										pass
									else:
										NEGAS[NP]=4
										LEGAS[NP]=0
										IESHELL[NP]=0
										INDEX[NP]=0
										RGAS[NP]=RGAS4
										EIN[NP]=0.00
										IPN[NP]=-1
										L=18
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP4[2+NION4+JJ]
										PENFRA[1][NP]=0.0
										PENFRA[2][NP]=0.0
										PENFRA[3][NP]=0.0
								globals().update(locals())
								
								GOTO340(NP)
							if(NGAS == 3):
								GOTO600(NP)
							NP=NP+1
							IDG4=NP      
							NEGAS[NP]=4
							LEGAS[NP]=0
							IESHELL[NP]=0                                                     
							CF[IE][NP]=Q4[2][IE]*VAN4*BET[IE] 
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							INDEX[NP]=0
							#
							if(KEL4[2]== 1) :
								PSCT1=PEQEL4[2][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1  
							# endif
							if(KEL4[2]== 2) :
								PSCT[IE][NP]=PEQEL4[2][IE]
								INDEX[NP]=2
							# endif 
							#
							if(IE > 1):
								pass  
							else:                                  
								RGAS4=1.00+E4[2]/2.00                                           
								RGAS[NP]=RGAS4                                                    
								EIN[NP]=0.00                                                     
								IPN[NP]=0
								L=16                                                          
								IARRY[NP]=L
								IZBR[NP]=0
								DSCRPT[NP]=SCRP4[2]
								NAMEG[4]=NAME4 
								PENFRA[1][NP]=0.0
								PENFRA[2][NP]=0.0
								PENFRA[3][NP]=0.0
								AVPFRAC[1][4]=0.0 
								AVPFRAC[2][4]=0.0
								AVPFRAC[3][4]=0.0
								CMINEXSC[4]=E4[4]*AN4                                       
								CMINIXSC[4]=E4[5]*AN4
								ECLOSS[4]=E4[3]
								WPLN[4]=E4[6]
							if(EFINAL < E4[3]):
								GOTO330(NP)
							if(NION4 > 1):
								GOTO270(NP)                                   
							NP=NP+1
							IDG4=NP  
							# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
							if(ICOUNT == 1):
								CF[IE][NP]=Q4[5][IE]*VAN4*BET[IE]
								FCION[IE]=FCION[IE]+CF[IE][NP]
								DOUBLE[4][IE]=Q4[3][IE]/Q4[5][IE]-1.00
							else:                                                         
								CF[IE][NP]=Q4[3][IE]*VAN4*BET[IE]
								FCION[IE]=FCION[IE]+CF[IE][NP]
							# endif
							NEGAS[NP]=4
							LEGAS[NP]=0
							IESHELL[NP]=0
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							INDEX[NP]=0  
							#
							if(ICOUNT == 1):
								if(KEL4[5]== 1) :
									PSCT1=PEQEL4[5][IE]
									ANGCUT(PSCT1,ANGC,PSCT2)
									ANGCT[IE][NP]=ANGC
									PSCT[IE][NP]=PSCT2
									INDEX[NP]=1
								# endif
								if(KEL4[5]== 2) :
									PSCT[IE][NP]=PEQEL4[5][IE]
									INDEX[NP]=2
								# endif
							else:
								if(KEL4[3]== 1) :
									PSCT1=PEQEL4[3][IE]
									ANGCUT(PSCT1,ANGC,PSCT2)
									ANGCT[IE][NP]=ANGC
									PSCT[IE][NP]=PSCT2
									INDEX[NP]=1
								# endif
								if(KEL4[3]== 2) :
									PSCT[IE][NP]=PEQEL4[3][IE]
									INDEX[NP]=2
								# endif
							# endif
							#
							WPL[NP]=EB4[1]
							NC0[NP]=NC04[1]
							EC0[NP]=EC04[1]
							NG1[NP]=NG14[1]
							EG1[NP]=EG14[1]
							NG2[NP]=NG24[1]
							EG2[NP]=EG24[1]
							WKLM[NP]=WK4[1]
							EFL[NP]=EFL4[1]
							if(IE > 1):
								GOTO330(NP)
							RGAS[NP]=RGAS4                                                    
							EIN[NP]=E4[3]/RGAS4 
							IPN[NP]=1  
							L=17                                                        
							IARRY[NP]=L
							IZBR[NP]=0
							DSCRPT[NP]=SCRP4[3]   
							PENFRA[1][NP]=0.0  
							PENFRA[2][NP]=0.0 
							PENFRA[3][NP]=0.0  
							IONMODEL[NP]=IONMODL4
							for K in range(1,20+1):
								ESPLIT[NP][K]=ESPLIT4[IONMODL4][K] 
							GOTO330(NP)
							globals().update(locals())
							def GOTO270(NP):
								for KION in range(1,NION4+1):
									NP=NP+1
									IDG4=NP
									# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
									CF[IE][NP]=QION4[KION][IE]*VAN4*BET[IE]
									FCION[IE]=FCION[IE]+CF[IE][NP]
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									INDEX[NP]=0  
									NEGAS[NP]=4
									LEGAS[NP]=LEGAS4[KION]
									IESHELL[NP]=IESHEL4[KION]
									#
									if(KEL4[3]== 1):
										PSCT1=PEQION4[KION][IE]
										ANGCUT(PSCT1,ANGC,PSCT2)
										ANGCT[IE][NP]=ANGC
										PSCT[IE][NP]=PSCT2
										INDEX[NP]=1
									# endif
									if(KEL4[3]== 2):
										PSCT[IE][NP]=PEQION4[KION][IE]
										INDEX[NP]=2
									# endif
									# 
									WPL[NP]=EB4[KION]
									NC0[NP]=NC04[KION]
									EC0[NP]=EC04[KION]
									NG1[NP]=NG14[KION]
									EG1[NP]=EG14[KION]
									NG2[NP]=NG24[KION]
									EG2[NP]=EG24[KION]
									WKLM[NP]=WK4[KION]
									EFL[NP]=EFL4[KION]
									if(IE > 1):
										pass
									else:
										RGAS[NP]=RGAS4                                                    
										EIN[NP]=EION4[KION]/RGAS4
										# 
										IPN[NP]=1
										L=17                                                        
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP4[2+KION]
										PENFRA[1][NP]=0.0  
										PENFRA[2][NP]=0.0 
										PENFRA[3][NP]=0.0  
										IONMODEL[NP]=IONMODL4
										for K in range(1,20+1):
											ESPLIT[NP][K]=ESPLIT4[IONMODL4][K] 
								globals().update(locals())
								GOTO330(NP)
						if(EFINAL < E3[4]):
							pass
						else:


							if(NATT3 > 1):
								for JJ in range(1,NATT3+1):
									NP=NP+1
									IDG3=NP
									CF[IE][NP]=QATT3[JJ][IE]*VAN3*BET[IE]  
									FCATT[IE]=FCATT[IE]+CF[IE][NP]      
									PSCT[IE][NP]=0.5
									ANGCT[IE][NP]=1.0
									if(IE > 1):
										pass
									else:
										NEGAS[NP]=3
										LEGAS[NP]=0
										IESHELL[NP]=0
										INDEX[NP]=0
										RGAS[NP]=RGAS3
										EIN[NP]=0.00
										IPN[NP]=-1
										L=13
										IARRY[NP]=L
										IZBR[NP]=0
										DSCRPT[NP]=SCRP3[2+NION3+JJ]
										PENFRA[1][NP]=0.0
										PENFRA[2][NP]=0.0
										PENFRA[3][NP]=0.0
							else:
								NP=NP+1
								IDG3=NP                                                           
								CF[IE][NP]=Q3[4][IE]*VAN3*BET[IE]
								FCATT[IE]=FCATT[IE]+CF[IE][NP]
								PSCT[IE][NP]=0.5
								ANGCT[IE][NP]=1.0
								if(IE > 1):
									# GO TO 240	#yet to be 
									pass
								else:
									NEGAS[NP]=3
									LEGAS[NP]=0
									IESHELL[NP]=0
									INDEX[NP]=0                                            
									RGAS[NP]=RGAS3                                                   
									EIN[NP]=0.00                                                     
									IPN[NP]=-1 
									L=13                                                        
									IARRY[NP]=L
									IZBR[NP]=0
									DSCRPT[NP]=SCRP3[3+NION3]
									PENFRA[1][NP]=0.0 
									PENFRA[2][NP]=0.0
									PENFRA[3][NP]=0.0        
									pass
						
						# 240 
						if(NIN3 == 0):
							GOTO260(NP)
						for J in range(1,NIN3+1):
							NP=NP+1
							IDG3=NP      
							NEGAS[NP]=3
							LEGAS[NP]=0
							IESHELL[NP]=0                                                     
							CF[IE][NP]=QIN3[J][IE]*VAN3*BET[IE]
							# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
							if(IZBR3[J]!= 0 and LBRM == 0):
								CF[IE][NP]=0.0
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							INDEX[NP]=0
							#
							if(KIN3[J]== 1) :
								PSCT1=PEQIN3[J][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1
							# endif
							if(KIN3[J]== 2) :
								PSCT[IE][NP]=PEQIN3[J,IE]
								INDEX[NP]=2
							# endif
							#
							if(IE > 1):
								pass                                     
							else:
								RGAS[NP]=RGAS3                                                    
								EIN[NP]=EI3[J]/RGAS3
								L=14
								if(EI3[J]< 0.00):
									L=15                                          
								IPN[NP]=0
								IARRY[NP]=L
								IZBR[NP]=IZBR3[J]
								DSCRPT[NP]=SCRP3[4+NION3+NATT3+J]
								PENFRA[1][NP]=PENFRA3[1][J]
								PENFRA[2][NP]=PENFRA3[2][J]*1.0*(10**-6)/math.sqrt(3.00)
								PENFRA[3][NP]=PENFRA3[3][J]  
								if(PENFRA[1][NP] > AVPFRAC[1][3]) : 
									AVPFRAC[1][3]=PENFRA[1][NP]
									AVPFRAC[2][3]=PENFRA[2][NP]
									AVPFRAC[3][3]=PENFRA[3][NP]
								# endif
								if(J == NIN3):
									CMINEXSC[3]=CMINEXSC[3]*AVPFRAC[1][3]   
					if(EFINAL < E2[4]):
						pass
					else:    
						if(NATT2 > 1):
							# GO TO 561      # This 561 snipet was cut-pasted from below                           
							# 561 
							for JJ in range(1,NATT2+1):
								NP=NP+1
								IDG2=NP
								CF[IE][NP]=QATT2[JJ][IE]*VAN2*BET[IE]
								FCATT[IE]=FCATT[IE]+CF[IE][NP]
								PSCT[IE][NP]=0.5
								ANGCT[IE][NP]=1.0
								if(IE > 1):
									pass
								else:
									NEGAS[NP]=2
									LEGAS[NP]=0
									IESHELL[NP]=0
									INDEX[NP]=0
									RGAS[NP]=RGAS2
									EIN[NP]=0.00
									IPN[NP]=-1
									L=8
									IARRY[NP]=L
									IZBR[NP]=0
									DSCRPT[NP]=SCRP2[2+NION2+JJ]
									PENFRA[1][NP]=0.0
									PENFRA[2][NP]=0.0
									PENFRA[3][NP]=0.0
						else:
							NP=NP+1
							IDG2=NP                                                           
							CF[IE][NP]=Q2[4][IE]*VAN2*BET[IE]
							FCATT[IE]=FCATT[IE]+CF[IE][NP]  
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							if(IE > 1):
								pass
							else:
								NEGAS[NP]=2
								LEGAS[NP]=0
								IESHELL[NP]=0
								INDEX[NP]=0                                  
								RGAS[NP]=RGAS2                                                    
								EIN[NP]=0.00                                                     
								IPN[NP]=-1            
								L=8                                              
								IARRY[NP]=L
								IZBR[NP]=0      
								DSCRPT[NP]=SCRP2[3+NION2]
								PENFRA[1][NP]=0.0  
								PENFRA[2][NP]=0.0
								PENFRA[3][NP]=0.0        
								# GO TO 140  #yet to be 
								pass

					# 140 
					if(NIN2 == 0):
						pass 
					else:     #yet to be                                     
						for J in range(1,NIN2+1):
							NP=NP+1
							IDG2=NP    
							NEGAS[NP]=2
							LEGAS[NP]=0
							IESHELL[NP]=0                                                   
							CF[IE][NP]=QIN2[J][IE]*VAN2*BET[IE]
							# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
							if(IZBR2[J]!= 0 and LBRM == 0):
								CF[IE][NP]=0.0
							PSCT[IE][NP]=0.5
							ANGCT[IE][NP]=1.0
							INDEX[NP]=0
							#
							if(KIN2[J]== 1) :
								PSCT1=PEQIN2[JIE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1
							# endif
							if(KIN2[J]== 2) :
								PSCT[IE][NP]=PEQIN2[J][IE]
								INDEX[NP]=2
							# endif
							#
							if(IE > 1):
								pass                                   
							RGAS[NP]=RGAS2                                                   
							EIN[NP]=EI2[J]/RGAS2
							L=9 
							if(EI2[J]< 0.00):
								L=10                                          
							IPN[NP]=0         
							IARRY[NP]=L
							IZBR[NP]=IZBR2[J]
							DSCRPT[NP]=SCRP2[4+NION2+NATT2+J]
							PENFRA[1][NP]=PENFRA2[1][J]
							PENFRA[2][NP]=PENFRA2[2][J]*1*(10**-6)/math.sqrt(3.00)
							PENFRA[3][NP]=PENFRA2[3][J]
							if(PENFRA[1][NP] > AVPFRAC[1][2]) : 
								AVPFRAC[1][2]=PENFRA[1][NP]
								AVPFRAC[2][2]=PENFRA[2][NP]
								AVPFRAC[3][2]=PENFRA[3][NP]
							# endif
							if(J == NIN2):
								CMINEXSC[2]=CMINEXSC[2]*AVPFRAC[1][2]
						#                                                   
					if(NGAS == 2):
						GOTO600(NP)
					NP=NP+1
					IDG3=NP              
					NEGAS[NP]=3
					LEGAS[NP]=0
					IESHELL[NP]=0                                             
					CF[IE][NP]=Q3[2][IE]*VAN3*BET[IE]
					PSCT[IE][NP]=0.5
					ANGCT[IE][NP]=1.0
					INDEX[NP]=0
					#      
					if(KEL3[2]== 1) :
						PSCT1=PEQEL3[2][IE]
						ANGCUT(PSCT1,ANGC,PSCT2)
						ANGCT[IE][NP]=ANGC
						PSCT[IE][NP]=PSCT2
						INDEX[NP]=1
					# endif 
					if(KEL3[2]== 2) :
						PSCT[IE][NP]=PEQEL3[2][IE]
						INDEX[NP]=2
					# endif
					#
					if(IE > 1):
						pass
					else:                                     
						RGAS3=1.00+E3[2]/2.00                                           
						RGAS[NP]=RGAS3                                                    
						EIN[NP]=0.00                                                     
						IPN[NP]=0  
						L=11                                                        
						IARRY[NP]=L
						IZBR[NP]=0
						DSCRPT[NP]=SCRP3[2]
						NAMEG[3]=NAME3
						PENFRA[1][NP]=0.0 
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0
						AVPFRAC[1][3]=0.0
						AVPFRAC[2][3]=0.0
						AVPFRAC[3][3]=0.0
						CMINEXSC[3]=E3[4]*AN3                                   
						CMINIXSC[3]=E3[5]*AN3 
						ECLOSS[3]=E3[3]
						WPLN[3]=E3[6]
					if(EFINAL < E3[3]):
						GOTO230(NP) 	 #yet to be
					if(NION3 > 1):
						pass
					else:
						NP=NP+1
						IDG3=NP
						# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
						if(ICOUNT == 1):
							CF[IE][NP]=Q3[5][IE]*VAN3*BET[IE]
							FCION[IE]=FCION[IE]+CF[IE][NP]
							DOUBLE[3][IE]=Q3[3][IE]/Q3[5][IE]-1.00
						else:                              
							CF[IE][NP]=Q3[3][IE]*VAN3*BET[IE]
							FCION[IE]=FCION[IE]+CF[IE][NP]
						# endif
						NEGAS[NP]=3
						LEGAS[NP]=0
						IESHELL[NP]=0
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						#
						if(ICOUNT == 1):
							if(KEL3[5]== 1) :
								PSCT1=PEQEL3[5][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1
							# endif
							if(KEL3[5]== 2) :
								PSCT[IE][NP]=PEQEL3[5][IE]
								INDEX[NP]=2
							# endif
						else:
							if(KEL3[3]== 1) :
								PSCT1=PEQEL3[3][IE]
								ANGCUT(PSCT1,ANGC,PSCT2)
								ANGCT[IE][NP]=ANGC
								PSCT[IE][NP]=PSCT2
								INDEX[NP]=1
							# endif
							if(KEL3[3]== 2) :
								PSCT[IE][NP]=PEQEL3[3][IE]
								INDEX[NP]=2
							# endif
						# endif
						# 
						WPL[NP]=EB3[1]
						NC0[NP]=NC03[1]
						EC0[NP]=EC03[1]
						NG1[NP]=NG13[1]
						EG1[NP]=EG13[1]
						NG2[NP]=NG23[1]
						EG2[NP]=EG23[1]
						WKLM[NP]=WK3[1]
						EFL[NP]=EFL3[1]
						if(IE > 1):
							GOTO230(NP)
						RGAS[NP]=RGAS3                                                    
						EIN[NP]=E3[3]/RGAS3 
						IPN[NP]=1
						L=12                                                           
						IARRY[NP]=L
						IZBR[NP]=0
						DSCRPT[NP]=SCRP3[3] 
						PENFRA[1][NP]=0.0  
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0 
						IONMODEL[NP]=IONMODL3
						for K in range(1,20+1):
							ESPLIT[NP][K]=ESPLIT3[IONMODL3][K] 
						GOTO230(NP)
					# 170 
					for KION in range(1,NION3+1):
						NP=NP+1
						IDG3=NP
						# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
						CF[IE][NP]=QION3[KION][IE]*VAN3*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						NEGAS[NP]=3
						LEGAS[NP]=LEGAS3[KION]
						IESHELL[NP]=IESHEL3[KION]
						#
						if(KEL3[3]== 1) :
							PSCT1=PEQION3[3][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KEL3[3]== 2) :
							PSCT[IE][NP]=PEQION3[KION][IE]
							INDEX[NP]=2
						# endif
						# 
						WPL[NP]=EB3[KION]
						NC0[NP]=NC03[KION]
						EC0[NP]=EC03[KION]
						NG1[NP]=NG13[KION]
						EG1[NP]=EG13[KION]
						NG2[NP]=NG23[KION]
						EG2[NP]=EG23[KION]
						WKLM[NP]=WK3[KION]
						EFL[NP]=EFL3[KION]
						if(IE > 1):
							pass
						else:                                            
							RGAS[NP]=RGAS3                                                    
							EIN[NP]=EION3[KION]/RGAS3 
							#
							IPN[NP]=1
							L=12                                                           
							IARRY[NP]=L
							IZBR[NP]=0
							DSCRPT[NP]=SCRP3[2+KION]
							PENFRA[1][NP]=0.0  
							PENFRA[2][NP]=0.0
							PENFRA[3][NP]=0.0    
							IONMODEL[NP]=IONMODL3
							for K in range(1,20+1):
								ESPLIT[NP][K]=ESPLIT3[IONMODL3][K]
					globals().update(locals())
					
					GOTO230(NP)
					#     
					globals().update(locals())             
					
					GOTO260(NP)			
				if(NIN1 == 0):
					pass
				else:                                           
					for J in range(1,NIN1+1):
						NP=NP+1
						IDG1=NP      
						NEGAS[NP]=1
						LEGAS[NP]=0
						IESHELL[NP]=0                                                     
						CF[IE][NP]=QIN1[J][IE]*VAN1*BET[IE]
						# NO X-SECTION FOR BREMSSTRAHLUNG if LBRM=0
						if(IZBR1[J]!= 0 and LBRM == 0):
							CF[IE][NP]=0.0
						PSCT[IE][NP]=0.5
						ANGCT[IE][NP]=1.0
						INDEX[NP]=0
						#
						if(KIN1[J]== 1) :   
							PSCT1=PEQIN1[J][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1   
						# endif
						if(KIN1[J]== 2) :
							PSCT[IE][NP]=PEQIN1[J][IE]
							INDEX[NP]=2
						# endif
						#
						if(IE > 1):
							pass         
						else:                          
							RGAS[NP]=RGAS1                                                    
							EIN[NP]=EI1[J]/RGAS1
							L=4
							if(EI1[J]< 0.00):
								L=5                                           
							IPN[NP]=0  
							IARRY[NP]=L
							IZBR[NP]=IZBR1[J]
							DSCRPT[NP]=SCRP1(4+NION1+NATT1+J)
							PENFRA[1][NP]=PENFRA1[1][J]
							PENFRA[2][NP]=PENFRA1[2][J]*1*(10**-6)/math.sqrt(3.00)
							PENFRA[3][NP]=PENFRA1[3][J]
							if(PENFRA[1][NP] > AVPFRAC[1][1]) : 
								AVPFRAC[1][1]=PENFRA[1][NP]
								AVPFRAC[2][1]=PENFRA[2][NP]
								AVPFRAC[3][1]=PENFRA[3][NP]
							# endif
							if(J == NIN1):
								CMINEXSC[1]=CMINEXSC[1]*AVPFRAC[1][1]
				#                                                    
				if(NGAS == 1):
					GOTO600(NP)
				NP=NP+1
				IDG2=NP  
				NEGAS[NP]=2
				LEGAS[NP]=0
				IESHELL[NP]=0                                                 
				CF[IE][NP]=Q2[2][IE]*VAN2*BET[IE]
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				INDEX[NP]=0
				#
				if(KEL2[2]== 1) :
					PSCT1=PEQEL2[2][IE]
					ANGCUT(PSCT1,ANGC,PSCT2)
					ANGCT[IE][NP]=ANGC
					PSCT[IE][NP]=PSCT2
					INDEX[NP]=1
				# endif
				if(KEL2[2]== 2) :
					PSCT[IE][NP]=PEQEL2[2][IE]
					INDEX[NP]=2 
				# endif 
				#
				if(IE > 1):
					pass  
				else:                                   
					RGAS2=1.00+E2[2]/2.0                                           
					RGAS[NP]=RGAS2                                                    
					EIN[NP]=0.00                                                     
					IPN[NP]=0
					L=6                                                          
					IARRY[NP]=L      
					IZBR[NP]=0
					DSCRPT[NP]=SCRP2[2]  
					NAMEG[2]=NAME2
					PENFRA[1][NP]=0.0 
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0
					AVPFRAC[1][2]=0.0
					AVPFRAC[2][2]=0.0
					AVPFRAC[3][2]=0.0                        
					CMINEXSC[2]=E2[4]*AN2                                        
					CMINIXSC[2]=E2[5]*AN2
					ECLOSS[2]=E2[3]
					WPLN[2]=E2[6]
				if(EFINAL < E2[3]):
					GOTO130(NP)
				if(NION2 > 1):
					pass
				else:                                  
					NP=NP+1
					IDG2=NP
					# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
					if(ICOUNT == 1):
						CF[IE][NP]=Q2[5][IE]*VAN2*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
						DOUBLE[2][IE]=Q2[3][IE]/Q2[5][IE]-1.00
					else:                             
						CF[IE][NP]=Q2[3][IE]*VAN2*BET[IE]
						FCION[IE]=FCION[IE]+CF[IE][NP]
					# endif
					NEGAS[NP]=2
					LEGAS[NP]=0
					IESHELL[NP]=0
					PSCT[IE][NP]=0.5
					ANGCT[IE][NP]=1.0
					INDEX[NP]=0
					#
					if(ICOUNT == 1):
						if(KEL2[5]== 1) :
							PSCT1=PEQEL2[5][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KEL2[5]== 2) :
							PSCT[IE][NP]=PEQEL2[5][IE]
							INDEX[NP]=2
						# endif
					else:
						if(KEL2[3]== 1) :
							PSCT1=PEQEL2[3][IE]
							ANGCUT(PSCT1,ANGC,PSCT2)
							ANGCT[IE][NP]=ANGC
							PSCT[IE][NP]=PSCT2
							INDEX[NP]=1
						# endif
						if(KEL2[3]== 2) :
							PSCT[IE][NP]=PEQEL2[3][IE]
							INDEX[NP]=2
						# endif
					# endif
					#
					WPL[NP]=EB2[1]
					NC0[NP]=NC02[1]
					EC0[NP]=EC02[1]
					NG1[NP]=NG12[1]
					EG1[NP]=EG12[1]
					NG2[NP]=NG22[1]
					EG2[NP]=EG22[1]
					WKLM[NP]=WK2[1]
					EFL[NP]=EFL2[1]
					if(IE > 1):
						GOTO130(NP)
					RGAS[NP]=RGAS2                                                    
					EIN[NP]=E2[3]/RGAS2 
					IPN[NP]=1  
					L=7                                                        
					IARRY[NP]=L
					IZBR[NP]=0      
					DSCRPT[NP]=SCRP2[3]     
					PENFRA[1][NP]=0.0 
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0  
					IONMODEL[NP]=IONMODL2
					for K in range(1,20+1):
						ESPLIT[NP][K]=ESPLIT2[IONMODL2][K] 
					GOTO130(NP)
				#70
				for KION in range(1,NION2+1):
					NP=NP+1
					IDG2=NP
					CF[IE][NP]=QION2[KION][IE]*VAN2*BET[IE]
					FCION[IE]=FCION[IE]+CF[IE][NP]
					PSCT[IE][NP]=0.5
					ANGCT[IE][NP]=1.0
					INDEX[NP]=0
					NEGAS[NP]=2
					LEGAS[NP]=LEGAS2[KION]
					IESHELL[NP]=IESHEL2[KION]
					#
					if(KEL2[3]== 1) :
						PSCT1=PEQION2[KION][IE]
						ANGCUT(PSCT1,ANGC,PSCT2)
						ANGCT[IE][NP]=ANGC
						PSCT[IE][NP]=PSCT2
						INDEX[NP]=1
					# endif
					if(KEL2[3]== 2) :
						PSCT[IE][NP]=PEQION2[KION][IE]
						INDEX[NP]=2
					# endif
					#
					WPL[NP]=EB2[KION]
					NC0[NP]=NC02[KION]
					EC0[NP]=EC02[KION]
					NG1[NP]=NG12[KION]
					EG1[NP]=EG12[KION]
					NG2[NP]=NG22[KION]
					EG2[NP]=EG22[KION]
					WKLM[NP]=WK2[KION]
					EFL[NP]=EFL2[KION]
					if(IE > 1):
						pass
					else:
						RGAS[NP]=RGAS2                                                    
						EIN[NP]=EION2[KION]/RGAS2 
						#
						IPN[NP]=1  
						L=7                                                        
						IARRY[NP]=L
						IZBR[NP]=0      
						DSCRPT[NP]=SCRP2[2+KION]
						PENFRA[1][NP]=0.0 
						PENFRA[2][NP]=0.0
						PENFRA[3][NP]=0.0       
						IONMODEL[NP]=IONMODL2
						for K in range(1,20+1):
							ESPLIT[NP][K]=ESPLIT2[IONMODL2][K]                                  
				globals().update(locals())
				GOTO130(NP)
			if(EFINAL < E1[4]):
				GOTO40(NP)
			if(NATT1 > 1):
				pass   
			else:                               
				NP=NP+1
				IDG1=NP                                                           
				CF[IE][NP]=Q1[4][IE]*VAN1*BET[IE]
				FCATT[IE]=FCATT[IE]+CF[IE][NP] 
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				if(IE > 1):
					GOTO40(NP)
				NEGAS[NP]=1
				LEGAS[NP]=0
				IESHELL[NP]=0
				INDEX[NP]=0                                     
				RGAS[NP]=RGAS1                                                   
				EIN[NP]=0.00                                                     
				IPN[NP]=-1              
				L=3                                           
				IARRY[NP]=L
				IZBR[NP]=0
				DSCRPT[NP]=SCRP1[3+NION1]
				PENFRA[1][NP]=0.0
				PENFRA[2][NP]=0.0
				PENFRA[3][NP]=0.0 
				GOTO40(NP)
			for JJ in range(1,NATT1+1):
				NP=NP+1
				IDG1=NP
				CF[IE][NP]=QATT1[JJ][IE]*VAN1*BET[IE]
				FCATT[IE]=FCATT[IE]+CF[IE][NP]
				PSCT[IE][NP]=0.5
				ANGCT[IE][NP]=1.0
				if(IE > 1):
					pass
				else:
					NEGAS[NP]=1
					LEGAS[NP]=0
					IESHELL[NP]=0
					INDEX[NP]=0
					RGAS[NP]=RGAS1
					EIN[NP]=0.00
					IPN[NP]=-1
					L=3
					IARRY[NP]=L
					IZBR[NP]=0
					DSCRPT[NP]=SCRP1(2+NION1+JJ)
					PENFRA[1][NP]=0.0
					PENFRA[2][NP]=0.0
					PENFRA[3][NP]=0.0
			GOTO40(NP)
			#     WRITE(6,841) (INDEX[J],J, J=1,IPLAST)
			# 841 print(2X,' INDEX=',I3,' J=',I3)                   
			#  SET ANISOTROPIC FLAG if ANISOTROPIC SCATTERING DATA IS DETECTED
			KELSUM=0 #2479
			#########                  RESET INDENTATION                ###########################
			for J in range(1,6+1):
				KELSUM=KELSUM+KEL1[J]+KEL2[J]+KEL3[J]+KEL4[J]+KEL5[J]+KEL6[J]
			for J in range(1,250+1):
				KELSUM=KELSUM+KIN1[J]+KIN2[J]+KIN3[J]+KIN4[J]+KIN5[J]+KIN6[J]
			if(KELSUM > 0):
				NISO=1  
			#     if(NISO == 1) WRITE(6,7765) NISO
			#7765 print(3X,' ANISOTROPIC SCATTERING DETECTED NISO=',I5)         
			# -------------------------------------------------------------------   
			#   CALCULATE NULL COLLISION FREQUENCY                                  
			# -------------------------------------------------------------------   
			BP=EFIELD*EFIELD*CONST1           #2490                               
			F2=EFIELD*CONST3                                                  
			ELOW=TMAX*(TMAX*BP-F2*math.sqrt(0.50*EFINAL))/ESTEP-1.00            
			ELOW=min(ELOW,SMALL)
			EHI=TMAX*(TMAX*BP+F2*math.sqrt(0.50*EFINAL))/ESTEP+1.00
			if(EHI > 20000.0):
				EHI=20000.0
			JONE=1
			JLARGE=20000  
			for I in range(1,10+1):
					JLOW=20000-2000*(11-I)+1+int(ELOW)                               
					JHI=20000-2000*(10-I)+int(EHI)
					JLOW=max(JLOW,JONE)
					JHI=min(JHI,JLARGE)
			for J in range(JLOW,JHI+1):
				if(TCF[J]>= TCFMAX[I]):
					TCFMAX[I]=TCF[J]                          
			#---------------------------------------------------------------------
			# FIND MAXIMUM COLLISION FREQUENCY
			#     TLIM=TCFMAX[1]
			#     DO 835 I=1,10
			# 835 if(TLIM < TCFMAX[I]) TLIM=TCFMAX[I]
			#     TCFMAX1=TLIM  
			TLIM=0.0
			for I in range(1,20000+1):	
				if(TLIM < TCF[I]):
					print(TLIM,TCF[I])
					# time.sleep(1)
					TLIM=TCF[I]
			TCFMAX1=TLIM  
			print("Mixer 3281 TCFMAX1=", TCFMAX1)                                                  
			# -------------------------------------------------------------------   
			#   CROSS SECTION DATA FOR INTEGRALS IN  OUTPUT               
			# --------------------------------------------------------------------- 
			for I in range(1,NSTEP+1):      #900                                         
				QTOT[I]=AN1*Q1[1][I]+AN2*Q2[1][I]+AN3*Q3[1][I]+AN4*Q4[1][I]+AN5*Q5[1][I]+AN6*Q6[1][I]     
				QEL[I]=AN1*Q1[2][I]+AN2*Q2[2][I]+AN3*Q3[2][I]+AN4*Q4[2][I]+AN5*Q5[2][I]+AN6*Q6[2][I]             
			#                                                                       
			QION[1][I]=Q1[3][I]*AN1   
			if(NION1 > 1):
				for KION in range(1,NION1+1):
					#811
					QION[1][I]=QION1[KION][I]*AN1
			# endif                                           
			QION[2][I]=Q2[3][I]*AN2                                             
			if(NION2 > 1):
				for KION in range(1,NION2+1):
				    #812
					QION[2][I]=QION2[KION][I]*AN2
			# endif                                           
			QION[3][I]=Q3[3][I]*AN3                                             
			if(NION3 > 1):
				for KION in range(1,NION3+1):
					QION[3][I]=QION3[KION][I]*AN3
			# endif                                           
			QION[4][I]=Q4[3][I]*AN4
			if(NION4 > 1):
				for KION in range(1,NION4+1):
					QION[4][I]=QION4[KION][I]*AN4
			# endif                                           
			QION[5][I]=Q5[3][I]*AN5
			if(NION5 > 1):
				for KION in range(1,NION5+1):
					QION[5][I]=QION5[KION][I]*AN5
			# endif                                           
			QION[6][I]=Q6[3][I]*AN6                                             
			if(NION6 > 1):
				for KION in range(1,NION6+1):
					QION[6][I]=QION6[KION][I]*AN6
			# endif                                           
			QATT[1][I]=Q1[4][I]*AN1                                             
			QATT[2][I]=Q2[4][I]*AN2                                             
			QATT[3][I]=Q3[4][I]*AN3                                             
			QATT[4][I]=Q4[4][I]*AN4
			QATT[5][I]=Q5[4][I]*AN5
			QATT[6][I]=Q6[4][I]*AN6                                             
			#                                                                       
			QREL[I]=0.00                                                     
			QSATT[I]=0.00                                                   
			QSUM[I]=0.00                                                     
			for J in range(1,NGAS+1):
				QSUM[I]=QSUM[I]+QION[J][I]+QATT[J][I]                               
				QSATT[I]=QSATT[I]+QATT[J][I]                                       
				QREL[I]=QREL[I]+QION[J][I]-QATT[J][I]                               
			#                                                                       
			if(NIN1 == 0):
				pass
			else:
				for J in range(1,NIN1+1):
					QSUM[I]=QSUM[I]+QIN1[J][I]*AN1                                     
			if(NIN2 == 0):
				pass                                           
			else:
				for J in range(1,NIN2+1):
					QSUM[I]=QSUM[I]+QIN2[J][I]*AN2                                     
			if(NIN3 == 0):
				pass                                           
			else:
				for J in range(1,NIN3+1):
					QSUM[I]=QSUM[I]+QIN3[J][I]*AN3                                     
			if(NIN4 == 0):
				pass                                           
			else:
				for J in range(1,NIN4+1):
					QSUM[I]=QSUM[I]+QIN4[J][I]*AN4                                     
			if(NIN5 == 0):
				pass 
			else:
				for J in range(1,NIN5+1):
						QSUM[I]=QSUM[I]+QIN5[J][I]*AN5
			if(NIN6 == 0):
				pass
			else:
				for J in range(1,NIN6+1):
					QSUM[I]=QSUM[I]+QIN6[J][I]*AN6                                     
			##
			globals().update(locals())
			##
			                                                                     
			return                                                            
	for IE in range(1,20000+1):
		FCION[IE]=0.00
		FCATT[IE]=0.00
		#
		NP=1 
		IDG1=1
		NEGAS[NP]=1  
		LEGAS[NP]=0
		IESHELL[NP]=0                                               
		CF[IE][NP]=Q1[2][IE]*VAN1*BET[IE]
		PSCT[IE][NP]=0.50
		ANGCT[IE][NP]=1.00    
		INDEX[NP]=0 
		#   ELASTIC ANG  
		if(KEL1[2]== 1):
			PSCT1=PEQEL1[2][IE]
			ANGCUT(PSCT1,ANGC,PSCT2)
			ANGCT[IE][NP]=ANGC
			PSCT[IE][NP]=PSCT2  
			INDEX[NP]=1   
		# endif 
		if(KEL1[2]== 2):
			PSCT[IE][NP]=PEQEL1[2][IE]
			INDEX[NP]=2
		# endif
		#
		if(IE > 1):
			pass
		else:                              
			RGAS1=1.00+E1[2]/2.00                                           
			RGAS[NP]=RGAS1                                                    
			EIN[NP]=0.00                                                     
			IPN[NP]=0 
			L=1                                                      
			IARRY[NP]=L 
			IZBR[NP]=0
			# print("Mixer 755 ",DSCRPT[NP],type(DSCRPT[NP]),SCRP1[2],type(SCRP1[2]))
			DSCRPT[NP]=SCRP1[2]  
			# print("linr 757 NAME1=",NAME1," NAMEG[1]=",NAMEG[1])
			NAMEG[1]=NAME1
			PENFRA[1][NP]=0.0
			PENFRA[2][NP]=0.0
			PENFRA[3][NP]=0.0
			AVPFRAC[1][1]=0.0
			AVPFRAC[2][1]=0.0
			AVPFRAC[3][1]=0.0
			CMINEXSC[1]=E1[4]*AN1                                        
			CMINIXSC[1]=E1[5]*AN1
			ECLOSS[1]=E1[3]
			WPLN[1]=E1[6]
		if(EFINAL < E1[3]):
			GOTO30(NP)  
		if(NION1 > 1):
			pass  
		else:
			NP=NP+1
			IDG1=NP
			# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
			if(ICOUNT == 1):
				CF[IE][NP]=Q1[5][IE]*VAN1*BET[IE]
				FCION[IE]=FCION[IE]+CF[IE][NP]
				DOUBLE[1][IE]=Q1[3][IE]/Q1[5][IE]-1.00
			else:                                    
				CF[IE][NP]=Q1[3][IE]*VAN1*BET[IE]
				FCION[IE]=FCION[IE]+CF[IE][NP]
			# endif
			NEGAS[NP]=1 
			LEGAS[NP]=0
			IESHELL[NP]=0
			PSCT[IE][NP]=0.5
			ANGCT[IE][NP]=1.0
			INDEX[NP]=0
			# 
			if(ICOUNT == 1):
				if(KEL1[5]== 1) :
					PSCT1=PEQEL1[5][IE] 
					ANGCUT(PSCT1,ANGC,PSCT2)
					ANGCT[IE][NP]=ANGC
					PSCT[IE][NP]=PSCT2
					INDEX[NP]=1
				# endif
				if(KEL1[5]== 2) :
					PSCT[IE][NP]=PEQEL1[5][IE]
					INDEX[NP]=2
				# endif
			else:
				if(KEL1[3]== 1) :
					PSCT1=PEQEL1[3][IE]
					ANGCUT(PSCT1,ANGC,PSCT2)
					ANGCT[IE][NP]=ANGC
					PSCT[IE][NP]=PSCT2
					INDEX[NP]=1
				# endif
				if(KEL1[3]== 2) :
					PSCT[IE][NP]=PEQEL1[3][IE]
					INDEX[NP]=2
				# endif
			# endif
			#
			WPL[NP]=EB1[1]
			NC0[NP]=NC01[1]
			EC0[NP]=EC01[1]
			NG1[NP]=NG11[1]
			EG1[NP]=EG11[1]
			NG2[NP]=NG21[1]
			EG2[NP]=EG21[1]
			WKLM[NP]=WK1[1]
			EFL[NP]=EFL1[1]
			if(IE > 1):
				GOTO30(NP)  
			RGAS[NP]=RGAS1                                                    
			EIN[NP]=E1[3]/RGAS1
			IPN[NP]=1 
			L=2                                                      
			IARRY[NP]=L 
			IZBR[NP]=0
			DSCRPT[NP]=SCRP1[3]
			PENFRA[1][NP]=0.0
			PENFRA[2][NP]=0.0
			PENFRA[3][NP]=0.0
			IONMODEL[NP]=IONMODL1
			for K in range(1,20+1):
				ESPLIT[NP][K]=ESPLIT1[IONMODL1][K]
			GOTO30(NP)  
		for KION in range(1,NION1+1):
			NP=NP+1
			IDG1=NP
			# CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
			CF[IE][NP]=QION1[KION][IE]*VAN1*BET[IE]
			FCION[IE]=FCION[IE]+CF[IE][NP]
			PSCT[IE][NP]=0.50
			ANGCT[IE][NP]=1.00
			INDEX[NP]=0 
			NEGAS[NP]=1
			LEGAS[NP]=LEGAS1[KION]
			IESHELL[NP]=IESHEL1[KION]
			#                           
			if(KEL1[3]== 1) :
				PSCT1=PEQION1[KION][IE]
				ANGCUT(PSCT1,ANGC,PSCT2)
				ANGCT[IE][NP]=ANGC
				PSCT[IE][NP]=PSCT2
				INDEX[NP]=1
			# endif
			if(KEL1[3]== 2) :
				PSCT[IE][NP]=PEQION1[KION][IE]
				INDEX[NP]=2
			# endif
			#
			WPL[NP]=EB1[KION]
			NC0[NP]=NC01[KION]
			EC0[NP]=EC01[KION]
			NG1[NP]=NG11[KION]
			EG1[NP]=EG11[KION]
			NG2[NP]=NG21[KION]
			EG2[NP]=EG21[KION]
			WKLM[NP]=WK1[KION]
			EFL[NP]=EFL1[KION]
			if(IE > 1):
				pass                                    
			else:
				RGAS[NP]=RGAS1                                                    
				EIN[NP]=EION1[KION]/RGAS1
				# 
				IPN[NP]=1 
				L=2                                                      
				IARRY[NP]=L 
				IZBR[NP]=0
				DSCRPT[NP]=SCRP1[2+KION]
				PENFRA[1][NP]=0.0
				PENFRA[2][NP]=0.0
				PENFRA[3][NP]=0.0
				IONMODEL[NP]=IONMODL1
				for K in range(1,20+1):
					ESPLIT[NP][K]=ESPLIT1[IONMODL1][K]    
			globals().update(locals())
		GOTO30(NP)
		conf.AN1=AN1
		conf.AN2=AN2
		conf.AN3=AN3
		conf.AN4=AN4
		conf.AN5=AN5
		conf.AN6=AN6
		conf.FRAC=FRAC
		conf.NGASN=NGASN
		conf.QELM=QELM
		conf.QSUM=QSUM
		conf.QION=QION
		conf.QIN1=QIN1
		conf.QIN2=QIN2
		conf.QIN3=QIN3
		conf.QIN4=QIN4
		conf.QIN5=QIN5
		conf.QIN6=QIN6
		conf.QSATT=QSATT
		conf.E=E
		conf.EROOT=EROOT
		conf.QTOT=QTOT
		conf.QREL=QREL
		conf.QINEL=QINEL
		conf.QEL=QEL
		conf.NIN1=NIN1
		conf.NIN2=NIN2
		conf.NIN3=NIN3
		conf.NIN4=NIN4
		conf.NIN5=NIN5
		conf.NIN6=NIN6
		conf.LION=LION
		conf.LIN1=LIN1
		conf.LIN2=LIN2
		conf.LIN3=LIN3
		conf.LIN4=LIN4
		conf.LIN5=LIN5
		conf.LIN6=LIN6
		conf.ALION=ALION
		conf.ALIN1=ALIN1
		conf.ALIN2=ALIN2
		conf.ALIN3=ALIN3
		conf.ALIN4=ALIN4
		conf.ALIN5=ALIN5
		conf.ALIN6=ALIN6
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
		conf.CONST1=CONST1	
		conf.CONST2=CONST2	
		conf.CONST3=CONST3	
		conf.CONST4=CONST4	
		conf.CONST5=CONST5                  
		conf.TMAX=TMAX
		conf.SMALL=SMALL
		conf.API=API
		conf.ESTART=ESTART
		conf.THETA=THETA
		conf.PHI=PHI
		conf.TCFMAX=TCFMAX
		conf.TCFMAX1=TCFMAX1
		conf.RSTART=RSTART
		conf.EFIELD=EFIELD
		conf.ETHRM=ETHRM
		conf.ECUT=ECUT
		conf.NDELTA=NDELTA
		conf.IMIP=IMIP
		conf.IWRITE=IWRITE
		conf.NPLAST=NPLAST
		conf.CF=CF
		conf.EIN=EIN
		conf.TCF=TCF
		conf.IARRY=IARRY
		conf.RGAS=RGAS
		conf.IPN=IPN
		conf.WPL=WPL
		conf.IZBR=IZBR
		conf.IPLAST=IPLAST
		conf.PENFRA=PENFRA
		conf.CFN=CFN
		conf.TCFN=TCFN
		conf.SCLENUL=SCLENUL
		conf.PSCT=PSCT
		conf.ANGCT=ANGCT
		conf.INDEX=INDEX
		conf.NISO=NISO
		conf.FCION=FCION
		conf.FCATT=FCATT
		conf.NEGAS=NEGAS
		conf.LEGAS=LEGAS
		conf.IESHELL=IESHELL
		conf.VAN1=VAN1
		conf.VAN2=VAN2
		conf.VAN3=VAN3
		conf.VAN4=VAN4
		conf.VAN5=VAN5
		conf.VAN6=VAN6
		conf.VAN=VAN
		conf.IECASC=IECASC
		conf.DOUBLE=DOUBLE
		conf.CMINIXSC=CMINIXSC
		conf.CMINEXSC=CMINEXSC
		conf.ECLOSS=ECLOSS
		conf.WPLN=WPLN
		conf.ICOUNT=ICOUNT
		conf.AVPFRAC=AVPFRAC
		conf.NC0=NC0
		conf.EC0=EC0
		conf.NG1=NG1
		conf.EG1=EG1
		conf.NG2=NG2
		conf.EG2=EG2
		conf.WKLM=WKLM
		conf.EFL=EFL
		conf.LCMP=LCMP
		conf.LCFLG=LCFLG
		conf.LRAY=LRAY
		conf.LRFLG=LRFLG
		conf.LPAP=LPAP
		conf.LPFLG=LPFLG
		conf.LBRM=LBRM
		conf.LBFLG=LBFLG
		conf.LPEFLG=LPEFLG
		conf.NAMEG=NAMEG
		conf.NGEXC1=NGEXC1
		conf.NGEXC2=NGEXC2
		conf.NGEXC3=NGEXC3
		conf.NGEXC4=NGEXC4
		conf.NGEXC5=NGEXC5
		conf.NGEXC6=NGEXC6
		conf.IDG1=IDG1
		conf.IDG2=IDG2
		conf.IDG3=IDG3
		conf.IDG4=IDG4
		conf.IDG5=IDG5
		conf.IDG6=IDG6      
		conf.DSCRPT=DSCRPT
		conf.DSCRPTN=DSCRPTN
		conf.ESPLIT=ESPLIT
		conf.IONMODEL=IONMODEL
		conf.BET=BET
		conf.GAM=GAM
		conf.VC=VC
		conf.EMS=EMS
		return 
		# end 
