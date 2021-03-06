import numpy
from Gasn import *
def GASMIX(NGS,Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN):
	#IMPLICIT #real*8 (A-H,O-Z) 
	# CHARACTER*25 
	NAME=numpy.zeros(25+1,dtype=str)
	# CHARACTER*50 
	SCRPT=numpy.zeros(300+1,dtype=str)
	SCRPTN=numpy.zeros(10+1,dtype=str)                       
	E=numpy.zeros((6+1))
	EI=numpy.zeros((250+1))
	KIN=numpy.zeros((250+1))
	Q=numpy.zeros((6+1,20000+1))
	QIN=numpy.zeros((250+1,20000+1))
	EION=numpy.zeros((30+1))
	EB=numpy.zeros((30+1))   
	QION=numpy.zeros((30+1,20000+1))      
	PEQION=numpy.zeros((30+1,20000+1))
	PEQEL=numpy.zeros((6+1,20000+1))
	PEQIN=numpy.zeros((250+1,20000+1))
	KEL=numpy.zeros((6+1))
	PENFRA=numpy.zeros((3+1,250+1))
	NC0=numpy.zeros((30+1))
	EC0=numpy.zeros((30+1))
	WK=numpy.zeros((30+1))
	EFL=numpy.zeros((30+1))
	NG1=numpy.zeros((30+1))
	EG1=numpy.zeros((30+1))
	NG2=numpy.zeros((30+1))
	EG2=numpy.zeros((30+1))
	IZBR=numpy.zeros((250+1))
	LEGAS=numpy.zeros((30+1))
	IESHELL=numpy.zeros((30+1))
	QATT=numpy.zeros((8+1,20000+1))
	QNULL=numpy.zeros((10+1,20000+1))
	SCLN=numpy.zeros((10+1))
	ESPLIT=numpy.zeros((5+1,20+1))
	# 
	#GO TO (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80) NGS

	if(NGS==1):
		NATT=GAS1(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		print(type(NATT))
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT
	if(NGS==2):
		Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT=GAS2(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		# print(GAS2(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN))
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT
	if(NGS==3):
		GAS3(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return  Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if(NGS==4):
		GAS4(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT   
	if (NGS==5):
		GAS5(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==6):
		GAS6(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==7):
		GAS7(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==8):
		GAS8(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==9):
		GAS9(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==10):
		GAS10(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==11):
		GAS11(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT  
	if (NGS==12):
		Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT=GAS12(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		# print(GAS12(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN))
		# print("GASMIX gas12 natt type=",type(NATT))
		return Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT
	if (NGS==13):
		GAS13(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==14):
		GAS14(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==15):
		GAS15(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==16):
		GAS16(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==17):
		GAS17(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==18):
		GAS18(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==19):
		GAS19(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==20):
		GAS20(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==21):
		GAS21(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==22):
		GAS22(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==23):
		GAS23(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==24):
		GAS24(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==25):
		GAS25(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==26):
		GAS26(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==27):
		GAS27(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==28):
		GAS28(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==29):
		GAS29(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KQION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==30):
		GAS30(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==31):
		GAS31(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==32):
		GAS32(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==33):
		GAS33(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==34):
		GAS34(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==35):
		GAS35(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==36):
		GAS36(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==37):
		GAS37(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==38):
		GAS38(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==39):
		GAS39(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==40):
		GAS40(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==41):
		GAS41(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==42):
		GAS42(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==43):
		GAS43(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==44):
		GAS44(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==45):
		GAS45(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==46):
		GAS46(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==47):
		GAS47(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==48):
		GAS48(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==49):
		GAS49(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==50):
		GAS50(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==51):
		GAS51(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==52):
		GAS52(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==53):
		GAS53(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==54):
		GAS54(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==55):
		GAS55(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==56):
		GAS56(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==57):
		GAS57(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==58):
		GAS58(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==59):
		GAS59(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==60):
		GAS60(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==61):
		GAS61(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==62):
		GAS62(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==63):
		GAS63(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==64):
		GAS64(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==65):
		GAS65(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==66):
		GAS66(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==67):
		GAS67(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==68):
		GAS68(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==69):
		GAS69(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==70):
		GAS70(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==71):
		GAS71(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==72):
		GAS72(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==73):
		GAS73(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==74):
		GAS74(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==75):
		GAS75(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==76):
		GAS76(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==77):
		GAS77(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==78):
		GAS78(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==79):
		GAS79(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
	if (NGS==80):
		GAS80(Q,QIN,NIN,E,EI,NAME,VIRL,EB,PEQEL,PEQIN,PENFRA,KEL,KIN,QION,PEQION,EION,NION,QATT,NATT,QNULL,NNULL,SCLN,NC0,EC0,WK,EFL,NG1,EG1,NG2,EG2,IZBR,LEGAS,IESHELL,IONMODEL,ESPLIT,SCRPT,SCRPTN)
		return   
      # end 