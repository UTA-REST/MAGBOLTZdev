import conf
import numpy
import sys
import conf
import Inthrm1
def OUTPUTC(NEVENT,IMIP):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN,MSUM,MCOMP,MRAYL,MPAIR,MPHOT,MVAC,IONSM,IFLSM,ESTOR,EPHOT,X,Y,Z,DRX0,DRY0,DRZ0,IONF1,ESTF1,X1,Y1,Z1,DRX1,DRY1,DRZ1,IONF2,ESTF2,X2,Y2,Z2,DRX2,DRY2,DRZ2,IONF3,ESTF3,X3,Y3,Z3,DRX3,DRY3,DRZ3,IONF4,ESTF4,X4,Y4,Z4,DRX4,DRY4,DRZ4,IONF5,ESTF5,X5,Y5,Z5,DRX5,DRY5,DRZ5,EPPST,XPP,YPP,ZPP,DRXPP,DRYPP,DRZPP,AIONFRQ,AIFLFRQ,EAV,EPHAV,ETOTAV,AIONAV,NPTPE,ET,XT,YT,ZT,DRX,DRY,DRZ,NJFLR,IEVENTL,IBAD,IBADTOT
	def get_globals():
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
		MSUM=conf.MSUM
		MCOMP=conf.MCOMP
		MRAYL=conf.MRAYL
		MPAIR=conf.MPAIR
		MPHOT=conf.MPHOT
		MVAC=conf.MVAC
		IONSM=conf.IONSM
		IFLSM=conf.IFLSM
		ESTOR=conf.ESTOR
		EPHOT=conf.EPHOT
		X=conf.X
		Y=conf.Y
		Z=conf.Z
		DRX0=conf.DRX0
		DRY0=conf.DRY0
		DRZ0=conf.DRZ0
		IONF1=conf.IONF1
		ESTF1=conf.ESTF1
		X1=conf.X1
		Y1=conf.Y1
		Z1=conf.Z1
		DRX1=conf.DRX1
		DRY1=conf.DRY1
		DRZ1=conf.DRZ1
		IONF2=conf.IONF2
		ESTF2=conf.ESTF2
		X2=conf.X2
		Y2=conf.Y2
		Z2=conf.Z2
		DRX2=conf.DRX2
		DRY2=conf.DRY2
		DRZ2=conf.DRZ2
		IONF3=conf.IONF3
		ESTF3=conf.ESTF3
		X3=conf.X3
		Y3=conf.Y3
		Z3=conf.Z3
		DRX3=conf.DRX3
		DRY3=conf.DRY3
		DRZ3=conf.DRZ3
		IONF4=conf.IONF4
		ESTF4=conf.ESTF4
		X4=conf.X4
		Y4=conf.Y4
		Z4=conf.Z4
		DRX4=conf.DRX4
		DRY4=conf.DRY4
		DRZ4=conf.DRZ4
		IONF5=conf.IONF5
		ESTF5=conf.ESTF5
		X5=conf.X5
		Y5=conf.Y5
		Z5=conf.Z5
		DRX5=conf.DRX5
		DRY5=conf.DRY5
		DRZ5=conf.DRZ5
		EPPST=conf.EPPST
		XPP=conf.XPP
		YPP=conf.YPP
		ZPP=conf.ZPP
		DRXPP=conf.DRXPP
		DRYPP=conf.DRYPP
		DRZPP=conf.DRZPP
		AIONFRQ=conf.AIONFRQ
		AIFLFRQ=conf.AIFLFRQ
		EAV=conf.EAV
		EPHAV=conf.EPHAV
		ETOTAV=conf.ETOTAV
		AIONAV=conf.AIONAV
		NPTPE=Inthrm1.NPTPE
		ET=Inthrm1.ET
		XT=Inthrm1.XT
		YT=Inthrm1.YT
		ZT=Inthrm1.ZT
		DRX=Inthrm1.DRX
		DRY=Inthrm1.DRY
		DRZ=Inthrm1.DRZ
		NJFLR=Inthrm1.NJFLR
		IEVENTL=Inthrm1.IEVENTL
		IBAD=Inthrm1.IBAD
		IBADTOT=Inthrm1.IBADTOT
		globals().update(locals())
	get_globals()
	def update_globals():
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
		conf.MSUM=MSUM
		conf.MCOMP=MCOMP
		conf.MRAYL=MRAYL
		conf.MPAIR=MPAIR
		conf.MPHOT=MPHOT
		conf.MVAC=MVAC
		conf.IONSM=IONSM
		conf.IFLSM=IFLSM
		conf.ESTOR=ESTOR
		conf.EPHOT=EPHOT
		conf.X=X
		conf.Y=Y
		conf.Z=Z
		conf.DRX0=DRX0
		conf.DRY0=DRY0
		conf.DRZ0=DRZ0
		conf.IONF1=IONF1
		conf.ESTF1=ESTF1
		conf.X1=X1
		conf.Y1=Y1
		conf.Z1=Z1
		conf.DRX1=DRX1
		conf.DRY1=DRY1
		conf.DRZ1=DRZ1
		conf.IONF2=IONF2
		conf.ESTF2=ESTF2
		conf.X2=X2
		conf.Y2=Y2
		conf.Z2=Z2
		conf.DRX2=DRX2
		conf.DRY2=DRY2
		conf.DRZ2=DRZ2
		conf.IONF3=IONF3
		conf.ESTF3=ESTF3
		conf.X3=X3
		conf.Y3=Y3
		conf.Z3=Z3
		conf.DRX3=DRX3
		conf.DRY3=DRY3
		conf.DRZ3=DRZ3
		conf.IONF4=IONF4
		conf.ESTF4=ESTF4
		conf.X4=X4
		conf.Y4=Y4
		conf.Z4=Z4
		conf.DRX4=DRX4
		conf.DRY4=DRY4
		conf.DRZ4=DRZ4
		conf.IONF5=IONF5
		conf.ESTF5=ESTF5
		conf.X5=X5
		conf.Y5=Y5
		conf.Z5=Z5
		conf.DRX5=DRX5
		conf.DRY5=DRY5
		conf.DRZ5=DRZ5
		conf.EPPST=EPPST
		conf.XPP=XPP
		conf.YPP=YPP
		conf.ZPP=ZPP
		conf.DRXPP=DRXPP
		conf.DRYPP=DRYPP
		conf.DRZPP=DRZPP
		conf.AIONFRQ=AIONFRQ
		conf.AIFLFRQ=AIFLFRQ
		conf.EAV=EAV
		conf.EPHAV=EPHAV
		conf.ETOTAV=ETOTAV
		conf.AIONAV=AIONAV
		Inthrm1.NPTPE=NPTPE
		Inthrm1.ET=ET
		Inthrm1.XT=XT
		Inthrm1.YT=YT
		Inthrm1.ZT=ZT
		Inthrm1.DRX=DRX
		Inthrm1.DRY=DRY
		Inthrm1.DRZ=DRZ
		Inthrm1.NJFLR=NJFLR
		Inthrm1.IEVENTL=IEVENTL
		Inthrm1.IBAD=IBAD
		Inthrm1.IBADTOT=IBADTOT

	# DIMENSION 
	EST=numpy.zeros((10+1,10000+1))
	EPH=numpy.zeros((10+1,10000+1))
	EPSM=numpy.zeros((10+1,10000+1))
	ESTOT=numpy.zeros((10+1,10000+1))
	# DIMENSION 
	AIGEN1F=numpy.zeros((28+1))
	AIGEN2F=numpy.zeros((28+1))
	AIGEN3F=numpy.zeros((28+1))
	AIGEN4F=numpy.zeros((28+1))
	AIGEN5F=numpy.zeros((28+1))
	AITOT=numpy.zeros((50+1))
	AITOTS=numpy.zeros((50+1))
	#      
	#
	for L in range(1,28+1):
		AIONFRQ[L]=0.0
		AIGEN1F[L]=0.0
		AIGEN2F[L]=0.0
		AIGEN3F[L]=0.0
		AIGEN4F[L]=0.0
		AIGEN5F[L]=0.0
	# 1 CONTINUE
	for L in range(1,50+1):
		AITOT[L]=0.0
	# 76 CONTINUE
	IONG0=0
	IONG1=0
	IONG2=0
	IONG3=0
	IONG4=0
	IONG5=0
	IONGSUM=0
	NTOT=0
	IPR=0
	for I in range(1,10000+1):
		IPR=IPR+MCOMP[I]+MPAIR[I]
	# 300 CONTINUE
	# FIND AVERAGES OVER EVENTS FOR EACH GAS 
	for J in range(1,NEVENT+1):
		NPTPE[J]=MVAC[J]
		for K in range(1,MVAC[J]+1):
			EST[K][J]=0.0
			EPH[K][J]=0.0
			EPSM[K][J]=0.0
			ESTOT[K][J]=0.0
			NTOT=NTOT+1
			if(IONG0 < int(IONSM[K][J])):
				IONG0=int(IONSM[K][J])
			if(IONG1 < IONF1[K][J]):
				IONG1=IONF1[K][J]
			if(IONG2 < IONF2[K][J]):
				IONG2=IONF2[K][J]
			if(IONG3 < IONF3[K][J]):
				IONG3=IONF3[K][J]
			if(IONG4 < IONF4[K][J]):
				IONG4=IONF4[K][J]
			if(IONG5 < IONF5[K][J]):
				IONG5=IONF5[K][J]
			ITOT=int(IONSM[K][J])+IONF1[K][J]+IONF2[K][J]+IONF3[K][J]+IONF4[K][J]+IONF5[K][J]
			if(ITOT > 50):
				# WRITE(6,811) J
				# 811 
				print(' NEVENT=',J,' ITOT OVERFLOW IN OUTPUT')
				ITOT=50
			# endif
			if(IONGSUM < ITOT):
				IONGSUM=ITOT
			if(int(IONSM[K][J])<= 0):
				# GO TO 101
				pass
			else:
				AIONFRQ[int(IONSM[K][J])]=AIONFRQ[int(IONSM[K][J])]+1.0
			# 101 
			if(IONF1[K][J] <= 0):
				# GO TO 102
				pass
			else:
				AIGEN1F[IONF1[K][J]]=AIGEN1F[IONF1[K][J]]+1.0
			# 102 
			if(IONF2[K][J] <= 0):
				# GO TO 103
				pass
			else:
				AIGEN2F[IONF2[K][J]]=AIGEN2F[IONF2[K][J]]+1.0
			# 103 
			if(IONF3[K][J] <= 0):
				# GO TO 104
				pass
			else:
				AIGEN3F[IONF3[K][J]]=AIGEN3F[IONF3[K][J]]+1.0
			# 104 
			if(IONF4[K][J] <= 0):
				# GO TO 105
				pass
			else:
				AIGEN4F[IONF4[K][J]]=AIGEN4F[IONF4[K][J]]+1.0
			# 105 
			if(IONF5[K][J] <= 0):
				# GO TO 106
				pass
			else:
				AIGEN5F[IONF5[K][J]]=AIGEN5F[IONF5[K][J]]+1.0
			# 106 
			if(ITOT <= 0):
				# GO TO 107
				pass
			else:
				AITOT[int(ITOT)]=AITOT[int(ITOT)]+1.0
			# 107 
			if(IFLSM[K][J] == 0):
				# GO TO 2
				pass
			else:
				AIFLFRQ[IFLSM[K][J]]=AIFLFRQ[IFLSM[K][J]]+1.0
			# 2 CONTINUE
			for L in range(1,28+1):
				EST[K][J]=EST[K][J]+ESTOR[K][L][J]
				EPH[K][J]=EPH[K][J]+EPHOT[K][L][J]
			# 4 CONTINUE
			ESTOT[K][J]=EST[K][J]
			EPSM[K][J]=EPH[K][J]+EST[K][J]
			IEVENTL[K][J]=int(IONSM[K][J])+IONF1[K][J]+IONF2[K][J]+IONF3[K][J]+IONF4[K][J]+IONF5[K][J]
			if(IEVENTL[K][J]> 50) :
				# WRITE(6,99) 
				# 99  
				print(' IEVENTL GT 50 , IEVENTL=%d PRIMARY NUMBER=%d EVENT NUMBER =%d'%(IEVENTL[K][J],K,J))
				sys.exit()
			# endif
			# PRINT SOME RAW DATA
			# STORE EVENT FOR INPUT TO THERMALISATION
			for M in range(1,int(IONSM[K][J])+1):
				ET[K][M][J]=ESTOR[K][M][J]
				XT[K][M][J]=X[K][M][J]
				YT[K][M][J]=Y[K][M][J]
				ZT[K][M][J]=Z[K][M][J]
				DRX[K][M][J]=DRX0[K][M][J]
				DRY[K][M][J]=DRY0[K][M][J]
				DRZ[K,M,J]=DRZ0[K][M][J]
				NJFLR[K][M][J]=0
			# 6 CONTINUE
			if(IONF1[K][J]== 0):
				# GO TO 17
				pass
			else:
				for M in range(1,IONF1[K][J]+1):
					M1=M+int(IONSM[K][J])
					ET[K][M1][J]=ESTF1[K][M][J]   
					XT[K][M1][J]=X1[K][M][J]
					YT[K][M1][J]=Y1[K][M][J]
					ZT[K][M1][J]=Z1[K][M][J]
					DRX[K][M1][J]=DRX1[K][M][J]
					DRY[K][M1][J]=DRY1[K][M][J]
					DRZ[K,M1,J]=DRZ1[K][M][J]
					ESTOT[K][J]=ESTOT[K][J]+ESTF1[K][M][J]
					NJFLR[K][M1][J]=M
				# 7 CONTINUE
			# 17 
			if(IONF2[K][J] == 0):
				# GO TO 18
				pass
			else:
				for M in range(1,IONF2[K][J]+1):
					M2=M+int(IONSM[K][J])+IONF1[K][J]
					ET[K][M2][J]=ESTF2[K][M][J]
					XT[K][M2][J]=X2[K][M][J]
					YT[K][M2][J]=Y2[K][M][J]
					ZT[K][M2][J]=Z2[K][M][J]
					DRX[K][M2][J]=DRX2[K][M][J]
					DRY[K][M2][J]=DRY2[K][M][J]
					DRZ[K,M2,J]=DRZ2[K][M][J]
					ESTOT[K][J]=ESTOT[K][J]+ESTF2[K][M][J]
					NJFLR[K][M2][J]=2
				# 8 CONTINUE
			# 18 
			if(IONF3[K][J] == 0):
				# GO TO 19
				pass
			else:
				for M in range(1,IONF3[K][J]+1):
					M3=M+int(IONSM[K][J])+IONF1[K][J]+IONF2[K][J]
					ET[K][M3][J]=ESTF3[K][M][J]
					XT[K][M3][J]=X3[K][M][J]
					YT[K][M3][J]=Y3[K][M][J]
					ZT[K][M3][J]=Z3[K][M][J]
					DRX[K][M3][J]=DRX3[K][M][J]
					DRY[K][M3][J]=DRY3[K][M][J]
					DRZ[K,M3,J]=DRZ3[K][M][J]
					ESTOT[K][J]=ESTOT[K][J]+ESTF3[K][M][J]
					NJFLR[K][M3][J]=3
				# 9 CONTINUE
			# 19 
			if(IONF4[K][J] == 0):
				# GO TO 20
				pass
			else:
				for M in range(1,IONF4[K][J]+1):
					M4=M+int(IONSM[K][J])+IONF1[K][J]+IONF2[K][J]+IONF3[K][J]
					ET[K][M4][J]=ESTF4[K][M][J]
					XT[K][M4][J]=X4[K][M][J]
					YT[K][M4][J]=Y4[K][M][J]
					ZT[K][M4][J]=Z4[K][M][J]
					DRX[K][M4][J]=DRX4[K][M][J]
					DRY[K][M4][J]=DRY4[K][M][J]
					DRZ[K,M4,J]=DRZ4[K][M][J]
					ESTOT[K][J]=ESTOT[K][J]+ESTF4[K][M][J]
					NJFLR[K][M4][J]=4
				# 10 CONTINUE
			# 20 
			if(IONF5[K][J] == 0):
				# GO TO 21
				pass
			else:
				for M in range(1,IONF5[K][J]+1):
					M5=M+int(IONSM[K][J])+IONF1[K][J]+IONF2[K][J]+IONF3[K][J]+IONF4[K][J]
					ET[K][M5][J]=ESTF5[K][M][J]
					XT[K][M5][J]=X5[K][M][J]
					YT[K][M5][J]=Y5[K][M][J]
					ZT[K][M5][J]=Z5[K][M][J]
					DRX[K][M5][J]=DRX5[K][M][J]
					DRY[K][M5][J]=DRY5[K][M][J]
					DRZ[K,M5,J]=DRZ5[K][M][J]
					ESTOT[K][J]=ESTOT[K][J]+ESTF5[K][M][J]
					NJFLR[K][M5][J]=5
				# 11 CONTINUE
			# 21 CONTINUE
			# PRINT SOME RAW DATA
			#     IF(J <= 525) :
			#     EDUM=0.0
			#     DO 666 JJ=1,IEVENTL[J]
			# 666 EDUM=EDUM+ET(JJ,J)
			#     WRITE(6,232) J
			#     WRITE(6,2321) EDUM
			#2321 print(' TOT ENERGY=','%.3f' %)
			# 232 print(' DATA FOR EVENT=',I3)
			#     DO 234 M=1,IEVENTL[J]
			#     WRITE(6,233) ET(M,J),XT(M,J),YT(M,J),ZT(M,J),TH(M,J),PH(M,J)
			# 233 print(' E=','%.3f' %,' X=','%.3f' %,' Y=','%.3f' %,' Z=','%.3f' %,' THETA=',
			#    /'%.3f' %,' PHI=','%.3f' %)
			# 234 CONTINUE
			#     # endIF
	# 12 CONTINUE
	AIONAV=0.0
	for I in range(1,28+1):
		AIONFRQ[I]=AIONFRQ[I]/float(NTOT)
		AIGEN1F[I]=AIGEN1F[I]/float(NTOT)
		AIGEN2F[I]=AIGEN2F[I]/float(NTOT)
		AIGEN3F[I]=AIGEN3F[I]/float(NTOT)
		AIGEN4F[I]=AIGEN4F[I]/float(NTOT)
		AIGEN5F[I]=AIGEN5F[I]/float(NTOT)
		AIFLFRQ[I]=AIFLFRQ[I]/float(NTOT)
		AIONAV=AIONAV+float(I)*AIONFRQ[I]
	# 22 CONTINUE
	AITOTAV=0.0
	AITOTSUM=0.0
	for I in range(1,50+1):
		AITOT[I]=AITOT[I]/float(NTOT)
		AITOTSUM=AITOTSUM+AITOT[I]
		AITOTAV=AITOTAV+float(I)*AITOT[I]
	# 77 CONTINUE
	for I in range(1,50+1):
		AITOTS[I]=AITOT[I]/AITOTSUM
	for I in range(2,50+1):
		AITOTS[I]=AITOTS[I]+AITOTS[I-1]
	EAV=0.0
	EPHAV=0.0
	ETOTAV=0.0
	IBADTOT=0
	for J in range(1,NEVENT+1):
		EDUM=0.0
		IBAD[J]=0
		for K in range(1,MVAC[J]+1):
			EAV=EAV+EST[K][J]
			EPHAV=EPHAV+EPH[K][J]
			ETOTAV=ETOTAV+ESTOT[K][J]
			EDUM=EDUM+ESTOT[K][J]
		# 30 CONTINUE
		EAV=EAV+EPPST[1][J]+EPPST[2][J]
		ETOTAV=ETOTAV+EPPST[1][J]+EPPST[2][J]
		EDUM=EDUM+EPPST[1][J]+EPPST[2][J]
		if(IMIP == 5):
			# GO TO 33
			pass
		else:
			if(EDUM > (EFINAL+0.1)):
				# WRITE(6,999) J,EDUM
				# 999 
				print(' EVENT NO =%d ETOT =%.5f EV.    BAD EVENT\n'%(J,EDUM))
				IBAD[J]=1
				IBADTOT=IBADTOT+1
			# endif
			# GO TO 35
			continue
		# 33 
		if(EDUM > (2.0*EFINAL+0.1)) :
			# WRITE(6,999) J,EDUM
			print(' EVENT NO =%d ETOT =%.5f EV.    BAD EVENT\n'%(J,EDUM))
			IBAD[J]=1
			IBADTOT=IBADTOT+1
		# endif
	# 35 CONTINUE
	EAV=EAV/float(NEVENT)
	EPHAV=EPHAV/float(NEVENT)
	ETOTAV=ETOTAV/float(NEVENT)
	# DO NOT PRINT ION ANALYSIS IF COMPTON OR PAIR PRODUCTION USED
	if(IPR > 0):
		update_globals()
		return  
	for I in range(1,28+1):
		# WRITE(6,88) I,AIONFRQ[I],I,AIFLFRQ[I]
		# 88 
		print(' FREQ FOR %d CHARGE IONS = %.4f FREQUENCY FOR %d PHOTONS=%.4f' %(I,AIONFRQ[I],I,AIFLFRQ[I]) )
	# 40 CONTINUE
	# WRITE(6,89) EAV,EPHAV,AIONAV
	# 89 
	print('\n\n AVERAGE ELECTRON ENERGY (GENERATION 0) =%.6f \n AVERAGE PHOTON ENERGY (GENERATION 0) =%.6f \n  AVERAGE IONIC CHARGE (GENERATION 0) =%.3f \n\n'%(EAV,EPHAV,AIONAV))
	# WRITE(6,90)
	# 90 
	print(' ION FREQENCIES FOR IST SECOND THIRD AND FOURTH GENERATION PHOTON ABSORPTION')
	for I in range(1,28+1):
		# WRITE(6,91) I,AIGEN1F[I],AIGEN2F[I],AIGEN3F[I],AIGEN4F[I],AIGEN5F[I]
		# 91 
		print(' FREQ FOR %d  IST GEN IONS= %.4f 2ND GEN= %.3f  3RD GEN= %.3f 4TH GEN= %.3f 5TH GEN=%.3f' %(I,AIGEN1F[I],AIGEN2F[I],AIGEN3F[I],AIGEN4F[I],AIGEN5F[I])) 
	# 50 CONTINUE
	for I in range(1,50+1):
		# WRITE(6,92) I,AITOT[I],AITOTS[I]
		# 92 
		print(' TOTAL FREQ FOR %d ELECTRONS= %.4f NORMALISED INTEGRAL PROB=%.4f' %(I,AITOT[I],AITOTS[I]) ) 
	# 60 CONTINUE  
	# WRITE(6,93) IONG0,IONG1,IONG2,IONG3,IONG4,IONG5,IONGSUM,AITOTAV,ETOTAV
	# 93 
	print(' MAX IONS GEN 0 =%d \n MAX IONS GEN 1 =%d \n MAX IONS GEN 2 =%d \n MAX IONS GEN 3 =%d \n MAX IONS GEN 4 =%d \n MAX IONS GEN 5 =%d \n MAX NO. OF ELECTRONS AFTER PHOTON ABSORPTION =%d \n AVERAGE NO. OF ELECTRONS =%.3f \n AVERAGE TOTAL ELECTRON ENERGY =%.6f \n\n'%(IONG0,IONG1,IONG2,IONG3,IONG4,IONG5,IONGSUM,AITOTAV,ETOTAV)) 
	update_globals()
	return     
  # end         