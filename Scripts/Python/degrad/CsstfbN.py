def CSSTFB1(NVAC,L1,DIST1):           
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	#COMMON/CALCASB/
	global IONSUM0#(10)
	global IFLSUM0#(10)
	global ESTORE0#(10,28)
	global EPHOTON0#(10,28)
	global DRXE0#(10,28)
	global DRYE0#(10,28)
	global DRZE0#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	#COMMON/CALCAS1B/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#[10,28]
	#COMMON/GENB1/
	global IONF1#(10)
	global ESTF1#(10,28)
	global X1#(10,28)
	global Y1#(10,28)
	global Z1#(10,28)
	global DRXS#(10,28)
	global DRYS#(10,28)
	global DRZS#(10,28)
	#COMMON/GEN11/
	global X11#(10,28)
	global Y11#(10,28)
	global Z11#(10,28)
	#COMMON/GEN01/
	global X01#(10)
	global Y01#(10)
	global Z01#(10)
	#
	if(L1 == 0):
		# ZERO COUNTER
		IONF1[NVAC]=0
		for K in range(1,28):
			ESTF1[NVAC][K]=0.0
		return
	# endif
	# STORE EVENT DATA FOR FIRST GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 28) :
		print(' WARNING FIRST GENERATION CONVERTED FLUORESCENCE HAS AN EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
		sys.exit()
	# endif
	IONF1[NVAC]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF1[NVAC][J]=ESTORE[NVAC][J]
		X1[NVAC][J]=X01[NVAC]+DIST1*DRX0[NVAC][L1]
		Y1[NVAC][J]=Y01[NVAC]+DIST1*DRY0[NVAC][L1]
		Z1[NVAC][J]=Z01[NVAC]+DIST1*DRZ0[NVAC][L1]
		X11[NVAC][L1]=X1[NVAC][J]
		Y11[NVAC][L1]=Y1[NVAC][J]
		Z11[NVAC][L1]=Z1[NVAC][J]
		DRXS[NVAC][J]=DRXE[NVAC][J]
		DRYS[NVAC][J]=DRYE[NVAC][J]
		DRZS[NVAC][J]=DRZE[NVAC][J]
	return
	# end
def CSSTFB2(NVAC,L1,DIST1):               
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	#COMMON/CALCAS1B/
	#CALCAS1B#
	global IONSUM0#(10)
	global IFLSUM0#(10)
	global ESTORE0#(10,28)
	global EPHOTON0#(10,28)
	global DRXE0#(10,28)
	global DRYE0#(10,28)
	global DRZE0#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)

	#COMMON/CALCAS2B/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#[10,28]

	#COMMON/GEN21/
	global X21#(10,28)
	global Y21#(10,28)
	global Z21#(10,28)
	#COMMON/GEN11/
	global X11#(10,28)
	global Y11#(10,28)
	global Z11#(10,28)
	#
	if(L1 == 0):
		# ZERO COUNTER
		IONF2[NVAC]=0
		for K in range(1,28):
			ESTF2[NVAC][K]=0.0
		return
	# endif
	# STORE EVENT DATA FOR FIRST GENERATION FLUORESCENCE
	# STORE EVENT DATA FOR SECOND GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 28) :
		print(' WARNING SECOND GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
		sys.exit()
	# endif
	IONF2[NVAC]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF2[NVAC][J]=ESTORE[NVAC][J]
		X2[NVAC][J]=X11[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y2[NVAC][J]=Y11[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z2[NVAC][J]=Z11[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X21[NVAC][L1]=X2[NVAC][J]
		Y21[NVAC][L1]=Y2[NVAC][J]
		Z21[NVAC][L1]=Z2[NVAC][J]
		DRXS[NVAC][J]=DRXE[NVAC][J]
		DRYS[NVAC][J]=DRYE[NVAC][J]
		DRZS[NVAC][J]=DRZE[NVAC][J]
	return
	# end
def CSSTFB3(NVAC,L1,DIST1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	#COMMON/CALCAS2B/
	global IONSUM0#(10)
	global IFLSUM0#(10)
	global ESTORE0#(10,28)
	global EPHOTON0#(10,28)
	global DRXE0#(10,28)
	global DRYE0#(10,28)
	global DRZE0#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	#COMMON/CALCAS3B/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#[10,28]
	#COMMON/GENB3/
	global IONF3#(10)
	global ESTF3#(10,15)
	global X3#(10,15)
	global Y3#(10,15)
	global Z3#(10,15)
	global DRXS#(10,15)
	global DRYS#(10,15)
	global DRZS#(10,15)
	#COMMON/GEN31/
	global X31#(10,28)
	global Y31#(10,28)
	global Z31#(10,28)
	#COMMON/GEN21/
	global X21#(10,28)
	global Y21#(10,28)
	global Z21#(10,28)
	#
	if(L1 == 0):
		# ZERO COUNTER
		IONF3[NVAC]=0
		for K in range(1,15):
			ESTF3[NVAC][K]=0.0
			return
	# endif
	# STORE EVENT DATA FOR THIRD GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 15) :
		print(' WARNING THIRD GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
		sys.exit()
	# endif
	IONF3[NVAC]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF3[NVAC][J]=ESTORE[NVAC][J]
		X3[NVAC][J]=X21[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Z3[NVAC][J]=Y21[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z3[NVAC][J]=Z21[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X31[NVAC][L1]=X3[NVAC][J]
		Y31[NVAC][L1]=Z3[NVAC][J]
		Z31[NVAC][L1]=Z3[NVAC][J]
		DRXS[NVAC][J]=DRXE[NVAC][J]
		DRYS[NVAC][J]=DRYE[NVAC][J]
		DRZS[NVAC][J]=DRZE[NVAC][J]
	return
	# end
def CSSTFB4(NVAC,L1,DIST1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	#COMMON/CALCAS3B/
	global IONSUM0#(10)
	global IFLSUM0#(10)
	global ESTORE0#(10,28)
	global EPHOTON0#(10,28)
	global DRXE0#(10,28)
	global DRYE0#(10,28)
	global DRZE0#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	#COMMON/CALCAS4B/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#[10,28]
	#COMMON/GENB4/
	global IONF4#(10)
	global ESTF4#(10,12)
	global X4#(10,12)
	global Y4#(10,12)
	global Z4#(10,12)
	global DRXS#(10,12)
	global DRYS#(10,12)
	global DRZS#(10,12)
	#COMMON/GEN31/
	global X31#(10,28)
	global Y31#(10,28)
	global Z31#(10,28)
	#COMMON/GEN41/
	global X41#(10,28)
	global Y41#(10,28)
	global Z41#(10,28)
	#
	if(L1 == 0):
		# ZERO COUNTER
		IONF4[NVAC]=0
		for K in range(1,12):
			ESTF4[NVAC][K]=0.0
			return
	# endif
	# STORE EVENT DATA FOR FOURTH GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 12) :
		print(' WARNING FOURTH GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
		sys.exit()
	# endif
	IONF4[NVAC]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF4[NVAC][J]=ESTORE[NVAC][J]
		X4[NVAC][J]=X31[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y4[NVAC][J]=Y31[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z4[NVAC][J]=Z31[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X41[NVAC][L1]=X4[NVAC][J]
		Y41[NVAC][L1]=Y4[NVAC][J]
		Z41[NVAC][L1]=Z4[NVAC][J]
		DRXS[NVAC][J]=DRXE[NVAC][J]
		DRYS[NVAC][J]=DRYE[NVAC][J]
		DRZS[NVAC][J]=DRZE[NVAC][J]
	return
	# end
def CSSTFB5(NVAC,L1,DIST1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	#COMMON/CALCAS4B/
	global IONSUM0#(10)
	global IFLSUM0#(10)
	global ESTORE0#(10,28)
	global EPHOTON0#(10,28)
	global DRXE0#(10,28)
	global DRYE0#(10,28)
	global DRZE0#(10,28)
	global DRX0#(10,28)
	global DRY0#(10,28)
	global DRZ0#(10,28)
	#COMMON/CALCAS5B/
	global IONSUM#(10)
	global IFLSUM#(10)
	global ESTORE#(10,28)
	global EPHOTON#(10,28)
	global DRXE#(10,28)
	global DRYE#(10,28)
	global DRZE#(10,28)
	global DRX#(10,28)
	global DRY#(10,28)
	global DRZ#[10,28]
	#COMMON/GENB5/
	global IONF5#(10)
	global ESTF5#(10,5)
	global X5#(10,5)
	global Y5#(10,5)
	global Z5#(10,5)
	global DRXS#(10,5)
	global DRYS#(10,5)
	global DRZS#(10,5)
	#COMMON/GEN41/
	global X41#(10,28)
	global Y41#(10,28)
	global Z41#(10,28)
	#COMMON/GEN51/
	global X51#(10,28)
	global Y51#(10,28)
	global Z51#(10,28)
	#
	if(L1 == 0):
		# ZERO COUNTER
		IONF5[NVAC]=0
		for K in range(1,5):
			ESTF5[NVAC][K]=0.0
			return
	# endif
	# STORE EVENT DATA FOR FIFTH GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 5) :
		print(' WARNING FIFTH GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
		sys.exit()
	# endif
	IONF5[NVAC]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF5[NVAC][J]=ESTORE[NVAC][J]
		X5[NVAC][J]=X41[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y5[NVAC][J]=Y41[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z5[NVAC][J]=Z41[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X51[NVAC][L1]=X5[NVAC][J]
		Y51[NVAC][L1]=Y5[NVAC][J]
		Z51[NVAC][L1]=Z5[NVAC][J]
		DRXS[NVAC][J]=DRXE[NVAC][J]
		DRYS[NVAC][J]=DRYE[NVAC][J]
		DRZS[NVAC][J]=DRZE[NVAC][J]
	return
	# end
