def CASCADEE(J11,KGAS,LGAS,X0,Y0,Z0,T0,EINIT,ISHELL):
	# IMPLICIT #real*8(A-H,O-Z)
	# IMPLICIT #integer*8(I-N)
	# CHARACTER*6 SCR(17),SCR1(17)
	# COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	# COMMON/GENCAS/ELEV[17,79],NSDEG(17),AA[17],BB[17],SCR,SCR1
	# COMMON/MIXC/PRSH(6,3,17,17),ESH(6,3,17),AUG(6,3,17,17,17),RAD[6,3,17,17],PRSHBT(6,3,17),IZ[6,3],INIOCC(6,3,17),ISHLMX(6,3),AMZ[6,3]
	# COMMON/UPD/NOCC(6,3,17),AUGR(6,3,17,17,17),RADR(6,3,17,17)
	# COMMON/CALCASE/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	# COMMON/CALCAS1E/IONSUM1(10),IFLSUM1(10),ESTOR1(10,28),EPHOTG1(10,28),DRXE1(10,28),DRYE1(10,28),DRZE1(10,28),DRX1(10,28),DRY1(10,28),DRZ1(10,28)
	# COMMON/CALCAS2E/IONSUM2(10),IFLSUM2(10),ESTOR2(10,28),EPHOTG2(10,28),DRXE2(10,28),DRYE2(10,28),DRZE2(10,28),DRX2(10,28),DRY2(10,28),DRZ2(10,28)
	# COMMON/CALCAS3E/IONSUM3(10),IFLSUM3(10),ESTOR3(10,28),EPHOTG3(10,28),DRXE3(10,28),DRYE3(10,28),DRZE3(10,28),DRX3(10,28),DRY3(10,28),DRZ3(10,28)
	# COMMON/CALCAS4E/IONSUM4(10),IFLSUM4(10),ESTOR4(10,28),EPHOTG4(10,28),DRXE4(10,28),DRYE4(10,28),DRZE4(10,28),DRX4(10,28),DRY4(10,28),DRZ4(10,28)
	# COMMON/CALCAS5E/IONSUM5(10),IFLSUM5(10),ESTOR5(10,28),EPHOTG5(10,28),DRXE5(10,28),DRYE5(10,28),DRZE5(10,28),DRX5(10,28),DRY5(10,28),DRZ5(10,28)
	# COMMON/RESE/IONSM(10),IFLSM(10),ESTOR(10,28),EPHOT(10,28),XN(10,28),YN(10,28),ZN(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28),TN(10,28)
	# COMMON/GENE1/IONF1(10),ESTF1(10,28),X1(10,28),Y1(10,28),Z1(10,28),DRXS1(10,28),DRYS1(10,28),DRZS1(10,28),T1(10,28)
	# COMMON/GENE2/IONF2(10),ESTF2(10,28),X2(10,28),Y2(10,28),Z2(10,28),DRXS2(10,28),DRYS2(10,28),DRZS2(10,28),T2(10,28)
	# COMMON/GENE3/IONF3(10),ESTF3(10,15),X3(10,15),Y3(10,15),Z3(10,15),DRXS3(10,15),DRYS3(10,15),DRZS3(10,15),T3(10,15)
	# COMMON/GENE4/IONF4(10),ESTF4(10,12),X4(10,12),Y4(10,12),Z4(10,12),DRXS4(10,12),DRYS4(10,12),DRZS4(10,12),T4(10,12)
	# COMMON/GENE5/IONF5(10),ESTF5(10,5),X5(10,5),Y5(10,5),Z5(10,5),DRXS5(10,5),DRYS5(10,5),DRZS5(10,5),T5(10,5)
	#COMMON/COMP/
	global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	#COMMON/GENCAS/
	global ELEV#(17,79)
	global NSDEG#(17)
	global AA#(17)
	global BB#(17)
	global SCR,SCR1
	#COMMON/MIXC/
	global PRSH#(6,3,17,17)
	global ESH#(6,3,17)
	global AUG#(6,3,17,17,17)
	global RAD#(6,3,17,17)
	global PRSHBT#(6,3,17)
	global IZ#(6,3)
	global INIOCC#(6,3,17)
	global ISHLMX#(6,3)
	global AMZ#(6,3)
	#COMMON/UPD/
	global NOCC#(6,3,17)
	global AUGR#(6,3,17,17,17)
	global RADR#(6,3,17,17)
	#COMMON/CALCASE/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#(10,28)
	#COMMON/CALCAS1E/
	global IONSUM1#(10)
	global IFLSUM1#(10)
	global ESTOR1#(10,28)
	global EPHOTG1#(10,28)
	global DRXE1#(10,28)
	global DRYE1#(10,28)
	global DRZE1#(10,28)
	global DRX1#(10,28)
	global DRY1#(10,28)
	global DRZ1#(10,28)
	#COMMON/CALCAS2E/
	global IONSUM2#(10)
	global IFLSUM2#(10)
	global ESTOR2#(10,28)
	global EPHOTG2#(10,28)
	global DRXE2#(10,28)
	global DRYE2#(10,28)
	global DRZE2#(10,28)
	global DRX2#(10,28)
	global DRY2#(10,28)
	global DRZ2#(10,28)
	#COMMON/CALCAS3E/
	global IONSUM3#(10)
	global IFLSUM3#(10)
	global ESTOR3#(10,28)
	global EPHOTG3#(10,28)
	global DRXE3#(10,28)
	global DRYE3#(10,28)
	global DRZE3#(10,28)
	global DRX3#(10,28)
	global DRY3#(10,28)
	global DRZ3#(10,28)
	#COMMON/CALCAS4E/
	global IONSUM4#(10)
	global IFLSUM4#(10)
	global ESTOR4#(10,28)
	global EPHOTG4#(10,28)
	global DRXE4#(10,28)
	global DRYE4#(10,28)
	global DRZE4#(10,28)
	global DRX4#(10,28)
	global DRY4#(10,28)
	global DRZ4#(10,28)
	#COMMON/CALCAS5E/
	global IONSUM5#(10)
	global IFLSUM5#(10)
	global ESTOR5#(10,28)
	global EPHOTG5#(10,28)
	global DRXE5#(10,28)
	global DRYE5#(10,28)
	global DRZE5#(10,28)
	global DRX5#(10,28)
	global DRY5#(10,28)
	global DRZ5#(10,28)
	#COMMON/RESE/
	global IONSM#(10)
	global IFLSM#(10)
	global ESTOR#(10,28)
	global EPHOT#(10,28)
	global XN#(10,28)
	global YN#(10,28)
	global ZN#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	global TN#(10,28)
	#COMMON/GENE1/
	global IONF1#(10)
	global ESTF1#(10,28)
	global X1#(10,28)
	global Y1#(10,28)
	global Z1#(10,28)
	global DRXS1#(10,28)
	global DRYS1#(10,28)
	global DRZS1#(10,28)
	global T1#(10,28)
	#COMMON/GENE2/
	global IONF2#(10)
	global ESTF2#(10,28)
	global X2#(10,28)
	global Y2#(10,28)
	global Z2#(10,28)
	global DRXS2#(10,28)
	global DRYS2#(10,28)
	global DRZS2#(10,28)
	global T2#(10,28)
	#COMMON/GENE3/
	global IONF3#(10)
	global ESTF3#(10,15)
	global X3#(10,15)
	global Y3#(10,15)
	global Z3#(10,15)
	global DRXS3#(10,15)
	global DRYS3#(10,15)
	global DRZS3#(10,15)
	global T3#(10,15)
	#COMMON/GENE4/
	global IONF4#(10)
	global ESTF4#(10,12)
	global X4#(10,12)
	global Y4#(10,12)
	global Z4#(10,12)
	global DRXS4#(10,12)
	global DRYS4#(10,12)
	global DRZS4#(10,12)
	global T4#(10,12)
	#COMMON/GENE5/
	global IONF5#(10)
	global ESTF5#(10,5)
	global X5#(10,5)
	global Y5#(10,5)
	global Z5#(10,5)
	global DRXS5#(10,5)
	global DRYS5#(10,5)
	global DRZS5#(10,5)
	global T5#(10,5)

	#     COMMON/NSIZE/NJHIGH
	#----------------------------------------------------------------------
	# CALCULATE CASCADE FROM A VACANCY= ISHELL  IN KGAS LGAS 
	# ENERGY OF ESCAPE ELECTRON FROM VACANCY =EINIT ( NEEDED FOR SHAKE OFF)
	# ESCAPE ELECTRON NOT INCLUDED IN CASCADE SUM
	#----------------------------------------------------------------------
	#   SET OR ZERO SOME VARIABLES 
	#----------------------------------------------------------------------
	#     WRITE(6,77) J11,KGAS,LGAS,X0,Y0,Z0,T0,EINIT,ISHELL
	KGASST=KGAS
	LGASST=LGAS
	EINITST=EINIT
	ISHELLST=ISHELL
	def GOTO10():  
		API=numpy.arccos(-1.00)
		NJHIGH=0
		KGAS=KGASST
		LGAS=LGASST
		EINIT=EINITST
		ISHELL=ISHELLST
		#  
		# ZERO SOME ARRAYS
		for K in range(1,10):
			for J in range(1,28):
				EPHOTON[K][J]=0.0
				EPHOTG1[K][J]=0.0
				EPHOTG2[K][J]=0.0
				EPHOTG3[K][J]=0.0
				EPHOTG4[K][J]=0.0
				EPHOTG5[K][J]=0.0
				ESTORE[K][J]=0.0
				ESTOR1[K][J]=0.0
				ESTOR2[K][J]=0.0
				ESTOR3[K][J]=0.0
				ESTOR4[K][J]=0.0
				ESTOR5[K][J]=0.0
				ESTOR[K][J]=0.0
				ESTF1[K][J]=0.0
				ESTF2[K][J]=0.0
			IFLSUM[K]=0
			IFLSUM1[K]=0
			IFLSUM2[K]=0
			IFLSUM3[K]=0
			IFLSUM4[K]=0
			IFLSUM5[K]=0
			IONSUM[K]=0
			IONSUM1[K]=0
			IONSUM2[K]=0
			IONSUM3[K]=0
			IONSUM4[K]=0
			IONSUM5[K]=0
			IONSM[K]=0
			IONF1[K]=0
			IONF2[K]=0
			IONF3[K]=0
			IONF4[K]=0
			IONF5[K]=0
		# INITIAL ENERGY IN SHELL
		ESHSTART=ELEV[ISHELL,IZ[KGAS][LGAS]]   
		# LOOP OVER SHELL VACANCIES
		CONTROLE(KGAS,LGAS,X0,Y0,Z0,T0,EINIT,ISHELL)
		# COMPRESS AUGER AND FLUORESCENCE DATA INTO BLOCKS
		COMPRESSE(ETOT)
		#  REPEAT FOR POSSIBLE K-SHELLROUNDING ERROR
		if((ESHSTART-ETOT)> 2200.):
			GOTO10()
		# LOAD INTO COMMON/CASRSE/
		CASRESE()
		#     WRITE(6,77) J11,KGAS,LGAS,X0,Y0,Z0,T0,EINIT,ISHELL
		# 77  print(' J11=',I6,' KGAS=',I3,' LGAS=',I3,' X0=','%.4f' % ,' Y0=',
		#    /'%.4f' % ,' Z0=','%.4f' % ,' T0=','%.4f' % ,/,' EINIT=','%.4f' % ,' ISHELL=',I3) 
	GOTO10()
	return
	# end