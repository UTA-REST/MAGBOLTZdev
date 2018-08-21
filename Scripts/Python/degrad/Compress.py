def COMPRESS(IDBG,ENSUM):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	# COMMON/PRIM4/MSUM1,MCOMP1,MRAYL1,MPAIR1,MPHOT1,MVAC1
	# COMMON/RESB/IONSM(10),IFLSM(10),ESTOR(10,28),EPHOT(10,28),X(10,28),Y(10,28),Z[10,28],DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	# COMMON/GENB1/IONF1(10),ESTF1(10,28),X1(10,28),Y1(10,28),Z1(10,28),DRX1(10,28),DRY1(10,28),DRZ1(10,28)
	# COMMON/GENB2/IONF2(10),ESTF2(10,28),X2(10,28),Y2(10,28),Z2(10,28),DRX2(10,28),DRY2(10,28),DRZ2(10,28)
	# COMMON/GENB3/IONF3(10),ESTF3(10,15),X3(10,15),Y3(10,15),Z3(10,15),DRX3(10,15),DRY3(10,15),DRZ3(10,15)
	# COMMON/GENB4/IONF4(10),ESTF4(10,12),X4(10,12),Y4(10,12),Z4(10,12),DRX4(10,12),DRY4(10,12),DRZ4(10,12)
	# COMMON/GENB5/IONF5(10),ESTF5(10,5),X5(10,5),Y5(10,5),Z5(10,5),DRX5(10,5),DRY5(10,5),DRZ5(10,5)
	# COMMON/INTHRMB1/NPTPE,ET(10,50),XT(10,50),YT(10,50),ZT(10,50),DRX(10,50),DRY(10,50),DRZ[10,50],NJFLR(10,50),IEVENTL(10) 
	# COMMON/PPSTRB/NPTP,EPPST[2],XPP[2],YPP[2],ZPP[2],DRXPP[2],DRYPP[2],DRZPP[2]
	#COMMON/INPT/
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	#COMMON/PRIM4/
	global MSUM1,MCOMP1,MRAYL1,MPAIR1,MPHOT1,MVAC1
	#COMMON/RESB/
	global IONSM#(10)
	global IFLSM#(10)
	global ESTOR#(10,28)
	global EPHOT#(10,28)
	global X#(10,28)
	global Y#(10,28)
	global Z#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	#COMMON/GENB1/
	global IONF1#(10)
	global ESTF1#(10,28)
	global X1#(10,28)
	global Y1#(10,28)
	global Z1#(10,28)
	global DRX1#(10,28)
	global DRY1#(10,28)
	global DRZ1#(10,28)
	#COMMON/GENB2/
	global IONF2#(10)
	global ESTF2#(10,28)
	global X2#(10,28)
	global Y2#(10,28)
	global Z2#(10,28)
	global DRX2#(10,28)
	global DRY2#(10,28)
	global DRZ2#(10,28)
	#COMMON/GENB3/
	global IONF3#(10)
	global ESTF3#(10,15)
	global X3#(10,15)
	global Y3#(10,15)
	global Z3#(10,15)
	global DRX3#(10,15)
	global DRY3#(10,15)
	global DRZ3#(10,15)
	#COMMON/GENB4/
	global IONF4#(10)
	global ESTF4#(10,12)
	global X4#(10,12)
	global Y4#(10,12)
	global Z4#(10,12)
	global DRX4#(10,12)
	global DRY4#(10,12)
	global DRZ4#(10,12)
	#COMMON/GENB5/
	global IONF5#(10)
	global ESTF5#(10,5)
	global X5#(10,5)
	global Y5#(10,5)
	global Z5#(10,5)
	global DRX5#(10,5)
	global DRY5#(10,5)
	global DRZ5#(10,5)
	#COMMON/INTHRMB1/
	global NPTPE
	global ET#(10,50)
	global XT#(10,50)
	global YT#(10,50)
	global ZT#(10,50)
	global DRX#(10,50)
	global DRY#(10,50)
	global DRZ#(10,50)
	global NJFLR#(10,50)
	global IEVENTL#(10) 
	#COMMON/PPSTRB/
	global NPTP
	global EPPST#(2)
	global XPP#(2)
	global YPP#(2)
	global ZPP#(2)
	global DRXPP#(2)
	global DRYPP#(2)
	global DRZPP#(2)
	#DIMENSION 
	ESTOT=[0 for x in range(10)]
	NPTPE=MVAC1
	for I in range(1,10+1):
		ESTOT[I]=0.0
	#     IF(IDBG == 1) :
	#     WRITE(6,66) MVAC1
	#  66 print(' IN COMPRESS MVAC1=',I4)
	#     DO 67 KK=1,MVAC1
	#     WRITE(6,68) IONSM(KK),IONF1(KK),IONF2(KK),IONF3(KK),IONF4(KK),
	#    /IONF5(KK)
	#  68 print(' IONSUM 0-5=',6I4)
	#     WRITE(6,69) (ESTOR(KK,KKK),KKK=1,28)
	#  69 print(' ESTOR=',4(7'%.4f' % ,/))
	#     WRITE(6,70) (ESTF1(KK,KKK),KKK=1,28)
	#  70 print(' ESTF1=',4(7'%.4f' % ,/))
	#  67 CONTINUE
	#     # endIF
	#      
	#  STORE CASCADE DATA INTO COMMON/INTHRMB1/
	for K in range(1,MVAC1+1):
		ITOT=IONSM[K]+IONF1[K]+IONF2[K]+IONF3[K]+IONF4[K]+IONF5[K]
		IEVENTL[K]=ITOT
		if(ITOT > 50):
			print(' NEVENT=',J,' ITOT OVERFLOW IN OUTPUTBC')
			sys.exit()       
		# endif
		# STORE EVENT FOR INPUT TO THERMALISATION
		for M in range(1,IONSM[K]+1):
			ET[K][M]=ESTOR[K][M]
			XT[K][M]=X[K][M]
			YT[K][M]=Y[K][M]
			ZT[K][M]=Z[K,M]
			DRX[K][M]=DRX0[K][M]
			DRY[K][M]=DRY0[K][M]
			DRZ[K,M]=DRZ0[K][M]
			NJFLR[K][M]=0
			ESTOT[K]=ESTOT[K]+ESTOR[K][M]
		if(IONF1[K]== 0):
			pass
		else:
			for M in range(1,IONF1[K]+1):
				M1=M+IONSM[K]
				ET[K][M1]=ESTF1[K][M]   
				XT[K][M1]=X1[K][M]
				YT[K][M1]=Y1[K][M]
				ZT[K][M1]=Z1[K][M]
				DRX[K][M1]=DRX1[K][M]
				DRY[K][M1]=DRY1[K][M]
				DRZ[K,M1]=DRZ1[K][M]
				ESTOT[K]=ESTOT[K]+ESTF1[K][M]
				NJFLR[K][M1]=1
		if(IONF2[K] == 0):
			pass
		else:
			for M in range(1,IONF2[K]+1):
				M2=M+IONSM[K]+IONF1[K]
				ET[K][M2]=ESTF2[K][M]
				XT[K][M2]=X2[K][M]
				YT[K][M2]=Y2[K][M]
				ZT[K][M2]=Z2[K][M]
				DRX[K][M2]=DRX2[K][M]
				DRY[K][M2]=DRY2[K][M]
				DRZ[K,M2]=DRZ2[K][M]
				ESTOT[K]=ESTOT[K]+ESTF2[K][M]
				NJFLR[K][M2]=2
		if(IONF3[K] == 0):
			pass
		else:
			for M in range(1,IONF3[K]+1):
				M3=M+IONSM[K]+IONF1[K]+IONF2[K]
				ET[K][M3]=ESTF3[K][M]
				XT[K][M3]=X3[K][M]
				YT[K][M3]=Y3[K][M]
				ZT[K][M3]=Z3[K][M]
				DRX[K][M3]=DRX3[K][M]
				DRY[K][M3]=DRY3[K][M]
				DRZ[K,M3]=DRZ3[K][M]
				ESTOT[K]=ESTOT[K]+ESTF3[K][M]
				NJFLR[K][M3]=3
		if(IONF4[K] == 0):
			pass
		else:
			for M in range(1,IONF4[K]+1):
				M4=M+IONSM[K]+IONF1[K]+IONF2[K]+IONF3[K]
				ET[K][M4]=ESTF4[K][M]
				XT[K][M4]=X4[K][M]
				YT[K][M4]=Y4[K][M]
				ZT[K][M4]=Z4[K][M]
				DRX[K][M4]=DRX4[K][M]
				DRY[K][M4]=DRY4[K][M]
				DRZ[K,M4]=DRZ4[K][M]
				ESTOT[K]=ESTOT[K]+ESTF4[K][M]
				NJFLR[K][M4]=4
		if(IONF5[K] == 0):
			pass
		else:
			for M in range(1,IONF5[K]+1):
				M5=M+IONSM[K]+IONF1[K]+IONF2[K]+IONF3[K]+IONF4[K]
				ET[K][M5]=ESTF5[K][M]
				XT[K][M5]=X5[K][M]
				YT[K][M5]=Y5[K][M]
				ZT[K][M5]=Z5[K][M]
				DRX[K][M5]=DRX5[K][M]
				DRY[K][M5]=DRY5[K][M]
				DRZ[K,M5]=DRZ5[K][M]
				ESTOT[K]=ESTOT[K]+ESTF5[K][M]
				NJFLR[K][M5]=5
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
		EDUM=0.0
	for K in range(1,MVAC1+1):
		EDUM=EDUM+ESTOT[K]
	EDUM=EDUM+EPPST[1]+EPPST[2]
	ENSUM=EDUM
	if(EDUM > (EFINAL+0.1)):
		print(' ETOT =','%.5f' % EDUM,'EV.    BAD EVENT IN COMPRESS\n')
		IBAD=1
		sys.exit()
	# endif
	return     
	# end         