import conf
import numpy
def CASSTORE(NEV,NVAC,X,Y,Z):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	def get_globals():
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
		IONSM=conf.IONSM
		IFLSM=conf.IFLSM
		ESTOR=conf.ESTOR
		EPHOT=conf.EPHOT
		X0=conf.X0
		Y0=conf.Y0
		Z0=conf.Z0
		DRX0=conf.DRX0
		DRY0=conf.DRY0
		DRZ0=conf.DRZ0
		X01=conf.X01
		Y01=conf.Y01
		Z01=conf.Z01
		globals().update(locals())
	get_globals()
	def update_globals():
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
		conf.IONSM=IONSM
		conf.IFLSM=IFLSM
		conf.ESTOR=ESTOR
		conf.EPHOT=EPHOT
		conf.X0=X0
		conf.Y0=Y0
		conf.Z0=Z0
		conf.DRX0=DRX0
		conf.DRY0=DRY0
		conf.DRZ0=DRZ0
		conf.X01=X01
		conf.Y01=Y01
		conf.Z01=Z01
	# STORE EVENT DATA 
	IONSM[NVAC][NEV]=IONSUM[NVAC]
	IFLSM[NVAC][NEV]=IFLSUM[NVAC]
	if(IONSUM[NVAC]> 28 or IFLSUM[NVAC] > 28):
		print(' IONSUM OR IFLSUM GT.28 IONSUM=',IONSUM[NVAC],'  IFSUM=',IFLSUM[NVAC],' NVAC=',NVAC)
		sys.exit()
	# endif
	for J in range(1,int(IFLSUM[NVAC])+1):
		EPHOT[NVAC][J][NEV]=EPHOTON[NVAC][J]
	for J in range(1,int(IONSUM[NVAC])+1):
		ESTOR[NVAC][J][NEV]=ESTORE[NVAC][J]
		X0[NVAC][J][NEV]=X
		Y0[NVAC][J][NEV]=Y
		Z0[NVAC][J][NEV]=Z
		X01[NVAC]=X0[NVAC][J][NEV]
		Y01[NVAC]=Y0[NVAC][J][NEV]
		Z01[NVAC]=Z0[NVAC][J][NEV]
		DRX0[NVAC][J][NEV]=DRXE[NVAC][J]
		DRY0[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZ0[NVAC][J][NEV]=DRZE[NVAC][J]
	update_globals()
	return
	# end