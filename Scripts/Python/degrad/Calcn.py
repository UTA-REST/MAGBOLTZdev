import conf
import numpy
import random
from Shake import *
def CALC(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
    # IMPLICIT #real*8(A-H,O-Z)
    # IMPLICIT #integer*8(I-N)
    # SCR=""\
    # SCR1=""
    global IFIRST,ESHK,ELECN,JVAC,R1
    ESHK=0.0
    JVAC=0.0
    def get_globals():
        NDVEC=conf.NDVEC
        MSUM=conf.MSUM
        MCOMP=conf.MCOMP
        MRAYL=conf.MRAYL
        MPAIR=conf.MPAIR
        MPHOT=conf.MPHOT
        MVAC=conf.MVAC
        ELEV=conf.ELEV
        NSDEG=conf.NSDEG
        AA=conf.AA
        BB=conf.BB
        SCR=conf.SCR
        SCR1=conf.SCR1
        PRSH=conf.PRSH
        ESH=conf.ESH
        AUG=conf.AUG
        RAD=conf.RAD
        PRSHBT=conf.PRSHBT
        IZ=conf.IZ
        INIOCC=conf.INIOCC
        ISHLMX=conf.ISHLMX
        AMZ=conf.AMZ
        NOCC=conf.NOCC
        AUGR=conf.AUGR
        RADR=conf.RADR
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
        globals().update(locals())    
    get_globals()
    def update_globals():
        conf.NDVEC=NDVEC
        conf.MSUM=MSUM
        conf.MCOMP=MCOMP
        conf.MRAYL=MRAYL
        conf.MPAIR=MPAIR
        conf.MPHOT=MPHOT
        conf.MVAC=MVAC
        conf.ELEV=ELEV
        conf.NSDEG=NSDEG
        conf.AA=AA
        conf.BB=BB
        conf.SCR,SCR1=SCR,SCR1
        conf.PRSH=PRSH
        conf.ESH=ESH
        conf.AUG=AUG
        conf.RAD=RAD
        conf.PRSHBT=PRSHBT
        conf.IZ=IZ
        conf.INIOCC=INIOCC
        conf.ISHLMX=ISHLMX
        conf.AMZ=AMZ
        conf.NOCC=NOCC
        conf.AUGR=AUGR
        conf.RADR=RADR
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
        globals().update(locals())
    #DIMENSION 
    TEMP=[0 for x in range(17+1)]
    TEMP1=[0 for x in range(289+1)]
    #
    # CALCULATE CASCADE IN GAS KGAS AND MOLECULAR COMPONENT LGAS
    # WITH INTIAL ENERGY DEPOSIT ELECEN AND SHELL VACANCY CREATED AT ISHELL
    #
    # INITIAL PHOTON DIRECTION  DRX, DRY AND DRZ
    DRXINIT=DRXE[int(NVAC)][1]
    DRYINIT=DRYE[int(NVAC)][1]
    DRZINIT=DRZE[int(NVAC)][1]
    ISHELLST=ISHELL
    def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        global IFIRST,ESHK,ELECN,JVAC
        if(ICON==2 and IONSUM[int(NVAC)] == 1):
            return
        # GO INTO SECOND BETA LOOP
        print("calc 104 ICON,IONSUM[int(NVAC)],ISECOND= ",ICON,IONSUM[int(NVAC)],ISECOND)
        if(ICON == 3 and IONSUM[int(NVAC)] == 1 and ISECOND == 1):
            GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
        print("calc 107 ICON,IFIRST,JVAC,ISECOND= ",ICON,IFIRST,JVAC,ISECOND)
        if(ICON == 3 and IFIRST == 1 and JVAC == 0 and ISECOND == 2):
            return 1
        # C
        update_globals()
        UPDATE(KGAS,LGAS,ISHELL)
        # C  CHOOSE FLUORESCENCE OR AUGER TRANSITION
        TSUM=0.0
        for I in range(1,17+1):
            TSUM=TSUM+RADR[KGAS][LGAS][ISHELL][I]
            for J in range(1,17+1):
                TSUM=TSUM+AUGR[KGAS][LGAS][ISHELL][I][J]
            # 10 CONTINUE
        # C NO MORE TRANSITIONS POSSIBLE
        if(TSUM == 0.0 and ICON == 3 and ISECOND == 1):
            globals().update(locals())

            GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
        if(TSUM == 0.0):
            return 1
        # C NORMALISE TO 1.0
        for I in range(1,17+1):
            RADR[KGAS][LGAS][ISHELL][I]=RADR[KGAS][LGAS][ISHELL][I]/TSUM
            for J in range(1,17+1):
                AUGR[KGAS][LGAS][ISHELL][I][J]=AUGR[KGAS][LGAS][ISHELL][I][J]/TSUM
        # 11 CONTINUE
        # C CREATE CUMULATIVE SUM ARRAY
        TEMP[1]=RADR[KGAS][LGAS][ISHELL][1]
        for I in range(2,17+1):
            TEMP[I]=RADR[KGAS][LGAS][ISHELL][I]+TEMP[I-1]
        # 12 CONTINUE
        TEMP1[1]=AUGR[KGAS][LGAS][ISHELL][1][1]
        for I in range(2,17+1):
            TEMP1[I]=AUGR[KGAS][LGAS][ISHELL][I][1]+TEMP1[I-1]
        # 13 CONTINUE
        for J in range(1,16+1):
            for I in range(1,17+1):
                TEMP1[I+(J*17)]=AUGR[KGAS][LGAS][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
        # 14 CONTINUE
        # C FIND FLUORESCENCE OR AUGER TRANSITION
        # 15 
        R1=random.uniform(0.0,1.0)
        for I in range(1,17+1):
            if(R1 < TEMP[I]):
                # C STORE PHOTON ENERGY AND ANGLE THEN UPDATE NOCC
                IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[KGAS][LGAS]]-ELEV[I][IZ[KGAS][LGAS]]
                if(ICON == 2):
                    EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[KGAS][LGAS]+1]-ELEV[I][IZ[KGAS][LGAS]+1]
                if(ICON == 3):
                    EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[KGAS][LGAS]+2]-ELEV[I][IZ[KGAS][LGAS]+2]
                if(EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]] < 0.0):
                    # WRITE(6,545) 
                    # 545  
                    print(' PHOTON ENERGY=%.3f NVAC=%d IFLSUM=%d IN CALC'%(EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]],IFLSUM[int(NVAC)],NVAC))
                ELEFT=ELEFT-DABS(EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]])
                if(ELEFT < 0.0):
                    GOTO100()
                # C RANDOM EMISSION DIRECTION
                R3=random.uniform(0.0,1.0)
                THET=numpy.arccos(1.0-2.0*R3)
                R3=random.uniform(0.0,1.0)
                PHI=TWOPI*R3
                # C CALC DIRECTION COSINES OF FLUORESCENCE
                DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                # C   
                NOCC[KGAS][LGAS][ISHELL]=NOCC[KGAS][LGAS][ISHELL]+1
                NOCC[KGAS][LGAS][I]=NOCC[KGAS][LGAS][I]-1
                # C FIND LOWEST VACANCY
                update_globals()
                VACANCY(KGAS,LGAS,ISHELL,ILAST)
                if(ILAST == 1):
                    # C NO MORE TRANSITIONS POSSIBLE
                    # C  SECOND ELECTRON IN DOUBLE BETA DECAY
                    if(ICON == 3 and ISECOND == 1):
                        globals().update(locals())
                        GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    return    
                # ENDif
                globals().update(locals())
                GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            # ENDif 
        # 16 CONTINUE
        globals().update(locals())
        return 1
    def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        global IFIRST,ESHK,ELECN,JVAC
        globals().update(locals())
        # CHECK FOR ELECTRON SHAKEOFF
        IFIRST=IFIRST+1
        if(IFIRST > 1):
            ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        globals().update(locals())    
        ISHELL,ELECN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC=SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,ICON,IFIRST,JVAC)
        globals().update(locals())    
        #  CALCULATE ENERGY OF ELECTRON
        print("calc 203 JVAC=",JVAC)
        if(JVAC == 0):
            pass
        else:    
            if(IFIRST == 1):
                # INITIAL ELECTRON + SHAKEOFF
                if(ICON == 1):
                    ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
                if(ICON == 2):
                    ELECN=ELECN-ESHK-ELEV[JVAC,(IZ[KGAS][int(LGAS)]+1)]
                if(ICON == 2 or ICON == 3):
                    ISHELL=JVAC
                if(ICON == 3):
                    ELECN=ELECN-ESHK-ELEV[JVAC][(IZ[int(KGAS)][int(LGAS)]+2)]
                # PRIMARY ELECTRON
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
            # endif
            if(ICON == 1 and IFIRST != 1):
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            # endif
            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[int(NVAC)]> 28):
                #WRITE(6,99) IONSUM[int(NVAC)] 
                #99  
                print(' WARNING ION CHARGE LIMITED TO 28+ IN THIS VERSION') 
                sys.exit()
            # endif
            # SHAKE ELECTRON
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK
            if(ICON == 1):
                ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            if(ICON == 2):
                ELEFT=ELEFT-ESHK-ELEV[JVAC,(IZ[KGAS,LGAS]+1)]
            if(ICON == 3):
                ELEFT=ELEFT-ESHK-ELEV[JVAC][(IZ[int(KGAS)][int(LGAS)]+2)]
            if(ELEFT < 0.0):
                globals().update(locals())    
                complete=GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                return complete
            # RANDOM EMISSION DIRECTION
            R3=random.uniform(0.0,1.0)
            THET=numpy.arccos(1.0-2.0*R3)
            R3=random.uniform(0.0,1.0)
            PHI=TWOPI*R3
            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            # RETURN IF NO SHAKE OFF WITH BETA DECAY
        
        complete=GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)    
        if(complete):
            return 1
        counter116=1
        while(counter116):
            counter116=0
            R2=R1-TEMP[17]
            for J in range(1,17+1):
                if(counter116):
                    break
                for I in range(1,17+1):
                    if(R2 < TEMP1[I+((J-1)*17)]):
                        # AUGER OR COSTER KRONIG  
                        # STORE EJECTED ELECTRON AND UPDATE NOCC
                        ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                        if(ICON == 2):
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]+1]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]+1]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+2])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]+1]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+2])*0.5
                        if(ICON == 3):
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]+2]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]+2]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+3])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]+2]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+3])*0.5
                        if(ETEMP < 0.0):
                            # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                            counter117=1
                            while(counter117):
                                counter117=0
                                R1=random.uniform(0.0,1.0)
                                if(R1 < TEMP[17]):
                                    counter117=1
                            counter116=1
                            break
                        # endif
                        IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                        if(IONSUM[int(NVAC)]> 28): 
                            print(' IONSUM LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[int(NVAC)],' IN CALC')
                            sys.exit()
                        # endif
                        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                        ELEFT=ELEFT-ETEMP
                        if(ELEFT < 0.0):
                            GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R3=random.uniform(0.0,1.0)
                        PHI=TWOPI*R3
                        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            #  SECOND ELECTRON IN DOUBLE BETA DECAY
                            if(ICON == 3 and ISECOND == 1):
                                GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            update_globals()
                            return
                        # endif
                        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
                    # endif

        globals().update(locals())
    def GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        global IFIRST,ESHK,ELECN,JVAC
        IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESECOND
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THESEC)*numpy.cos(PHISEC)
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THESEC)*numpy.sin(PHISEC)
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THESEC)
        ELECN=ESECOND
        ISECOND=2
        ISHELL=0
        IFIRST=0
        # LOOP AROUND CASCADE
        globals().update(locals())
        
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
        return 1
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        print("calcn ISHELL=", ISHELL)
        global IFIRST,ESHK,ELECN,JVAC
        complete=0
        ELEFT=ELECEN
        ISHELL=ISHELLST
        API=numpy.arccos(-1.00)
        TWOPI=2.00*API
        ISECOND=1
        IFIRST=0
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        # PHOTONS
        print("344 calc ICON=",ICON)
        if(ICON == 1):
            IONSUM[int(NVAC)]=1
            IFLSUM[int(NVAC)]=0
            # STORE INITIAL PHOTOELECTRON ENERGY AND ANGLE
            ESTORE[int(NVAC)][1]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
            ELECN=ESTORE[int(NVAC)][1]
            ELEFT=ELEFT-ESTORE[int(NVAC)][1]
            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
            #    ENTRY FOR COMPTON ELECTRON.....
            if(NVAC <= MCOMP[IPN]):
                #    IF COMPTON EVENT ELECTRON ANGLE FROM COMPTON (ALREADY STORED)
                globals().update(locals())    
                complete=GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                return complete
            # endif
            # USE PHOTOELCTRON ANGULAR DISTRIBUTION
            APE=AA[ISHELL]
            BPE=BB[ISHELL]
            ANGGEN(APE,BPE,THET)
            if(THET < 0.0):
                THET=THET+API
            R3=random.uniform(0.0,1.0)
            PHI=TWOPI*R3
            # INITIAL PHOTON DIRECTION  DRXINIT, DRYINIT AND DRZINIT
            DRCOS(DRXINIT,DRYINIT,DRZINIT,THET,PHI,DRXX,DRYY,DRZZ)
            DRXE[int(NVAC)][1]=DRXX
            DRYE[int(NVAC)][1]=DRYY
            DRZE[int(NVAC)][1]=DRZZ
            globals().update(locals())    
            complete=GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            return complete
        # endif
        if(ICON == 2):
            # BETA DECAY
            IONSUM[int(NVAC)]=1
            IFLSUM[int(NVAC)]=0
            ISHELL=0
            ELECN=ELECEN
            ESTORE[int(NVAC)][1]=ELECN
            if(NDVEC == 2):
                # RANDOM EMISSION DIRECTION
                R3=random.uniform(0.0,1.0)
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
            R3=random.uniform(0.0,1.0)
            PHI=TWOPI*R3
            DRXE[int(NVAC)][1]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][1]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][1]=numpy.cos(THET)
        # endif
        # DOUBLE BETA DECAY
        if(ICON == 3):
            IONSUM[int(NVAC)]=1
            IFLSUM[int(NVAC)]=0
            ISHELL=0
            ELECN=ELECEN
            ESTORE[int(NVAC)][1]=ELECN
            ESECOND=ELECN
            if(NDVEC == 2):
                # RANDOM EMISSION DIRECTION
                R3=random.uniform(0.0,1.0)
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
            R3=random.uniform(0.0,1.0)
            PHI=TWOPI*R3
            DRXE[int(NVAC)][1]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][1]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][1]=numpy.cos(THET)
        # endif
        #
        THESEC=API-THET
        if(PHI < API):
            PHISEC=API+PHI
        else:
            PHISEC=PHI-API
        # endif
        globals().update(locals())
        print("calc IFIRST=",IFIRST)
        complete=GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
        print("got this ",complete)
        return complete
        globals().update(locals())

        GOTO66(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    globals().update(locals())    
    complete=GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    if(complete):
        return
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
    ISTART=IONSUM[int(NVAC)]
    ISTARTF=IFLSUM[int(NVAC)]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        IONSUM[int(NVAC)]=ISTART+1
        IFLSUM[int(NVAC)]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
        ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        ELEFT=ELEFT-ELECN
        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
        # USE PHOTELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=random.uniform(0.0,1.0)
        PHI=TWOPI*R3
        DRCOS(DRX0[int(NVAC)][L1],DRY0[int(NVAC)][L1],DRZ0[int(NVAC)][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRXX
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRYY
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
            INSUM=IONSUM[int(NVAC)]
            globals().update(locals())
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                pass
            else:
                #  ELECTRON + SHAKEOFF
                ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
                IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                # MAXIMUM ION CHARGE STATE =28
                if(IONSUM[int(NVAC)]> 28) : 
                    print(' 1ST GEN LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[int(NVAC)])  
                    sys.exit()        
                # endif 
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK 
                ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[KGAS,LGAS]]
                if(ELEFT < 0.0):
                    globals().update(locals())
                    complete=GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    return 1
                # RANDOM EMISSION DIRECTION 
                R3=random.uniform(0.0,1.0)
                THET=numpy.arccos(1.0-2.0*R3)
                R4=random.uniform(0.0,1.0)
                PHI=TWOPI*R4
                DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17+1):
                    TSUM=TSUM+RADR[int(KGAS)][int(LGAS)][ISHELL][I]
                    for J in range(1,17+1):
                        TSUM=TSUM+AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17+1):
                    RADR[int(KGAS)][int(LGAS)][ISHELL][I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]/TSUM
                    for J in range(1,17+1):
                        AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[int(KGAS)][int(LGAS)][ISHELL][1]
                for I in range(2,17+1):
                    TEMP[I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[int(KGAS)][int(LGAS)][ISHELL][1][1]
                for I in range(2,17+1):
                    TEMP1[I]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16+1):
                    for I in range(1,17+1):
                        TEMP1[I+(J*17)]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J+1]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=random.uniform(0.0,1.0)
                for I in range(1,17+1):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND ANGLE : UPDATE NOCC
                        IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                        EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-ELEV[I][IZ[int(KGAS)][int(LGAS)]]
                        ELEFT=ELEFT-EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]
                        if(ELEFT < 0.0):
                            globals().update(locals())
                            complete=GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            return complete
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=random.uniform(0.0,1.0)       
                        PHI=TWOPI*R4
                        DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        # FIND LOWEST VACANCY
                        globals().update(locals())
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        globals().update(locals())
                        GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                globals().update(locals())
                return 1
                    # endif
            GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17+1):
                    if(counter116):
                        break
                    for I in range(1,17+1):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=random.uniform(0.0,1.0)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                            if(IONSUM[int(NVAC)]> 28) :
                                print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[int(NVAC)]) #34602
                                sys.exit()
                            # endif
                            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                globals().update(locals())
                                complete=GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                                return complete
                            # RANDOM EMISSION DIRECTION
                            R3=random.uniform(0.0,1.0)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=random.uniform(0.0,1.0)
                            PHI=TWOPI*R4
                            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                            NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                            NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                            # FIND LOWEST VACANCY
                            globals().update(locals())
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            globals().update(locals())
                            GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)    
                    # endif
        globals().update(locals())
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    globals().update(locals())
    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)            
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
    ISTART=IONSUM[int(NVAC)]
    ISTARTF=IFLSUM[int(NVAC)]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        IONSUM[int(NVAC)]=ISTART+1
        IFLSUM[int(NVAC)]=ISTARTF
        # STORE INITIAL PHOTELECTRON AND ANGLE
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
        ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        ELEFT=ELEFT-ELECN
        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=random.uniform(0.0,1.0)
        PHI=TWOPI*R3
        DRCOS(DRX0[int(NVAC)][L1],DRY0[int(NVAC)][L1],DRZ0[int(NVAC)][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRXX
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRYY
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
            INSUM=IONSUM[int(NVAC)]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                pass
            else:
                #  ELECTRON + SHAKEOFF
                ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
                IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                # MAXIMUM ION CHARGE STATE =28
                if(IONSUM[int(NVAC)]> 28) :
                    print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[int(NVAC)]) 
                    sys.exit()
                # endif
                ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK
                ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
                if(ELEFT < 0.0):
                    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                # RANDOM EMISSION DIRECTION
                R3=random.uniform(0.0,1.0)
                THET=numpy.arccos(1.0-2.0*R3)
                R4=random.uniform(0.0,1.0)
                PHI=TWOPI*R4
                DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17+1):
                    TSUM=TSUM+RADR[int(KGAS)][int(LGAS)][ISHELL][I]
                    for J in range(1,17+1):
                        TSUM=TSUM+AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17+1):
                    RADR[int(KGAS)][int(LGAS)][ISHELL][I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]/TSUM
                    for J in range(1,17+1):
                        AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[int(KGAS)][int(LGAS)][ISHELL][1]
                for I in range(2,17+1):
                    TEMP[I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[int(KGAS)][int(LGAS)][ISHELL][1][1]
                for I in range(2,17+1):
                    TEMP1[I]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16+1):
                    for I in range(1,17+1):
                        TEMP1[I+(J*17)]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=random.uniform(0.0,1.0)
                for I in range(1,17+1):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                        EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-ELEV[I][IZ[int(KGAS)][int(LGAS)]]
                        if(EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]] < 0.0):
                            print(' EPHOTON=','%.3f' % EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]],' NVAC=',NVAC,' IN CALC2')
                        ELEFT=ELEFT-EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]
                        if(ELEFT < 0.0):
                            GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=random.uniform(0.0,1.0)
                        PHI=TWOPI*R4
                        DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    # endif
            GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
            counter116
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17+1):
                    if(counter116):
                        break
                    for I in range(1,17+1):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=random.uniform(0.0,1.0)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1 #34598
                                break
                            # endif
                            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                            if(IONSUM[int(NVAC)]> 28) :
                                print(' 2ND GEN IONS LIMITED TO 28 IN THIS VERSION IONSUM=',IONSUM[int(NVAC)])
                                sys.exit()
                            # endif
                            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            # RANDOM EMISSION DIRECTION
                            R3=random.uniform(0.0,1.0)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=random.uniform(0.0,1.0)
                            PHI=TWOPI*R4
                            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                            NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                            NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # endif 
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
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
    ISTART=IONSUM[int(NVAC)]
    ISTARTF=IFLSUM[int(NVAC)]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        IONSUM[int(NVAC)]=ISTART+1
        IFLSUM[int(NVAC)]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
        ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        ELEFT=ELEFT-ELECN
        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=random.uniform(0.0,1.0)
        PHI=TWOPI*R3
        DRCOS(DRX0[int(NVAC)][L1],DRY0[int(NVAC)][L1],DRZ0[int(NVAC)][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRXX
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRYY
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
            INSUM=IONSUM[int(NVAC)]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[int(NVAC)]> 28) :
                print(' 3RD GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[int(NVAC)]) 
                sys.exit()
            # endif
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            if(ELEFT < 0.0):
                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            # RANDOM EMISSION ANGLE
            R3=random.uniform(0.0,1.0)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=random.uniform(0.0,1.0)
            PHI=TWOPI*R4
            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17+1):
                    TSUM=TSUM+RADR[int(KGAS)][int(LGAS)][ISHELL][I]
                    for J in range(1,17+1):
                        TSUM=TSUM+AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17+1):
                    RADR[int(KGAS)][int(LGAS)][ISHELL][I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]/TSUM
                    for J in range(1,17+1):
                        AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[int(KGAS)][int(LGAS)][ISHELL][1]
                for I in range(2,17+1):
                    TEMP[I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[int(KGAS)][int(LGAS)][ISHELL][1][1]
                for I in range(2,17+1):
                    TEMP1[I]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16+1):
                    for I in range(1,17+1):
                        TEMP1[I+(J*17)]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=random.uniform(0.0,1.0)
                for I in range(1,17+1):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                        EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-ELEV[I][IZ[int(KGAS)][int(LGAS)]]
                        ELEFT=ELEFT-EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]
                        if(ELEFT < 0.0):
                            GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=random.uniform(0.0,1.0)
                        PHI=TWOPI*R4
                        DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    # endif 
            GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)  
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17+1):
                    if(counter116):
                        break
                    for I in range(1,17+1):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=random.uniform(0.0,1.0)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                                # endif
                            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                            if(IONSUM[int(NVAC)]> 28) :
                                print(' 3RD GEN ION CHARGE LIMITED TO 28  IONSUM=', IONSUM[int(NVAC)])
                                sys.exit()
                            # endif
                            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            # RANDOM EMISSION DIRECTION
                            R3=random.uniform(0.0,1.0)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=random.uniform(0.0,1.0)
                            PHI=TWOPI*R4
                            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                            NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                            NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
                        # endif
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
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
    ISTART=IONSUM[int(NVAC)]
    ISTARTF=IFLSUM[int(NVAC)]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        IONSUM[int(NVAC)]=ISTART+1
        IFLSUM[int(NVAC)]=ISTARTF
        # STORE PHOTOELECTRON ENERGY AND ANGLE
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
        ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        ELEFT=ELEFT-ELECN
        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=random.uniform(0.0,1.0)
        PHI=TWOPI*R3
        DRCOS(DRX0(NVAC,L1),DRY0(NVAC,L1),DRZ0(NVAC,L1),THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRXX
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRYY
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
            INSUM=IONSUM[int(NVAC)]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[int(NVAC)]> 28) :
                print(' 4TH GEN ION CHARGE LIMITED TO 28 IONSUM=',IONSUM[int(NVAC)]) 
                sys.exit()
            # endif
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            if(ELEFT < 0.0):
                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            # RANDOM EMISSION ANGLE
            R3=random.uniform(0.0,1.0)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=random.uniform(0.0,1.0)
            PHI=TWOPI*R4
            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17+1):
                    TSUM=TSUM+RADR[int(KGAS)][int(LGAS)][ISHELL][I]
                    for J in range(1,17+1):
                        TSUM=TSUM+AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17+1):
                    RADR[int(KGAS)][int(LGAS)][ISHELL][I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]/TSUM
                    for J in range(1,17+1):
                        AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[int(KGAS)][int(LGAS)][ISHELL][1]
                for I in range(2,17+1):
                    TEMP[I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[int(KGAS)][int(LGAS)][ISHELL][1][1]
                for I in range(2,17+1):
                    TEMP1[I]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16+1):
                    for I in range(1,17+1):
                        TEMP1[I+(J*17)]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=random.uniform(0.0,1.0)
                for I in range(1,17+1):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                        EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-ELEV[I][IZ[int(KGAS)][int(LGAS)]]
                        ELEFT=ELEFT-EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]
                        if(ELEFT < 0.0):
                            GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=random.uniform(0.0,1.0)
                        PHI=TWOPI*R4
                        DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    # endif 
            GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            counter116=1
            while(counter116):
                R2=R1-TEMP[17]
                for J in range(1,17+1):
                    if(counter116):
                        break
                    for I in range(1,17+1):
                        if(R2 < TEMP1(I+((J-1)*17))) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=random.uniform(0.0,1.0)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                            if(IONSUM[int(NVAC)]> 28) :
                                print(' 4TH GEN ION CHARGE LIMITED TO 28 IONSUM=',IONSUM[int(NVAC)])
                                sys.exit()
                            # endif
                            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            # RANDOM EMISSION DIRECTION
                            R3=random.uniform(0.0,1.0)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=random.uniform(0.0,1.0)
                            PHI=TWOPI*R4
                            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                            NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                            NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
                        # endif
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)            
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
    ISTART=IONSUM[int(NVAC)]
    ISTARTF=IFLSUM[int(NVAC)]
    API=numpy.arccos(-1.00)
    TWOPI=2.00*API
    def GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
        ELEFT=ELECEN
        INIT=1
        # SET STARTING ARRAY NOCC EQUAL TO INIOCC
        for I in range(1,17+1):
            NOCC[int(KGAS)][int(LGAS)][I]=INIOCC[int(KGAS)][int(LGAS)][I]
        IONSUM[int(NVAC)]=ISTART+1
        IFLSUM[int(NVAC)]=ISTARTF
        ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECEN-ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]
        ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
        ELEFT=ELEFT-ELECN
        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]-1  
        # USE PHOTOELECTRON ANGULAR DISTRIBUTION
        APE=AA[ISHELL]
        BPE=BB[ISHELL]
        ANGGEN(APE,BPE,THET)
        if(THET < 0.0):
            THET=THET+API
        R3=random.uniform(0.0,1.0)
        PHI=TWOPI*R3
        DRCOS(DRX0[int(NVAC)][L1],DRY0[int(NVAC)][L1],DRZ0[int(NVAC)][L1],THET,PHI,DRXX,DRYY,DRZZ)
        DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRXX
        DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRYY
        DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=DRZZ
        # LOOP AROUND CASCADE
        def GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
            # CHECK FOR ELECTRON SHAKEOFF
            IDUM=1
            if(INIT > 1):
                ELECN=ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]
            INSUM=IONSUM[int(NVAC)]
            SHAKE(ISHELL,ELECN,KGAS,LGAS,ESHK,IDUM,INSUM,JVAC)
            #  CALCULATE ENERGY OF ELECTRON
            if(JVAC == 0):
                GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            #  ELECTRON + SHAKEOFF
            ELECN=ELECN-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ELECN
            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
            # MAXIMUM ION CHARGE STATE =28
            if(IONSUM[int(NVAC)]> 28) :
                print(' 5TH GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[int(NVAC)])
                sys.exit() 
            # endif
            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ESHK
            ELEFT=ELEFT-ESHK-ELEV[JVAC][IZ[int(KGAS)][int(LGAS)]]
            if(ELEFT < 0.0):
                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            # RANDOM EMISSION ANGLE
            R3=random.uniform(0.0,1.0)
            THET=numpy.arccos(1.0-2.0*R3)
            R4=random.uniform(0.0,1.0)
            PHI=TWOPI*R4
            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
            def GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON):
                UPDATE(KGAS,LGAS,ISHELL)
                INIT=2
                # CHOOSE FLUORESCENCE OR AUGER TRANSITION
                TSUM=0.0
                for I in range(1,17+1):
                    TSUM=TSUM+RADR[int(KGAS)][int(LGAS)][ISHELL][I]
                    for J in range(1,17+1):
                        TSUM=TSUM+AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]
                # NO MORE TRANSITIONS POSSIBLE
                if(TSUM == 0.0):
                    return  
                # NORMALISE TO 1.0
                for I in range(1,17+1):
                    RADR[int(KGAS)][int(LGAS)][ISHELL][I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]/TSUM
                    for J in range(1,17+1):
                        AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][J]/TSUM
                # CREATE CUMULATIVE SUM ARRAY
                TEMP[1]=RADR[int(KGAS)][int(LGAS)][ISHELL][1]
                for I in range(2,17+1):
                    TEMP[I]=RADR[int(KGAS)][int(LGAS)][ISHELL][I]+TEMP[I-1]
                TEMP1[1]=AUGR[int(KGAS)][int(LGAS)][ISHELL][1][1]
                for I in range(2,17+1):
                    TEMP1[I]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][1]+TEMP1[I-1]
                for J in range(1,16+1):
                    for I in range(1,17+1):
                        TEMP1[I+(J*17)]=AUGR[int(KGAS)][int(LGAS)][ISHELL][I][(J+1)]+TEMP1[I+(J*17)-1]
                # FIND FLUORESCENCE OR AUGER TRANSITION
                R1=random.uniform(0.0,1.0)
                for I in range(1,17+1):
                    if(R1 < TEMP[I]) :
                        # STORE PHOTON ENERGY AND UPDATE NOCC
                        IFLSUM[int(NVAC)]=IFLSUM[int(NVAC)]+1
                        EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-ELEV[I][IZ[int(KGAS)][int(LGAS)]]
                        ELEFT=ELEFT-EPHOTON[int(NVAC)][IFLSUM[int(NVAC)]]
                        if(ELEFT < 0.0):
                            GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                        # RANDOM EMISSION DIRECTION
                        R3=random.uniform(0.0,1.0)
                        THET=numpy.arccos(1.0-2.0*R3)
                        R4=random.uniform(0.0,1.0)
                        PHI=TWOPI*R4
                        DRX[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.cos(PHI)
                        DRY[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.sin(THET)*numpy.sin(PHI)
                        DRZ[int(NVAC)][IFLSUM[int(NVAC)]]=numpy.cos(THET)
                        NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                        NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                        # FIND LOWEST VACANCY
                        VACANCY(KGAS,LGAS,ISHELL,ILAST)
                        if(ILAST == 1):
                            # NO MORE TRANSITIONS POSSIBLE
                            return    
                        # endif
                        GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                    # endif 
            GOTO2(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
            counter116=1
            while(counter116):
                counter116=0
                R2=R1-TEMP[17]
                for J in range(1,17+1):
                    if(counter116):
                        break
                    for I in range(1,17+1):
                        if(R2 < TEMP1[I+((J-1)*17)]) :
                            # AUGER OR COSTER KRONIG  
                            # STORE EJECTED ELECTRON AND UPDATE NOCC
                            ETEMP=ELEV[ISHELL][IZ[int(KGAS)][int(LGAS)]]-(ELEV[I][IZ[int(KGAS)][int(LGAS)]]+ELEV[I][IZ[int(KGAS)][int(LGAS)]+1])*0.5-(ELEV[J][IZ[int(KGAS)][int(LGAS)]]+ELEV[J][IZ[int(KGAS)][int(LGAS)]+1])*0.5
                            if(ETEMP < 0.0):
                                # DO NOT ALLOW NEGATIVE ENERGY TRANSITIONS
                                counter117=1
                                while(counter117):
                                    counter117=0
                                    R1=random.uniform(0.0,1.0)
                                    if(R1 < TEMP[17]):
                                        counter117=1
                                counter116=1
                                break
                            # endif
                            IONSUM[int(NVAC)]=IONSUM[int(NVAC)]+1
                            if(IONSUM[int(NVAC)]> 28) :
                                print(' 5TH GEN ION CHARGE LIMITED TO 28  IONSUM=',IONSUM[int(NVAC)])
                                sys.exit()
                            # endif
                            ESTORE[int(NVAC)][int(IONSUM[int(NVAC)])]=ETEMP
                            ELEFT=ELEFT-ETEMP
                            if(ELEFT < 0.0):
                                GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
                            # RANDOM EMISSION DIRECTION
                            R3=random.uniform(0.0,1.0)
                            THET=numpy.arccos(1.0-2.0*R3)
                            R4=random.uniform(0.0,1.0)
                            PHI=TWOPI*R4
                            DRXE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.cos(PHI)
                            DRYE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.sin(THET)*numpy.sin(PHI)
                            DRZE[int(NVAC)][int(IONSUM[int(NVAC)])]=numpy.cos(THET)
                            NOCC[int(KGAS)][int(LGAS)][ISHELL]=NOCC[int(KGAS)][int(LGAS)][ISHELL]+1
                            NOCC[int(KGAS)][int(LGAS)][I]=NOCC[int(KGAS)][int(LGAS)][I]-1
                            NOCC[int(KGAS)][int(LGAS)][J]=NOCC[int(KGAS)][int(LGAS)][J]-1
                            # FIND LOWEST VACANCY
                            VACANCY(KGAS,LGAS,ISHELL,ILAST)
                            if(ILAST == 1):
                                # NO MORE TRANSITIONS POSSIBLE
                                return
                            # endif
                            GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON) 
                        # endif
        GOTO4(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)
    GOTO100(IPN,NVAC,KGAS,LGAS,ELECEN,ISHELL,ICON)    
    print(' ERROR IN CASCADE 5') 
    sys.exit() 
  # end
