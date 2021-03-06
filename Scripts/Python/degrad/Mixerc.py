import numpy
from Gasmixc import *
import conf
def MIXERC():
	# IMPLICIT #real*8 (A-H,O-Z) 
	# IMPLICIT #integer*8 (I-N)
	# COMMON/INPT/
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	#COMMON/MIXC/
	# global conf.PRSH,conf.ESH,conf.AUG,conf.RAD,conf.PRSHBT,conf.IZ,conf.INIOCC,conf.ISHLMX,conf.AMZ 
	#COMMON/MIXPE/
	# global conf.XPE,conf.YPE
	#COMMON/MIXCN/
	# global conf.XCP,conf.YRY,conf.YCP,conf.YPP
	#COMMON/COMPTIN/
	# global conf.FRMFR,conf.FRMFC
	#COMMON/GASN/
	global NGASN
	PRSH1=numpy.zeros((3+1,17+1,17+1))
	PRSH2=numpy.zeros((3+1,17+1,17+1))
	PRSH3=numpy.zeros((3+1,17+1,17+1))
	PRSH4=numpy.zeros((3+1,17+1,17+1))
	PRSH5=numpy.zeros((3+1,17+1,17+1))
	PRSH6=numpy.zeros((3+1,17+1,17+1))
	PRSHBT1=numpy.zeros((3+1,17+1))
	PRSHBT2=numpy.zeros((3+1,17+1))
	PRSHBT3=numpy.zeros((3+1,17+1))
	PRSHBT4=numpy.zeros((3+1,17+1))
	PRSHBT5=numpy.zeros((3+1,17+1))
	PRSHBT6=numpy.zeros((3+1,17+1))
	ESH1=numpy.zeros((3+1,17+1))
	ESH2=numpy.zeros((3+1,17+1))
	ESH3=numpy.zeros((3+1,17+1))
	ESH4=numpy.zeros((3+1,17+1))
	ESH5=numpy.zeros((3+1,17+1))
	ESH6=numpy.zeros((3+1,17+1))
	AUG1=numpy.zeros((3+1,17+1,17+1,17+1))
	AUG2=numpy.zeros((3+1,17+1,17+1,17+1))
	AUG3=numpy.zeros((3+1,17+1,17+1,17+1))
	AUG4=numpy.zeros((3+1,17+1,17+1,17+1))
	AUG5=numpy.zeros((3+1,17+1,17+1,17+1))
	AUG6=numpy.zeros((3+1,17+1,17+1,17+1))
	RAD1=numpy.zeros((3+1,17+1,17+1))
	RAD2=numpy.zeros((3+1,17+1,17+1))
	RAD3=numpy.zeros((3+1,17+1,17+1))
	RAD4=numpy.zeros((3+1,17+1,17+1))
	RAD5=numpy.zeros((3+1,17+1,17+1))
	RAD6=numpy.zeros((3+1,17+1,17+1))
	INIOCC1=numpy.zeros((3+1,17+1))
	INIOCC2=numpy.zeros((3+1,17+1))
	INIOCC3=numpy.zeros((3+1,17+1))
	INIOCC4=numpy.zeros((3+1,17+1))
	INIOCC5=numpy.zeros((3+1,17+1))
	INIOCC6=numpy.zeros((3+1,17+1))
	XP1=numpy.zeros((3+1,17+1,60+1))
	YP1=numpy.zeros((3+1,17+1,60+1))
	XP2=numpy.zeros((3+1,17+1,60+1))
	YP2=numpy.zeros((3+1,17+1,60+1))
	XP3=numpy.zeros((3+1,17+1,60+1))
	YP3=numpy.zeros((3+1,17+1,60+1))
	XP4=numpy.zeros((3+1,17+1,60+1))
	YP4=numpy.zeros((3+1,17+1,60+1))
	XP5=numpy.zeros((3+1,17+1,60+1))
	YP5=numpy.zeros((3+1,17+1,60+1))
	XP6=numpy.zeros((3+1,17+1,60+1))
	YP6=numpy.zeros((3+1,17+1,60+1))
	XC1=numpy.zeros((3+1,54+1))
	YR1=numpy.zeros((3+1,54+1))
	YC1=numpy.zeros((3+1,54+1))
	YPP1=numpy.zeros((3+1,54+1))
	XC2=numpy.zeros((3+1,54+1))
	YR2=numpy.zeros((3+1,54+1))
	YC2=numpy.zeros((3+1,54+1))
	YPP2=numpy.zeros((3+1,54+1))
	XC3=numpy.zeros((3+1,54+1))
	YR3=numpy.zeros((3+1,54+1))
	YC3=numpy.zeros((3+1,54+1))
	YPP3=numpy.zeros((3+1,54+1))
	XC4=numpy.zeros((3+1,54+1))
	YR4=numpy.zeros((3+1,54+1))
	YC4=numpy.zeros((3+1,54+1))
	YPP4=numpy.zeros((3+1,54+1))
	XC5=numpy.zeros((3+1,54+1))
	YR5=numpy.zeros((3+1,54+1))
	YC5=numpy.zeros((3+1,54+1))
	YPP5=numpy.zeros((3+1,54+1))
	XC6=numpy.zeros((3+1,54+1))
	YR6=numpy.zeros((3+1,54+1))
	YC6=numpy.zeros((3+1,54+1))
	YPP6=numpy.zeros((3+1,54+1))
	FFAC1=numpy.zeros((3+1,45+1))
	FFAC2=numpy.zeros((3+1,45+1))
	FFAC3=numpy.zeros((3+1,45+1))
	FFAC4=numpy.zeros((3+1,45+1))
	FFAC5=numpy.zeros((3+1,45+1))
	FFAC6=numpy.zeros((3+1,45+1))
	FFAR1=numpy.zeros((3+1,45+1))
	FFAR2=numpy.zeros((3+1,45+1))
	FFAR3=numpy.zeros((3+1,45+1))
	FFAR4=numpy.zeros((3+1,45+1))
	FFAR5=numpy.zeros((3+1,45+1))
	FFAR6=numpy.zeros((3+1,45+1))
	IZ1=numpy.zeros((3+1))
	IZ2=numpy.zeros((3+1))
	IZ3=numpy.zeros((3+1))
	IZ4=numpy.zeros((3+1))
	IZ5=numpy.zeros((3+1))
	IZ6=numpy.zeros((3+1))
	AMZ1=numpy.zeros((3+1))
	AMZ2=numpy.zeros((3+1))
	AMZ3=numpy.zeros((3+1))
	AMZ4=numpy.zeros((3+1))
	AMZ5=numpy.zeros((3+1))
	AMZ6=numpy.zeros((3+1))

	# LOAD PHOTOELECTRIC AND COMPTON X-SECS
	# LOAD INITIAL SHELL OCCUPANCIES FOR EACH GAS
	# LOAD ENERGY LEVELS
	# LOAD TRANSITION PROBABILITIES AUGER AND RADIATIVE
	# LOAD SHAKE OFF PROBABILITIES AND ENERGIES
	for I in range(1,6+1):
		for M in range(1,3+1):
			conf.IZ[I][M]=0
			conf.AMZ[I][M]=0.00
			for J in range(1,17+1):
				conf.ESH[I][M][J]=0.0
				conf.INIOCC[I][M][J]=0
				conf.PRSHBT[I][M][J]=0.0
				for K in range(1,17+1):
					conf.PRSH[I][M][J][K]=0.0
					conf.RAD[I][M][J][K]=0.0
					for L in range(1,17+1):
						conf.AUG[I][M][J][K][L]=0.0
	PRSH1,PRSHBT1,ESH1,AUG1,RAD1,XP1,YP1,XC1,YR1,YC1,YPP1,FFAR1,FFAC1,IZ1,AMZ1,INIOCC1=GASMIXC(conf.NGASN[1],PRSH1,PRSHBT1,ESH1,AUG1,RAD1,XP1,YP1,XC1,YR1,YC1,YPP1,FFAR1,FFAC1,IZ1,AMZ1,INIOCC1)
	if(conf.NGAS == 1):
		pass
	else:
		PRSH2,PRSHBT2,ESH2,AUG2,RAD2,XP2,YP2,XC2,YR2,YC2,YPP2,FFAR2,FFAC2,IZ2,AMZ2,INIOCC2=GASMIXC(conf.NGASN[2],PRSH2,PRSHBT2,ESH2,AUG2,RAD2,XP2,YP2,XC2,YR2,YC2,YPP2,FFAR2,FFAC2,IZ2,AMZ2,INIOCC2)
		if(conf.NGAS == 2):
			pass
		else:
			PRSH3,PRSHBT3,ESH3,AUG3,RAD3,XP3,YP3,XC3,YR3,YC3,YPP3,FFAR3,FFAC3,IZ3,AMZ3,INIOCC3=GASMIXC(conf.NGASN[3],PRSH3,PRSHBT3,ESH3,AUG3,RAD3,XP3,YP3,XC3,YR3,YC3,YPP3,FFAR3,FFAC3,IZ3,AMZ3,INIOCC3)
			if(conf.NGAS == 3):
				pass
			else:
				PRSH4,PRSHBT4,ESH4,AUG4,RAD4,XP4,YP4,XC4,YR4,YC4,YPP4,FFAR4,FFAC4,IZ4,AMZ4,INIOCC4=GASMIXC(conf.NGASN[4],PRSH4,PRSHBT4,ESH4,AUG4,RAD4,XP4,YP4,XC4,YR4,YC4,YPP4,FFAR4,FFAC4,IZ4,AMZ4,INIOCC4)
				if(conf.NGAS == 4):
					pass
				else:
					PRSH5,PRSHBT5,ESH5,AUG5,RAD5,XP5,YP5,XC5,YR5,YC5,YPP5,FFAR5,FFAC5,IZ5,AMZ5,INIOCC5=GASMIXC(conf.NGASN[5],PRSH5,PRSHBT5,ESH5,AUG5,RAD5,XP5,YP5,XC5,YR5,YC5,YPP5,FFAR5,FFAC5,IZ5,AMZ5,INIOCC5)
					if(conf.NGAS == 5):
						pass
					else:
						PRSH6,PRSHBT6,ESH6,AUG6,RAD6,XP6,YP6,XC6,YR6,YC6,YPP6,FFAR6,FFAC6,IZ6,AMZ6,INIOCC6=GASMIXC(conf.NGASN[6],PRSH6,PRSHBT6,ESH6,AUG6,RAD6,XP6,YP6,XC6,YR6,YC6,YPP6,FFAR6,FFAC6,IZ6,AMZ6,INIOCC6)
						if(conf.NGAS == 6):
							pass
	# 10 CONTINUE
	I=1
	print(conf.XPE.shape,XP1.shape)
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ1[J1]
		conf.AMZ[I][J1]=AMZ1[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[1][J1][J][M]=XP1[J1][J][M]
				conf.YPE[1][J1][J][M]=YP1[J1][J][M]
			conf.ESH[I][J1][J]=ESH1[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC1[J1][J]
			if(INIOCC1[J1][J]!= 0):
				conf.ISHLMX[1][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT1[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH1[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD1[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG1[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[1][J][M]=XC1[J][M]
			conf.YRY[1][J][M]=YR1[J][M]
			conf.YCP[1][J][M]=YC1[J][M]
			# print("mixerc ", type(J),type(M))
			# print("mixerc  ",type(conf.YPP[1][J][M]),type(YPP1[J][M]))
			conf.YPP[1][J][M]=YPP1[J][M]
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[1][J][K]=FFAR1[J][K]
			conf.FRMFC[1][J][K]=FFAC1[J][K]
	if(conf.NGAS == 1):
		return
	I=2
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ2[J1]
		conf.AMZ[I][J1]=AMZ2[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[2][J1][J][M]=XP2[J1][J][M]
				conf.YPE[2][J1][J][M]=YP2[J1][J][M]
			conf.ESH[I][J1][J]=ESH2[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC2[J1][J]
			if(INIOCC2[J1][J]!= 0):
				conf.ISHLMX[2][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT2[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH2[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD2[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG2[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[2][J][M]=XC2[J][M]
			conf.YRY[2][J][M]=YR2[J][M]
			conf.YCP[2][J][M]=YC2[J][M]
			conf.YPP[2][J][M]=YPP2[J][M]
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[2][J][K]=FFAR2[J][K]
			conf.FRMFC[2][J][K]=FFAC2[J][K]
	if(conf.NGAS == 2):
		return
	I=3
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ3[J1]
		conf.AMZ[I][J1]=AMZ3[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[3][J1][J][M]=XP3[J1][J][M]
				conf.YPE[3][J1][J][M]=YP3[J1][J][M]
			conf.ESH[I][J1][J]=ESH3[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC3[J1][J]
			if(INIOCC3[J1][J]!= 0):
				conf.ISHLMX[3][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT3[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH3[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD3[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG3[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[3][J][M]=XC3[J][M]
			conf.YRY[3][J][M]=YR3[J][M]
			conf.YCP[3][J][M]=YC3[J][M]
			conf.YPP[3][J][M]=YPP3[J][M]
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[3][J][K]=FFAR3[J][K]
			conf.FRMFC[3][J][K]=FFAC3[J][K]
	if(conf.NGAS == 3):
		return
	I=4
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ4[J1]
		conf.AMZ[I][J1]=AMZ4[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[4][J1][J][M]=XP4[J1][J][M]
				conf.YPE[4][J1][J][M]=YP4[J1][J][M]
			conf.ESH[I][J1][J]=ESH4[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC4[J1][J]
			if(INIOCC4[J1][J]!= 0):
				conf.ISHLMX[4][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT4[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH4[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD4[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG4[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[4][J][M]=XC4[J][M]
			conf.YRY[4][J][M]=YR4[J][M]
			conf.YCP[4][J][M]=YC4[J][M]
			conf.YPP[4][J][M]=YPP4[J][M]
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[4][J][K]=FFAR4[J][K]
			conf.FRMFC[4][J][K]=FFAC4[J][K]
	if(conf.NGAS == 4):
		return
	I=5
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ5[J1]
		conf.AMZ[I][J1]=AMZ5[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[5][J1][J][M]=XP5[J1][J][M]
				conf.YPE[5][J1][J][M]=YP5[J1][J][M]
			conf.ESH[I][J1][J]=ESH5[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC5[J1][J]
			if(INIOCC5[J1][J]!= 0):
				conf.ISHLMX[5][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT5[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH5[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD5[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG5[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[5][J][M]=XC5[J][M]
			conf.YRY[5][J][M]=YR5[J][M]
			conf.YCP[5][J][M]=YC5[J][M]
			conf.YPP[5][J][M]=YPP5[J][M] 
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[5][J][K]=FFAR5[J][K]
			conf.FRMFC[5][J][K]=FFAC5[J][K]
	if(conf.NGAS == 5):
		return
	I=6
	for J1 in range(1,3+1):
		conf.IZ[I][J1]=IZ6[J1]
		conf.AMZ[I][J1]=AMZ6[J1]
		for J in range(1,17+1):
			for M in range(1,60+1):
				conf.XPE[6][J1][J][M]=XP6[J1][J][M]
				conf.YPE[6][J1][J][M]=YP6[J1][J][M]
			conf.ESH[I][J1][J]=ESH6[J1][J]
			conf.INIOCC[I][J1][J]=INIOCC6[J1][J]
			if(INIOCC6[J1][J]!= 0):
				conf.ISHLMX[6][J1]=J
			conf.PRSHBT[I][J1][J]=PRSHBT6[J1][J]
			for K in range(1,17+1):
				conf.PRSH[I][J1][J][K]=PRSH6[J1][J][K]
				conf.RAD[I,J1,J,K]=RAD6[J1][J][K]
				for L in range(1,17+1):
					conf.AUG[I][J1][J][K][L]=AUG6[J1][J][K][L]
	for J in range(1,3+1):
		for M in range(1,54+1):
			conf.XCP[6][J][M]=XC6[J][M]
			conf.YRY[6][J][M]=YR6[J][M]
			conf.YCP[6][J][M]=YC6[J][M]
			conf.YPP[6][J][M]=YPP6[J][M]
	for J in range(1,3+1):
		for K in range(1,45+1):
			conf.FRMFR[6][J][K]=FFAR6[J][K]
			conf.FRMFC[6][J][K]=FFAC6[J][K]
	if(conf.NGAS > 6):
		print(' subroutine STOPPED: NGAS=',conf.NGAS,' IN MIXERC')
		sys.exit()
	# endif
	# 1000 CONTINUE
	return
	# end