import numpy
def BREMSCASC(J11,EGAMMA,X0,Y0,Z0,T0,GDCX,GDCY,GDCZ,ILOW):
	# IMPLICIT #real*8(A-H,O-Z)
	# IMPLICIT #integer*8(I-N)
	#CHARACTER*6 SCR(17),SCR1(17)
	# COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	# COMMON/COMPTOUT/EGAM,EELEC,THETAG,THETAE
	# COMMON/PRIM4/MSUM1,MCOMP1,MRAYL1,MPAIR1,MPHOT1,MVAC1
	# COMMON/GENCAS/ELEV[17,79],NSDEG(17),AA[17],BB[17],SCR,SCR1
	# COMMON/MIXC/PRSH(6,3,17,17),ESH(6,3,17),AUG(6,3,17,17,17),RAD[6,3,17,17],PRSHBT(6,3,17),IZ[6,3],INIOCC(6,3,17),ISHLMX(6,3),AMZ[6,3]
	# COMMON/UPD/NOCC(6,3,17),AUGR(6,3,17,17,17),RADR(6,3,17,17)
	# COMMON/CALCASB/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	# COMMON/CALCAS1B/IONSUM1(10),IFLSUM1(10),ESTOR1(10,28),EPHOTG1(10,28),DRXE1(10,28),DRYE1(10,28),DRZE1(10,28),DRX1(10,28),DRY1(10,28),DRZ1(10,28)
	# COMMON/CALCAS2B/IONSUM2(10),IFLSUM2(10),ESTOR2(10,28),EPHOTG2(10,28),DRXE2(10,28),DRYE2(10,28),DRZE2(10,28),DRX2(10,28),DRY2(10,28),DRZ2(10,28)
	# COMMON/CALCAS3B/IONSUM3(10),IFLSUM3(10),ESTOR3(10,28),EPHOTG3(10,28),DRXE3(10,28),DRYE3(10,28),DRZE3(10,28),DRX3(10,28),DRY3(10,28),DRZ3(10,28)
	# COMMON/CALCAS4B/IONSUM4(10),IFLSUM4(10),ESTOR4(10,28),EPHOTG4(10,28),DRXE4(10,28),DRYE4(10,28),DRZE4(10,28),DRX4(10,28),DRY4(10,28),DRZ4(10,28)
	# COMMON/CALCAS5B/IONSUM5(10),IFLSUM5(10),ESTOR5(10,28),EPHOTG5(10,28),DRXE5(10,28),DRYE5(10,28),DRZE5(10,28),DRX5(10,28),DRY5(10,28),DRZ5(10,28)
	# COMMON/RESB/IONSM(10),IFLSM(10),ESTOR(10,28),EPHOT(10,28),X10(10,28),Y10(10,28),Z10(10,28),DRX01(10,28),DRY01(10,28),DRZ01(10,28)
	# COMMON/GENB1/IONF1(10),ESTF1(10,28),X11(10,28),Y11(10,28),Z11(10,28),DRX11(10,28),DRY11(10,28),DRZ11(10,28)
	# COMMON/GENB2/IONF2(10),ESTF2(10,28),X21(10,28),Y21(10,28),Z21(10,28),DRX21(10,28),DRY21(10,28),DRZ21(10,28)
	# COMMON/GENB3/IONF3(10),ESTF3(10,15),X31(10,15),Y31(10,15),Z31(10,15),DRX31(10,15),DRY31(10,15),DRZ31(10,15)
	# COMMON/GENB4/IONF4(10),ESTF4(10,12),X41(10,12),Y41(10,12),Z41(10,12),DRX41(10,12),DRY41(10,12),DRZ41(10,12)
	# COMMON/GENB5/IONF5(10),ESTF5(10,5),X51(10,5),Y51(10,5),Z51(10,5),DRX51(10,5),DRY51(10,5),DRZ51(10,5)
	# COMMON/COUTE/ECMP(10),ECDRX(10),ECDRY(10),ECDRZ[10],XCPOS(10),YCPOS(10),ZCPOS(10),KCGAS(10),LCGAS(10),ICSHELL(10)
	# COMMON/COUTTB/TT(10),TTP
	# COMMON/PPSTRB/NPTP,EPPST[2],XPP[2],YPP[2],ZPP[2],DRXPP[2],DRYPP[2],DRZPP[2]
	# COMMON/COMP/
	global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	#COMMON/COMPTOUT/
	global EGAM,EELEC,THETAG,THETAE
	#COMMON/PRIM4/
	global MSUM1,MCOMP1,MRAYL1,MPAIR1,MPHOT1,MVAC1
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
	#COMMON/CALCASB/
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
	#COMMON/CALCAS1B/
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
	#COMMON/CALCAS2B/
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
	#COMMON/CALCAS3B/
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
	#COMMON/CALCAS4B/
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
	#COMMON/CALCAS5B/
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
	#COMMON/RESB/
	global IONSM#(10)
	global IFLSM#(10)
	global ESTOR#(10,28)
	global EPHOT#(10,28)
	global X10#(10,28)
	global Y10#(10,28)
	global Z10#(10,28)
	global DRX01#(10,28)
	global DRY01#(10,28)
	global DRZ01#(10,28)
	#COMMON/GENB1/
	global IONF1#(10)
	global ESTF1#(10,28)
	global X11#(10,28)
	global Y11#(10,28)
	global Z11#(10,28)
	global DRX11#(10,28)
	global DRY11#(10,28)
	global DRZ11#(10,28)
	#COMMON/GENB2/
	global IONF2#(10)
	global ESTF2#(10,28)
	global X21#(10,28)
	global Y21#(10,28)
	global Z21#(10,28)
	global DRX21#(10,28)
	global DRY21#(10,28)
	global DRZ21#(10,28)
	#COMMON/GENB3/
	global IONF3#(10)
	global ESTF3#(10,15)
	global X31#(10,15)
	global Y31#(10,15)
	global Z31#(10,15)
	global DRX31#(10,15)
	global DRY31#(10,15)
	global DRZ31#(10,15)
	#COMMON/GENB4/
	global IONF4#(10)
	global ESTF4#(10,12)
	global X41#(10,12)
	global Y41#(10,12)
	global Z41#(10,12)
	global DRX41#(10,12)
	global DRY41#(10,12)
	global DRZ41#(10,12)
	#COMMON/GENB5/
	global IONF5#(10)
	global ESTF5#(10,5)
	global X51#(10,5)
	global Y51#(10,5)
	global Z51#(10,5)
	global DRX51#(10,5)
	global DRY51#(10,5)
	global DRZ51#(10,5)
	#COMMON/COUTE/
	global ECMP#(10)
	global ECDRX#(10)
	global ECDRY#(10)
	global ECDRZ#(10)
	global XCPOS#(10)
	global YCPOS#(10)
	global ZCPOS#(10)
	global KCGAS#(10)
	global LCGAS#(10)
	global ICSHELL#(10)
	#COMMON/COUTTB/
	global TT#(10)
	global TTP
	#COMMON/PPSTRB/
	global NPTP
	global EPPST#(2)
	global XPP#(2)
	global YPP#(2)
	global ZPP#(2)
	global DRXPP#(2)
	global DRYPP#(2)
	global DRZPP#(2)
	#----------------------------------------------------------------------
	# BREMSSTRAHLUNG CASCADE TREE:
	#   SET OR ZERO SOME VARIABLES 
	#   CREATE INTERACTION TREE FOR PE COMPTON RAYLEIGH AND PAIR PRODUCTION
	#   STORE ELECTRON ENERGY DIRECTION COSINES AND POSITION WITH SHELL
	#   LEVEL AND GAS IDENTITY IN COMMON/COUT/ FOR EACH COMPTON AND PE EVENT
	#   STORE PAIR PRODUCTION ELECTRON AND POSITRON DATA IN COMMON/PPSTR/
	#   STORE FINAL CASCADE RESULTS IN COMMON/CASRSB/
	#----------------------------------------------------------------------
	API=numpy.arccos(-1.00)
	TWOPI=2.00*API
	IDBG=0
	#     IF(J11 == 2) IDBG=1
	def GOTO5():
		ILOW=0
		# USE VELOCITY IN METRES/PICOSECONDS
		VV=2.99792458E-4 
		#  
		LFIX=0
		# ALLOW FLUORESCENCE CALCULATION
		def GOTO123():
			ICONPH=1
			#  PHOTON ORIGIN
			X=X0
			Y=Y0
			Z=Z0
			TSUM=T0
			#  LOAD INITIAL DIRECTION COSINES BEFORE INTERACTION 
			DRXS=GDCX
			DRYS=GDCY
			DRZS=GDCZ
			#   INITIAL ENERGY
			ENERGY=EGAMMA
			#
			# ZERO SOME ARRAYS
			EPPST[1]=0.00
			EPPST[2]=0.00
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
				for J in range(1,15):
					ESTF3[K][J]=0.0
				for J in range(1,12):
					ESTF4[K][J]=0.0
				for J in range(1,5):
					ESTF5[K][J]=0.0
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
				KCGAS[K]=0
				LCGAS[K]=0
				ICSHELL[K]=0
				ECMP[K]=0.0
			NCOMP=0
			NRAYL=0
			NPAIR=0
			NPHOT=0
			NVAC=0
			NPTP=0
			#    
			IFIRST=1
			ISECOND=2
			def GOTO2(): 
				NTOTI=NCOMP+NRAYL+NPAIR+NPHOT
				# PHOTONS
				ABSO(IFIRST,ENERGY,ISHELL,KGAS,LGAS,DIST)
				#     IF(IDBG == 1) :
				#     WRITE(6,888) ENERGY,ISHELL,J11
				# 888 print(' AFTER ABSO ENERGY=',D12.5,' ISHELL=',I3,' EVENT NO=',I4)
				#     # endIF
				if(ISHELL == -1):
					# BREMSSTRAHLUNG GAMMA TOO LOW IN ENERGY TO IONISE
					ILOW=1
					return
				# endif
				#  
				#  CREATE INTERACTION TREE
				flag=0
				if(LPEFLG == 1):
					flag=100
				if(LCFLG == 1):
					flag=10			###############################
				elif(LRFLG == 1):	##							 ##
					flag=20			## Made significant changes  ##
				elif(LPFLG == 1):	##							 ##
					flag=30			###############################
				# COMPTON SCATTERING
				if(flag==10 or flag==0): 
					COMPTON(KGAS,LGAS,ENERGY)
					NCOMP=NCOMP+1
					NVAC=NVAC+1
					if(NVAC > 10):
						# MAXIMUM OF 10 PRIMARY INTERACTIONS
						#      NJHIGH=NJHIGH+1
						GOTO123()
					# endif
					# RANDOMISE ANGLE PHI
					R3=DRAND48(RDUM)
					PHI=TWOPI*R3
					# CALCULATE COMPTON ELECTRON DIRECTION COSINES USING THETAE AND PHI
					DRCOS(DRXS,DRYS,DRZS,THETAE,PHI,DRXX,DRYY,DRZZ)
					# FOR COMPTON EFFECT STORE ELECTRON DIRECTION COSINES
					ECDRX[NVAC]=DRXX
					ECDRY[NVAC]=DRYY
					ECDRZ[NVAC]=DRZZ
					# CALCULATE WHICH SHELL HAS VACANCY FROM COMPTON EVENT
					CVAC(KGAS,LGAS,EELEC,KSHELL,KBAD)
					# REJECT EVENT WITHOUT SUFFICIENT ENERGY TO IONISE SHELLS
					if(KBAD == 1):
						GOTO123()
					# STORE ELECTRON ENERGY SHELL VACANCY ISHELL KGAS LGAS POSITION 
					ECMP[NVAC]=EELEC
					ICSHELL[NVAC]=KSHELL
					KCGAS[NVAC]=KGAS
					LCGAS[NVAC]=LGAS
					# INTERACTION POSITIONS
					XCPOS[NVAC]=X+DIST*DRXS
					YCPOS[NVAC]=Y+DIST*DRYS
					ZCPOS[NVAC]=Z+DIST*DRZS
					TT[NVAC]=TSUM+DIST/VV 
					# UPDATE PHOTON STARTING ENERGY POSITION AND ANGLES
					ENERGY=EGAM
					X=XCPOS[NVAC]
					Y=YCPOS[NVAC]
					Z=ZCPOS[NVAC]
					PHIG=PHI+API
					if(PHIG >= TWOPI):
						PHIG=PHI-API
					DRCOS(DRXS,DRYS,DRZS,THETAG,PHIG,DRXX,DRYY,DRZZ)
					# NEW DIRECTION COSINES
					DRXS=DRXX
					DRYS=DRYY
					DRZS=DRZZ
					# LOOP BACK 
					GOTO2()
					
				if(flag==20 or flag==0):
					# RAYLEIGH SCATTERING
					RAYLEIGH(KGAS,LGAS,ENERGY,THETAR)
					NRAYL=NRAYL+1
					#  CALCULATE ENERGY LOSS IN RAYLEIGH SCATTERING
					RAYLOS(KGAS,LGAS,ENERGY,THETAR,ELRAY)
					#     IF(IDBG == 1) WRITE(6,776) ENERGY,ELRAY
					# 776 print(' AFTER RAYLOS ENERGY=','%.4f' % ,' ELRAY=','%.4f' % )
					# UPDATE X-RAY STARTING ENERGY POSITION AND ANGLES
					ENERGY=ENERGY-ELRAY
					X=X+DIST*DRXS
					Y=Y+DIST*DRYS
					Z=Z+DIST*DRZS
					TSUM=TSUM+DIST/VV
					# RANDOMISE ANGLE PHI
					R3=DRAND48(RDUM)
					PHIR=TWOPI*R3
					DRCOS(DRXS,DRYS,DRZS,THETAR,PHIR,DRXX,DRYY,DRZZ)
					DRXS=DRXX
					DRYS=DRYY
					DRZS=DRZZ
					# LOOP BACK
					GOTO2()
				
				if(flag==30 or flag==0): 
					# PAIR PRODUCTION
					PAIR(KGAS,LGAS,ENERGY,E1,E2,THET1,PHI1,THET2,PHI2)
					NPAIR=NPAIR+1
					if(NPAIR > 2):
						print(' ERROR NPAIR GT 2 =',NPAIR,' IN BREMSCASC EVENT NO =',J11)
						sys.exit()
					# endif
					NPTP=NPAIR
					# STORE ELECTRON AND POSITRON ENERGY POSITION AND ANGLES
					EPPST[1]=E1
					EPPST[2]=E2
					if(NVAC == 0):
						# FIRST INTERACTION IS PAIR PRODUCTION
						XPP[1]=X
						YPP[1]=Y
						ZPP[1]=Z
						XPP[2]=X
						YPP[2]=Y
						ZPP[2]=Z
						TTP=TSUM
						pass
					# endif
					else:
						XPP[1]=X+DIST*DRXS
						YPP[1]=Y+DIST*DRYS
						ZPP[1]=Z+DIST*DRZS
						XPP[2]=XPP[1]
						YPP[2]=YPP[1]
						ZPP[2]=ZPP[1]
						TTP=TSUM+DIST/VV
					DRCOS(DRXS,DRYS,DRZS,THET1,PHI1,DRXX,DRYY,DRZZ)
					DRXPP[1]=DRXX
					DRYPP[1]=DRYY
					DRZPP[1]=DRZZ
					DRCOS(DRXS,DRYS,DRZS,THET2,PHI2,DRXX,DRYY,DRZZ)
					DRXPP[2]=DRXX
					DRYPP[2]=DRYY
					DRZPP[2]=DRZZ
					flag=200
					# PHOTOELECTRIC ABSORPTION
					#  STORE ENERGY ISHELL KGAS
				if(flag==100 or flag==0): 
					NVAC=NVAC+1
					if(NVAC > 10):
						# ONLY ALLOW MAXIMUM OF 10 PRIMARY INTERACTIONS
						GOTO123()
						sys.exit()
					# endif
				
					NPHOT=NPHOT+1
					# ECMP= TOTAL ENERGY= EGAMMA = ELECTRON KINETIC ENERGY+ VACANCY ENERGY
					ECMP[NVAC]=ENERGY
					ICSHELL[NVAC]=ISHELL
					XCPOS[NVAC]=X+DIST*DRXS
					YCPOS[NVAC]=Y+DIST*DRYS
					ZCPOS[NVAC]=Z+DIST*DRZS
					TT[NVAC]=TSUM+DIST/VV
					KCGAS[NVAC]=KGAS
					LCGAS[NVAC]=LGAS
					# FOR PE EFFECT STORE PHOTON INCIDENT ANGLE
					ECDRX[NVAC]=DRXS
					ECDRY[NVAC]=DRYS
					ECDRZ[NVAC]=DRZS
				# LOOP OVER SHELL VACANCIES
				if(flag==200 or flag==0):
					# STORE NUMBER AND TYPE OF PRIMARY INTERACTIONS
					MSUM1=NTOTI
					MCOMP1=NCOMP
					MRAYL1=NRAYL
					MPAIR1=NPAIR
					MPHOT1=NPHOT
					MVAC1=NVAC
					# LOOP OVER SHELL INTERACTIONS
					#     IF(IDBG == 1) :
					#     WRITE(6,54) NVAC
					#  54 print(' NVAC=',I3)
					#    for 6 in range(M1=1,NVAC):
					#     WRITE(6,55) M1, (ESTORE(M1,K1),K1=1,28)
					#  55 print(' M1=',I3,/,' ESTORE(M1,K)=',4(7'%.4f' % ,/))
					#  56 CONTINUE
					#    for 8 in range(M1=1,NVAC):
					#     WRITE(6,57) (EPHOTON(M1,K1),K1=1,28)
					#  57 print(' EPHOTON=',4(7'%.4f' % ,/))
					#  58 CONTINUE 
					#     # endIF
					for K in range(1,NVAC):
						CONTROLB(IDBG,K)
					#  COMPRESS AUGER AND FLUORESCENCE DATA INTO BLOCKS
					COMPRESS(IDBG,ENSUM)
					# CATCH DROPPED KSHELL FLUORESCENCE
					if(abs(ENSUM-EGAMMA)> 2200.) :
						DIF=ENSUM-EGAMMA
					if(IDBG == 1):
						print('\n Dif=','%.6f' % DIF,' J11=',J11,'\n') 
						GOTO5()
					# endif
					# ADD PAIR DATA AND LOAD INTO COMMON/CASRSB/
					CASRESB()
			GOTO2()
		GOTO123()
	GOTO5()
	return
	# end