import numpy
# from degrad1 import *
from Setup import *
from Gasmixc import *
from Mixerc import *
from Gasmix import *
from Printer import *
from Mipcalc import *
from Density import *
from Cascdat import *
from Mixer import *
import sys
def DEGRADE():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	global TMAX,SMALL,API,ESTART,THETA,PHI
	global TCFMAX #array size 10
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE,EOVB,WB,BTHETA,BMAG
	LAST=0
	LAST=SETUP(LAST)
	if(LAST == 1):
		sys.exit()
	DENSITY()
	CASCDAT()
	MIXERC()
	MIXER()
	# CALCULATE FLUORESCENCE ABSORPTION DISTANCES 
	FLDIST()
	PRINTER()
	if(IMIP == 1):
		MIPCALC()
	# if MIP OR ELECTRON BEAM SKIP DIRECT CASCADE CALCULATION
	if(IMIP <= 2):
		PASSING	
	else:
		ICON=IMIP-2
		#  ICON=1 XRAY,   ICON=2 BETA DECAY , ICON=3 DOUBLE BETA DECAY  
		CONTROL0(NEVENT,ESTART,ICON)
		# CALCULATE AND OUTPUT AVERAGES FROM SHELLS
		OUTPUTC(NEVENT,IMIP)
		# AFTER ALL SHELL EMISSIONS THERMALISE ELECTRONS
	if(BMAG == 0.00):
		MONTEFE()
	if(BMAG != 0.00):
		if(BTHETA == 0.00 or BTHETA == 180.00):
			MONTEFA()
		elif(BTHETA == 90.00) :
			MONTEFB()
		else:
			MONTEFC()
		# endif
	# endif
	STATS2()
	OUTPUT()
	DEGRADE()
	sys.exit()
    # end

DEGRADE()