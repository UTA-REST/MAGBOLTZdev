def CSSTF1E(NVAC,L1,DIST1):           
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)
    # COMMON/CALCASE/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS1E/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # COMMON/GENE1/IONF1(10),ESTF1(10,28),X1(10,28),Y1(10,28),Z1(10,28),DRXS(10,28),DRYS(10,28),DRZS(10,28),T1(10,28)
    #COMMON/CALCASE/
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
    #COMMON/CALCAS1E/
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
    #COMMON/GENE1/
    global IONF1#(10)
    global ESTF1#(10,28)
    global X1#(10,28)
    global Y1#(10,28)
    global Z1#(10,28)
    global DRXS#(10,28)
    global DRYS#(10,28)
    global DRZS#(10,28)
    global T1#(10,28)

    
    # COMMON/GEN111/X11(10,28),Y11(10,28),Z11(10,28),T11(10,28)
    # COMMON/GEN101/X01(10),Y01(10),Z01(10),T01(10)
    #    COMMON/GEN111/
    global X11#(10,28)
    global Y11#(10,28)
    global Z11#(10,28)
    global T11#(10,28)
    #    COMMON/GEN101/
    global X01#(10)
    global Y01#(10)
    global Z01#(10)
    global T01#(10)

    if(L1 == 0):
        # ZERO COUNTER
        IONF1[NVAC]=0
        for K in range(1,28):
            ESTF1[NVAC][K]=0.0
        return
    # endif
    # STORE EVENT DATA FOR FIRST GENERATION FLUORESCENCE
    if(IONSUM[NVAC]> 28) :
        print(' WARNING FIRST GENERATION CONVERTED FLUORESCENCE HAS AN EVENT WITH',IONSUM[NVAC],' IONS.\n',' COMPTON BRANCH NO=',NVAC,'\n')
        sys.exit()
    # endif
    # VEL IN METRES/PICOSECOND
    VV=2.99792458*(10**-4)
    IONF1[NVAC]=IONSUM[NVAC]
    for J in range(1,IONSUM[NVAC]):
        ESTF1[NVAC][J]=ESTORE[NVAC][J]
        X1[NVAC][J]=X01[NVAC]+DIST1*DRX0[NVAC][L1]
        Y1[NVAC][J]=Y01[NVAC]+DIST1*DRY0[NVAC][L1]
        Z1[NVAC][J]=Z01[NVAC]+DIST1*DRZ0[NVAC][L1]
        T1[NVAC][J]=T01[NVAC]+DIST1/VV
        X11[NVAC][L1]=X1[NVAC][J]
        Y11[NVAC][L1]=Y1[NVAC][J]
        Z11[NVAC][L1]=Z1[NVAC][J]
        T11[NVAC][L1]=T1[NVAC][J]
        DRXS[NVAC][J]=DRXE[NVAC][J]
        DRYS[NVAC][J]=DRYE[NVAC][J]
        DRZS[NVAC][J]=DRZE[NVAC][J]
    return
  # end
def CSSTF2E(NVAC,L1,DIST1):               
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)
    # COMMON/CALCAS1E/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS2E/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # COMMON/GENE2/IONF2(10),ESTF2(10,28),X2(10,28),Y2(10,28),Z2(10,28),DRXS(10,28),DRYS(10,28),DRZS(10,28),T2(10,28)
    #COMMON/CALCASE/
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
    #COMMON/CALCAS1E/
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
    #COMMON/GENE1/
    global IONF1#(10)
    global ESTF1#(10,28)
    global X1#(10,28)
    global Y1#(10,28)
    global Z1#(10,28)
    global DRXS#(10,28)
    global DRYS#(10,28)
    global DRZS#(10,28)
    global T1#(10,28)

    
    # COMMON/GEN121/X21(10,28),Y21(10,28),Z21(10,28),T21(10,28)
    # COMMON/GEN111/X11(10,28),Y11(10,28),Z11(10,28),T11(10,28)
    # #   COMMON/GEN121/
    global X21#(10,28)
    global Y21#(10,28)
    global Z21#(10,28)
    global T21#(10,28)
    #    COMMON/GEN111/
    global X11#(10,28)
    global Y11#(10,28)
    global Z11#(10,28)
    global T11#(10,28)

    if(L1 == 0):
        # ZERO COUNTER
        IONF2[NVAC]=0
        for K in range(1,28):
            ESTF2[NVAC][K]=0.0
        return
    # endif
    # STORE EVENT DATA FOR SECOND GENERATION FLUORESCENCE
    if(IONSUM[NVAC]> 28) :
        print(' WARNING SECOND GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.\n',' COMPTON BRANCH NO=',NVAC,'\n')
        sys.exit()
    # endif
    # VEL IN METRES/PICOSECOND
    VV=2.99792458*10**-4
    IONF2[NVAC]=IONSUM[NVAC]
    for J in range(1,IONSUM[NVAC]):
        ESTF2[NVAC][J]=ESTORE[NVAC][J]
        X2[NVAC][J]=X11[NVAC][L1]+DIST1*DRX0[NVAC][L1]
        Y2[NVAC][J]=Y11[NVAC][L1]+DIST1*DRY0[NVAC][L1]
        Z2[NVAC][J]=Z11[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
        T2[NVAC][J]=T11[NVAC][L1]+DIST1/VV
        X21[NVAC][L1]=X2[NVAC][J]
        Y21[NVAC][L1]=Y2[NVAC][J]
        Z21[NVAC][L1]=Z2[NVAC][J]
        T21[NVAC][L1]=T2[NVAC][J]
        DRXS[NVAC][J]=DRXE[NVAC][J]
        DRYS[NVAC][J]=DRYE[NVAC][J]
        DRZS[NVAC][J]=DRZE[NVAC][J]
    return
    # end
def CSSTF3E(NVAC,L1,DIST1):
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)
    # COMMON/CALCAS2E/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS3E/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # COMMON/GENE3/IONF3(10),ESTF3(10,15),X3(10,15),Y3(10,15),Z3(10,15),DRXS(10,15),DRYS(10,15),DRZS(10,15),T3(10,15)
    #COMMON/CALCASE/
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
    #COMMON/CALCAS1E/
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
    #COMMON/GENE1/
    global IONF1#(10)
    global ESTF1#(10,28)
    global X1#(10,28)
    global Y1#(10,28)
    global Z1#(10,28)
    global DRXS#(10,28)
    global DRYS#(10,28)
    global DRZS#(10,28)
    global T1#(10,28)

    
    # COMMON/GEN131/X31(10,28),Y31(10,28),Z31(10,28),T31(10,28)
    # COMMON/GEN121/X21(10,28),Y21(10,28),Z21(10,28),T21(10,28)
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
    # VEL IN METRES/PICOSECOND
    VV=2.99792458*10**-4
    IONF3[NVAC]=IONSUM[NVAC]
    for J in range(1,IONSUM[NVAC]):
        ESTF3[NVAC][J]=ESTORE[NVAC][J]
        X3[NVAC][J]=X21[NVAC][L1]+DIST1*DRX0[NVAC][L1]
        Z3[NVAC][J]=Y21[NVAC][L1]+DIST1*DRY0[NVAC][L1]
        Z3[NVAC][J]=Z21[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
        T3[NVAC][J]=T21[NVAC][L1]+DIST1/VV
        X31[NVAC][L1]=X3[NVAC][J]
        Y31[NVAC][L1]=Z3[NVAC][J]
        Z31[NVAC][L1]=Z3[NVAC][J]
        T31[NVAC][L1]=T3[NVAC][J]
        DRXS[NVAC][J]=DRXE[NVAC][J]
        DRYS[NVAC][J]=DRYE[NVAC][J]
        DRZS[NVAC][J]=DRZE[NVAC][J]
    return
    # end
def CSSTF4E(NVAC,L1,DIST1):
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)
    # COMMON/CALCAS3E/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS4E/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # COMMON/GENE4/IONF4(10),ESTF4(10,12),X4(10,12),Y4(10,12),Z4(10,12),DRXS(10,12),DRYS(10,12),DRZS(10,12),T4(10,12)
    #COMMON/CALCASE/
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
    #COMMON/CALCAS1E/
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
    #COMMON/GENE1/
    global IONF1#(10)
    global ESTF1#(10,28)
    global X1#(10,28)
    global Y1#(10,28)
    global Z1#(10,28)
    global DRXS#(10,28)
    global DRYS#(10,28)
    global DRZS#(10,28)
    global T1#(10,28)
 
    
    # COMMON/GEN131/X31(10,28),Y31(10,28),Z31(10,28),T31(10,28)
    # COMMON/GEN141/X41(10,28),Y41(10,28),Z41(10,28),T41(10,28)
    #
    # #   COMMON/GEN131/
    global X31#(10,28)
    global Y31#(10,28)
    global Z31#(10,28)
    global T31#(10,28)
    #    COMMON/GEN121/
    global X21#(10,28)
    global Y21#(10,28)
    global Z21#(10,28)
    global T21#(10,28)

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
    # VEL IN METRES/PICOSECOND
    VV=2.99792458*10**-4
    IONF4[NVAC]=IONSUM[NVAC]
    DO 1 J=1,IONSUM[NVAC]
        ESTF4[NVAC][J]=ESTORE[NVAC][J]
        X4[NVAC][J]=X31[NVAC][L1]+DIST1*DRX0[NVAC][L1]
        Y4[NVAC][J]=Y31[NVAC][L1]+DIST1*DRY0[NVAC][L1]
        Z4[NVAC][J]=Z31[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
        T4[NVAC][J]=T31[NVAC][L1]+DIST1/VV
        X41[NVAC][L1]=X4[NVAC][J]
        Y41[NVAC][L1]=Y4[NVAC][J]
        Z41[NVAC][L1]=Z4[NVAC][J]
        T41[NVAC][L1]=T4[NVAC][J]
        DRXS[NVAC][J]=DRXE[NVAC][J]
        DRYS[NVAC][J]=DRYE[NVAC][J]
        DRZS[NVAC][J]=DRZE[NVAC][J]
    return
    # end
def CSSTF5E(NVAC,L1,DIST1):
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)
    # COMMON/CALCAS4E/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS5E/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # COMMON/GENE5/IONF5(10),ESTF5(10,5),X5(10,5),Y5(10,5),Z5(10,5),DRXS(10,5),DRYS(10,5),DRZS(10,5),T5(10,5)
    #COMMON/CALCASE/
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
    #COMMON/CALCAS1E/
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
    #COMMON/GENE1/
    global IONF1#(10)
    global ESTF1#(10,28)
    global X1#(10,28)
    global Y1#(10,28)
    global Z1#(10,28)
    global DRXS#(10,28)
    global DRYS#(10,28)
    global DRZS#(10,28)
    global T1#(10,28)

    # COMMON/GEN141/X41(10,28),Y41(10,28),Z41(10,28),T41(10,28)
    # COMMON/GEN151/X51(10,28),Y51(10,28),Z51(10,28),T51(10,28)
    #   COMMON/GEN131/
    global X31#(10,28)
    global Y31#(10,28)
    global Z31#(10,28)
    global T31#(10,28)  
#    COMMON/GEN141/
    global X41#(10,28)
    global Y41#(10,28)
    global Z41#(10,28)
    global T41#(10,28)
    if(L1 == 0):
        # ZERO COUNTER
        IONF5[NVAC]=0
        for K in range(1,5):
            ESTF5[NVAC][K]=0.0
        return
    # endif
    # STORE EVENT DATA FOR FIFTH GENERATION FLUORESCENCE
    if(IONSUM[NVAC]> 5) :
        print(' WARNING FifTH GENERATION CONVERTED FLUORESCENCE HAS AN  EVENT WITH',IONSUM[NVAC],' IONS.','\n COMPTON BRANCH NO=',NVAC,'\n')
        sys.exit()
    # endif
    # VEL IN METRES/PICOSECOND
    VV=2.99792458*10**-4
    IONF5[NVAC]=IONSUM[NVAC]
    for J in range(1,IONSUM[NVAC]):
        ESTF5[NVAC][J]=ESTORE[NVAC][J]
        X5[NVAC][J]=X41[NVAC][L1]+DIST1*DRX0[NVAC][L1]
        Y5[NVAC][J]=Y41[NVAC][L1]+DIST1*DRY0[NVAC][L1]
        Z5[NVAC][J]=Z41[NVAC][L1]+DIST1*DRZ0[NVAC][L1]
        T5[NVAC][J]=T41[NVAC][L1]+DIST1/VV
        X51[NVAC][L1]=X5[NVAC][J]
        Y51[NVAC][L1]=Y5[NVAC][J]
        Z51[NVAC][L1]=Z5[NVAC][J]
        T51[NVAC][L1]=T5[NVAC][J]
        DRXS[NVAC][J]=DRXE[NVAC][J]
        DRYS[NVAC][J]=DRYE[NVAC][J]
        DRZS[NVAC][J]=DRZE[NVAC][J]
    return
    # end