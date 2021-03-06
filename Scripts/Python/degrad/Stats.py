import numpy
import conf
import sys
import random 
def STATS(NEVENT,NGOOD):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)                                         
	# COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE  
	# COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
	# COMMON/PRIM3/MSUM(10000),MCOMP(10000),MRAYL(10000),MPAIR(10000),MPHOT(10000),MVAC(10000)
	# COMMON/STTS/XST(150000),YST(150000),ZST(150000),TIME(150000),TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,NEGION,EST1,EST2
	# COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),TSTEXC(150000),NSTEXC
	# COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),TSTN(150000),IDNUL(150000),NEXCNUL
	# COMMON/CLUS/XAV[100000],YAV[100000],ZAV[100000],TAV[100000],XYAV[100000],XYZAV[100000],DX(100000),DY(100000),DZ[100000],DT(100000),DXY(100000),DXYZ[100000],NCL(100000),FARX1(100000),FARY1(100000),FARZ1(100000),FARXY1(100000),RMAX1(100000),TSUM(100000),XNEG(100000), YNEG(100000),ZNEG(100000),EDELTA[100000],EDELTA2(100000),NCLEXC(100000)
	# COMMON/PLOT/NXPL10(31),NYPL10(31),NZPL10(31),NXPL40(31),NYPL40(31),NZPL40(31),NXPL100(31),NYPL100(31),NZPL100(31),NXPL400(31),NYPL400(31),NZPL400(31),NXPL1000(31),NYPL1000(31),NZPL1000(31),NXPL2(31),NYPL2(31),NZPL2(31),NXPL4000(31),NYPL4000(31),NZPL4000(31),NXPL10000(31),NYPL10000(31),NZPL10000(31),NXPL40000(31),NYPL40000(31),NZPL40000(31),NXPL100000(31),NYPL100000(31),NZPL100000(31),NRPL2(31),NRPL10(31),NRPL40(31),NRPL100(31),NRPL400(31),NRPL1000(31),NRPL4000(31),NRPL10000(31),NRPL40000(31),NRPL100000(31),NEPL1(100),NEPL10(100),NEPL100(100),MELEC(1000),MELEC3(1000),MELEC10(1000),MELEC30(1000),MELEC100(1000),MELEC300(1000)                 
	#COMMON/SETP/
	global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX#(10)
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE  
	#COMMON/IDEXC/
	global NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
	#COMMON/PRIM3/
	global MSUM#(10000)
	global MCOMP#(10000)
	global MRAYL#(10000)
	global MPAIR#(10000)
	global MPHOT#(10000)
	global MVAC#(10000)
	#COMMON/STTS/
	global XST#(150000)
	global YST#(150000)
	global ZST#(150000)
	global TIME#(150000)
	global TTIME#(150000)
	global NFGF#(150000)
	global NFGPP#(150000)
	global NFGBR#(150000)
	global NELEC,NEGION,EST1,EST2
	#COMMON/STEXC/
	global XSTEXC#(150000)
	global YSTEXC#(150000)
	global ZSTEXC#(150000)
	global TSTEXC#(150000)
	global NSTEXC
	#COMMON/STEXCNUL/
	global XSTN#(150000)
	global YSTN#(150000)
	global ZSTN#(150000)
	global TSTN#(150000)
	global IDNUL#(150000)
	global NEXCNUL
	#COMMON/CLUS/
	global XAV#(100000)
	global YAV#(100000)
	global ZAV#(100000)
	global TAV#(100000)
	global XYAV#(100000)
	global XYZAV#(100000)
	global DX#(100000)
	global DY#(100000)
	global DZ#(100000)
	global DT#(100000)
	global DXY#(100000)
	global DXYZ#(100000)
	global NCL#(100000)
	global FARX1#(100000)
	global FARY1#(100000)
	global FARZ1#(100000)
	global FARXY1#(100000)
	global RMAX1#(100000)
	global TSUM#(100000)
	global XNEG#(100000)
	global YNEG#(100000)
	global ZNEG#(100000)
	global EDELTA#(100000)
	global EDELTA2#(100000)
	global NCLEXC#(100000)
	#COMMON/PLOT/
	global NXPL10#(31)
	global NYPL10#(31)
	global NZPL10#(31)
	global NXPL40#(31)
	global NYPL40#(31)
	global NZPL40#(31)
	global NXPL100#(31)
	global NYPL100#(31)
	global NZPL100#(31)
	global NXPL400#(31)
	global NYPL400#(31)
	global NZPL400#(31)
	global NXPL1000#(31)
	global NYPL1000#(31)
	global NZPL1000#(31)
	global NXPL2#(31)
	global NYPL2#(31)
	global NZPL2#(31)
	global NXPL4000#(31)
	global NYPL4000#(31)
	global NZPL4000#(31)
	global NXPL10000#(31)
	global NYPL10000#(31)
	global NZPL10000#(31)
	global NXPL40000#(31)
	global NYPL40000#(31)
	global NZPL40000#(31)
	global NXPL100000#(31)
	global NYPL100000#(31)
	global NZPL100000#(31)
	global NRPL2#(31)
	global NRPL10#(31)
	global NRPL40#(31)
	global NRPL100#(31)
	global NRPL400#(31)
	global NRPL1000#(31)
	global NRPL4000#(31)
	global NRPL10000#(31)
	global NRPL40000#(31)
	global NRPL100000#(31)
	global NEPL1#(100)
	global NEPL10#(100)
	global NEPL100#(100)
	global MELEC#(1000)
	global MELEC3#(1000)
	global MELEC10#(1000)
	global MELEC30#(1000)
	global MELEC100#(1000)
	global MELEC300#(1000)                 
	def get_globals():
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
		IWRITE  =conf.IWRITE  
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
		MSUM=conf.MSUM
		MCOMP=conf.MCOMP
		MRAYL=conf.MRAYL
		MPAIR=conf.MPAIR
		MPHOT=conf.MPHOT
		MVAC=conf.MVAC
		XST=conf.XST
		YST=conf.YST
		ZST=conf.ZST
		TIME=conf.TIME
		TTIME=conf.TTIME
		NFGF=conf.NFGF
		NFGPP=conf.NFGPP
		NFGBR=conf.NFGBR
		NELEC=conf.NELEC
		NEGION=conf.NEGION
		EST1=conf.EST1
		EST2=conf.EST2
		XSTEXC=conf.XSTEXC
		YSTEXC=conf.YSTEXC
		ZSTEXC=conf.ZSTEXC
		TSTEXC=conf.TSTEXC
		NSTEXC=conf.NSTEXC
		XSTN=conf.XSTN
		YSTN=conf.YSTN
		ZSTN=conf.ZSTN
		TSTN=conf.TSTN
		IDNUL=conf.IDNUL
		NEXCNUL=conf.NEXCNUL
		XAV=conf.XAV
		YAV=conf.YAV
		ZAV=conf.ZAV
		TAV=conf.TAV
		XYAV=conf.XYAV
		XYZAV=conf.XYZAV
		DX=conf.DX
		DY=conf.DY
		DZ=conf.DZ
		DT=conf.DT
		DXY=conf.DXY
		DXYZ=conf.DXYZ
		NCL=conf.NCL
		FARX1=conf.FARX1
		FARY1=conf.FARY1
		FARZ1=conf.FARZ1
		FARXY1=conf.FARXY1
		RMAX1=conf.RMAX1
		TSUM=conf.TSUM
		XNEG=conf.XNEG
		YNEG=conf.YNEG
		ZNEG=conf.ZNEG
		EDELTA=conf.EDELTA
		EDELTA2=conf.EDELTA2
		NCLEXC=conf.NCLEXC
		NXPL10=conf.NXPL10
		NYPL10=conf.NYPL10
		NZPL10=conf.NZPL10
		NXPL40=conf.NXPL40
		NYPL40=conf.NYPL40
		NZPL40=conf.NZPL40
		NXPL100=conf.NXPL100
		NYPL100=conf.NYPL100
		NZPL100=conf.NZPL100
		NXPL400=conf.NXPL400
		NYPL400=conf.NYPL400
		NZPL400=conf.NZPL400
		NXPL1000=conf.NXPL1000
		NYPL1000=conf.NYPL1000
		NZPL1000=conf.NZPL1000
		NXPL2=conf.NXPL2
		NYPL2=conf.NYPL2
		NZPL2=conf.NZPL2
		NXPL4000=conf.NXPL4000
		NYPL4000=conf.NYPL4000
		NZPL4000=conf.NZPL4000
		NXPL10000=conf.NXPL10000
		NYPL10000=conf.NYPL10000
		NZPL10000=conf.NZPL10000
		NXPL40000=conf.NXPL40000
		NYPL40000=conf.NYPL40000
		NZPL40000=conf.NZPL40000
		NXPL100000=conf.NXPL100000
		NYPL100000=conf.NYPL100000
		NZPL100000=conf.NZPL100000
		NRPL2=conf.NRPL2
		NRPL10=conf.NRPL10
		NRPL40=conf.NRPL40
		NRPL100=conf.NRPL100
		NRPL400=conf.NRPL400
		NRPL1000=conf.NRPL1000
		NRPL4000=conf.NRPL4000
		NRPL10000=conf.NRPL10000
		NRPL40000=conf.NRPL40000
		NRPL100000=conf.NRPL100000
		NEPL1=conf.NEPL1
		NEPL10=conf.NEPL10
		NEPL100=conf.NEPL100
		MELEC=conf.MELEC
		MELEC3=conf.MELEC3
		MELEC10=conf.MELEC10
		MELEC30=conf.MELEC30
		MELEC100=conf.MELEC100
		MELEC300=conf.MELEC300
		globals().update(locals())
	get_globals()
	def update_globals():
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
		conf.IWRITE  =IWRITE  
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
		conf.MSUM=MSUM
		conf.MCOMP=MCOMP
		conf.MRAYL=MRAYL
		conf.MPAIR=MPAIR
		conf.MPHOT=MPHOT
		conf.MVAC=MVAC
		conf.XST=XST
		conf.YST=YST
		conf.ZST=ZST
		conf.TIME=TIME
		conf.TTIME=TTIME
		conf.NFGF=NFGF
		conf.NFGPP=NFGPP
		conf.NFGBR=NFGBR
		conf.NELEC=NELEC
		conf.NEGION=NEGION
		conf.EST1=EST1
		conf.EST2=EST2
		conf.XSTEXC=XSTEXC
		conf.YSTEXC=YSTEXC
		conf.ZSTEXC=ZSTEXC
		conf.TSTEXC=TSTEXC
		conf.NSTEXC=NSTEXC
		conf.XSTN=XSTN
		conf.YSTN=YSTN
		conf.ZSTN=ZSTN
		conf.TSTN=TSTN
		conf.IDNUL=IDNUL
		conf.NEXCNUL=NEXCNUL
		conf.XAV=XAV
		conf.YAV=YAV
		conf.ZAV=ZAV
		conf.TAV=TAV
		conf.XYAV=XYAV
		conf.XYZAV=XYZAV
		conf.DX=DX
		conf.DY=DY
		conf.DZ=DZ
		conf.DT=DT
		conf.DXY=DXY
		conf.DXYZ=DXYZ
		conf.NCL=NCL
		conf.FARX1=FARX1
		conf.FARY1=FARY1
		conf.FARZ1=FARZ1
		conf.FARXY1=FARXY1
		conf.RMAX1=RMAX1
		conf.TSUM=TSUM
		conf.XNEG=XNEG
		conf.YNEG=YNEG
		conf.ZNEG=ZNEG
		conf.EDELTA=EDELTA
		conf.EDELTA2=EDELTA2
		conf.NCLEXC=NCLEXC
		conf.NXPL10=NXPL10
		conf.NYPL10=NYPL10
		conf.NZPL10=NZPL10
		conf.NXPL40=NXPL40
		conf.NYPL40=NYPL40
		conf.NZPL40=NZPL40
		conf.NXPL100=NXPL100
		conf.NYPL100=NYPL100
		conf.NZPL100=NZPL100
		conf.NXPL400=NXPL400
		conf.NYPL400=NYPL400
		conf.NZPL400=NZPL400
		conf.NXPL1000=NXPL1000
		conf.NYPL1000=NYPL1000
		conf.NZPL1000=NZPL1000
		conf.NXPL2=NXPL2
		conf.NYPL2=NYPL2
		conf.NZPL2=NZPL2
		conf.NXPL4000=NXPL4000
		conf.NYPL4000=NYPL4000
		conf.NZPL4000=NZPL4000
		conf.NXPL10000=NXPL10000
		conf.NYPL10000=NYPL10000
		conf.NZPL10000=NZPL10000
		conf.NXPL40000=NXPL40000
		conf.NYPL40000=NYPL40000
		conf.NZPL40000=NZPL40000
		conf.NXPL100000=NXPL100000
		conf.NYPL100000=NYPL100000
		conf.NZPL100000=NZPL100000
		conf.NRPL2=NRPL2
		conf.NRPL10=NRPL10
		conf.NRPL40=NRPL40
		conf.NRPL100=NRPL100
		conf.NRPL400=NRPL400
		conf.NRPL1000=NRPL1000
		conf.NRPL4000=NRPL4000
		conf.NRPL10000=NRPL10000
		conf.NRPL40000=NRPL40000
		conf.NRPL100000=NRPL100000
		conf.NEPL1=NEPL1
		conf.NEPL10=NEPL10
		conf.NEPL100=NEPL100
		conf.MELEC=MELEC
		conf.MELEC3=MELEC3
		conf.MELEC10=MELEC10
		conf.MELEC30=MELEC30
		conf.MELEC100=MELEC100
		conf.MELEC300=MELEC300    	
	#-----------------------------------------------------------------------
	#  NEVENT IS EVENT EVENT POINTER. NGOOD IS GOOD EVENT POINTER
	#  FORMS AVERAGES OVER EACH DELTA AND DOES SOME STATISTICS
	#  LOADS PLOT ARRAYS XPLOT YPLOT AND ZPLOT (SCALED BY 1 10 AND 100)
	#  OUTPUTS RAW DATA TO FILE IF IWRITE CONTROL GT  0
	#  OUTPUTS THERMALISED ELECTRON X,Y,Z AND T IF  IWRITE EQ 1
	#  OUTPUTS ALSO X,Y,Z AND T FOR EACH  EXCITATION IF 
	#  IWRITE EQ 2        
	# ----------------------------------------------------------------------
	if(NGOOD <= 0):
		print(' IN STATS NEVENT=',NEVENT,' NGOOD=',NGOOD)
	# endif
	NCLUS=NELEC-NEGION
	if(NCLUS > 150000):
		# GO TO 99
		pass
	else:
		SUMX=0.00
		SUMX2=0.00
		SUMY=0.00
		SUMY2=0.00
		SUMZ=0.00
		SUMZ2=0.00
		SUMRXY=0.00
		SUMRXY2=0.00
		SUMRXYZ=0.00
		SUMRXYZ2=0.00
		SUMT=0.00
		SUMT2=0.00
		FARX=0.00
		FARY=0.00
		FARZ=0.00
		FARXY=0.00
		RMAX=0.00
		SUMTT=0.00
		NXNEG=0
		NYNEG=0
		NZNEG=0
		ESUM=0.0
		ATOTR=0.0
		ATOTC=0.0
		ATOTP=0.0
		ATOTPE=0.0
		#
		for IS in range(1,int(NCLUS)+1):
			XST[IS]=XST[IS]*1.e6
			X=XST[IS]
			if(X < 0.0):
				NXNEG=NXNEG+1
				I1=int(X/2.0-0.5)
				I2=int(X/10.0-0.5)
				I3=int(X/40.0-0.5)
				I4=int(X/100.0-0.5)
				I5=int(X/400.0-0.5)
				I6=int(X/1000.0-0.5)
				I7=int(X/4000.0-0.5)
				I8=int(X/10000.0-0.5)
				I9=int(X/40000.0-0.5)
				I10=int(X/100000.0-0.5)
			else: 
				I1=int(X/2.0+0.5)
				I2=int(X/10.0+0.5)
				I3=int(X/40.0+0.5)
				I4=int(X/100.0+0.5)
				I5=int(X/400.0+0.5)
				I6=int(X/1000.0+0.5)
				I7=int(X/4000.0+0.5) 
				I8=int(X/10000.0+0.5)
				I9=int(X/40000.0+0.5)
				I10=int(X/100000.0+0.5)
			# endif
			I1=I1+16
			I2=I2+16
			I3=I3+16
			I4=I4+16
			I5=I5+16
			I6=I6+16
			I7=I7+16
			I8=I8+16
			I9=I9+16
			I10=I10+16
			if(I1 < 1):
				I1=1
			if(I1 > 31):
				I1=31
			if(I2 < 1):
				I2=1
			if(I2 > 31):
				I2=31
			if(I3 < 1):
				I3=1
			if(I3 > 31):
				I3=31
			if(I4 < 1):
				I4=1
			if(I4 > 31):
				I4=31
			if(I5 < 1):
				I5=1
			if(I5 > 31):
				I5=31
			if(I6 < 1):
				I6=1
			if(I6 > 31):
				I6=31
			if(I7 < 1):
				I7=1
			if(I7 > 31):
				I7=31
			if(I8 < 1):
				I8=1
			if(I8 > 31):
				I8=31
			if(I9 < 1):
				I9=1
			if(I9 > 31):
				I9=31
			if(I10 < 1):
				I10=1
			if(I10 > 31):
				I10=31
			NXPL2[I1]=NXPL2[I1]+1
			NXPL10[I2]=NXPL10[I2]+1
			NXPL40[I3]=NXPL40[I3]+1
			NXPL100[I4]=NXPL100[I4]+1
			NXPL400[I5]=NXPL400[I5]+1
			NXPL1000[I6]=NXPL1000[I6]+1
			NXPL4000[I7]=NXPL4000[I7]+1
			NXPL10000[I8]=NXPL10000[I8]+1
			NXPL40000[I9]=NXPL40000[I9]+1
			NXPL100000[I10]=NXPL100000[I10]+1
			X2=X*X
			SUMX=SUMX+X
			SUMX2=SUMX2+X2
			if(abs(X)> abs(FARX)):
				FARX=abs(X)
			YST[IS]=YST[IS]*1.e6
			Y=YST[IS]
			if(Y < 0.0):
				NYNEG=NYNEG+1
				I1=int(Y/2.0-0.5)
				I2=int(Y/10.0-0.5)
				I3=int(Y/40.0-0.5)
				I4=int(Y/100.0-0.5)
				I5=int(Y/400.0-0.5)
				I6=int(Y/1000.0-0.5)
				I7=int(Y/4000.0-0.5)
				I8=int(Y/10000.0-0.5)
				I9=int(Y/40000.0-0.5)
				I10=int(Y/100000.0-0.5)
			else: 
				I1=int(Y/2.0+0.5)
				I2=int(Y/10.0+0.5)
				I3=int(Y/40.0+0.5)
				I4=int(Y/100.0+0.5)
				I5=int(Y/400.0+0.5)
				I6=int(Y/1000.0+0.5)
				I7=int(Y/4000.0+0.5) 
				I8=int(Y/10000.0+0.5)
				I9=int(Y/40000.0+0.5)
				I10=int(Y/100000.0+0.5)
			# endif
			I1=I1+16
			I2=I2+16
			I3=I3+16
			I4=I4+16
			I5=I5+16
			I6=I6+16
			I7=I7+16
			I8=I8+16
			I9=I9+16
			I10=I10+16
			if(I1 < 1):
				I1=1
			if(I1 > 31):
				I1=31
			if(I2 < 1):
				I2=1
			if(I2 > 31):
				I2=31
			if(I3 < 1):
				I3=1
			if(I3 > 31):
				I3=31
			if(I4 < 1):
				I4=1
			if(I4 > 31):
				I4=31
			if(I5 < 1):
				I5=1
			if(I5 > 31):
				I5=31
			if(I6 < 1):
				I6=1
			if(I6 > 31):
				I6=31
			if(I7 < 1):
				I7=1
			if(I7 > 31):
				I7=31
			if(I8 < 1):
				I8=1
			if(I8 > 31):
				I8=31
			if(I9 < 1):
				I9=1
			if(I9 > 31):
				I9=31
			if(I10 < 1):
				I10=1
			if(I10 > 31):
				I10=31
			NYPL2[I1]=NYPL2[I1]+1
			NYPL10[I2]=NYPL10[I2]+1
			NYPL40[I3]=NYPL40[I3]+1
			NYPL100[I4]=NYPL100[I4]+1
			NYPL400[I5]=NYPL400[I5]+1
			NYPL1000[I6]=NYPL1000[I6]+1
			NYPL4000[I7]=NYPL4000[I7]+1
			NYPL10000[I8]=NYPL10000[I8]+1
			NYPL40000[I9]=NYPL40000[I9]+1
			NYPL100000[I10]=NYPL100000[I10]+1
			Y2=Y*Y
			SUMY=SUMY+Y
			SUMY2=SUMY2+Y2 
			if(abs(Y)> abs(FARY)):
				FARY=abs(Y)
			ZST[IS]=ZST[IS]*1.e6
			Z=ZST[IS]
			if(Z < 0.0):
				NZNEG=NZNEG+1
				I1=int(Z/2.0-0.5)
				I2=int(Z/10.0-0.5)
				I3=int(Z/40.0-0.5)
				I4=int(Z/100.0-0.5)
				I5=int(Z/400.0-0.5)
				I6=int(Z/1000.0-0.5)
				I7=int(Z/4000.0-0.5)
				I8=int(Z/10000.0-0.5)
				I9=int(Z/40000.0-0.5)
				I10=int(Z/100000.0-0.5)
			else: 
				I1=int(Z/2.0+0.5)
				I2=int(Z/10.0+0.5)
				I3=int(Z/40.0+0.5)
				I4=int(Z/100.0+0.5)
				I5=int(Z/400.0+0.5) 
				I6=int(Z/1000.0+0.5)
				I7=int(Z/4000.0+0.5)
				I8=int(Z/10000.0+0.5)
				I9=int(Z/40000.0+0.5)
				I10=int(Z/100000.0+0.5)
			# endif
			I1=I1+16
			I2=I2+16
			I3=I3+16
			I4=I4+16
			I5=I5+16
			I6=I6+16
			I7=I7+16
			I8=I8+16
			I9=I9+16
			I10=I10+16
			if(I1 < 1):
				I1=1
			if(I1 > 31):
				I1=31
			if(I2 < 1):
				I2=1
			if(I2 > 31):
				I2=31
			if(I3 < 1):
				I3=1
			if(I3 > 31):
				I3=31
			if(I4 < 1):
				I4=1
			if(I4 > 31):
				I4=31
			if(I5 < 1):
				I5=1
			if(I5 > 31):
				I5=31
			if(I6 < 1):
				I6=1
			if(I6 > 31):
				I6=31
			if(I7 < 1):
				I7=1
			if(I7 > 31):
				I7=31
			if(I8 < 1):
				I8=1
			if(I8 > 31):
				I8=31
			if(I9 < 1):
				I9=1
			if(I9 > 31):
				I9=31
			if(I10 < 1):
				I10=1
			if(I10 > 31):
				I10=31
			NZPL2[I1]=NZPL2[I1]+1
			NZPL10[I2]=NZPL10[I2]+1
			NZPL40[I3]=NZPL40[I3]+1
			NZPL100[I4]=NZPL100[I4]+1
			NZPL400[I5]=NZPL400[I5]+1
			NZPL1000[I6]=NZPL1000[I6]+1
			NZPL4000[I7]=NZPL4000[I7]+1
			NZPL10000[I8]=NZPL10000[I8]+1
			NZPL40000[I9]=NZPL40000[I9]+1
			NZPL100000[I10]=NZPL100000[I10]+1
			Z=ZST[IS]
			R=math.sqrt(X*X+Y*Y+Z*Z)
			I1=int(R/2.0+0.5)
			I2=int(R/10.0+0.5)
			I3=int(R/40.0+0.5)
			I4=int(R/100.0+0.5)
			I5=int(R/400.0+0.5) 
			I6=int(R/1000.0+0.5)
			I7=int(R/4000.0+0.5)
			I8=int(R/10000.0+0.5)
			I9=int(R/40000.0+0.5)
			I10=int(R/100000.0+0.5)
			I1=I1+16
			I2=I2+16
			I3=I3+16
			I4=I4+16
			I5=I5+16
			I6=I6+16
			I7=I7+16
			I8=I8+16
			I9=I9+16
			I10=I10+16
			if(I1 > 31):
				I1=31
			if(I2 > 31):
				I2=31
			if(I3 > 31):
				I3=31
			if(I4 > 31):
				I4=31
			if(I5 > 31):
				I5=31
			if(I6 > 31):
				I6=31
			if(I7 > 31):
				I7=31
			if(I8 > 31):
				I8=31
			if(I9 > 31):
				I9=31
			if(I10 > 31):
				I10=31
			if(I1 < 1):
				I1=1
			if(I2 < 1):
				I2=1
			if(I3 < 1):
				I3=1
			if(I4 < 1):
				I4=1
			if(I5 < 1):
				I5=1
			if(I6 < 1):
				I6=1
			if(I7 < 1):
				I7=1
			if(I8 < 1):
				I8=1
			if(I9 < 1):
				I9=1
			if(I10 < 1):
				I10=1
			NRPL2[I1]=NRPL2[I1]+1
			NRPL10[I2]=NRPL10[I2]+1
			NRPL40[I3]=NRPL40[I3]+1
			NRPL100[I4]=NRPL100[I4]+1
			NRPL400[I5]=NRPL400[I5]+1
			NRPL1000[I6]=NRPL1000[I6]+1
			NRPL4000[I7]=NRPL4000[I7]+1
			NRPL10000[I8]=NRPL10000[I8]+1
			NRPL40000[I9]=NRPL40000[I9]+1
			NRPL100000[I10]=NRPL100000[I10]+1
			Z2=Z*Z
			SUMZ=SUMZ+Z
			SUMZ2=SUMZ2+Z2 
			if(abs(Z)> abs(FARZ)):
				FARZ=abs(Z)
			RXY=math.sqrt(X2+Y2)
			RXYZ=math.sqrt(X2+Y2+Z2)
			SUMRXY=SUMRXY+RXY
			SUMRXY2=SUMRXY2+RXY*2 
			SUMRXYZ=SUMRXYZ+RXYZ
			SUMRXYZ2=SUMRXYZ2+RXYZ*2
			if(RXY > FARXY):
				FARXY=RXY
			if(RXYZ > RMAX):
				RMAX=RXYZ   
			T=TIME[IS]
			SUMT=SUMT+T 
			SUMT2=SUMT2+T*T
			SUMTT=SUMTT+TTIME(IS)
			#
			XSTEXC[IS]=XSTEXC[IS]*1.e6
			YSTEXC[IS]=YSTEXC[IS]*1.e6
			ZSTEXC[IS]=ZSTEXC[IS]*1.e6
		# 400 CONTINUE
		# OUTPUT THERMAL ELECTRON POSITIONS AND TIME 
		f=open("fort.50","w+")
		if(IWRITE == 1):
			#      ITEST=123456
			#      WRITE(50,*) ITEST
			# WRITE(50,*) 
			f.write(NGOOD,NCLUS,NSTEXC,NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,MCOMP[NEVENT],MPAIR[NEVENT],NEXCNUL)
			#      DO 8876 IPR=1,NCLUS
			#      WRITE(50,*) IPR,XST[IPR],YST[IPR],ZST[IPR],TIME[IPR],NFGF[IPR],
			#    /NFGPP[IPR],NFGBR[IPR]
			#8876 CONTINUE
			# WRITE(50,*) 
			for IPR in range(1,NCLUS+1):

				f.write(XST[IPR],YST[IPR],ZST[IPR],TIME[IPR],NFGF[IPR],NFGPP[IPR],NFGBR[IPR])
		# endif
		# OUTPUT EXCITATION CLOUD COORDINATES HERE  
		if(IWRITE == 2):
			#      ITEST=123456
			#      WRITE(50,*) ITEST
			# WRITE(50,*) 
			f.write(NGOOD,NCLUS,NSTEXC,NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,MCOMP[NEVENT],MPAIR[NEVENT],NEXCNUL)
			#      DO 8877 IPR=1,NCLUS
			#      WRITE(50,*) IPR,XST[IPR],YST[IPR],ZST[IPR],TIME[IPR],NFGF[IPR],
			#    /NFGPP[IPR],NFGBR[IPR]
			#8877 CONTINUE
			# WRITE(50,*) 
			for IPR in range(1,NCLUS+1):
				f.write(XST[IPR],YST[IPR],ZST[IPR],TIME[IPR],NFGF[IPR],NFGPP[IPR],NFGBR[IPR])
			#       DO 8878 IPR=1,NSTEXC
			#       WRITE(50,*) IPR,XSTEXC[IPR],YSTEXC[IPR],ZSTEXC[IPR],TSTEXC[IPR]
			# 8878 CONTINUE
			# WRITE(50,*) 
			for IPR in range(1,NSTEXC+1):
				f.write(XSTEXC[IPR],YSTEXC[IPR],ZSTEXC[IPR],TSTEXC[IPR])
			if(NEXCNUL > 0):
				# WRITE(50,*) 
				for IPR in range(1,NEXCNUL+1):
					f.write(XSTN[IPR],YSTN[IPR],ZSTN[IPR],TSTN[IPR],IDNUL[IPR])
			else:
				# WRITE BLANK LINE
				# WRITE(50,*) 
				f.write(0.0,0.0,0.0,0.0,0 )
			# endif      
		# endif
		f.close()
		#---------------------------------------------------
		I1=int(EST1+1.0)
		I2=int(EST1/10.0+1.0)
		I3=int(EST1/100.0+1.0)
		if(I1 > 100):
			I1=100
		if(I2 > 100):
			I2=100
		if(I3 > 100):
			I3=100
		NEPL1[I1]=NEPL1[I1]+1
		NEPL10[I2]=NEPL10[I2]+1
		NEPL100[I3]=NEPL100[I3]+1
		KDUM=NELEC
		KDUM3=1+(NELEC/3)
		KDUM10=1+(NELEC/10)
		KDUM30=1+(NELEC/30)
		KDUM100=1+(NELEC/100)
		KDUM300=1+(NELEC/300)
		if(KDUM > 1000):
			KDUM=1000
		MELEC[int(KDUM)]=MELEC[int(KDUM)]+1
		if(KDUM3 > 1000):
			KDUM3=1000
		MELEC3[int(KDUM3)]=MELEC3[int(KDUM3)]+1
		if(KDUM10 > 1000):
			KDUM10=1000
		MELEC10[int(KDUM10)]=MELEC10[int(KDUM10)]+1
		if(KDUM30 > 1000):
			KDUM30=1000
		MELEC30[int(KDUM30)]=MELEC30[int(KDUM30)]+1
		if(KDUM100 > 1000):
			KDUM100=1000
		MELEC100[int(KDUM100)]=MELEC100[int(KDUM100)]+1
		if(KDUM300 > 1000):
			KDUM300=1000
		MELEC300[int(KDUM300)]=MELEC300[int(KDUM300)]+1
		# 
		# STORE AVERAGES AND WIDTHS FOR EACH DELTA
		#
		if(NCLUS == 0):
			return
		ACLUS=float(NCLUS)
		XAV[NGOOD]=SUMX/ACLUS
		YAV[NGOOD]=SUMY/ACLUS
		ZAV[NGOOD]=SUMZ/ACLUS
		TAV[NGOOD]=SUMT/ACLUS
		XYAV[NGOOD]=SUMRXY/ACLUS
		XYZAV[NGOOD]=SUMRXYZ/ACLUS
		#  IONISATION CLUSTER SIZE
		NCL[NGOOD]=NCLUS
		# EXCITATION CLUSTER SIZE
		NCLEXC[NGOOD]=NSTEXC
		#
		FARX1[NGOOD]=FARX
		FARY1[NGOOD]=FARY
		FARZ1[NGOOD]=FARZ
		FARXY1[NGOOD]=FARXY
		RMAX1[NGOOD]=RMAX
		TSUM[NGOOD]=SUMTT
		XNEG[NGOOD]=float(NXNEG)/ACLUS
		YNEG[NGOOD]=float(NYNEG)/ACLUS
		ZNEG[NGOOD]=float(NZNEG)/ACLUS
		EDELTA[NGOOD]=EST1
		EDELTA2[NGOOD]=EST2
		if(NCLUS > 1):
			NC2=NCLUS*NCLUS-NCLUS
			ANC2=float(NC2)
			DX[NGOOD]=math.sqrt(abs((ACLUS*SUMX2-SUMX*SUMX)/ANC2))
			DY[NGOOD]=math.sqrt(abs((ACLUS*SUMY2-SUMY*SUMY)/ANC2))
			DZ[NGOOD]=math.sqrt(abs((ACLUS*SUMZ2-SUMZ*SUMZ)/ANC2))
			DT[NGOOD]=math.sqrt(abs((ACLUS*SUMT2-SUMT*SUMT)/ANC2))
			DXY[NGOOD]=math.sqrt(abs((ACLUS*SUMRXY2-SUMRXY*SUMRXY)/ANC2))
			DXYZ[NGOOD]=math.sqrt(abs((ACLUS*SUMRXYZ2-SUMRXYZ*SUMRXYZ)/ANC2))
		else:
			DX[NGOOD]=0.0
			DY[NGOOD]=0.0
			DZ[NGOOD]=0.0
			DZ[NGOOD]=0.0
			DT[NGOOD]=0.0
			DXY[NGOOD]=0.0
			DXYZ[NGOOD]=0.0
		# endif
		return
	# 99 WRITE(6,991) NCLUS
	# 991 
	print('\n\n\n WARNING OVERFLOW IN ARRAYS IN FUNCTION STATS. NCLUS =',NCLUS,' STOPPED: FUNCTION')
	sys.exit()
	# end