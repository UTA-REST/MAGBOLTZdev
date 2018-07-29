def PRINTER():
	# IMPLICIT #real*8 (A-H,O-Z) 
	# IMPLICIT #integer*8 (I-N)   
	#integer*4 NSEED                                     
	#COMMON/INPT/
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	#COMMON/INPT2/
	global KGAS,LGAS,DETEFF,EXCWGHT
	#COMMON/INPT1/
	global NDVEC
	#COMMON/COMP/
	global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG 
	#COMMON/RATIO/
	global AN1,AN2,AN3,AN4,AN5,AN6,AN
	global FRAC#(6)              
	#COMMON/SETP/
	global TMAX,SMALL,API,ESTART,THETA,PHI
	global TCFMAX#(10),
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                      
	#COMMON/BFLD/
	global EOVB,WB,BTHETA,BMAG  
	#COMMON/IONC/
	global DOUBLE#(6,20000),
	global CMINIXSC#(6),
	global CMINEXSC#(6),
	global ECLOSS#(6),
	global WPLN#(6),
	global ICOUNT,AVPFRAC#(3,6)
	#COMMON/LARGE/
	global CF#(20000,512),
	global EIN#(512),
	global TCF#(20000),
	global IARRY#(512),
	global RGAS#(512),
	global IPN#(512),
	global WPL#(512),
	global IZBR#(512),
	global IPLAST,PENFRA#(3,512)   
	#COMMON/NAMES/
	global NAMEG#(6)  
	#COMMON/KSEED/
	global NSEED 
	#COMMON/ECASC/
	global NEGAS#(512),
	global LEGAS#(512),
	global IESHELL#(512),
	global IECASC  
	NAMEG=numpy.zeros(25+1,dtype=str)
	# WRITE(6,1)     
	print('\n           DEGRAD VERSION 3.3  \n','      -----------------------------\n\n')      
	if(IMIP == 1):
		print('   MIP AND DE/DX SIMULATION')	#2
	if(IMIP == 2):
		print('   ELECTRON BEAM SIMULATION')    
	if(IMIP == 3):
		print('   X-RAY SIMULATION')	#4
	if(IMIP == 4):
		print('   BETA DECAY SIMULATION')	#5
	if(IMIP == 5):
		print('   DOUBLE BETA DECAY SIMULATION')	#6
	print('----------------------------------\n\n')
	if(LCMP == 0):
		print('   SIMULATION WITHOUT COMPTON SCATTERING')  	#7
	if(LCMP == 1):
		print('   SIMULATION WITH COMPTON SCATTERING')	#8
	if(LRAY == 0):
		print('   SIMULATION WITHOUT RAYLEIGH SCATTERING')	#9
	if(LRAY == 1):
		print('   SIMULATION WITH RAYLEIGH SCATTERING')	#11 
	if(LPAP == 0):
		print('   SIMULATION WITHOUT PAIR PRODUCTION')	#12 
	if(LPAP == 1):
		print('   SIMULATION WITH PAIR PRODUCTION')	#13 
	if(LBRM == 0):
		print('   SIMULATION WITHOUT BREMSSTRAHLUNG')	#14 
	if(LBRM == 1):	
		print('   SIMULATION WITH BREMSSTRAHLUNG')	#15 
	if(IECASC == 0):
		print('   SIMULATION WITH PARAMETERISED SHELL CASCADE')	#16 
	if(IECASC == 1):
		print('   SIMULATION WITH COMPLETE SHELL CASCADE')	#17 
	print('----------------------------------\n\n')
	print('   MONTE CARLO SOLUTION FOR MIXTURE OF ',NGAS,' GASES.\n   DEGRADATION CALCULATION ALL TIMES IN PICOSECS, DISTANCE IN MICRONS\n   -----------------------------------------------------------------')
	# WRITE(6,30) (NAMEG[J],FRAC[J], J=1,NGAS)     
	for J in range(1,NGAS+1):
		print('\n',5*' ','  GASES  USED ',15*' ',' PERCENTAGE USED ',2*'\n',6*' ',NAMEG[J],5*' ','%.4f' % FRAC[J],'\n')
	print('\n','  ','GAS TEMPERATURE =','%.1f' % TEMPC,' DEGREES CENTIGRADE.','\n','  ','GAS PRESSURE = ','%.1f' % TORR,' TORR.')
	if(NSEED != 0):
		# WRITE(6,51) NSEED
		print(2*'\n',' RANDOM NUMBER SEED =',NSEED)
	if(NSEED == 0):
		# WRITE(6,52) 
		print(2*'\n',' STANDARD RANDOM NUMBER SEED = 54217137')
	if(IPEN == 0):
		# WRITE(6,55)
		print(2*'\n','  ',' PENNING IONISATION NOT ALLOWED')
	if(IPEN == 1):
		# WRITE(6,56)                              
		print(2*'\n','  ',' PENNING IONISATION ALLOWED')
	# WRITE(6,60) EFINAL,NSTEP                                          
	print(1*'\n','  ','INTEGRATION FROM 0.0 TO ','%.1f' % EFINAL,' EV.  IN ',NSTEP,' STEPS. ') 
	# WRITE(6,90) EFIELD,BMAG,BTHETA,WB                                 
	print(1*'\n','  ELECTRIC FIELD =','%.4f' % EFIELD,' VOLTS/CM.','\n''  MAGNETIC FIELD =','%.4f' % BMAG,' KILOGAUSS.','\n','  ANGLE BETWEEN ELECTRIC AND MAGNETIC FIELD =','%.3f' % BTHETA,' DEGREES.','\n','  CYCLOTRON FREQ. =','%.3f' % WB,' RADIANS/PICOSECOND')
	# WRITE(6,43)
	print('\n',' USED ANISOTROPIC X-SECTIONS (OKHRIMOVSKYY ET AL) ')
	if(ICOUNT == 1):
		# WRITE(6,34) 
		print(' USED COUNTING IONISATION X-SECTIONS')
	else:
		# WRITE(6,35)
		print(' USE GROSS IONISATION X-SECTIONS')
	# endif
	# WRITE(6,91) ESTART,NDELTA,ETHRM 
	print(1*'\n','  INITIAL ELECTRON OR X-RAY ENERGY =','%.1f' % ESTART,' EV.','\n',9*' ','NUMBER OF EVENTS =',NDELTA,'\n',4*' ','THERMALISATION ENERGY =','%.2f' % ETHRM,' EV.','\n')
	# WRITE(6,911) DETEFF,EXCWGHT
	print(' PHOTON DETECTION EFFICIENCY USED IN FANO CALCULATION =','%.3f' % DETEFF,' %','\n',7*' ','WEIGHT GIVEN TO EXCITATION IN FANO CALCULATION =','%.3f' % EXCWGHT,'\n') 
	if(IMIP == 4 or IMIP == 5):
		if(KGAS <= 0 or KGAS > NGAS):
			# WRITE(6,990) KGAS
			print(' ERROR IN INPUT: BETA DECAY IDENTifIER KGAS=',KGAS,'  PROGRAM STOPPED:')
			sys.exit()
		# endif
		if(LGAS <= 0 or LGAS > 3):
			# WRITE(6,991) LGAS
			print(' ERROR IN INPUT: BETA DECAY IDENTifIER LGAS=',LGAS,'  PROGRAM STOPPED:')
			sys.exit() 
		# endif
		# WRITE(6,88) KGAS,LGAS
		print('\n  BETA DECAY IN GAS NO =',KGAS,'\n  IF MOLECULE : BETA DECAY IN ATOMIC COMPONENT =',LGAS,'\n')
	# endif
	if(NDVEC == 2):
		# WRITE(6,915)
		print('  BETA OR X-RAY IN RANDOM DIRECTION TO E-FIELD')
		pass
	else:
		# endif
		if(abs(numpy.cos(THETA)) < 1.e-9 and IMIP > 2):
			# WRITE(6,92)
			print('  BETA OR X-RAY PERP# endICULAR TO E-FIELD IN X-Y PLANE')  
		if(abs(numpy.cos(THETA)) < 1.e-9 and IMIP == 2):
			# WRITE(6,922)
			print('  ELECTRON BEAM ALONG X DIRECTION')
		if(numpy.cos(THETA)== 1.0):
			# WRITE(6,93)
			print('  E-BEAM,BETA OR X-RAY ALONG Z-AXIS IN E-FIELD DIRECTION')
		if(numpy.cos(THETA)== -1.0):
			# WRITE(6,94)
			print('  E-BEAM,BETA OR X-RAY ALONG Z-AXIS OPPOSITE TO E-FIELD DIRECTION')     
	# 95  WRITE(6,96) TCFMAX1 
	print('\n','  ','NULL COLLISION FREQUENCY =','%.3f' % TCFMAX1 ,' *(10**12/SEC)','\n')
	# WRITE(6,111)  (TCF(L),L=500,9500,1000)
	for L in range(500,9500+1,1000):
		print('  ','#real COLLISION FREQUENCY AT 10 EQUALLY SPACED ENERGY INTERVALS (*10**12/SEC)','\n')
		print(3*' ','%.3f' % TCF[L],'\t')
		if L==4500:
			print('\n')
	return                                                            
	# end                                                               