def DRAND48(DUMMY):
	NVEC=1000
	IVEC=0
	if(IVEC == 0 or IVEC >= NVEC):
		RM48(RVEC,NVEC)
		IVEC=1
	else:
		IVEC=IVEC+1
	return RVEC[IVEC]