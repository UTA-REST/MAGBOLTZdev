def MIPCALC():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)                                         
	#/INPT/
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	#/SETP/
	global TMAX,SMALL,API,ESTART,THETA,PHI
	global TCFMAX#(10)
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE  
	#/SET2/
	global DRXINIT,DRYINIT,DRZINIT
	#/LARGE/
	global CF#(20000,512)
	global EIN#(512)
	global TCF#(20000)
	global IARRY#(512)
	global RGAS#(512)
	global IPN#(512)
	global WPL#(512)
	global IZBR#(512)
	global IPLAST
	global PENFRA#[3][512]
	#/ANIS/
	global PSCT#(20000,512)
	global ANGCT#(20000,512)
	global INDEX#(512)
	global NISO
	#/RLTVY/
	global BET#[2000]
	global GAM#(20000)
	global VC,EMS
	#/MIPCLC/
	global ANPRELA,ANPRATT,ANPREXC,ANPRION,ANPREXCI,ANPRBRM
	#/DEDX/
	global ELOSS,ELOSEX,ELOSION,ESUM,BETAGAM,TCFHIGH,VELC,EMAXDEL,ELOSIONC,CUTIONFRC,ELOSEXI,ELOSBREM,NREJECT
	#/COMP/
	global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	#/MIPOUT/
	global ENM#(100000,20)
	global XS#(100000,20)
	global YS#(100000,20)
	global ZS#(100000,20)
	global DIRX#(100000,20)
	global DIRY#(100000,20)
	global DIRZ#[100000,20]
	global TS#(100000,20)
	global IEVENT#(100000)
	#/IONFL/
	global NC0#(512)
	global EC0#(512)
	global NG1#(512)
	global EG1#(512)
	global NG2#(512)
	global EG2#(512)
	global WKLM#(512)
	global DSTFL#(512)
	#/IONMOD/
	global ESPLIT#(512,20)
	global IONMODEL#(512) 
	CFTEMP=[0 for x in range(512)]
	PSTEMP=[0 for x in range(512)]
	ANTEMP=[0 for x in range(512)]
	# CALCULATE DE/DX AND DISTANCE BETWEEN PRIMARY CLUSTERS AND ALSO
	# PRIMARY ELECTRON ENERGY AND VACANCY FOR INPUT TO THERMALISATION
	# ALSO ADDS EXCITATION CLUSTERS WHICH HAVE PENNING FRACTIONS GT 0.0
	#
	# USE VELOCITY IN METRES/PICOSECOND
	VV=2.99792458*(10**-4 )
	# MAXIMUM DELTA ELECTRON ENERGY ALLOWED IN EVENT OUTPUT SECTION= EMAXDEL
	# NOTE NO LIMIT ON GLOBAL DE/DX CALCULATION
	#
	EMAXDEL=ECUT      
	NREJECT=0
	NCUT=0
	NCUTT=0
	#
	IEVMAX=100000  	
	NPMAX=0    
	API=numpy.arccos(-1.00)
	TWOPI=2.00*API
	ANPRELA=0.00
	ANPRATT=0.00
	ANPREXC=0.00
	ANPREXCI=0.00
	ANPRION=0.00
	ANPRBRM=0.00
	ELOSS=0.00
	ELOSEX=0.00
	ELOSEXI=0.00
	ELOSION=0.00
	ELOSIONC=0.00
	ELOSBREM=0.00
	for I in range(1,IPLAST):
		CFTEMP[I]=CF[20000][I]
		PSTEMP[I]=PSCT[20000][I]
		ANTEMP[I]=ANGCT[20000][I]
		TCFF=TCF[20000]
		BETA=BET[2000]
		GAMM=GAM[20000]
	VEL=BETA*VC
	for J in range(1,IPLAST):
		IA=IARRY[J]
		if(IA == 4 or IA == 5 or IA == 9 or IA == 10 or IA == 14 or IA == 15 or IA == 19 or IA == 20 or IA == 24 or IA == 25 or IA == 29 or IA == 30):
			# BREMSSTRAHLUNG EXCITATION OR SUPERELASTIC
			if(J != 1):
				CFT=TCFF*(CFTEMP[J]-CFTEMP[J-1])
			if(J == 1):
				CFT=TCFF*CFTEMP[J]
			# CHECK IF BREMSSTRAHLUNG
			if(LBRM == 1 and IZBR[J]!= 0) :
				# BREMSSTRAHLUNG
				# FIND AVERAGE BREMSSTRAHLUNG ENERGY LOSS OVER 10000 EVENTS
				IATOMNO=IZBR[J]
				E=ESTART
				ESUMBR=0.0
				print(' ENERGY=','%.4f' % E)
				for K in range(1,10000):
					BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
					ESUMBR=ESUMBR+EGAMMA
				ELBRM=ESUMBR/10000.0
				print(' ELBRM=','%.4f' % ELBRM)
				ANPRBRM=ANPRBRM+CFT/VEL
				ELOSBREM=ELOSBREM+CFT*ELBRM/VEL
			# endif
			if(LBRM == 1 and IZBR[J]!= 0):
				pass
			else:
				# EXCITATION OR SUPERELASTIC
				ANPREXC=ANPREXC+CFT/VEL
				ELOSEX=ELOSEX+CFT*EIN[J]*RGAS[J]/VEL
				if(IPEN == 1 and PENFRA[1,J] > 0.0):
					# PENNING TRANSFER OF EXCITATION TO IONISATION
					 ANPREXCI=ANPREXCI+PENFRA[1,J]*CFT/VEL
					 ELOSEXI=ELOSEXI+PENFRA[1,J]*CFT*EIN[J]*RGAS[J]/VEL
			# endif
		elif(IA == 1 or IA == 6 or IA == 11 or IA == 16 or IA == 21 or IA == 26) :
			# ELASTIC ENERGY LOSS
			if(J != 1):
				CFT=TCFF*(CFTEMP[J]-CFTEMP[J-1])
			if(J == 1):
				CFT=TCFF*CFTEMP[J]
			ANPRELA=ANPRELA+CFT/VEL
			# CALCULATE ELASTIC ENERGY LOSS AVERAGED OVER NE EVENTS
			# USE ANISOTROPIC SCATTERING
			NE=10000
			ELAS=0.00
			RFAC=1.00+GAMM*(RGAS[J]-1.00)
			RFAC=(RFAC-1.00)/(RFAC*RFAC)
			for K in range(1,NE):
				R3=DRAND48(RDUM)
				if(INDEX[J]== 1):
					R31=DRAND48(RDUM)
					F3=1.00-R3*ANTEMP[J]
					if(R31 > PSTEMP[J]):
						F3=-F3
				elif(INDEX[J] == 2):
					EPSI=PSTEMP[J]
					F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3)))
				else:
					# ISOTROPIC SCATTERING
					F3=1.00-2.00*R3
				# endif
				ELAS=ELAS+(1.00-F3)
			ELOSS=CFT*2.00*RFAC*EFINAL*ELAS/VEL
			ELOSS=ELOSS/float(NE)
		elif(IA == 3 or IA == 8 or IA == 13 or IA == 18 or IA == 23 or IA == 28):
			# ATTACHMENT
			ANPRATT=ANPRATT+TCFF*(CFTEMP[J]-CFTEMP[J-1])/VEL
		elif(IA == 2 or IA == 7 or IA == 12 or IA == 17 or IA == 22 or IA == 27):
			# IONISATION
			ANPRION=ANPRION+TCFF*(CFTEMP[J]-CFTEMP[J-1])/VEL
		else: 
			print(' WARNING NO COLLISION TYPE IN FUNCTION MIPCALC')    
		# endif
	# CALCULATE ENERGY LOSS TO IONISATION AVERAGED OVER NEV EVENTS
	NEV=10000000
	ETEMP=0.0
	ETEMPC=0.0
	for J in range(1,IPLAST):
		IA=IARRY[J]
		if(IA == 2 or IA == 7 or IA == 12 or IA == 17 or IA == 22 or IA==27) :
			if(EFINAL < EIN[J]):
				pass 
			else:
				#  NEV = NO OF IONISATION EVENTS TO AVERAGE
				for K in range(1,NEV):
					if(IONMODEL[J]> 0) :
						# CALCULATE SECONDARY ENERGY ,ESEC, IN IONISATION COLLISION USING
						# FIVE DIFFERENT POSSIBLE MODELS
						IONSPLIT(J,ESTART,EIN[J],ETEMP1)
						pass
					# endif # doing to pass and hence the next else
					else:
						R9=DRAND48(RDUM)
						ETEMP1=WPL[J]*numpy.tan(R9*numpy.arctan((ESTART-EIN[J])/(2.00*WPL[J]))) 
						ETEMP1=WPL[J]*(ETEMP1/WPL[J])**0.9524
					ETEMP=ETEMP+ETEMP1+EIN[J]*RGAS[J]
					NCUTT=NCUTT+1
					if((ETEMP1+EIN[J]*RGAS[J]) < EMAXDEL) :
						ETEMPC=ETEMPC+ETEMP1+EIN[J]*RGAS[J]
						NCUT=NCUT+1
					# endif
				if(J != 1):
					CFT=TCFF*(CFTEMP[J]-CFTEMP[J-1])
				if(J == 1):
					CFT=TCFF*CFTEMP[J]
				ETEMP=CFT*ETEMP/VEL
				ETEMPC=CFT*ETEMPC/VEL
				ETEMP=ETEMP/float(NEV)
				ETEMPC=ETEMPC/float(NEV)
				ELOSION=ELOSION+ETEMP
				ELOSIONC=ELOSIONC+ETEMPC
		else:
			pass
	BETAGAM=BETA*GAMM
	# CONVERT TO EV/CM
	ELOSS=ELOSS*1*(10**10)
	ELOSEX=ELOSEX*1*(10**10)
	ELOSEXI=ELOSEXI*1*(10**10)
	ELOSION=ELOSION*1*(10**10)
	ELOSIONC=ELOSIONC*1*(10**10)
	ELOSBREM=ELOSBREM*1*(10**10)
	# CONVERT COLLISIONS/CM
	ANPRELA=ANPRELA*1*(10**10)
	ANPRATT=ANPRATT*1*(10**10)
	ANPREXC=ANPREXC*1*(10**10)
	ANPREXCI=ANPREXCI*1*(10**10)
	ANPRION=ANPRION*1*(10**10)
	ANPRBRM=ANPRBRM*1*(10**10)
	ESUM=ELOSS+ELOSEX+ELOSION+ELOSBREM
	VELC=VEL*100.
	TCFHIGH=TCF(20000)*1*(10**12)
	CUTIONFRC=float(NCUT)/float(NCUTT)
	# 
	#  LOAD EVENT ARRAYS WITH ELECTRON ENERGY AND DIRECTION COSINES
	#  ADDS ELECTRONS FROM PENNING EXCITATION IF ALLOWED
	for K in range(1,NEVENT ):
		if(K > IEVMAX):
			print(' WARNING MAXIMUM NUMBER OF EVENTS=',IEVMAX,' def STOPPED:')
		# endif
		NP=0
		#
		# DETERMINE COLLISION TYPE   
		#
		#10
		def GOTO10():
			R1=DRAND48(RDUM)
			I=0
			counter11=1
			while(counter11):
				counter11=0
				I=I+1 
				if(CFTEMP[I]< R1):
					counter11=1
			# FIND TYPE OF INTERACTION
			IA=IARRY[I]
			if(IA == 2 or IA == 7 or IA == 12 or IA == 17 or IA == 22 or IA==27) :
				#  IONISATION
				#-----------------------------------------------------------------
				counter12=1 # self added for looping
				while(counter12):
					counter12=0
					R9=DRAND48(RDUM)
					ESEC=WPL[I]*TAN(R9*ATAN((ESTART-EIN[I])/(2.00*WPL[I]))) 
					ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
					if(ESEC > EMAXDEL):
						NREJECT=NREJECT+1
						counter12=1
					# endif
				# CALCULATE PRIMARY SCATTERING ANGLE 
				# ANISOTROPIC SCATTERING
				R3=DRAND48(RDUM)
				if(INDEX[I]== 1):
					R31=DRAND48(RDUM)
				F3=1.00-R3*ANTEMP[I]
				if(R31 > PSTEMP[I]):
					F3=-F3
				elif(INDEX[I] == 2) :
					EPSI=PSTEMP[I] 
					F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3)))
				else: 
					# ISOTROPIC SCATTERING
					F3=1.00-2.00*R3
				# endif
				THETAP=numpy.arccos(F3)
				F5P=numpy.sin(THETAP)
				GAMSEC=(EMS+ESEC)/EMS
				# CALCULATE SECONDARY RECOIL ANGLE FROM FREE KINEMATICS
				F5S=F5P*math.sqrt(ESTART/ESEC)*GAMM/GAMSEC
				if(F5S > 1.0):
					F5S=1.0
				THETAS=numpy.arcsin(F5S)
				R1=DRAND48(RDUM)
				PHIS=TWOPI*R1
				# CALCULATE NEW DIRECTION COSINES FROM INITIAL VALUES AND SCAT. ANGLES
				DRCOS(DRXINIT,DRYINIT,DRZINIT,THETAS,PHIS,DRXX,DRYY,DRZZ)
				# LOAD SECONDARY ELECTRON DATA  
				NP=NP+1
				if(NP > NPMAX):
					NPMAX=NP
				if(NP > 20):
					print(' EVENT WITH N0 OF PRIMARIES GT 20 IN MIPCALC STOPPED PROGRAM')
				if(NP > 20):
					sys.exit()
				ENM[K][NP]=ESEC
				DIRX[K][NP]=DRXX 
				DIRY[K][NP]=DRYY 
				DIRZ[K,NP]=DRZZ
				XS[K][NP]=0.0
				YS[K][NP]=0.0
				ZS[K][NP]=0.0
				TS[K][NP]=0.0
				IEVENT[K]=NP
				# CALCULATE POSSIBLE SHELL EMISSIONS: AUGER OR FLUORESCENCE
				IFLTST=0
				if(WKLM[I]> 0.0) :
					R9=DRAND48(RDUM)
					if(R9 < WKLM[I]):
						IFLTST=1
				# endif
				if(IFLTST == 0):
					# AUGER EMISSION WITHOUT FLUORESCENCE
					NAUG=NC0[I]
					EAVAUG=EC0[I]/float(NAUG)
					for JFL in range(1,NC0[I]):
						NP=NP+1
						if(NP > NPMAX):
							NPMAX=NP
						if(NP > 20):
							print(' EVENT WITH N0 OF PRIMARIES > 20 IN MIPCALC STOPPED PROGRAM')
						if(NP > 20):
							sys.exit()
						ENM[K][NP]=EAVAUG
						# RANDOM EMISSION ANGLE
						R3=DRAND48(RDUM)
						F3=1.00-2.00*R3
						THETAS=numpy.arccos(F3)
						F6=numpy.cos(THETAS)
						F5=numpy.sin(THETAS)
						R4=DRAND48(RDUM)
						PHIS=TWOPI*R4
						F8=numpy.sin(PHIS)
						F9=numpy.cos(PHIS)
						DIRX[K][NP]=F9*F5
						DIRY[K][NP]=F8*F5
						DIRZ[K,NP]=F6
						XS[K][NP]=0.0
						YS[K][NP]=0.0
						ZS[K][NP]=0.0
						TS[K][NP]=0.0
					IEVENT[K]=NP
				else: 
					# AUGER EMISSION AND FLUORESCENCE
					if(NG2[I]== 0):
						pass
					else:
						NAUG=NG2[I]
						EAVAUG=EG2[I]/float(NAUG)
						for JFL in range(1,NG2[I]):
							NP=NP+1
							if(NP > NPMAX):
								NPMAX=NP
							if(NP > 20):
								print(' EVENT WITH N0 OF PRIMARIES > 20 IN MIPCALC STOPPED PROGRAM')
							if(NP > 20):
								sys.exit()
							ENM[K][NP]=EAVAUG
							# RANDOM EMISSION ANGLE
							R3=DRAND48(RDUM)
							THETAS=numpy.arccos(1.0-2.0*R3)
							F6=numpy.cos(THETAS)
							F5=numpy.sin(THETAS)
							R4=DRAND48(RDUM)
							PHIS=TWOPI*R4
							F8=numpy.sin(PHIS)
							F9=numpy.cos(PHIS)
							DIRX[K][NP]=F9*F5
							DIRY[K][NP]=F8*F5
							DIRZ[K,NP]=F6
							XS[K][NP]=0.0
							YS[K][NP]=0.0
							ZS[K][NP]=0.0
							TS[K][NP]=0.0
						IEVENT[K]=NP
					if(NG1[I] == 0):
						pass
					else:
						NAUG=NG1[I]
						EAVAUG=EG1[I]/float(NAUG)
						R9=DRAND48(RDUM)
						# FLUORESCENCE ABSORPTION DISTANCE
						DFL=-math.log(R9)*DSTFL[I]
						for JFL in range(1,NG1[I]):
							NP=NP+1
							if(NP > NPMAX):
								NPMAX=NP
							if(NP > 20):
								print(' EVENT WITH N0 OF PRIMARIES > 20 IN MIPCALC STOPPED PROGRAM')
							if(NP > 20):
								sys.exit()
							ENM[K][NP]=EAVAUG
							# RANDOM EMISSION ANGLE
							R3=DRAND48(RDUM)
							THETAS=numpy.arccos(1.0-2.0*R3)
							F6=numpy.cos(THETAS)
							F5=numpy.sin(THETAS)
							R4=DRAND48(RDUM)
							PHIS=TWOPI*R4
							F8=numpy.sin(PHIS)
							F9=numpy.cos(PHIS)
							DIRX[K][NP]=F9*F5
							DIRY[K][NP]=F8*F5
							DIRZ[K,NP]=F6
							R3=DRAND48(RDUM)
							THEFL=numpy.arccos(1.0-2.0*R3) 
							R4=DRAND48(RDUM)
							PHifL=TWOPI*R4
							XS[K][NP]=DFL*numpy.sin(THEFL)*numpy.cos(PHifL)
							YS[K][NP]=DFL*numpy.sin(THEFL)*numpy.sin(PHifL)
							ZS[K][NP]=DFL*numpy.cos(THEFL)  
							TS[K][NP]=DFL/VV
						IEVENT[K]=NP  
				# endif
			elif(IA == 4 or IA == 9 or IA == 14 or IA == 14 or IA == 19 or IA == 24 or IA == 29) :
				# EXCITATION
				#----------------------------------------------------------------
				if(PENFRA[1,I] == 0.0 or IPEN == 0):
					GOTO10()
				# POSSIBLE PENNING TRANSFER
				R9=DRAND48(RDUM)
				if(R9 < PENFRA[1,I]):
					# PENNING TRANSFER
					NP=NP+1
					if(NP > NPMAX):
						NPMAX=NP
					if(NP > 20):
						print(' EVENT WITH N0 OF PRIMARIES > 20 IN MIPCALC STOPPED PROGRAM')
					if(NP > 20):
						sys.exit()
					# FINITE PENNING FIXED ELECTRON ENERGY TO 4.0EV
					ENM[K][NP]=4.0
					# RANDOM EMISSION ANGLE
					R3=DRAND48(RDUM)
					THETAS=numpy.arccos(1.0-2.0*R3)
					F6=numpy.cos(THETAS)
					F5=numpy.sin(THETAS)
					R4=DRAND48(RDUM)
					PHIS=TWOPI*R4
					F8=numpy.sin(PHIS)
					F9=numpy.cos(PHIS)
					DIRX[K][NP]=F9*F5
					DIRY[K][NP]=F8*F5
					DIRZ[K,NP]=F6
					# PENNING TRANSFER DISTANCE
					ASIGN=1.00
					R1=DRAND48(RDUM)
					if(R1 < 0.5):
						ASIGN=-ASIGN
					R9=DRAND48(RDUM)
					XS[K][NP]=-math.log(R9)*PENFRA[2,I]*1*10**-6*ASIGN
					R1=DRAND48(RDUM)
					if(R1 < 0.5):
						ASIGN=-ASIGN
					R9=DRAND48(RDUM)
					YS[K][NP]=-math.log(R9)*PENFRA[2,I]*1*10**-6*ASIGN
					R1=DRAND48(RDUM)
					if(R1 < 0.5):
						ASIGN=-ASIGN
					R9=DRAND48(RDUM)
					ZS[K][NP]=-math.log(R9)*PENFRA[2,I]*1*10**-6*ASIGN
					R9=DRAND48(RDUM)
					TS[K][NP]=-math.log(R9)*PENFRA[3,I]
					IEVENT[K]=NP
				else:
					GOTO10()
				# endif  
			else:
				# ELASTIC
				#-----------------------------------------------------------------
				GOTO10()
			# endif
	print(' NPMAX=',NPMAX)
	return
	# end