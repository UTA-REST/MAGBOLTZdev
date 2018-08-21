import time 
import Inthrm1
import conf
import sys
import numpy
import random 
import casrs
def CASRES(NEVENT,IBADTT1,IBAD1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	def get_globals():
		NPTP=conf.NPTP
		EPPST=conf.EPPST
		XPP=conf.XPP
		YPP=conf.YPP
		ZPP=conf.ZPP
		DRXPP=conf.DRXPP
		DRYPP=conf.DRYPP
		DRZPP=conf.DRZPP

		NPTPE=Inthrm1.NPTPE
		ET=Inthrm1.ET
		XT=Inthrm1.XT
		YT=Inthrm1.YT
		ZT=Inthrm1.ZT
		DRXX=Inthrm1.DRXX
		DRYY=Inthrm1.DRYY
		DRZZ=Inthrm1.DRZZ
		NJFLR=Inthrm1.NJFLR
		IEVENTL=Inthrm1.IEVENTL
		IBAD=Inthrm1.IBAD
		IBADTOT=Inthrm1.IBADTOT

		TT=conf.TT
		TTP=conf.TTP
		E=casrs.E
		X=casrs.X
		Y=casrs.Y
		Z=casrs.Z
		DRX=casrs.DRX
		DRY=casrs.DRY
		DRZ=casrs.DRZ
		T=casrs.T
		NFLGF=casrs.NFLGF
		NFLGPP=casrs.NFLGPP
		IEVENT=casrs.IEVENT
		globals().update(locals())
	get_globals()
	def update_globals():
		conf.NPTP=NPTP
		conf.EPPST=EPPST
		conf.XPP=XPP
		conf.YPP=YPP
		conf.ZPP=ZPP
		conf.DRXPP=DRXPP
		conf.DRYPP=DRYPP
		conf.DRZPP=DRZPP

		Inthrm1.NPTPE=NPTPE
		Inthrm1.ET=ET
		Inthrm1.XT=XT
		Inthrm1.YT=YT
		Inthrm1.ZT=ZT
		Inthrm1.DRXX=DRXX
		Inthrm1.DRYY=DRYY
		Inthrm1.DRZZ=DRZZ
		Inthrm1.NJFLR=NJFLR
		Inthrm1.IEVENTL=IEVENTL
		Inthrm1.IBAD=IBAD
		Inthrm1.IBADTOT=IBADTOT

		conf.TT=TT
		conf.TTP=TTP
		casrs.E=E
		casrs.X=X
		casrs.Y=Y
		casrs.Z=Z
		casrs.DRX=DRX
		casrs.DRY=DRY
		casrs.DRZ=DRZ
		casrs.T=T
		casrs.NFLGF=NFLGF
		casrs.NFLGPP=NFLGPP
		casrs.IEVENT=IEVENT

	# LOADS AUGER CASCADE ELECTRON POSITIONS,ANGLES AND ENERGY FOR EACH
	# EVENT INTO THE COMMON BLOCK/CASRS/
	K=0
	ESM=0.0
	for I in range(1,int(NPTPE[int(NEVENT)])+1):
		for J in range(1,int(IEVENTL[I][int(NEVENT)])+1):
			K=K+1
			E[K]=ET[I][J][int(NEVENT)]
			X[K]=XT[I][J][int(NEVENT)]
			Y[K]=YT[I][J][int(NEVENT)]
			Z[K]=ZT[I][J][int(NEVENT)]
			ESM=ESM+E[K]
			DRX[K]=DRXX[I][J][int(NEVENT)]
			DRY[K]=DRYY[I][J][int(NEVENT)]
			DRZ[K]=DRZZ[I][J][int(NEVENT)]
			NFLGF[K]=NJFLR[I][J][int(NEVENT)]
			NFLGPP[K]=0
			T[K]=TT[I][int(NEVENT)]
	# 1 CONTINUE 
	# LOAD PAIR PRODUCTION
	if(NPTP[int(NEVENT)]== 0):
		# GO TO 3
		pass
	else:
		for I in range(1,NPTP[int(NEVENT)]+1):
			K=K+1
			E[K]=EPPST[I][int(NEVENT)]
			X[K]=XPP[I][int(NEVENT)]
			Y[K]=YPP[I][int(NEVENT)]
			Z[K]=ZPP[I][int(NEVENT)]
			NFLGF[K]=0
			NFLGPP[K]=1
			T[K]=TTP[int(NEVENT)]
			DRX[K]=DRXPP[I][int(NEVENT)]
			DRY[K]=DRYPP[I][int(NEVENT)]
			DRZ[K]=DRZPP[I][int(NEVENT)]
			K=K+1
			E[K]=EPPST[I+1][int(NEVENT)]
			X[K]=XPP[I+1][int(NEVENT)]
			Y[K]=YPP[I+1][int(NEVENT)]
			Z[K]=ZPP[I+1][int(NEVENT)]
			NFLGF[K]=0
			NFLGPP[K]=2
			T[K]=TTP[int(NEVENT)]
			DRX[K]=DRXPP[I+1][int(NEVENT)]
			DRY[K]=DRYPP[I+1][int(NEVENT)] 
			DRZ[K]=DRZPP[I+1][int(NEVENT)]
		# 2 CONTINUE
	# 3 
	IBAD1=IBAD[int(NEVENT)]
	IEVENT=K
	IBADTT1=IBADTOT
	if(K > 400):
		# WRITE(6,99) K
		print(' ARRAY TOO LARGE IN CASRES K=',K) 
		sys.exit()
	# endif
	update_globals()
	return
	# end