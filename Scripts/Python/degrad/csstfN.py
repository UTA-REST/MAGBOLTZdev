def CSSTF1(NEV,NVAC,L1,DIST1):           
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	COMMON/CALCAS/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	COMMON/CALCAS1/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	COMMON/GEN1/IONF1(10,10000),ESTF1(10,28,10000),X1(10,28,10000),Y1(10,28,10000),Z1(10,28,10000),DRXS(10,28,10000),DRYS(10,28,10000),DRZS(10,28,10000)
	COMMON/GEN11/X11(10,28),Y11(10,28),Z11(10,28)
	COMMON/GEN01/X01(10),Y01(10),Z01(10)
	# STORE EVENT DATA FOR FIRST GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 28) :
		print(' WARNING FIRST GENERATION CONVERTED FLUORESCENCE HAS AN EVENT WITH',I3IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',I3NVAC,'\n PRIMARY INTERACTION NUMBER =',I3NEV)
		sys.exit()
	# endif
	IONF1[NVAC][NEV]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF1[NVAC][J][NEV]=ESTORE[NVAC][J]
		X1[NVAC][J][NEV]=X01[NVAC]+DIST1*DRX0[NVAC][L1]
		Y1[NVAC][J][NEV]=Y01[NVAC]+DIST1*DRY0[NVAC][L1]
		Z1[NVAC][J][NEV]=Z01[NVAC]+DIST1*DRZ0[NVAC][L1]
		X11[NVAC][L1]=X1[NVAC][J][NEV]
		Y11[NVAC][L1]=Y1[NVAC][J][NEV]
		Z11[NVAC][L1]=Z1[NVAC][J][NEV]
		DRXS[NVAC][J][NEV]=DRXE[NVAC][J]
		DRYS[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZS[NVAC][J][NEV]=DRZE[NVAC][J]
	return
	# end
def CSSTF2(NEV,NVAC,L1,DIST1):               
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	COMMON/CALCAS1/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	COMMON/CALCAS2/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	COMMON/GEN2/IONF2(10,10000),ESTF2(10,28,10000),X2(10,28,10000),Y2(10,28,10000),Z2(10,28,10000),DRXS(10,28,10000),DRYS(10,28,10000),DRZS(10,28,10000)
	COMMON/GEN21/X21(10,28),Y21(10,28),Z21(10,28)
	COMMON/GEN11/X11(10,28),Y11(10,28),Z11(10,28)
	# STORE EVENT DATA FOR SECOND GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 28) :
		print(' WARNING SECOND GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n PRIMARY INTERACTION NUMBER =',NEV)
		sys.exit()
	# endif
	IONF2[NVAC][NEV]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF2[NVAC][J][NEV]=ESTORE[NVAC][J]
		X2[NVAC][J][NEV]=X11[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y2[NVAC][J][NEV]=Y11[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z2[NVAC][J][NEV]=Z11[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X21[NVAC][L1]=X2[NVAC][J][NEV]
		Y21[NVAC][L1]=Y2[NVAC][J][NEV]
		Z21[NVAC][L1]=Z2[NVAC][J][NEV]
		DRXS[NVAC][J][NEV]=DRXE[NVAC][J]
		DRYS[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZS[NVAC][J][NEV]=DRZE[NVAC][J]
	return
	# end
def CSSTF3(NEV,NVAC,L1,DIST1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	COMMON/CALCAS2/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	COMMON/CALCAS3/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	COMMON/GEN3/IONF3(10,10000),ESTF3(10,15,10000),X3(10,15,10000),Y3(10,15,10000),Z3(10,15,10000),DRXS(10,15,10000),DRYS(10,15,10000),DRZS(10,15,10000)
	COMMON/GEN31/X31(10,28),Y31(10,28),Z31(10,28)
	COMMON/GEN21/X21(10,28),Y21(10,28),Z21(10,28)
	# STORE EVENT DATA FOR THIRD GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 15) :
		print(' WARNING THIRD GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',INVAC3,'\n PRIMARY INTERACTION NUMBER =',NEV)
		sys.exit()
	# endif
	IONF3[NVAC][NEV]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF3[NVAC][J][NEV]=ESTORE[NVAC][J]
		X3[NVAC][J][NEV]=X21[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y3[NVAC][J][NEV]=Y21[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z3[NVAC][J][NEV]=Z21[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X31[NVAC][L1]=X3[NVAC][J][NEV]
		Y31[NVAC][L1]=Y3[NVAC][J][NEV]
		Z31[NVAC][L1]=Z3[NVAC][J][NEV]
		DRXS[NVAC][J][NEV]=DRXE[NVAC][J]
		DRYS[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZS[NVAC][J][NEV]=DRZE[NVAC][J]
	return
	# end
def CSSTF4(NEV,NVAC,L1,DIST1):
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	COMMON/CALCAS3/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	COMMON/CALCAS4/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	COMMON/GEN4/IONF4(10,10000),ESTF4(10,12,10000),X4(10,12,10000),Y4(10,12,10000),Z4(10,12,10000),DRXS(10,12,10000),DRYS(10,12,10000),DRZS(10,12,10000)
	COMMON/GEN31/X31(10,28),Y31(10,28),Z31(10,28)
	COMMON/GEN41/X41(10,28),Y41(10,28),Z41(10,28)
	# STORE EVENT DATA FOR FOURTH GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 12) :
		print(' WARNING FOURTH GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n PRIMARY INTERACTION NUMBER =',NEV)
		sys.exit()
	# endif
	IONF4[NVAC][NEV]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF4[NVAC][J][NEV]=ESTORE[NVAC][J]
		X4[NVAC][J][NEV]=X31[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y4[NVAC][J][NEV]=Y31[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z4[NVAC][J][NEV]=Z31[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X41[NVAC][L1]=X4[NVAC][J][NEV]
		Y41[NVAC][L1]=Y4[NVAC][J][NEV]
		Z41[NVAC][L1]=Z4[NVAC][J][NEV]
		DRXS[NVAC][J][NEV]=DRXE[NVAC][J]
		DRYS[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZS[NVAC][J][NEV]=DRZE[NVAC][J]
	1 CONTINUE
	return
	# end
def CSSTF5(NEV,NVAC,L1,DIST1): 
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	COMMON/CALCAS4/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
	COMMON/CALCAS5/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
	COMMON/GEN5/IONF5(10,10000),ESTF5(10,5,10000),X5(10,5,10000),Y5(10,5,10000),Z5(10,5,10000),DRXS(10,5,10000),DRYS(10,5,10000),DRZS(10,5,10000)
	COMMON/GEN41/X41(10,28),Y41(10,28),Z41(10,28)
	COMMON/GEN51/X51(10,28),Y51(10,28),Z51(10,28)
	# STORE EVENT DATA FOR FIFTH GENERATION FLUORESCENCE
	if(IONSUM[NVAC]> 5) :
		print(' WARNING FIFTH GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.\n',' COMPTON BRANCH NO=',NVAC,'\n PRIMARY INTERACTION NUMBER=',NEV)
		sys.exit()
	# endif
	IONF5[NVAC][NEV]=IONSUM[NVAC]
	for J in range(1,IONSUM[NVAC]):
		ESTF5[NVAC][J][NEV]=ESTORE[NVAC][J]
		X5[NVAC][J][NEV]=X41[NVAC][L1]+DIST1*DRX0[NVAC][L1]
		Y5[NVAC][J][NEV]=Y41[NVAC][L1]+DIST1*DRY0[NVAC][L1]
		Z5[NVAC][J][NEV]=Z41[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
		X51[NVAC][L1]=X5[NVAC][J][NEV]
		Y51[NVAC][L1]=Y5[NVAC][J][NEV]
		Z51[NVAC][L1]=Z5[NVAC][J][NEV]
		DRXS[NVAC][J][NEV]=DRXE[NVAC][J]
		DRYS[NVAC][J][NEV]=DRYE[NVAC][J]
		DRZS[NVAC][J][NEV]=DRZE[NVAC][J]
	return
	# end