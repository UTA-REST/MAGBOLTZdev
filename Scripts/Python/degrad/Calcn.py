def CALC(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)
    # SCR=""\
    # SCR1=""
    #COMMON/INPT1/
    global NDVEC
    #COMMON/PRIM3/
    global MSUM#(10000)
    global MCOMP#(10000)
    global MRAYL#(10000)
    global MPAIR#(10000)
    global MPHOT#(10000)
    global MVAC#(10000)
    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#(17)
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]    
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS/
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
    #DIMENSION 
    TEMP=[0 for x in range(17)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    # INITIAL PHOTON DIRECTION  DRX, DRY AND DRZ
    DRXINIT=DRXE[NVAC][1]
    DRYINIT=DRYE[NVAC][1]
    DRZINIT=DRZE[NVAC][1]
    ISHELLST=ISHELL
    def GOTO100():
        ELEFT=ELECEN
        ISHELL=ISHELLST
        API=numpy.arccos(-1.00)
        TWOPI=2.00*API
        ISECOND=1
        IFIRST=0
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        # PHOTONS
        if(ICON == 1):
            IONSUM[NVAC]=1
            IFLSUM[NVAC]=0
            # STORE INITIAL PHOTOELECTRON ENERGY AND ANGLE
            ESTORE[NVAC][1]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
            ELECN=ESTORE[NVAC][1]
            ELEFT=ELEFT-ESTORE[NVAC][1]
            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
            #    ENTRY FOR COMPTON ELECTRON.....
            if(NVAC <= MCOMP[IPN]):
                #    IF COMPTON EVENT ELECTRON ANGLE FROM COMPTON (ALREADY STORED)
                GOTO4()
            # endif
            # USE PHOTOELCTRON ANGULAR DISTRIBUTION
            APE=AA[ISHELL]
            BPE=BB[ISHELL]
            ANGGEN(APE,BPE,THET)
            if(THET < 0.0):
                THET=THET+API
            R3=DRAND48(RDUM)
            PHI=TWOPI*R3
            # INITIAL PHOTON DIRECTION  DRXINIT, DRYINIT AND DRZINIT
            DRCOS(DRXINIT,DRYINIT,DRZINIT,THET,PHI,DRXX,DRYY,DRZZ)
            DRXE[NVAC][1]=DRXX
            DRYE[NVAC][1]=DRYY
            DRZE[NVAC][1]=DRZZ
            GOTO4()
        # endif
        if(ICON == 2):
            # BETA DECAY
            IONSUM[NVAC]=1
            IFLSUM[NVAC]=0
            ISHELL=0
            ELECN=ELECEN
            ESTORE[NVAC][1]=ELECN
            if(NDVEC == 2):
                # RANDOM EMISSION DIRECTION
                R3=DRAND48(RDUM)
                THET=numpy.arccos(1.0-2.0*R3)
            elif(NDVEC == 0):
                # RANDOM EMISSION IN THE X-Y PLANE
                THET=API/2.0
            elif(NDVEC == 1):
                # EMISSION ALONG Z AXIS
                THET=0.00
            elif(NDVEC == -1):
                # EMISSION ALONG -Z AXIS
                THET=numpy.arccos(-1.00)
            else:
                print(' ERROR NDVEC NOT CORRECT SUBROUTINE STOPPED:')
                sys.exit()
            # endif
            R3=DRAND48(RDUM)
            PHI=TWOPI*R3
            DRXE[NVAC][1]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[NVAC][1]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[NVAC][1]=numpy.cos(THET)
        # endif
        # DOUBLE BETA DECAY
        if(ICON == 3):
            IONSUM[NVAC]=1
            IFLSUM[NVAC]=0
            ISHELL=0
            ELECN=ELECEN
            ESTORE[NVAC][1]=ELECN
            ESECOND=ELECN
            if(NDVEC == 2):
                # RANDOM EMISSION DIRECTION
                R3=DRAND48(RDUM)
                THET=numpy.arccos(1.0-2.0*R3)
            elif(NDVEC == 0):
                # RANDOM EMISSION IN THE X-Y PLANE
                THET=API/2.0
            elif(NDVEC == 1):
                # EMISSION ALONG Z AXIS
                THET=0.00
            elif(NDVEC == -1):
                # EMISSION ALONG -Z AXIS
                THET=numpy.arccos(-1.00)
            else:
                print(' ERROR NDVEC NOT CORRECT SUBROUTINE STOPPED:')
                sys.exit()
            # endif
            R3=DRAND48(RDUM)
            PHI=TWOPI*R3
            DRXE[NVAC][1]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[NVAC][1]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[NVAC][1]=numpy.cos(THET)
        # endif
        #
        THESEC=API-THET
        if(PHI < API):
            PHISEC=API+PHI
        else:
            PHISEC=PHI-API
        # endif
        GOTO4()
        def GOTO66():
            IONSUM[NVAC]=IONSUM[NVAC]+1
            ESTORE[NVAC][IONSUM[NVAC]]=ESECOND
            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THESEC)*numpy.cos(PHISEC)
            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THESEC)*numpy.sin(PHISEC)
            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THESEC)
            ELECN=ESECOND
            ISECOND=2
            ISHELL=0
            IFIRST=0
            # LOOP AROUND CASCADE
            def GOTO4():
                # CHECK FOR ELECTRON SHAKEOFF
                IFIRST=IFIRST+1
                if(IFIRST > 1):
                    ELECN=ESTORE[NVAC][IONSUM[NVAC]]
                SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC)
                #  CALCULATE ENERGY OF ELECTRON
                if(JVAC == 0):
                    pass
                else:    
                    if(IFIRST == 1):
                        # INITIAL ELECTRON + SHAKEOFF
                        if(ICON == 1):
                            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                        if(ICON == 2):
                            ELECN=ELECN-ESHK-ELEV[JVAC,(IZ[KGAS,LGAS]+1)]
                        if(ICON == 2 or ICON == 3):
                            ISHELL=JVAC
                        if(ICON == 3):
                            ELECN=ELECN-ESHK-ELEV[JVAC][(IZ[KGAS][LGAS]+2)]
                        # PRIMARY ELECTRON
                        ESTORE[NVAC][IONSUM[NVAC]]=ELECN
                    # endif
                    if(ICON == 1 and IFIRST != 1):
                        ESTORE[NVAC][IONSUM[NVAC]]=ESTORE[NVAC][IONSUM[NVAC]]-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                    # endif
                    IONSUM[NVAC]=IONSUM[NVAC]+1
                    # MAXIMUM ION CHARGE STATE =28
                    if(IONSUM[NVAC]> 28):
                        #WRITE(6,99) IONSUM[NVAC] 
                        #99  
                        print(' WARNING ION CHARGE LIMITED TO 28+ IN THIS VERSION') 
                        sys.exit()
                    # endif
                    # SHAKE ELECTRON
                    ESTORE[NVAC][IONSUM[NVAC]]=ESHK
                    if(ICON == 1):
                        ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                    if(ICON == 2):
                        ELEFT=ELEFT-ESHK-ELEV[JVAC,(IZ[KGAS,LGAS]+1)]
                    if(ICON == 3):
                        ELEFT=ELEFT-ESHK-ELEV[JVAC][(IZ[KGAS][LGAS]+2)]
                    if(ELEFT < 0.0):
                        GOTO100()
                    # RANDOM EMISSION DIRECTION
                    R3=DRAND48(RDUM)
                    THET=numpy.arccos(1.0-2.0*R3)
                    R3=DRAND48(RDUM)
                    PHI=TWOPI*R3
                    DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                    DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                    DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                    # RETURN IF NO SHAKE OFF WITH BETA DECAY
                def GOTO2():
                    if(ICON == 2 and IONSUM[NVAC] == 1):
                        return
                    # GO INTO SECOND BETA LOOP
                    if(ICON == 3 and IONSUM[NVAC]== 1 and ISECOND == 1):
                        GOTO66()
                    if(ICON == 3 and IFIRST == 1 and JVAC == 0 and ISECOND == 2):
                        return
                    #
                    UPDATE(KGAS,LGAS,ISHELL)
                    #  CHOOSE FLUORESCENCE OR AUGER TRANSITION
                    TSUM=0.0
                    for I in range(1,17):
                        TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                        for J in range(1,17):
                            TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                    # NO MORE TRANSITIONS POSSIBLE
                    if(TSUM == 0.0 and ICON == 3 and ISECOND == 1):
                        GOTO66()
                    if(TSUM == 0.0):
                        return  
                    # NORMALISE TO 1.0
                    for I in range(1,17):
                        RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                        for J in range(1,17):
                            AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                    # CREATE CUMULATIVE SUM ARRAY
                    TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                    for I in range(2,17):
                        TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                    TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                    for I in range(2,17):
                        TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                    for J in range(1,16):
                        for I in range(1,17):
                            TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                    # FIND FLUORESCENCE OR AUGER TRANSITION
                    R1=DRAND48(RDUM)
                    for I in range(1,17):
                        if(R1 < TEMP[I]) :
                            # STORE PHOTON ENERGY AND ANGLE : UPDATE NOCC
                            IFLSUM[NVAC]=IFLSUM[NVAC]+1
                            EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                            if(ICON == 2):
                                EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]+1]-ELEV[I][IZ[KGAS][LGAS]+1]
                            if(ICON == 3):
                                EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]+2]-ELEV[I][IZ[KGAS][LGAS]+2]
                            if(EPHOTON[NVAC][IFLSUM[NVAC]] < 0.0):
                                print(' PHOTON ENERGY=','%.3f' % EPHOTON[NVAC][IFLSUM[NVAC]],'NVAC=',NVAC,' IFLSUM=',IFLSUM[NVAC],' IN CALC')
                            ELEFT=ELEFT-abs(EPHOTON[NVAC][IFLSUM[NVAC]])
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R3=DRAND48(RDUM)
                            PHI=TWOPI*R3
                            # CALC DIRECTION COSINES OF FLUORESCENCE
                            DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                            #   
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                #  SECOND ELECTRON IN DOUBLE BETA DECAY
                                if(ICON == 3 and ISECOND == 1):
                                    GOTO66()
                                return    
                            # endif
                        GOTO2()
                        # endif 
                GOTO2()    
                counter116=1
                while(counter116):
                    counter116=0
                    R2=R1-TEMP[17]
                    for J in range(1,17):
                        if(counter116):
                            break
                        for I in range(1,17):
                            if(R2 < TEMP1[I+((J-1)*17)]):
                                # AUGER OR COSTER KRONIG  
                                # STORE EJECTED ELECTRON AND UPDATE NOCC
                                ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                                if(ICON == 2):
                                    ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]+1]-(ELEV[I][IZ[KGAS][LGAS]+1]+ELEV[I][IZ[KGAS][LGAS]+2])*0.5-(ELEV[J][IZ[KGAS][LGAS]+1]+ELEV[J][IZ[KGAS][LGAS]+2])*0.5
                                if(ICON == 3):
                                    ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]+2]-(ELEV[I][IZ[KGAS][LGAS]+2]+ELEV[I][IZ[KGAS][LGAS]+3])*0.5-(ELEV[J][IZ[KGAS][LGAS]+2]+ELEV[J][IZ[KGAS][LGAS]+3])*0.5
                                if(ETEMP < 0.0):
                                    # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                    counter117=1
                                    while(counter117):
                                        counter117=0
                                        R1=DRAND48(RDUM)
                                        if(R1 < TEMP[17]):
                                            counter117=1
                                    counter116=1
                                    break
                                # endif
                                IONSUM[NVAC]=IONSUM[NVAC]+1
                                if(IONSUM[NVAC]> 28): 
                                    print(' IONSUM LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[NVAC],' IN CALC')
                                    sys.exit()
                                # endif
                                ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                                ELEFT=ELEFT-ETEMP
                                if(ELEFT < 0.0):
                                    GOTO100()
                                # RANDOM EMISSION DIRECTION
                                R3=DRAND48(RDUM)
                                THET=numpy.arccos(1.0-2.0*R3)
                                R3=DRAND48(RDUM)
                                PHI=TWOPI*R3
                                DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                                DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                                DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                                NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                                NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                                NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                                # FIND LOWEST VACANCY
                                VACANCY(KGAS,LGAS,ISHELL,ILAST)
                                if(ILAST == 1):
                                    # NO MORE TRANSITIONS POSSIBLE
                                    #  SECOND ELECTRON IN DOUBLE BETA DECAY
                                    if(ICON == 3 and ISECOND == 1):
                                        GOTO66()
                                    return
                                # endif
                                    GOTO4() 
                            # endif
            GOTO4()
        GOTO66()
    GOTO100()
    print(' ERROR IN CASCADE 0') 
    sys.exit() 
    # end
def CALC1(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,L1):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)
    # SCR=""
    #    SCR1=""
    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#(17)
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS/
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
    #COMMON/CALCAS1/
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
    #DIMENSION 
    TEMP=[0 for x in range(17)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS 
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    ISTART=IONSUM[NVAC]
    ISTARTF=IFLSUM[NVAC]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100():
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        IONSUM[NVAC]=ISTART+1
        IFLSUM[NVAC]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[NVAC][IONSUM[NVAC]]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
        ELECN=ESTORE[NVAC][IONSUM[NVAC]]
        ELEFT=ELEFT-ELECN
        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
        # USE PHOTELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=DRAND48(RDUM)
        PHI=TWOPI*R3
        DRCOS(DRX0[NVAC][L1],DRY0[NVAC][L1],DRZ0[NVAC][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[NVAC][IONSUM[NVAC]]=DRXX
        DRYE[NVAC][IONSUM[NVAC]]=DRYY
        DRZE[NVAC][IONSUM[NVAC]]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4():
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[NVAC][IONSUM[NVAC]]
            INSUM=IONSUM[NVAC]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                pass
            else:
                #  ELECTRON + SHAKEOFF
                ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                ESTORE[NVAC][IONSUM[NVAC]]=ELECN
                IONSUM[NVAC]=IONSUM[NVAC]+1
                # MAXIMUM ION CHARGE STATE =28
                if(IONSUM[NVAC]> 28) : 
                    print(' 1ST GEN LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[NVAC])  
                    sys.exit()        
                # endif 
                ESTORE[NVAC][IONSUM[NVAC]]=ESHK 
                ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS,LGAS]]
                if(ELEFT < 0.0):
                    GOTO100()
                # RANDOM EMISSION DIRECTION 
                R3=DRAND48(RDUM)
                THET=numpy.arccos(1.0-2.0*R3)
                R4=DRAND48(RDUM)
                PHI=TWOPI*R4
                DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
            def GOTO2():
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17):
                    TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                    for J in range(1,17):
                        TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17):
                    RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                    for J in range(1,17):
                        AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                for I in range(2,17):
                    TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                for I in range(2,17):
                    TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16):
                    for I in range(1,17):
                        TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][J+1]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=DRAND48(RDUM)
                for I in range(1,17):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND ANGLE : UPDATE NOCC
                        IFLSUM[NVAC]=IFLSUM[NVAC]+1
                        EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                        ELEFT=ELEFT-EPHOTON[NVAC][IFLSUM[NVAC]]
                        if(ELEFT < 0.0):
                            GOTO100()
                        # RANDOM EMISSION DIRECTION
                        R3=DRAND48(RDUM)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=DRAND48(RDUM)       
                        PHI=TWOPI*R4
                        DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                        NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2()
                    # endif
            GOTO2() 
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17):
                    if(counter116):
                        break
                    for I in range(1,17):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=DRAND48(RDUM)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[NVAC]=IONSUM[NVAC]+1
                            if(IONSUM[NVAC]> 28) :
                                print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[NVAC]) #34602
                                sys.exit()
                            # endif
                            ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=DRAND48(RDUM)
                            PHI=TWOPI*R4
                            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4()    
                    # endif
        GOTO4()
    GOTO100()            
    print(' ERROR IN CASCADE 1') 
    sys.exit() 
    # end

def CALC2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,L1):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)

    # SCR=""
    # SCR1=""
    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#(17)
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS/
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
    #COMMON/CALCAS1/
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
    #DIMENSION 
    TEMP=[0 for x in range(17)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    ISTART=IONSUM[NVAC]
    ISTARTF=IFLSUM[NVAC]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100():
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        IONSUM[NVAC]=ISTART+1
        IFLSUM[NVAC]=ISTARTF
        # STORE INITIAL PHOTELECTRON AND ANGLE
        ESTORE[NVAC][IONSUM[NVAC]]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
        ELECN=ESTORE[NVAC][IONSUM[NVAC]]
        ELEFT=ELEFT-ELECN
        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=DRAND48(RDUM)
        PHI=TWOPI*R3
        DRCOS(DRX0[NVAC][L1],DRY0[NVAC][L1],DRZ0[NVAC][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[NVAC][IONSUM[NVAC]]=DRXX
        DRYE[NVAC][IONSUM[NVAC]]=DRYY
        DRZE[NVAC][IONSUM[NVAC]]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4():
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[NVAC][IONSUM[NVAC]]
            INSUM=IONSUM[NVAC]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                pass
            else:
                #  ELECTRON + SHAKEOFF
                ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                ESTORE[NVAC][IONSUM[NVAC]]=ELECN
                IONSUM[NVAC]=IONSUM[NVAC]+1
                # MAXIMUM ION CHARGE STATE =28
                if(IONSUM[NVAC]> 28) :
                    print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[NVAC]) 
                    sys.exit()
                # endif
                ESTORE[NVAC][IONSUM[NVAC]]=ESHK
                ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
                if(ELEFT < 0.0):
                    GOTO100()
                # RANDOM EMISSION DIRECTION
                R3=DRAND48(RDUM)
                THET=numpy.arccos(1.0-2.0*R3)
                R4=DRAND48(RDUM)
                PHI=TWOPI*R4
                DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
            def GOTO2():
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17):
                    TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                    for J in range(1,17):
                        TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17):
                    RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                    for J in range(1,17):
                        AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                for I in range(2,17):
                    TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                for I in range(2,17):
                    TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16):
                    for I in range(1,17):
                        TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=DRAND48(RDUM)
                for I in range(1,17):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[NVAC]=IFLSUM[NVAC]+1
                        EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                        if(EPHOTON[NVAC][IFLSUM[NVAC]] < 0.0):
                            print(' EPHOTON=','%.3f' % EPHOTON[NVAC][IFLSUM[NVAC]],' NVAC=',NVAC,' IN CALC2')
                        ELEFT=ELEFT-EPHOTON[NVAC][IFLSUM[NVAC]]
                        if(ELEFT < 0.0):
                            GOTO100()
                        # RANDOM EMISSION DIRECTION
                        R3=DRAND48(RDUM)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=DRAND48(RDUM)
                        PHI=TWOPI*R4
                        DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                        NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2()
                    # endif
            GOTO2() 
            counter116
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17):
                    if(counter116):
                        break
                    for I in range(1,17):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=DRAND48(RDUM)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1 #34598
                                break
                            # endif
                            IONSUM[NVAC]=IONSUM[NVAC]+1
                            if(IONSUM[NVAC]> 28) :
                                print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[NVAC])
                                sys.exit()
                            # endif
                            ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=DRAND48(RDUM)
                            PHI=TWOPI*R4
                            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4()
                        # endif 
        GOTO4()
    GOTO100()
    print(' ERROR IN CASCADE 2') 
    sys.exit() 
    # end
def CALC3(NVAC,KGAS,LGAS,ELECEN,ISHELL,L1):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)

    #CHARACTER*6 
    # SCR="",
    # SCR1=""
    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#[17]
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS2/
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
    #COMMON/CALCAS3/
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
    TEMP=[0 for x in range(18)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    ISTART=IONSUM[NVAC]
    ISTARTF=IFLSUM[NVAC]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100():
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        IONSUM[NVAC]=ISTART+1
        IFLSUM[NVAC]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[NVAC][IONSUM[NVAC]]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
        ELECN=ESTORE[NVAC][IONSUM[NVAC]]
        ELEFT=ELEFT-ELECN
        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=DRAND48(RDUM)
        PHI=TWOPI*R3
        DRCOS(DRX0[NVAC][L1],DRY0[NVAC][L1],DRZ0[NVAC][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[NVAC][IONSUM[NVAC]]=DRXX
        DRYE[NVAC][IONSUM[NVAC]]=DRYY
        DRZE[NVAC][IONSUM[NVAC]]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4():
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[NVAC][IONSUM[NVAC]]
            INSUM=IONSUM[NVAC]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2()
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            ESTORE[NVAC][IONSUM[NVAC]]=ELECN
            IONSUM[NVAC]=IONSUM[NVAC]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[NVAC]> 28) :
                print(' 3RD GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[NVAC]) 
                sys.exit()
            # endif
            ESTORE[NVAC][IONSUM[NVAC]]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            if(ELEFT < 0.0):
                GOTO100()
            # RANDOM EMISSION ANGLE
            R3=DRAND48(RDUM)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=DRAND48(RDUM)
            PHI=TWOPI*R4
            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
            def GOTO2():
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17):
                    TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                    for J in range(1,17):
                        TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17):
                    RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                    for J in range(1,17):
                        AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                for I in range(2,17):
                    TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                for I in range(2,17):
                    TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16):
                    for I in range(1,17):
                        TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=DRAND48(RDUM)
                for I in range(1,17):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[NVAC]=IFLSUM[NVAC]+1
                        EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                        ELEFT=ELEFT-EPHOTON[NVAC][IFLSUM[NVAC]]
                        if(ELEFT < 0.0):
                            GOTO100()
                        # RANDOM EMISSION DIRECTION
                        R3=DRAND48(RDUM)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=DRAND48(RDUM)
                        PHI=TWOPI*R4
                        DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                        NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2()
                    # endif 
            GOTO2()  
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17):
                    if(counter116):
                        break
                    for I in range(1,17):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=DRAND48(RDUM)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                                # endif
                            IONSUM[NVAC]=IONSUM[NVAC]+1
                            if(IONSUM[NVAC]> 28) :
                                print(' 3RD GEN ION CHARGE LIMITED TO 28  IONSUM=', IONSUM[NVAC])
                                sys.exit()
                            # endif
                            ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=DRAND48(RDUM)
                            PHI=TWOPI*R4
                            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4() 
                        # endif
        GOTO4()
    GOTO100()
    print(' ERROR IN CASCADE 3') 
    sys.exit() 
    # end

def CALC4(NVAC,KGAS,LGAS,ELECEN,ISHELL,L1):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)
    # SCR=""\nSCR1=""
    # COMMON/GENCAS/ELEV[17,79],NSDEG(17),AA[17],BB[17],SCR,SCR1
    # COMMON/MIXC/PRSH(6,3,17,17),ESH(6,3,17),AUG(6,3,17,17,17),RAD[6,3,17,17],PRSHBT(6,3,17),IZ[6,3],INIOCC(6,3,17),ISHLMX(6,3),AMZ[6,3]
    # COMMON/UPD/NOCC(6,3,17),AUGR(6,3,17,17,17),RADR(6,3,17,17)
    # COMMON/CALCAS3/IONSUM0(10),IFLSUM0(10),ESTORE0(10,28),EPHOTON0(10,28),DRXE0(10,28),DRYE0(10,28),DRZE0(10,28),DRX0(10,28),DRY0(10,28),DRZ0(10,28)
    # COMMON/CALCAS4/IONSUM(10),IFLSUM(10),ESTORE(10,28),EPHOTON(10,28),DRXE(10,28),DRYE(10,28),DRZE(10,28),DRX(10,28),DRY(10,28),DRZ[10,28]
    # DIMENSION TEMP[17],TEMP1(289)

    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#[17]
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS3/
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
    # COMMON/CALCAS4/
    global IONSUM#(10]
    global IFLSUM#(10]
    global ESTORE#(10,28]
    global EPHOTON#(10,28]
    global DRXE#(10,28]
    global DRYE#(10,28]
    global DRZE#(10,28]
    global DRX#(10,28]
    global DRY#(10,28]
    global DRZ#[10,28]
    #DIMENSION
    TEMP=[0 for x in range(17)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    ISTART=IONSUM[NVAC]
    ISTARTF=IFLSUM[NVAC]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100():
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        IONSUM[NVAC]=ISTART+1
        IFLSUM[NVAC]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[NVAC][IONSUM[NVAC]]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
        ELECN=ESTORE[NVAC][IONSUM[NVAC]]
        ELEFT=ELEFT-ELECN
        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=DRAND48(RDUM)
        PHI=TWOPI*R3
        DRCOS(DRX0(NVAC,L1),DRY0(NVAC,L1),DRZ0(NVAC,L1),THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[NVAC][IONSUM[NVAC]]=DRXX
        DRYE[NVAC][IONSUM[NVAC]]=DRYY
        DRZE[NVAC][IONSUM[NVAC]]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4():
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[NVAC][IONSUM[NVAC]]
            INSUM=IONSUM[NVAC]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2()
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            ESTORE[NVAC][IONSUM[NVAC]]=ELECN
            IONSUM[NVAC]=IONSUM[NVAC]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[NVAC]> 28) :
                print(' 4TH GEN ION CHARGE LIMITED TO 28 IONSUM=',IONSUM[NVAC]) 
                sys.exit()
            # endif
            ESTORE[NVAC][IONSUM[NVAC]]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            if(ELEFT < 0.0):
                GOTO100()
            # RANDOM EMISSION ANGLE
            R3=DRAND48(RDUM)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=DRAND48(RDUM)
            PHI=TWOPI*R4
            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
            def GOTO2():
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17):
                    TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                    for J in range(1,17):
                        TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17):
                    RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                    for J in range(1,17):
                        AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                for I in range(2,17):
                    TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                for I in range(2,17):
                    TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16):
                    for I in range(1,17):
                        TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=DRAND48(RDUM)
                for I in range(1,17):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[NVAC]=IFLSUM[NVAC]+1
                        EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                        ELEFT=ELEFT-EPHOTON[NVAC][IFLSUM[NVAC]]
                        if(ELEFT < 0.0):
                            GOTO100()
                        # RANDOM EMISSION DIRECTION
                        R3=DRAND48(RDUM)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=DRAND48(RDUM)
                        PHI=TWOPI*R4
                        DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                        NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2()
                    # endif 
            GOTO2()
            counter116=1
            while(counter116):
                R2=R1-TEMP[17]
                for J in range(1,17):
                    if(counter116):
                        break
                    for I in range(1,17):
                        if(R2 < TEMP1(I+((J-1)*17))) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=DRAND48(RDUM)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[NVAC]=IONSUM[NVAC]+1
                            if(IONSUM[NVAC]> 28) :
                                print(' 4TH GEN ION CHARGE LIMITED TO 28 IONSUM=',IONSUM[NVAC])
                                sys.exit()
                            # endif
                            ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=DRAND48(RDUM)
                            PHI=TWOPI*R4
                            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4() 
                        # endif
        GOTO4()
    GOTO100()            
    print(' ERROR IN CASCADE 4') 
    sys.exit() 
    # end

def CALC5(NVAC,KGAS,LGAS,ELECEN,ISHELL,L1):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)
    # SCR=""\nSCR1=""
    #COMMON/GENCAS/
    global ELEV#[17,79]
    global NSDEG#[17]
    global AA#[17]
    global BB#[17]
    global SCR,SCR1
    #COMMON/MIXC/
    global PRSH#(6,3,17,17)
    global ESH#(6,3,17)
    global AUG#(6,3,17,17,17)
    global RAD#[6,3,17,17]
    global PRSHBT#(6,3,17)
    global IZ#[6,3]
    global INIOCC#(6,3,17)
    global ISHLMX#(6,3)
    global AMZ#[6,3]
    #COMMON/UPD/
    global NOCC#(6,3,17)
    global AUGR#(6,3,17,17,17)
    global RADR#(6,3,17,17)
    #COMMON/CALCAS4/
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
    #COMMON/CALCAS5/
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
    #DIMENSION 
    TEMP=[0 for x in range(17)]
    TEMP1=[0 for x in range(289)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    ISTART=IONSUM[NVAC]
    ISTARTF=IFLSUM[NVAC]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100():
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17):
            NOCC[KGAS][LGAS][I]=INIOCC[KGAS][LGAS][I]
        IONSUM[NVAC]=ISTART+1
        IFLSUM[NVAC]=ISTARTF
        ESTORE[NVAC][IONSUM[NVAC]]=ELECEN-ELEV[ISHELL][IZ[KGAS][LGAS]]
        ELECN=ESTORE[NVAC][IONSUM[NVAC]]
        ELEFT=ELEFT-ELECN
        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=DRAND48(RDUM)
        PHI=TWOPI*R3
        DRCOS(DRX0[NVAC][L1],DRY0[NVAC][L1],DRZ0[NVAC][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[NVAC][IONSUM[NVAC]]=DRXX
        DRYE[NVAC][IONSUM[NVAC]]=DRYY
        DRZE[NVAC][IONSUM[NVAC]]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4():
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[NVAC][IONSUM[NVAC]]
            INSUM=IONSUM[NVAC]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2()
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            ESTORE[NVAC][IONSUM[NVAC]]=ELECN
            IONSUM[NVAC]=IONSUM[NVAC]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[NVAC]> 28) :
                print(' 5TH GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[NVAC])
                sys.exit() 
            # endif
            ESTORE[NVAC][IONSUM[NVAC]]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS][LGAS]]
            if(ELEFT < 0.0):
                GOTO100()
            # RANDOM EMISSION ANGLE
            R3=DRAND48(RDUM)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=DRAND48(RDUM)
            PHI=TWOPI*R4
            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
            def GOTO2():
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17):
                    TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
                    for J in range(1,17):
                        TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17):
                    RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
                    for J in range(1,17):
                        AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
                for I in range(2,17):
                    TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
                for I in range(2,17):
                    TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16):
                    for I in range(1,17):
                        TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=DRAND48(RDUM)
                for I in range(1,17):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[NVAC]=IFLSUM[NVAC]+1
                        EPHOTON[NVAC][IFLSUM[NVAC]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                        ELEFT=ELEFT-EPHOTON[NVAC][IFLSUM[NVAC]]
                        if(ELEFT < 0.0):
                            GOTO100()
                        # RANDOM EMISSION DIRECTION
                        R3=DRAND48(RDUM)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=DRAND48(RDUM)
                        PHI=TWOPI*R4
                        DRX[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[NVAC][IFLSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[NVAC][IFLSUM[NVAC]]=numpy.cos(THET)
                        NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                        NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2()
                    # endif 
            GOTO2()
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17):
                    if(counter116):
                        break
                    for I in range(1,17):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[KGAS][LGAS]]-(ELEV[I][IZ[KGAS][LGAS]]+ELEV[I][IZ[KGAS][LGAS]+1])*0.5-(ELEV[J][IZ[KGAS][LGAS]]+ELEV[J][IZ[KGAS][LGAS]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=DRAND48(RDUM)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[NVAC]=IONSUM[NVAC]+1
                            if(IONSUM[NVAC]> 28) :
                                print(' 5TH GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[NVAC])
                                sys.exit()
                            # endif
                            ESTORE[NVAC][IONSUM[NVAC]]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100()
                            # RANDOM EMISSION DIRECTION
                            R3=DRAND48(RDUM)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=DRAND48(RDUM)
                            PHI=TWOPI*R4
                            DRXE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[NVAC][IONSUM[NVAC]]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[NVAC][IONSUM[NVAC]]=numpy.cos(THET)
                            NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                            NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                            NOCC[KGAS][LGAS][J]=NOCC[KGAS][LGAS][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4() 
                        # endif
        GOTO4()
    GOTO100()    
    print(' ERROR IN CASCADE 5') 
    sys.exit() 
  # end
