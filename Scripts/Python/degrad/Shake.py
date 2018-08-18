import numpy
import conf
import random 
import sys
def SHAKE(ISHELL,EN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC):
	# IMPLICIT #real*8(A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# CHARACTER*6 SCR(17),SCR1(17)
	def get_globals():
		ELEV=conf.ELEV
		NSDEG=conf.NSDEG
		AA=conf.AA
		BB=conf.BB
		SCR=conf.SCR
		SCR1=conf.SCR1
		PRSH=conf.PRSH
		ESH=conf.ESH
		AUG=conf.AUG
		RAD=conf.RAD
		PRSHBT=conf.PRSHBT
		IZ=conf.IZ
		INIOCC=conf.INIOCC
		ISHLMX=conf.ISHLMX
		AMZ=conf.AMZ
		NOCC=conf.NOCC
		AUGR=conf.AUGR
		RADR=conf.RADR
		globals().update(locals())
	get_globals()
	def update_globals():
		conf.ELEV=ELEV
		conf.NSDEG=NSDEG
		conf.AA=AA
		conf.BB=BB
		conf.SCR=SCR
		conf.SCR1=SCR1
		conf.PRSH=PRSH
		conf.ESH=ESH
		conf.AUG=AUG
		conf.RAD=RAD
		conf.PRSHBT=PRSHBT
		conf.IZ=IZ
		conf.INIOCC=INIOCC
		conf.ISHLMX=ISHLMX
		conf.AMZ=AMZ
		conf.NOCC=NOCC
		conf.AUGR=AUGR
		conf.RADR=RADR
		globals().update(locals())
	# DIMENSION 
	PRSH1=numpy.zeros((17+1))
	PRSH2=numpy.zeros((17+1))
	#
	# SHAKE OFF IN SHELL (JVAC) WITH ENERGY OF SHAKE OFF ESHK
	# INITIAL VACANCY IN ISHELL WITH ELECTRON EMISSION OF ENERGY EN. 
	#     
	# CORRECTION TO PROBABILITIES FOR SHELL OCCUPANCIES
	# AND THRESHOLDS FROM SUDDEN APPROXIMATION
	# THRESHOLD FROM SUDDEN APPROXIMATION SET AT 3.0 TIMES SHELL
	# BINDING ENERGY
	PRSUM=0.0
	flag6=0
	if(ISHELL == 0):
		pass
	else:
		if(ICON == 1 or IFIRST > 1):
			for J in range(1,17+1):
				PRSH1[J]=0.0
				if(INIOCC[int(KGAS)][int(LGAS)][J]== 0):
					# GO TO 1
					continue
				CORR=float(NOCC[int(KGAS)][int(LGAS)][J])/float(INIOCC[int(KGAS)][int(LGAS)][J])
				if(EN < 1.5*(ELEV[J,IZ[int(KGAS)][int(LGAS)]]+ELEV[J,IZ[int(KGAS)][int(LGAS)]+1])):
					# GO TO 1
					continue
				PRSH1[J]=PRSH[int(KGAS)][int(LGAS)][ISHELL][J]*CORR
				PRSUM=PRSUM+PRSH1[J]
		flag6=1
	# endif
	# INITIAL BETA DECAY ELECTRON EJECTION
	if(flag6):
		pass
	else:
		if(ICON == 2 or ICON == 3) :
			for J in range(1,17+1):
				PRSH1[J]=0.0
				# print("shake ",ELEV[J][IZ[int(KGAS)][int(LGAS)]])
				if(EN < 1.5*(ELEV[J][int(IZ[int(KGAS)][int(LGAS)])]+ELEV[J][int(IZ[int(KGAS)][int(LGAS)])+1])):
					# GOTO 5
					continue
				PRSH1[J]=PRSHBT[int(KGAS)][int(LGAS)][J]
				PRSUM=PRSUM+PRSH1[J]
		# endif
	# 6
	R1=random.uniform(0.0,1.0)
	if(R1 >= PRSUM):
		# NO SHAKE OFF OCCURS
		JVAC=0
		ESHK=0.0
		update_globals()
		return ISHELL,EN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC
	# endif
	# SHAKE OFF NOW FIND SHELL OF ORIGIN
	for J in range(1,17+1):
		PRSH1[J]=PRSH1[J]/PRSUM
	PRSH2[1]=PRSH1[1]
	for J in range(2,17+1):
		PRSH2[J]=PRSH1[J]+PRSH2[J-1]
	R1=DRAND48(RDUM)
	for J in range(1,17+1):
		if(R1 < PRSH2[J]) :
			JVAC=J
			ESHK=ESH[int(KGAS)][int(LGAS)][J]
			# UPDATE SHELL OCCUPANCY
			NOCC[int(KGAS)][int(LGAS)][JVAC]=NOCC[int(KGAS)][int(LGAS)][JVAC]-1
			update_globals()
			return ISHELL,EN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC
		# endif
	update_globals()
	return ISHELL,EN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC
	# end     