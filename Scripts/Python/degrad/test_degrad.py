import numpy
# from degrad1 import *
import conf
from Setup import *
from Gasmixc import *
from Mixerc import *
from Gasmix import *
from Printer import *
from Mipcalc import *
from Density import *
from Cascdat import *
from Mixer import *
from Control0 import *
from Fldist import *
from Montefe import *
from Stats2 import *
from Outputc import *
from Montefc import *
import sys
def DEGRADE():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	global TMAX,SMALL,API,ESTART,THETA,PHI
	
	global TCFMAX #array size 10
	def get_globals():
		TMAX=conf.TMAX
		SMALL=conf.SMALL
		API=conf.API
		ESTART=conf.ESTART
		THETA=conf.THETA
		PHI=conf.PHI
		TCFMAX=conf.TCFMAX
		# global 
		TCFMAX1=conf.TCFMAX1
		RSTART=conf.RSTART
		EFIELD=conf.EFIELD
		ETHRM=conf.ETHRM
		ECUT=conf.ECUT
		NEVENT=conf.NEVENT
		IMIP=conf.IMIP
		IWRITE=conf.IWRITE
		EOVB=conf.EOVB
		WB=conf.WB
		BTHETA=conf.BTHETA
		BMAG=conf.BMAG
		IMIP=conf.IMIP
		globals().update(locals())
	get_globals()

	LAST=0
	LAST=SETUP(LAST)
	get_globals()

	if(LAST == 1):
		sys.exit()
	DENSITY()
	get_globals()

	CASCDAT()
	get_globals()

	MIXERC()
	get_globals()

	MIXER()
	get_globals()

	# CALCULATE FLUORESCENCE ABSORPTION DISTANCES 
	FLDIST()
	get_globals()

	PRINTER()
	get_globals()

	if(IMIP == 1):
		MIPCALC()
		get_globals()

	# if MIP OR ELECTRON BEAM SKIP DIRECT CASCADE CALCULATION
	if(IMIP <= 2):
		pass
	else:
		ICON=IMIP-2
		#  ICON=1 XRAY,   ICON=2 BETA DECAY , ICON=3 DOUBLE BETA DECAY  
		CONTROL0(NEVENT,ESTART,ICON)
		get_globals()

		# CALCULATE AND OUTPUT AVERAGES FROM SHELLS
		OUTPUTC(NEVENT,IMIP)
		get_globals()

		# AFTER ALL SHELL EMISSIONS THERMALISE ELECTRONS
	if(BMAG == 0.00):
		MONTEFE()
		get_globals()

	if(BMAG != 0.00):
		if(BTHETA == 0.00 or BTHETA == 180.00):
			MONTEFA()
			get_globals()

		elif(BTHETA == 90.00) :
			MONTEFB()
			get_globals()

		else:
			MONTEFC()
			get_globals()
		# endif
	# endif
	STATS2()
	get_globals()

	OUTPUT()
	get_globals()

	conf.TCFMAX1=TCFMAX1
	conf.RSTART=RSTART
	conf.EFIELD=EFIELD
	conf.ETHRM=ETHRM
	conf.ECUT=ECUT
	conf.NEVENT=NEVENT
	conf.IMIP=IMIP
	conf.IWRITE=IWRITE
	conf.EOVB=EOVB
	conf.WB=WB
	conf.BTHETA=BTHETA
	conf.BMAG=BMAG
	conf.TMAX=TMAX
	conf.SMALL=SMALL
	conf.API=API
	conf.ESTART=ESTART
	conf.THETA=THETA
	conf.PHI=PHI
	conf.TCFMAX=TCFMAX

	sys.exit()
    # end



DEGRADE()