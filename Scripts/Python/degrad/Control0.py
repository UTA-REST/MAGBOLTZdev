from Control import *
import conf
import numpy
def CONTROL0(NEVENT,EINIT,ICON):
	global THETAS
	global PHIS
	def get_globals():
		global THETAS,PHIS
		KGAS=conf.KGAS
		LGAS=conf.LGAS
		DETEFF=conf.DETEFF
		EXCWGHT=conf.EXCWGHT
		NDVEC=conf.NDVEC
		DRXINIT=conf.DRXINIT
		DRYINIT=conf.DRYINIT
		DRZINIT=conf.DRZINIT
		LCMP=conf.LCMP
		LCFLG=conf.LCFLG
		LRAY=conf.LRAY
		LRFLG=conf.LRFLG
		LPAP=conf.LPAP
		LPFLG=conf.LPFLG
		LBRM=conf.LBRM
		LBFLG=conf.LBFLG
		LPEFLG=conf.LPEFLG
		EGAM=conf.EGAM
		EELEC=conf.EELEC
		THETAG=conf.THETAG
		THETAE=conf.THETAE
		MSUM=conf.MSUM
		MCOMP=conf.MCOMP
		MRAYL=conf.MRAYL
		MPAIR=conf.MPAIR
		MPHOT=conf.MPHOT
		MVAC=conf.MVAC
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
		IONSUM=conf.IONSUM
		IFLSUM=conf.IFLSUM
		ESTORE=conf.ESTORE
		EPHOTON=conf.EPHOTON
		DRXE=conf.DRXE
		DRYE=conf.DRYE
		DRZE=conf.DRZE
		DRX=conf.DRX
		DRY=conf.DRY
		DRZ=conf.DRZ
		IONSUM1=conf.IONSUM1
		IFLSUM1=conf.IFLSUM1
		ESTOR1=conf.ESTOR1
		EPHOTG1=conf.EPHOTG1
		DRXE1=conf.DRXE1
		DRYE1=conf.DRYE1
		DRZE1=conf.DRZE1
		DRX1=conf.DRX1
		DRY1=conf.DRY1
		DRZ1=conf.DRZ1
		IONSUM2=conf.IONSUM2
		IFLSUM2=conf.IFLSUM2
		ESTOR2=conf.ESTOR2
		EPHOTG2=conf.EPHOTG2
		DRXE2=conf.DRXE2
		DRYE2=conf.DRYE2
		DRZE2=conf.DRZE2
		DRX2=conf.DRX2
		DRY2=conf.DRY2
		DRZ2=conf.DRZ2
		IONSUM3=conf.IONSUM3
		IFLSUM3=conf.IFLSUM3
		ESTOR3=conf.ESTOR3
		EPHOTG3=conf.EPHOTG3
		DRXE3=conf.DRXE3
		DRYE3=conf.DRYE3
		DRZE3=conf.DRZE3
		DRX3=conf.DRX3
		DRY3=conf.DRY3
		DRZ3=conf.DRZ3
		IONSUM4=conf.IONSUM4
		IFLSUM4=conf.IFLSUM4
		ESTOR4=conf.ESTOR4
		EPHOTG4=conf.EPHOTG4
		DRXE4=conf.DRXE4
		DRYE4=conf.DRYE4
		DRZE4=conf.DRZE4
		DRX4=conf.DRX4
		DRY4=conf.DRY4
		DRZ4=conf.DRZ4
		IONSUM5=conf.IONSUM5
		IFLSUM5=conf.IFLSUM5
		ESTOR5=conf.ESTOR5
		EPHOTG5=conf.EPHOTG5
		DRXE5=conf.DRXE5
		DRYE5=conf.DRYE5
		DRZE5=conf.DRZE5
		DRX5=conf.DRX5
		DRY5=conf.DRY5
		DRZ5=conf.DRZ5
		ECMP=conf.ECMP
		ECDRX=conf.ECDRX
		ECDRY=conf.ECDRY
		ECDRZ=conf.ECDRZ
		XCPOS=conf.XCPOS
		YCPOS=conf.YCPOS
		ZCPOS=conf.ZCPOS
		KCGAS=conf.KCGAS
		LCGAS=conf.LCGAS
		ICSHELL=conf.ICSHELL
		TT=conf.TT
		TTP=conf.TTP
		NPTP=conf.NPTP
		EPPST=conf.EPPST
		XPP=conf.XPP
		YPP=conf.YPP
		ZPP=conf.ZPP
		DRXPP=conf.DRXPP
		DRYPP=conf.DRYPP
		DRZPP=conf.DRZPP
		NJHIGH=conf.NJHIGH
		THETAS=conf.THETAS
		PHIS=conf.PHIS
		globals().update(locals())
	get_globals()
	print("THETAS",THETAS)
	def update_globals():
		global THETAS,PHIS
		conf.KGAS=KGAS
		conf.LGAS=LGAS
		conf.DETEFF=DETEFF
		conf.EXCWGHT=EXCWGHT
		conf.NDVEC=NDVEC
		conf.DRXINIT=DRXINIT
		conf.DRYINIT=DRYINIT
		conf.DRZINIT=DRZINIT
		conf.LCMP=LCMP
		conf.LCFLG=LCFLG
		conf.LRAY=LRAY
		conf.LRFLG=LRFLG
		conf.LPAP=LPAP
		conf.LPFLG=LPFLG
		conf.LBRM=LBRM
		conf.LBFLG=LBFLG
		conf.LPEFLG=LPEFLG
		conf.EGAM=EGAM
		conf.EELEC=EELEC
		conf.THETAG=THETAG
		conf.THETAE=THETAE
		conf.MSUM=MSUM
		conf.MCOMP=MCOMP
		conf.MRAYL=MRAYL
		conf.MPAIR=MPAIR
		conf.MPHOT=MPHOT
		conf.MVAC=MVAC
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
		conf.IONSUM=IONSUM
		conf.IFLSUM=IFLSUM
		conf.ESTORE=ESTORE
		conf.EPHOTON=EPHOTON
		conf.DRXE=DRXE
		conf.DRYE=DRYE
		conf.DRZE=DRZE
		conf.DRX=DRX
		conf.DRY=DRY
		conf.DRZ=DRZ
		conf.IONSUM1=IONSUM1
		conf.IFLSUM1=IFLSUM1
		conf.ESTOR1=ESTOR1
		conf.EPHOTG1=EPHOTG1
		conf.DRXE1=DRXE1
		conf.DRYE1=DRYE1
		conf.DRZE1=DRZE1
		conf.DRX1=DRX1
		conf.DRY1=DRY1
		conf.DRZ1=DRZ1
		conf.IONSUM2=IONSUM2
		conf.IFLSUM2=IFLSUM2
		conf.ESTOR2=ESTOR2
		conf.EPHOTG2=EPHOTG2
		conf.DRXE2=DRXE2
		conf.DRYE2=DRYE2
		conf.DRZE2=DRZE2
		conf.DRX2=DRX2
		conf.DRY2=DRY2
		conf.DRZ2=DRZ2
		conf.IONSUM3=IONSUM3
		conf.IFLSUM3=IFLSUM3
		conf.ESTOR3=ESTOR3
		conf.EPHOTG3=EPHOTG3
		conf.DRXE3=DRXE3
		conf.DRYE3=DRYE3
		conf.DRZE3=DRZE3
		conf.DRX3=DRX3
		conf.DRY3=DRY3
		conf.DRZ3=DRZ3
		conf.IONSUM4=IONSUM4
		conf.IFLSUM4=IFLSUM4
		conf.ESTOR4=ESTOR4
		conf.EPHOTG4=EPHOTG4
		conf.DRXE4=DRXE4
		conf.DRYE4=DRYE4
		conf.DRZE4=DRZE4
		conf.DRX4=DRX4
		conf.DRY4=DRY4
		conf.DRZ4=DRZ4
		conf.IONSUM5=IONSUM5
		conf.IFLSUM5=IFLSUM5
		conf.ESTOR5=ESTOR5
		conf.EPHOTG5=EPHOTG5
		conf.DRXE5=DRXE5
		conf.DRYE5=DRYE5
		conf.DRZE5=DRZE5
		conf.DRX5=DRX5
		conf.DRY5=DRY5
		conf.DRZ5=DRZ5
		conf.ECMP=ECMP
		conf.ECDRX=ECDRX
		conf.ECDRY=ECDRY
		conf.ECDRZ=ECDRZ
		conf.XCPOS=XCPOS
		conf.YCPOS=YCPOS
		conf.ZCPOS=ZCPOS
		conf.KCGAS=KCGAS
		conf.LCGAS=LCGAS
		conf.ICSHELL=ICSHELL
		conf.TT=TT
		conf.TTP=TTP
		conf.NPTP=NPTP
		conf.EPPST=EPPST
		conf.XPP=XPP
		conf.YPP=YPP
		conf.ZPP=ZPP
		conf.DRXPP=DRXPP
		conf.DRYPP=DRYPP
		conf.DRZPP=DRZPP
		conf.NJHIGH=NJHIGH
		conf.THETAS=THETAS
		conf.PHIS=PHIS
	# IMPLICIT #real*8(A-H,O-Z)
	# IMPLICIT #integer*8(I-N)
	# CHARACTER*6 SCR(17),SCR1(17)
		#----------------------------------------------------------------------
	#   SET OR ZERO SOME VARIABLES 
	#   CREATE INTERACTION TREE FOR PE COMPTON RAYLEIGH AND PAIR PRODUCTION
	#   STORE ELECTRON ENERGY DIRECTION COSINES AND POSITION WITH SHELL
	#   LEVEL AND GAS IDENTITY IN COMMON/COUT/ FOR EACH COMPTON AND PE EVENT
	#   STORE PAIR PRODUCTION ELECTRON AND POSITRON DATA IN COMMON/PPSTR/
	#   CALL CONTROL FOR EACH PRIMARY PHOTON INTERACTION
	#   FOR BETA DECAY STORE ENERGY POSITION AND GAS IDENTITY 
	#----------------------------------------------------------------------
	NTOTI=0.0
	API=numpy.arccos(-1.00)
	TWOPI=2.00*API
	NJHIGH=0
	# USE VELOCITY IN METRES/PICOSECONDS
	VV=2.99792458e-4 
	JF=-1
	if(ICON == 1):
		ABSO(JF,EINIT,ISHELL,KGAS,LGAS,DIST)
	#
	IODD=0  
	#  LOOP FOR NUMBER OF EVENTS
	for I in range(1,NEVENT+1):
		flag200=0
		IODD=IODD+1
		# *********************************************************************
		# OPTION TO FIX ABSORPTION ON A SHELL,ISHELL IN KGAS, COMPONENT LGAS 
		# USE LFIX=1 AND COMMENT OR DECOMMENT LINES BELOW
		#     ISHELL=1
		#     KGAS=1
		#     LGAS=1
		#     LFIX=1
		LFIX=0
		#*********************************************************************
		# ALLOW FLUORESCENCE CALCULATION
		# 123 
		flag123=1
		while(flag123):
			flag123=0
			ICONPH=1
			# FIX INITIAL INTERACTION AT 0,0,0
			X=0.0
			Y=0.0
			Z=0.0
			TSUM=0.0
			#  INITIAL DIRECTION COSINES BEFORE INTERACTION AT 0,0,0
			if(NDVEC == 1):
				PHI=0.00
				THETA=0.00
				if(ICON == 3 and IODD == 2):
					# FOR DOUBLE BETA DECAY REVERSE COORDINATES FOR EACH SECOND EVENT
					THETA=API
					PHI=0.00
					IODD=0
				# endif
			elif (NDVEC == -1) :
				PHI=0.00
				THETA=API
				if(ICON == 3 and IODD == 2):
					# FOR DOUBLE BETA DECAY REVERSE COORDINATES FOR EACH SECOND EVENT
					THETA=0.00
					PHI=0.00
					IODD=0
				# endif
			elif(NDVEC == 0) :
				R3=DRAND48(RDUM)
				PHI=TWOPI*R3
				THETA=API/2.0  
				if(IODD == 1):
					PHIS=PHI
				if(ICON == 3 and IODD == 2):
					# FOR DOUBLE BETA DECAY REVERSE COORDINATES FOR EACH SECOND EVENT
					PHI=PHIS+API
					if(PHI > 2.0*API):
						PHI=PHI-2.0*API
					THETA=API/2.0
					IODD=0
				# endif
			elif(NDVEC == 2) :
				R3=DRAND48(RDUM)
				PHI=TWOPI*R3
				R4=DRAND48(RDUM)
				THETA=numpy.arccos(1.00-2.00*R4)  
				if(IODD == 1):
					PHIS=PHI
				if(IODD == 1):
					THETAS=THETA
				if(ICON == 3 and IODD == 2):
					# FOR DOUBLE BETA DECAY REVERSE COORDINATES FOR EACH SECOND EVENT
					PHI=PHIS+API
					if(PHI > 2.0*API):
						PHI=PHI-2.0*API
					THETA=THETAS+API
					if(THETA > API):
						THETA=THETA-2.0*API
					IODD=0
				# endif
			else: 
				# WRITE(6,992) NDVEC
				# 992  
				print('\n  DIRECTION OF DELTA NOT DEFINED NDVEC = %d'%NDVEC)
				sys.exit()      
			# endif
			# INITIAL DIRECTION COSINES FOR CASCADE CALCULATION
			DRZINIT=numpy.cos(THETA)
			DRXINIT=numpy.sin(THETA)*numpy.cos(PHI)
			DRYINIT=numpy.sin(THETA)*numpy.sin(PHI)
			#  LOAD INITIAL DIRECTION COSINES BEFORE INTERACTION AT 0,0,0
			DRXS=DRXINIT
			DRYS=DRYINIT
			DRZS=DRZINIT
			#   INITIAL ENERGY
			ENERGY=EINIT
			#
			# ZERO SOME ARRAYS
			EPPST[1][I]=0.00
			EPPST[2][I]=0.00
			for K in range(1,10+1):
				for J in range(1,28+1):
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
					# 1  CONTINUE
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
				# 11 CONTINUE
			NCOMP=0
			NRAYL=0
			NPAIR=0
			NPHOT=0
			NVAC=0
			NPTP[I]=0
			#    
			IFIRST=1
			ISECOND=2
			print("control0 419 LFIX= ",LFIX)
			if(LFIX == 1):
				print("got into if control0")
				# FIXED SHELL VACANCY SEE ABOVE
				NVAC=1
				ECMP[NVAC]=ENERGY
				ICSHELL[NVAC]=ISHELL
				XCPOS[NVAC]=X
				YCPOS[NVAC]=Y
				ZCPOS[NVAC]=Z
				KCGAS[NVAC]=KGAS
				LCGAS[NVAC]=LGAS
				TT[NVAC][I]=0.0
				# GO TO 200
				pass
			else:
				# endif
				# BETA DECAY
				print("got into else control0")
				if(ICON == 2 or ICON == 3):
					NVAC=1
					ECMP[NVAC]=ENERGY
					XCPOS[NVAC]=X
					YCPOS[NVAC]=Y
					ZCPOS[NVAC]=Z
					KCGAS[NVAC]=KGAS
					LCGAS[NVAC]=LGAS
					TT[NVAC][I]=0.0
					# GO TO 200
					pass
				else:
					# endif
					flag2=1
					# 2 
					while(flag2):
						flag2=0
						NTOTI=NCOMP+NRAYL+NPAIR+NPHOT
						print(NTOTI)
						# PHOTONS
						if(ICON == 1):
							ABSO(IFIRST,ENERGY,ISHELL,KGAS,LGAS,DIST)
						#  
						#  CREATE INTERACTION TREE
						if(LPEFLG == 1):
							# GO TO 100
							pass
						else:
							flag=0
							if(LCFLG == 1):
								# GO TO 10
								flag=10
							if(LRFLG == 1 and flag==0):
								# GO TO 20
								flag=20
							if(LPFLG == 1 and flag==0):
								# GO TO 30
								flag=30
							# COMPTON SCATTERING
							if(flag==0 or flag==10):
								# 10 
								COMPTON(KGAS,LGAS,ENERGY)
								NCOMP=NCOMP+1
								NVAC=NVAC+1
								if(NVAC > 10):
									# MAXIMUM OF 10 PRIMARY INTERACTIONS
									NJHIGH=NJHIGH+1
									# GO TO 123
									flag123=1
									break
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
								#     IF(KBAD == 1) WRITE(6,445) EELEC,I 
								# 445 print(' COMPTON ELECTRON ENERGY =','%.4f' % ,' TOO LOW IN ENERGY. EVE
								#    /NT NO=',I5)  
								if(KBAD == 1):
									# GO TO 123
									flag123=1
									break
								# STORE ELECTRON ENERGY SHELL VACANCY ISHELL KGAS LGAS POSITION 
								ECMP[NVAC]=EELEC
								ICSHELL[NVAC]=KSHELL
								KCGAS[NVAC]=KGAS
								LCGAS[NVAC]=LGAS
								# INITIAL INTERACTION
								if(NTOTI == 0):
									XCPOS[NVAC]=X
									YCPOS[NVAC]=Y
									ZCPOS[NVAC]=Z
									TT[NVAC][I]=0.0
								else:
									# LATER INTERACTIONS
									XCPOS[NVAC]=X+DIST*DRXS
									YCPOS[NVAC]=Y+DIST*DRYS
									ZCPOS[NVAC]=Z+DIST*DRZS
									TSUM=TSUM+DIST/VV
									TT[NVAC][I]=TSUM
								# endif
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
								# GO TO 2
								flag2=1
								continue
								# RAYLEIGH SCATTERING
							if(flag==0 or flag==10 or flag==20):
								# 20 
								RAYLEIGH(KGAS,LGAS,ENERGY,THETAR)
								NRAYL=NRAYL+1
								#  CALCULATE ENERGY LOSS IN RAYLEIGH SCATTERING
								RAYLOS(KGAS,LGAS,ENERGY,THETAR,ELRAY)
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
								# GO TO 2
								flag2=1
								continue
								# PAIR PRODUCTION
							if(flag<=30):
								# 30 
								PAIR(KGAS,LGAS,ENERGY,E1,E2,THET1,PHI1,THET2,PHI2)
								NPAIR=NPAIR+1
								NPTP[I]=NPAIR
								# STORE ELECTRON AND POSITRON ENERGY POSITION AND ANGLES
								EPPST[1][I]=E1
								EPPST[2][I]=E2
								if(NVAC == 0):
									# FIRST INTERACTION IS PAIR PRODUCTION
									XPP[1][I]=X
									YPP[1][I]=Y
									ZPP[1][I]=Z
									XPP[2][I]=X
									YPP[2][I]=Y
									ZPP[2][I]=Z
									TTP[I]=0.0
									# GO TO 40       
									pass
								else:
									# endif
									XPP[1][I]=X+DIST*DRXS
									YPP[1][I]=Y+DIST*DRYS
									ZPP[1][I]=Z+DIST*DRZS
									XPP[2][I]=XPP[1][I]
									YPP[2][I]=YPP[1][I]
									ZPP[2][I]=ZPP[1][I]
									TSUM=TSUM+DIST/VV
									TTP[I]=TSUM
						# 40 
						DRCOS(DRXS,DRYS,DRZS,THET1,PHI1,DRXX,DRYY,DRZZ)
						DRXPP[1][I]=DRXX
						DRYPP[1][I]=DRYY
						DRZPP[1][I]=DRZZ
						DRCOS(DRXS,DRYS,DRZS,THET2,PHI2,DRXX,DRYY,DRZZ)
						DRXPP[2][I]=DRXX
						DRYPP[2][I]=DRYY
						DRZPP[2][I]=DRZZ
						# GO TO 200
						flag200=1
						flag123=0
						break
						# PHOTOELECTRIC ABSORPTION
						#  STORE ENERGY ISHELL KGAS
					# 100 
					NVAC=NVAC+1
					if(NVAC > 10):
						# ONLY ALLOW MAXIMUM OF 10 PRIMARY INTERACTIONS
						NJHIGH=NJHIGH+1
						# GO TO 123
						flag123=1
						continue
						sys.exit()
					# endif
					NPHOT=NPHOT+1
					# ECMP= TOTAL ENERGY= EGAMMA = ELECTRON KINETIC ENERGY+ VACANCY ENERGY
					ECMP[NVAC]=ENERGY
					ICSHELL[NVAC]=ISHELL
					if(NTOTI == 0):
						XCPOS[NVAC]=X
						YCPOS[NVAC]=Y
						ZCPOS[NVAC]=Z
						TT[NVAC][I]=0.0
					else:
						XCPOS[NVAC]=X+DIST*DRXS
						YCPOS[NVAC]=Y+DIST*DRYS
						ZCPOS[NVAC]=Z+DIST*DRZS
						TSUM=TSUM+DIST/VV
						TT[NVAC][I]=TSUM
					# endif
					KCGAS[NVAC]=KGAS
					LCGAS[NVAC]=LGAS
					# FOR PE EFFECT STORE PHOTON INCIDENT ANGLE
					ECDRX[NVAC]=DRXS
					ECDRY[NVAC]=DRYS
					ECDRZ[NVAC]=DRZS
				# LOOP OVER SHELL VACANCIES
		# 200 CONTINUE
		# STORE NUMBER AND TYPE OF PRIMARY INTERACTIONS
		MSUM[I]=NTOTI
		MCOMP[I]=NCOMP
		MRAYL[I]=NRAYL
		MPAIR[I]=NPAIR
		MPHOT[I]=NPHOT
		MVAC[I]=NVAC
		# LOOP OVER SHELL VACANCIES
		for K in range(1,NVAC+1):
			CONTROL(I,K,ICON)
		# 900 CONTINUE
		# LOOP OVER EXTRA ELECTRONS FROM COMPTON AND PAIR PRODUCTION AND LOAD 
		# INTO COMPTON ELECTRON STORE AND PAIR STORE
		# 1000 CONTINUE
	update_globals()
	return
  # end