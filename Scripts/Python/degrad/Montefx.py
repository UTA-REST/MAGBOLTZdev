# global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
# #COMMON/INPT1/
# global NDVEC
# #COMMON/CNSTS1/
# global CONST1,CONST2,CONST3,CONST4,CONST5                  
# #COMMON/SETP/
# global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX#(10)
# global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                    
# #COMMON/LARGE/
# global CF
# CF=[[0 for x in range(20000)] for y in range(512)]
# global EIN#(512)
# EIN=[0 for x in range(512)]
# global TCF#(20000)
# TCF=[0 for x in range(20000)]
# global IARRY#(512)
# IARRY=[0 for x in range(512)]
# global RGAS#(512)
# RGAS=[0 for x in range(512)]
# global IPN#(512)
# IPN=[0 for x in range(512)]
# global WPL#(512)
# WPL=[0 for x in range(512)]
# global IZBR#(512)
# IZBR=[0 for x in range(512)]
# global IPLAST
# IPLAST=1
# global PENFRA#(3,512)
# IARRY=[[0 for y in range(3)] for x in range(512)]
# #COMMON/LARGEN/
# global CFN#(20000,60)
# CFN=[[0 for x in range(20000)] for y in range(60)]
# global TCFN#(20000)
# TCFN=[0 for x in range(20000)]
# global SCLENUL#(60)
# SCLENUL=[0 for x in range(60)]
# global NPLAST
# #COMMON/OUTPT/
# global ICOLL#(30)
# ICOLL==[0 for x in range(30)]
# global NETOT,NPRIME,TMAX1,TIME#(300)
# TIME=[0 for x in range(300)]
# global NNULL,NITOT,ICOLN#(512)
# ICOLN=[0 for x in range(512)]
# global ICOLNN#(60)
# ICOLNN=[0 for x in range(60)]
# global NREAL,NEXCTOT 
# #COMMON/RLTVY/
# global BET#(2000)
# BET=[0 for x in range(2000)]
# global GAM#(20000)
# GAM=[0 for x in range(20000)]
# global VC,EMS
# #COMMON/STTS/
# global XST#(150000)
# XST=[0 for x in range(150000)]
# global YST#(150000)
# YST=[0 for x in range(150000)]
# global ZST#(150000)
# ZST=[0 for x in range(150000)]
# global TST#(150000)
# TST=[0 for x in range(150000)]
# global TTIME#(150000)
# TTIME=[0 for x in range(150000)]
# global NFGF#(150000)
# NFGF=[0 for x in range(150000)]
# global NFGPP#(150000)
# NFGPP=[0 for x in range(150000)]
# global NFGBR#(150000)
# NFGBR=[0 for x in range(150000)]
# global NELEC,NEGION,EST1,EST2
# #COMMON/STEXC/
# global XSTEXC#(150000)
# XSTEXC=[0 for x in range(150000)]
# global YSTEXC#(150000)
# YSTEXC=[0 for x in range(150000)]
# global ZSTEXC#(150000)
# ZSTEXC=[0 for x in range(150000)]
# global TSTEXC#(150000)
# TSTEXC=[0 for x in range(150000)]
# global NSTEXC
# #COMMON/STEXCNUL/
# global XSTN#(150000)
# XSTN=[0 for x in range(150000)]
# global YSTN#(150000)
# YSTN=[0 for x in range(150000)]
# global ZSTN#(150000)
# ZSTN=[0 for x in range(150000)]
# global TSTN#(150000)
# TSTN=[0 for x in range(150000)]
# global IDNUL#(150000)
# IDNUL=[0 for x in range(150000)]
# global NEXCNUL
# #COMMON/IONC/
# global DOUBLE#(6,20000)
# DOUBLE=[[0 for x in range(6)] for y in range(20000)]
# global CMINIXSC#(6)
# CMINIXSC=[0 for x in range(6)]
# global CMINEXSC#(6)
# CMINEXSC=[0 for x in range(6)]
# global ECLOSS#(6)
# ECLOSS=[0 for x in range(6)]
# global WPLN#(6)
# WPLN=[0 for x in range(6)]
# global ICOUNT,AVPFRAC#(3,6) 
# AVOFRAC=[[0 for x in range(3)] for y in range(6)]
# #COMMON/IONFL/
# global NC0#(512)
# NC0=[0 for x in range(512)]
# global EC0#(512)
# EC0=[0 for x in range(512)]
# global NG1#(512)
# NG1=[0 for x in range(512)]
# global EG1#(512)
# EG1=[0 for x in range(512)]
# global NG2#(512)
# NG2=[0 for x in range(512)]
# global EG2#(512)
# EG2=[0 for x in range(512)]
# global WKLM#(512)
# WKLM=[0 for x in range(512)]
# global DSTFL#(512)
# DSTFL=[0 for x in range(512)]
# #COMMON/IONMOD/
# global ESPLIT#(512,20)
# ESPLIT=[[0 for x in range(512)] for y in range(20)]
# global IONMODEL#(512)
# IONMODEL=[0 for x in range(512)]
# #COMMON/ANIS/
# global PSCT#(20000,512)
# PSCT=[[0 for y in range(20000)] for x in range(512)]
# global ANGCT#(20000,512)
# ANGCT=[[0 for y in range(20000)] for x in range(512)]
# global INDEX#(512)
# INDEX=[0 for x in range(512)]
# global NISO
# #COMMON/CASRS/
# global ECAS#(400)
# ECAS=[0 for x in range(400)]
# global XCAS#(400)
# XCAS=[0 for x in range(400)]
# global YCAS#(400)
# YCAS=[0 for x in range(400)]
# global ZCAS#(400)
# ZCAS=[0 for x in range(400)]
# global DRXS#(400)
# DRXS=[0 for x in range(400)]
# global DRYS#(400)
# DRYS=[0 for x in range(400)]
# global DRZS#(400)
# DRZS=[0 for x in range(400)]
# global TT1#(400)

# global NFLGF#(400)
# NFLGF=[0 for x in range(400)]
# global NFLGPP#(400)
# NFLGPP=[0 for x in range(400)]
# global IEVNTL
# #COMMON/COMP/
# global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
# #COMMON/BREMG/
# global EBRGAM#(10)
# EBRGAM=[0 for x in range(10)]
# global BRDCOSX#(10)
# BRDCOSX=[0 for x in range(10)]
# global BRDCOSY#(10)
# BRDCOSY=[0 for x in range(10)]
# global BRDCOSZ#(10)
# BRDCOSZ=[0 for x in range(10)]
# global BRX#(10)
# BRX=[0 for x in range(10)]
# global BRY#(10)
# BRY==[0 for x in range(10)]
# global BRZ#(10)
# BRZ=[0 for x in range(10)]
# global BRT#(10)
# BRT=[0 for x in range(10)]
# global EBRTOT#(6)
# EBRTOT=[0 for x in range(6)]
# global NBREM#(6)
# NBREM=[0 for x in range(6)]
# #COMMON/CASRSB/
# global ECASB#(400)
# ECASB=[0 for x in range(400)]
# global XCASB#(400)
# XCASB=[0 for x in range(400)]
# global YCASB#(400)
# YCASB=[0 for x in range(400)]
# global ZCASB#(400)
# ZCASB=[0 for x in range(400)]
# global DRXB#(400)
# DRXB=[0 for x in range(400)]
# global DRYB#(400)
# DRYB=[0 for x in range(400)]
# global DRZB#(400)
# DRZB=[0 for x in range(400)]
# global TTB1#(400)
# TTB1=[0 for x in range(400)]
# global NFLGFB#(400)
# NFLGFB=[0 for x in range(400)]
# global NFLGPPB#(400)
# NFLGPPB=[0 for x in range(400)]
# global IEVNTLB
# #COMMON/CASRSE/
# global ECASE#(400)
# ECASE=[0 for x in range(400)]
# global XCASE#(400)
# XCASE=[0 for x in range(400)]
# global YCASE#(400)
# YCASE=[0 for x in range(400)]
# global ZCASE#(400)
# ZCASE=[0 for x in range(400)]
# global DRXCE#(400)
# DRXCE=[0 for x in range(400)]
# global DRYCE#(400)
# DRYCE=[0 for x in range(400)]
# global DRZCE#(400)
# DRZCE=[0 for x in range(400)]
# global TCASE#(400)
# TCASE=[0 for x in range(400)]
# global NFLGFE#(400)
# NFLGFE=[0 for x in range(400)]
# global NFLGPPE#(400)
# NFLGPPE=[0 for x in range(400)]
# global IEVENTE
# #COMMON/ECASC/
# global NEGAS#(512)
# NEGAS=[0 for x in range(512)]
# global LEGAS#(512)
# LEGAS=[0 for x in range(512)]
# global IESHELL#(512)
# IESHELL=[0 for x in range(512)]
# global IECASC
# #COMMON/IDEXC/
# global NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
def MONTEFE():
    # IMPLICIT #real*8 (A-H,O-Z)
    # IMPLICIT #integer*8 (I-N)                                         
    # COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
    # COMMON/INPT1/NDVEC
    # COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
    # COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                    
    # COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA[3,512]
    # COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST
    # COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL,NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT 
    # COMMON/RLTVY/BET[2000],GAM(20000),VC,EMS
    # COMMON/STTS/XST(150000),YST(150000),ZST(150000),TST(150000),TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,NEGION,EST1,EST2
    # COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),TSTEXC(150000),NSTEXC
    # COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),TSTN(150000),IDNUL(150000),NEXCNUL
    # COMMON/IONC/DOUBLE(6,20000),CMINIXSC[6],CMINEXSC[6],ECLOSS[6],WPLN[6],ICOUNT,AVPFRAC(3,6) 
    # COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),EG2(512),WKLM(512),DSTFL(512)
    # COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512)
    # COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO
    # COMMON/CASRS/ECAS(400),XCAS(400),YCAS(400),ZCAS(400),DRXS(400),DRYS(400),DRZS(400),TT1(400),NFLGF(400),NFLGPP(400),IEVNTL
    # COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
    # COMMON/BREMG/EBRGAM(10),BRnumpy.cosX(10),BRnumpy.cosY(10),BRnumpy.cosZ[10],BRX(10),BRY(10),BRZ[10],BRT(10),EBRTOT[6],NBREM[6]
    # COMMON/CASRSB/ECASB[400],XCASB[400],YCASB[400],ZCASB[400],DRXB[400],DRYB[400],DRZB[400],TTB1(400),NFLGFB[400],NFLGPPB[400],IEVNTLB
    # COMMON/CASRSE/ECASE(400),XCASE(400),YCASE(400),ZCASE(400),DRXCE(400),DRYCE(400),DRZCE(400),TCASE(400),NFLGFE(400),NFLGPPE(400),IEVENTE
    # COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
    # COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
    #COMMON/INPT/
    global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
    #COMMON/INPT1/
    global NDVEC
    #COMMON/CNSTS1/
    global CONST1,CONST2,CONST3,CONST4,CONST5                  
    #COMMON/SETP/
    global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX#(10)
    global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                    
    #COMMON/LARGE/
    global CF#(20000,512)
    global EIN#(512)
    global TCF#(20000)
    global IARRY#(512)
    global RGAS#(512)
    global IPN#(512)
    global WPL#(512)
    global IZBR#(512)
    global IPLAST
    global PENFRA#(3,512)
    #COMMON/LARGEN/
    global CFN#(20000,60)
    global TCFN#(20000)
    global SCLENUL#(60)
    global NPLAST
    #COMMON/OUTPT/
    global ICOLL#(30)
    global NETOT,NPRIME,TMAX1,TIME#(300)
    global NNULL,NITOT,ICOLN#(512)
    global ICOLNN#(60)
    global NREAL,NEXCTOT 
    #COMMON/RLTVY/
    global BET#(2000)
    global GAM#(20000)
    global VC,EMS
    #COMMON/STTS/
    global XST#(150000)
    global YST#(150000)
    global ZST#(150000)
    global TST#(150000)
    global TTIME#(150000)
    global NFGF#(150000)
    global NFGPP#(150000)
    global NFGBR#(150000)
    global NELEC,NEGION,EST1,EST2
    #COMMON/STEXC/
    global XSTEXC#(150000)
    global YSTEXC#(150000)
    global ZSTEXC#(150000)
    global TSTEXC#(150000)
    global NSTEXC
    #COMMON/STEXCNUL/
    global XSTN#(150000)
    global YSTN#(150000)
    global ZSTN#(150000)
    global TSTN#(150000)
    global IDNUL#(150000)
    global NEXCNUL
    #COMMON/IONC/
    global DOUBLE#(6,20000)
    global CMINIXSC#(6)
    global CMINEXSC#(6)
    global ECLOSS#(6)
    global WPLN#(6)
    global ICOUNT,AVPFRAC#(3,6) 
    #COMMON/IONFL/
    global NC0#(512)
    global EC0#(512)
    global NG1#(512)
    global EG1#(512)
    global NG2#(512)
    global EG2#(512)
    global WKLM#(512)
    global DSTFL#(512)
    #COMMON/IONMOD/
    global ESPLIT#(512,20)
    global IONMODEL#(512)
    #COMMON/ANIS/
    global PSCT#(20000,512)
    global ANGCT#(20000,512)
    global INDEX#(512)
    global NISO
    #COMMON/CASRS/
    global ECAS#(400)
    global XCAS#(400)
    global YCAS#(400)
    global ZCAS#(400)
    global DRXS#(400)
    global DRYS#(400)
    global DRZS#(400)
    global TT1#(400)
    global NFLGF#(400)
    global NFLGPP#(400)
    global IEVNTL
    #COMMON/COMP/
    global LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
    #COMMON/BREMG/
    global EBRGAM#(10)
    global BRDCOSX#(10)
    global BRDCOSY#(10)
    global BRDCOSZ#(10)
    global BRX#(10)
    global BRY#(10)
    global BRZ#(10)
    global BRT#(10)
    global EBRTOT#(6)
    global NBREM#(6)
    #COMMON/CASRSB/
    global ECASB#(400)
    global XCASB#(400)
    global YCASB#(400)
    global ZCASB#(400)
    global DRXB#(400)
    global DRYB#(400)
    global DRZB#(400)
    global TTB1#(400)
    global NFLGFB#(400)
    global NFLGPPB#(400)
    global IEVNTLB
    #COMMON/CASRSE/
    global ECASE#(400)
    global XCASE#(400)
    global YCASE#(400)
    global ZCASE#(400)
    global DRXCE#(400)
    global DRYCE#(400)
    global DRZCE#(400)
    global TCASE#(400)
    global NFLGFE#(400)
    global NFLGPPE#(400)
    global IEVENTE
    #COMMON/ECASC/
    global NEGAS#(512)
    global LEGAS#(512)
    global IESHELL#(512)
    global IECASC
    #COMMON/IDEXC/
    global NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
        
    #DIMENSION 
    XS(150000),YS(150000),ZS(150000),TS(150000),ES(150000),DCX(150000),DCY(150000),DCZ(150000),NFLGFC(150000),NFLGPPC(150000),NFLGBRMC(150000)
    #DIMENSION 
    TEMP(20000)
    #     DIMENSION ETEMP(1000)
    # ----------------------------------------------------------------------
    #      RELATIVISTIC VERSION SEPTEMBER 2013
    #      ELECTRIC FIELD ALONG Z AXIS. NO MAGNETIC FIELD. 
    #      TRACKS DELTA ELECTRONS AND UPDATES ARRAYS CONTAINING POSITION AND
    #      TIME OF THERMALISED ELECTRONS.
    #     CALCULATES NUMBER OF PRODUCED ELECTRONS PER PRIMARY AND OTHER
    #     HIGHER FANO FACTORS. 
    #     RANGE IS ACCURATE ONLY FOR ANISOTROPIC X-SECTIONS              
    # ----------------------------------------------------------------------
    # VARYING ENERGY STEPS
    if(EFINAL <= 140000.):
        ESTEP1=(EFINAL-16000.0)/float(4000)
    else:
        ESTEP1=20.0
        ESTEP2=(EFINAL-92000.0)/float(4000)
    # endif
    NPRINT=0
    J20000=20000 
    J300=300
    API=numpy.arccos(-1.00)
    SMALL=1.0E-20                                                     
    TMAX1=0.00 
    EMAX=0.00                                                      
    RDUM=RSTART                                                       
    CONST9=CONST3*0.010
    for I in range(1,300):
        TIME[I]=0.00
    for I in range(1,30):
        ICOLL[I]=0
    for I in range(1,512):
        ICOLN[I]=0
    NREAL=0
    NNULL=0
    NETOT=0
    NEXCTOT=0
    NITOT=0
    NMXADD=0
    NTMPFLG=0
    BP=EFIELD*EFIELD*CONST1                                           
    F1=EFIELD*CONST2                                                  
    F2=EFIELD*CONST3                                                  
    F4=2.00*API
    THETA1=THETA
    PHI1=PHI
    # CALCULATE MAXIMUM COLLISION FREQUENCY    
    TLIM=0.0 
    for J in range(1,20000):
        TEMP[J]=TCFN[J]+TCF[J] 
        if(TLIM < TEMP[J]):
            TLIM=TEMP[J] 
    NEOVFL=0
    J1=0
    # START OF PRIMARY EVENT LOOP 
    for J11 in range(1,NDELTA):
        J1=J1+1
        NPRIME=J1
        NGEXC1=0
        NGEXC2=0
        NGEXC3=0
        NGEXC4=0
        NGEXC5=0
        NGEXC6=0
        #     INITIAL DIRECTION COSINES FOR ELECTRON BEAM                    
        DCZ1=numpy.cos(THETA1)
        DCX1=numpy.sin(THETA1)*numpy.cos(PHI1)                                      
        DCY1=numpy.sin(THETA1)*numpy.sin(PHI1)
        NFLGFF=0
        NFLGPPP=0
        NFLGBRMM=0
        NFLGHIGH=0
        EST1=ESTART
        E1=ESTART
        X=0.00
        Y=0.00
        Z=0.00
        K1=0
        KEXC=0
        NSTEXC=0
        NEXCNUL=0
        NCLUS=0
        NELEC=0
        NEGION=0
        TLAST=0.00
        ST=0.00
        TDASH=0.00
        if(IMIP == 2):
            pass
        else:
            if(IMIP > 2):
                # READIN FIRST ELECTRON FROM BETA DECAY OR XRAY UNTHERMALISED CLUSTERS
                CASRES(J11,IBADTOT,IBAD1)
                #  SKIP IF BAD EVENT
                if(IBAD1 == 1):
                    J1=J1-1
                    continue
                # endif 
            elif(IMIP == 1) :
                # READ IN FIRST ELECTRON FROM MIP INTERACTION
                CASREM(J11)
                EST1=ECAS[1]
                EST2=EST1
            # endif
            X=XCAS[1]
            Y=YCAS[1]
            Z=ZCAS[1]
            ST=TT1[1]
            TS[1]=TT1[1]
            E1=ECAS[1]
            DCZ1=DRZS[1]
            DCY1=DRYS[1]
            DCX1=DRXS[1]
            NFLGFF=NFLGF[1]
            NFLGPPP=NFLGPP[1]
            NFLGBRMM=0
            NFLGHIGH=NFLGFF
            # PUT REMAINDER OF ELECTRONS INTO CLUSTER STORE
            ISDUM=0
            for IST in range(2,IEVNTL):
                ISDUM=ISDUM+1
                XS[ISDUM]=XCAS[IST]
                YS[ISDUM]=YCAS[IST]
                ZS[ISDUM]=ZCAS[IST]
                TS[ISDUM]=TT1[IST]
                ES[ISDUM]=ECAS[IST]
                DCX[ISDUM]=DRXS[IST]
                DCY[ISDUM]=DRYS[IST]
                DCZ[ISDUM]=DRZS[IST]
                NFLGFC[ISDUM]=NFLGF[IST]
                NFLGPPC[ISDUM]=NFLGPP[IST]
                NFLGBRMC[ISDUM]=0
                NCLUS=ISDUM
                if(NFLGF[IST]> NFLGHIGH):
                    NFLGHIGH=NFLGF[IST]

            # START OF LOOP FOR NEWLY CREATED ELECTRONS
        flag190=0
        def GOTO1():
            R1=DRAND48(RDUM)
            T=-math.log(R1)/TLIM+TDASH
            TDASH=T
            #     AP=DCZ1*F2*math.sqrt(E1)
            GAM1=(EMS+E1)/EMS
            BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
            AP=DCZ1*EFIELD*BET1*VC*1.0E-10
            BP1=BP/GAM1              
            E=E1+(AP+BP1*T)*T
            if(E < 0.00):
                E=0.0010
            # endif    
            # INSERT NEW ALGORITHM TO FIND IE FOR VARYING ENERGY STEP          
            if(IMIP == 1):                          
                IE=int(E/ESTEP)+1                                               
            else:
                if(EFINAL <= 20000.):
                    IE=int(E/ESTEP)+1
                elif(EFINAL <= 140000.) :
                    if(E <= 16000.):
                        IE=int(E)+1
                    else:
                        IE=16000+int((E-16000.)/ESTEP1)
                    # endif 
                else:
                    if(E <= 12000.):
                        IE=int(E)+1
                    elif(E <= 92000.) :
                        IE=12000+int((E-12000.)/ESTEP1)
                    else:
                        IE=16000+int((E-92000.)/ESTEP2)
                    # endif
                # endif
            # endif 
            IE=DMIN0[IE][J20000]
            #                                                                       
            #     TEST FOR #real OR NULL COLLISION                                   
            #                                                                       
            R5=DRAND48(RDUM)
            TEST1=TCF[IE]/TLIM                                               
            if(R5 <= TEST1):
                pass
            else:
                NNULL=NNULL+1                          
                TEST2=TEMP[IE]/TLIM
                if(R5 < TEST2):
                    # TEST FOR NULL LEVELS
                    if(NPLAST == 0):
                        GOTO1()
                    R2=DRAND48(RDUM) 
                    I=0
                    flag888=1
                    while(flag888):
                        flag888=0
                        I=I+1
                        if(CFN[IE][I]< R2):
                            flag888=1
                    # INCREMENT NULL LEVEL SUM
                    NEXCNUL=NEXCNUL+1
                    ICOLNN[I]=ICOLNN[I]+1
                    # STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION FROM NULL EXCITATION
                    # NOTE:  SMALL APPROX USED POSITION OF PREVIOUS #real COLLISION
                    XSTN[NEXCNUL]=X
                    YSTN[NEXCNUL]=Y
                    ZSTN[NEXCNUL]=Z
                    TSTN[NEXCNUL]=ST
                    IDNUL[NEXCNUL]=I      
                    GOTO1()                          
                else:
                    # NULL 
                    GOTO1()
                # endif    
                #                                                                       
                #  CALCULATE DIRECTION COSINES AND POSITIONS AT INSTANT BEFORE COLLISION
            # 137 
            T2=T*T
            if(E > EMAX):
                EMAX=E
            if(T > TMAX1):
                TMAX1=T
            TDASH=0.00
            NREAL=NREAL+1                                                     
            #     CONST6=math.sqrt(E1/E)
            GAM2=(EMS+E)/EMS
            GAM12=(GAM1+GAM2)/2.00
            BET2=math.sqrt(1.00-1.00/(GAM2*GAM2))   
            CONST6=BET1/BET2                                             
            DCX2=DCX1*CONST6                                                  
            DCY2=DCY1*CONST6                                                  
            #     DCZ2=DCZ1*CONST6+EFIELD*T*CONST5/math.sqrt(E) 
            DCZ2=DCZ1*CONST6+EFIELD*T*2.0*10**(10*CONST1/(VC*BET2))
            #     CONST7=CONST9*math.sqrt(E1)  
            CONST7=VC*BET1*1.0E-12                          
            A=T*CONST7                                                        
            X=X+DCX1*A                                                        
            Y=Y+DCY1*A
            Z=Z+DCZ1*A+T2*F1/GAM12
            #     Z=Z+DCZ1*A+T2*F1     
            ST=ST+T
            IT=int(T+1.00)                                                  
            IT=DMIN0[IT][J300]                                               
            TIME[IT]=TIME[IT]+1.00                                           
            # --------------------------------------------------------------------- 
            #     DETERMINATION OF #real COLLISION TYPE                              
            # --------------------------------------------------------------------- 
            R2=DRAND48(RDUM)
            I=0                                                               
            flag140=1
            while(flag140):
                flag140=0
                I=I+1                                                             
                if(CF[IE][I]< R2):
                    flag140=1
            #************************************************************
            # CHECK IF BREMSSTRAHLUNG
            if(IZBR[I]!= 0 and LBRM == 1):
                NFLGBRMM=1
                IPT=IARRY[I]
                ICOLL[IPT]=ICOLL[IPT]+1
                ICOLN[I]=ICOLN[I]+1
                for KNGS in range(1,NGAS):
                    if(IPT == (KNGS*5)-1):
                        break
                IATOMNO=IZBR[I] 
                BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
                NBREM[KNGS]=NBREM[KNGS]+1
                EBRTOT[KNGS]=EBRTOT[KNGS]+EGAMMA
                # GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
                E1=EOUT
                DCX1=EDCX
                DCY1=EDCY
                DCZ1=EDCZ
                # RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE : STORE CONVERTED 
                # ELECTRONS IN COMMON/CASRSB/
                #
                BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
                # BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
                if(ILOW == 1):
                    GO TO 190
                #    
                #  STORE BREMSSTRAHLUNG DATA IN CLUSTER STORE
                # 
                ETSUM=0.0     
                for KBR in range(1,IEVNTLB):
                    NCLUS=NCLUS+1
                    if(NCLUS > 150000):
                        print('   def STOPPED: . NCLUS=',NCLUS,' NREAL=',NREAL)
                        sys.exit()
                    # endif    
                    ES[NCLUS]=ECASB[KBR]
                    ETSUM=ETSUM+ES[NCLUS]
                    XS[NCLUS]=XCASB[KBR]
                    YS[NCLUS]=YCASB[KBR]
                    ZS[NCLUS]=ZCASB[KBR]
                    TS[NCLUS]=TTB1[KBR]
                    DCX[NCLUS]=DRXB[KBR]
                    DCY[NCLUS]=DRYB[KBR]
                    DCZ[NCLUS]=DRZB[KBR]
                    NFLGFC[NCLUS]=NFLGFB[KBR]+NFLGHIGH
                    NFLGPPC[NCLUS]=NFLGPPB[KBR]
                    NFLGBRMC[NCLUS]=2
                if(NFLGFC[NCLUS]> NFLGHIGH):
                    NFLGHIGH=NFLGFC[NCLUS]
                GO TO 190
            # endif                
            891 CONTINUE  
            #*****************************************************************
            #     S1=RGAS[I]   
            S1=1.00+GAM2*(RGAS[I]-1.00)                                    
            EI=EIN[I]
            #     WRITE(6,8890) EIN[I],I
            #8890 print(' EIN=','%.4f' % ,' I=',I3)
            if(E < EI):
                EI=E-0.00010
            # endif                                                          
            if(IPN[I]== 0):
                GO TO 666
            # ATTACHMENT 
            flag335=0      
            if(IPN[I]== -1):
                NETOT=NETOT+1
                NITOT=NITOT+1
                NELEC=NELEC+1
                NEGION=NEGION+1
                IPT=IARRY[I]
                ICOLL[IPT]=ICOLL[IPT]+1
                ICOLN[I]=ICOLN[I]+1 
                IT=int(T+1.00)
                IT=DMIN0[IT][J300]
                TIME[IT]=TIME[IT]+1.00
                flag335=1
                # endif
            else:
                EISTR=EI
                if(IONMODEL[I]> 0): 
                    # CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
                    # FIVE DIFFERENT MODELS
                    IONSPLIT(I,E,EI,ESEC)
                    pass
                    # endif
                else:
                    R9=DRAND48(RDUM)
                    #    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
                    ESEC=WPL[I]*numpy.tan(R9*numpy.arctan((E-EI)/(2.00*WPL[I])))
                    ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
                # 544 CONTINUE
                EI=ESEC+EI 
                # STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
                # OF SECONDARY IONISATION ELECTRONS
                NCLUS=NCLUS+1
                NMXADD=MAX[NCLUS][NMXADD]
                if(NCLUS > 150000):
                    #546  
                    print('   ROUTINE STOPPED: . NCLUS=',NCLUS,' NREAL=',NREAL)
                    sys.exit()
                # endif     
                XS[NCLUS]=X       
                YS[NCLUS]=Y
                ZS[NCLUS]=Z
                TS[NCLUS]=ST
                ES[NCLUS]=ESEC   
                NFLGFC[NCLUS]=NFLGFF
                NFLGPPC[NCLUS]=NFLGPPP
                NFLGBRMC[NCLUS]=NFLGBRMM
                NTMPFLG=1
                NCLTMP=NCLUS
                #     ES[NCLUS]=ESEC
                # RANDOMISE SECONDARY ELECTRON DIRECTION
                #     R3=drand48(RDUM)
                #     F3=1.0-2.00*R3
                #     THETA0=DACOS(F3)
                #     F6=DCOS(THETA0)
                #     F5=DSIN(THETA0)
                #     R4=drand48(RDUM)
                #     PHI0=F4*R4
                #     F8=DSIN(PHI0)
                #     F9=DCOS(PHI0)               
                #     DCX[NCLUS]=F9*F5
                #     DCY[NCLUS]=F8*F5
                #     DCZ[NCLUS]=F6   
                #*********************************************************
                flag666=1
                if(IECASC == 0):
                    pass
                elif(LEGAS[I]== 0):  # changed if to elif cause same destination 
                    pass
                else:
                    # USE COMPLETE CASCADE FOR ELECTRON IONISATION
                    KG1=NEGAS[I]
                    LG1=LEGAS[I]
                    IGSHEL=IESHELL[I]
                    CASCADEE(J11,KG1,LG1,X,Y,Z,ST,ESEC,IGSHEL)
                    #
                    # STORE CASCADE IN CLUSTER STORE
                    #
                    ETSUM=0.0
                    for KBR in range(1,IEVENTE):
                        NCLUS=NCLUS+1
                        if(NCLUS > 150000):
                            print('   SUBROUTINE STOPPED: . NCLUS=',NCLUS,' NREAL=',NREAL)
                            sys.exit()
                        # endif
                        ES[NCLUS]=ECASE[KBR]
                        ETSUM=ETSUM+ES[NCLUS]
                        XS[NCLUS]=XCASE[KBR]
                        YS[NCLUS]=YCASE[KBR]
                        ZS[NCLUS]=ZCASE[KBR]
                        TS[NCLUS]=TCASE[KBR]
                        DCX[NCLUS]=DRXCE[KBR]
                        DCY[NCLUS]=DRYCE[KBR]
                        DCZ[NCLUS]=DRZCE[KBR]
                        NFLGFC[NCLUS]=NFLGFE[KBR]+NFLGHIGH
                        NFLGPPC[NCLUS]=NFLGPPE[KBR]
                        NFLGBRMC[NCLUS]=NFLGBRMM
                    if(NFLGFC[NCLUS]> NFLGHIGH):
                        NFLGHIGH=NFLGFC[NCLUS]
                    flag666=0
                    #*********************************************************
                    # STORE POSSIBLE SHELL EMISSIONS AUGER OR FLUORESCENCE 
                # 333 
                if(flag666):
                    if(EISTR > 30.0) :
                        #      WRITE(6,8891) EISTR
                        #8891  print(' EISTR=','%.4f' % )
                        # TEST IF FLUORESCENCE EMISSION
                        IFLTST=0:
                        if(WKLM[I]> 0.0):
                            R9=DRAND48(RDUM)
                        if(R9 < WKLM[I]):
                            IFLTST=1
                        # endif
                        if(IFLTST == 0):
                            # AUGER EMISSION WITHOUT FLUORESCENCE
                            NAUG=NC0[I]
                            EAVAUG=EC0[I]/float(NAUG)
                            for JFL in range(1,NC0[I]):
                                NCLUS=NCLUS+1
                                XS[NCLUS]=X
                                YS[NCLUS]=Y
                                ZS[NCLUS]=Z
                                TS[NCLUS]=ST
                                NFLGFC[NCLUS]=NFLGFF
                                NFLGPPC[NCLUS]=NFLGPPP
                                NFLGBRMC[NCLUS]=NFLGBRMM
                                ES[NCLUS]=EAVAUG
                                R3=DRAND48(RDUM)
                                F3=1.0-2.00*R3
                                THETA0=numpy.arccos(F3)
                                F6=numpy.cos(THETA0)
                                F5=numpy.sin(THETA0)
                                R4=DRAND48(RDUM)
                                PHI0=F4*R4
                                F8=numpy.sin(PHI0)
                                F9=numpy.cos(PHI0)               
                                DCX[NCLUS]=F9*F5
                                DCY[NCLUS]=F8*F5
                                DCZ[NCLUS]=F6
                        else:
                            # AUGER EMISSION AND FLUORESENCE 
                            if(NG2[I]== 0):
                                pass
                            else:
                                NAUG=NG2[I]
                                EAVAUG=EG2[I]/float(NAUG)
                                for JFL in range(1,NG2[I]):
                                    NCLUS=NCLUS+1
                                    XS[NCLUS]=X
                                    YS[NCLUS]=Y
                                    ZS[NCLUS]=Z
                                    NFLGFC[NCLUS]=NFLGFF
                                    NFLGPPC[NCLUS]=NFLGPPP
                                    NFLGBRMC[NCLUS]=NFLGBRMM
                                    TS[NCLUS]=ST
                                    ES[NCLUS]=EAVAUG
                                    R3=DRAND48(RDUM)
                                    F3=1.0-2.00*R3
                                    THETA0=numpy.arccos(F3)
                                    F6=numpy.cos(THETA0)
                                    F5=numpy.sin(THETA0)
                                    R4=DRAND48(RDUM)
                                    PHI0=F4*R4
                                    F8=numpy.sin(PHI0)
                                    F9=numpy.cos(PHI0)               
                                    DCX[NCLUS]=F9*F5
                                    DCY[NCLUS]=F8*F5
                                    DCZ[NCLUS]=F6
                            if(NG1[I] == 0):
                                pass
                            else:
                                NAUG=NG1[I]
                                EAVAUG=EG1[I]/float(NAUG)
                                R9=DRAND48(RDUM)
                                DFL=-math.log(R9)*DSTFL[I]
                                for JFL in range(1,NG1[I]):
                                    NCLUS=NCLUS+1
                                    R3=DRAND48(RDUM)
                                    THEFL=numpy.arccos(1.0-2.00*R3)
                                    R4=DRAND48(RDUM)
                                    PHIFL=F4*R4
                                    XS[NCLUS]=X+DFL*numpy.sin(THEFL)*numpy.cos(PHIFL)
                                    YS[NCLUS]=Y+DFL*numpy.sin(THEFL)*numpy.sin(PHIFL)
                                    ZS[NCLUS]=Z+DFL*numpy.cos(THEFL)
                                    NFLGFC[NCLUS]=NFLGHIGH+1
                                    NFLGPPC[NCLUS]=NFLGPPP
                                    NFLGBRMC[NCLUS]=NFLGBRMM
                                    TS[NCLUS]=ST
                                    ES[NCLUS]=EAVAUG
                                    R3=DRAND48(RDUM)
                                    F3=1.0-2.00*R3
                                    THETA0=numpy.arccos(F3)
                                    F6=numpy.cos(THETA0)
                                    F5=numpy.sin(THETA0)
                                    R4=DRAND48(RDUM)
                                    PHI0=F4*R4
                                    F8=numpy.sin(PHI0)
                                    F9=numpy.cos(PHI0)               
                                    DCX[NCLUS]=F9*F5
                                    DCY[NCLUS]=F8*F5
                                    DCZ[NCLUS]=F6
                                    NFLGHIGH=NFLGFC[NCLUS]
                        # endif
                    # endif
                #                                                                       
                #  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
                #   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
                #
                #666 
                IPT=IARRY[I]
                ICOLL[IPT]=ICOLL[IPT]+1 
                ICOLN[I]=ICOLN[I]+1 
                # IF EXCITATION : ADD PROBABILITY ,PENFRA(1,I),OF TRANSFER TO GIVE   
                # IONISATION OF THE OTHER GASES IN MIXTURE
                flag6=1
                if(IPEN == 0 or NGAS == 1):
                    pass
                else:
                    if(PENFRA[1][I] != 0.0):
                        RAN=DRAND48(RDUM)
                        if(RAN > PENFRA[1][I]):
                            pass
                        else:
                            NCLUS=NCLUS+1  
                            # ENTER HERE POSSIBLE DELOCALISATION LENGTH FOR PENNING TRANSFER
                            if(PENFRA[2][I] == 0.0):
                                XS[NCLUS]=X
                                YS[NCLUS]=Y      
                                ZS[NCLUS]=Z             
                                NFLGFC[NCLUS]=NFLGFF
                                NFLGPPC[NCLUS]=NFLGPPP
                                NFLGBRMC[NCLUS]=NFLGBRMM
                                pass

                            # endif
                            else:
                                ASIGN=1.0
                                RAN=DRAND48(RDUM)
                                RAN1=DRAND48(RDUM)
                                if(RAN1 < 0.5):
                                    ASIGN=-ASIGN
                                XS[NCLUS]=X-math.log(RAN)*PENFRA[2][I]*ASIGN
                                RAN=DRAND48(RDUM)
                                RAN1=DRAND48(RDUM)
                                if(RAN1 < 0.5):
                                    ASIGN=-ASIGN
                                YS[NCLUS]=Y-math.log(RAN)*PENFRA[2][I]*ASIGN
                                RAN=DRAND48(RDUM)
                                RAN1=DRAND48(RDUM)
                                if(RAN1 < 0.5):
                                    ASIGN=-ASIGN
                                ZS[NCLUS]=Z-math.log(RAN)*PENFRA[2][I]*ASIGN
                            #667  
                            RAN=DRAND48(RDUM)
                            TS[NCLUS]=ST-math.log(RAN)*PENFRA[3][I]
                            # ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
                            ES[NCLUS]=1.0
                            DCX[NCLUS]=DCX1
                            DCY[NCLUS]=DCY1
                            DCZ[NCLUS]=DCZ1
                            flag6=0
                    # endif 
                #      GO TO 6 
                # CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
                # 5  
                if(flag6):
                    if(IPN[I] == 0) :
                        if((RGAS[I]*EIN[I]) > 4.0):
                            KEXC=KEXC+1
                            if(KEXC > 150000):
                                print(2X,' def STOPPED: . KEXC=',KEXC)
                                sys.exit()
                            # endif
                            # FIND GAS IN WHICH EXCITATION OCCURED AND INCREMENT COUNTER
                            if(I <= IDG1):
                                NGEXC1=NGEXC1+1
                            elif(I <= IDG2) :
                                NGEXC2=NGEXC2+1
                            elif(I <= IDG3) :
                                NGEXC3=NGEXC3+1
                            elif(I <= IDG4) :
                                NGEXC4=NGEXC4+1
                            elif(I <= IDG5) :
                                NGEXC5=NGEXC5+1
                            elif(I <= IDG6) :
                                NGEXC6=NGEXC6+1
                            else:
                                print(' def STOPPED: BAD GAS ID IN MONTE')
                                sys.exit()
                            # endif
                            NEXCTOT=NEXCTOT+1
                            NSTEXC=NSTEXC+1
                            XSTEXC[KEXC]=X
                            YSTEXC[KEXC]=Y
                            ZSTEXC[KEXC]=Z
                            TSTEXC[KEXC]=ST
                        # endif
                    # endif 
                # 6  
                S2=(S1*S1)/(S1-1.00) 
                #   ANISOTROPIC SCATTERING
                R3=DRAND48(RDUM)
                if(INDEX[I]== 1):
                    R31=DRAND48(RDUM)
                    F3=1.00-R3*ANGCT[IE][I]          
                    if(R31 > PSCT[IE][I]):
                        F3=-F3
                elif(INDEX[I] == 2) :
                    EPSI=PSCT[IE][I]
                    F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3))) 
                else: 
                    # ISOTROPIC SCATTERING                                             
                    F3=1.00-2.00*R3
                # endif
                THETA0=numpy.arccos(F3)
                R4=DRAND48(RDUM)
                PHI0=F4*R4                                                        
                F8=numpy.sin(PHI0)                                                     
                F9=numpy.cos(PHI0)                                                     
                if(E < EI):
                    EI=0.00                                              
                ARG1=1.00-S1*EI/E                                                
                ARG1=DMAX1[ARG1][SMALL]                                            
                D=1.00-F3*math.sqrt(ARG1)                                            
                E1=E*(1.00-EI/(S1*E)-2.00*D/S2) 
                E1=DMAX1[E1][SMALL]                                                
                Q=math.sqrt((E/E1)*ARG1)/S1                                           
                Q=DMIN1[Q][1.00]                                                  
                THETA=numpy.arcsin(Q*numpy.sin(THETA0))                                       
                F6=numpy.cos(THETA)                                                    
                U=(S1-1.00)*(S1-1.00)/ARG1                                      
                CSQD=F3*F3                                                        
                if(F3 < 0.00 and CSQD > U):
                    F6=-1.00*F6                        
                F5=numpy.sin(THETA)                                                    
                DCZ2=DMIN1[DCZ2][1.00]                                            
                ARGZ=math.sqrt(DCX2*DCX2+DCY2*DCY2)
                if(ARGZ == 0.00):
                    DCZ1=F6         
                    DCX1=F9*F5                             
                    DCY1=F8*F5 
                    if(NTMPFLG == 1):
                        # USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
                        F5S=F5*math.sqrt(E1/ES[NCLTMP])
                        if(F5S > 1.0):
                            F5S=1.0
                        THSEC=numpy.arcsin(F5S)
                        F5S=numpy.sin(THSEC)
                        F6S=numpy.cos(THSEC)
                        if(F6 < 0.0):
                            F6S=-F6S
                        PHIS=PHI0+API   
                        if(PHIS > F4):
                            PHIS=PHI0-F4
                        F8S=numpy.sin(PHIS)
                        F9S=numpy.cos(PHIS)
                        DCZ[NCLTMP]=F6S
                        DCX[NCLTMP]=F9S*F5S
                        DCY[NCLTMP]=F8S*F5S
                        NTMPFLG=0
                    # endif
                    pass
                    # endif 
                else:
                    DCZ1=DCZ2*F6+ARGZ*F5*F8                                           
                    DCY1=DCY2*F6+(F5/ARGZ)*(DCX2*F9-DCY2*DCZ2*F8)                     
                    DCX1=DCX2*F6-(F5/ARGZ)*(DCY2*F9+DCX2*DCZ2*F8)
                    if(NTMPFLG == 1):
                        # USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
                        F5S=F5*math.sqrt(E1/ES[NCLTMP])
                        if(F5S > 1.0):
                            F5S=1.0            
                        THSEC=numpy.arcsin(F5S)
                        F5S=numpy.sin(THSEC)
                        F6S=numpy.cos(THSEC)
                        if(F6 < 0.0):
                            F6S=-F6S
                        PHIS=PHI0+API   
                        if(PHIS > F4):
                            PHIS=PHI0-F4
                        F8S=numpy.sin(PHIS)
                        F9S=numpy.cos(PHIS)
                        DCZ[NCLTMP]=DCZ2*F6S+ARGZ*F5S*F8S                               
                        DCY[NCLTMP]=DCY2*F6S+(F5S/ARGZ)*(DCX2*F9S-DCY2*DCZ2*F8S)        
                        DCX[NCLTMP]=DCX2*F6S-(F5S/ARGZ)*(DCY2*F9S+DCX2*DCZ2*F8S)
                        NTMPFLG=0
                    # endif 
                # 190 CONTINUE 
                # TEST IF ELECTRON IS THERMALISED
                if(E1 > ETHRM):
                    GOTO1()  
                # STORE POSITION AND TIME OF ELECTRON AND COLLISION HISTORY
                #191
            flag191=1
            while (flag191):
                flag191=0
                if(flag335==0):
                    K1=K1+1
                    XST[K1]=X
                    YST[K1]=Y
                    ZST[K1]=Z
                    TST[K1]=ST
                    NFGF[K1]=NFLGFF
                    NFGPP[K1]=NFLGPPP
                    NFGBR[K1]=NFLGBRMM
                    TTIME[K1]=ST-TLAST
                    NELEC=NELEC+1
                    NETOT=NETOT+1
                #335  
                if(K1 == 150000):
                    GOTO889()
                # CATCH SINGLE ELECTRON CLUSTER THAT WAS ATTACHED.
                #      if(NELEC == 1 and NCLUS == 0) GO TO 210 
                #
                if(NELEC == (NCLUS+1)):
                    #       WRITE(6,884) NELEC,NCLUS,NEGION,J11
                    # 884 print(' NELEC=',I6,' NCLUS=',I6,' NEGION=',I3,' J11=',I6)
                    # LAST ELECTRON IN CLUSTER DO STATISTICS OVER PRIMARY CLUSTER
                    STATS(J11,J1)
                    pass
                    # endif
                else:
                    if(NELEC < (NCLUS+1)) :
                        # GET NEW IONISATION ELECTRON FROM STORE
                        X=XS[NELEC]
                        Y=YS[NELEC]
                        Z=ZS[NELEC]
                        ST=TS[NELEC]
                        NFLGFF=NFLGFC[NELEC]
                        NFLGPPP=NFLGPPC[NELEC]
                        NFLGBRMM=NFLGBRMC[NELEC]
                        TLAST=TS[NELEC]
                        E1=ES[NELEC]
                        DCX1=DCX[NELEC]
                        DCY1=DCY[NELEC]
                        DCZ1=DCZ[NELEC]
                        if(E1 < ETHRM):
                            flag191=1
                        else:
                            GOTO1()   
                    # endif
                    #  MAIN LOOP # end    
        GOTO1()
    # RESET NUMBER OF EVENTS FOR BAD EVENTS
    if(IMIP > 2):
        NDELTA=NDELTA-IBADTOT
    #
    print(' EMAX=','%.7f' % EMAX,' NEOVFL=',NEOVFL)
    if(EMAX > EFINAL):
        print('INCREASE ENERGY LIMIT FROM','%.6f' % EFINAL,' EV TO AT LEAST','%.6f' % EMAX,' EV.')
        sys.exit()
    # endif                                         
    return 
    def GOTO889():
        NLEFT=NCLUS-NELEC
        print('\n\n\n WARNING STOPPED: AFTER NPRIME=',NPRIME,' LAST PRIMARY HASAT LEAST ',NLEFT,' SECONDARIES LEFT TO TRACK OUT OF ',NCLUS,' ELECTRONS ALREADY IN CLUSTER') 
        sys.exit()    
    GOTO889()  
                    
    return                                                            
    # end
def MONTEF():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)                                         
	COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	COMMON/INPT1/NDVEC
	COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
	COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE   
	COMMON/BFLD/EOVB,WB,BTHETA,BMAG                                   
	COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),    RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA[3,512]
	COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST
	COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL,NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT 
	COMMON/RLTVY/BET[2000],GAM(20000),VC,EMS
	COMMON/STTS/XST(150000),YST(150000),ZST(150000),TST(150000),TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,NEGION,EST1,EST2 
	COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),TSTEXC(150000),NSTEXC
	COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),TSTN(150000),IDNUL(150000),NEXCNUL
	COMMON/IONC/DOUBLE(6,20000),CMINIXSC[6],CMINEXSC[6],ECLOSS[6],WPLN[6],ICOUNT,AVPFRAC(3,6)
	COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),EG2(512),WKLM(512),DSTFL(512)
	COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512) 
	COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO
	COMMON/CASRS/ECAS(400),XCAS(400),YCAS(400),ZCAS(400),DRXS(400),DRYS(400),DRZS(400),TT1(400),NFLGF(400),NFLGPP(400),IEVNTL
	COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	COMMON/BREMG/EBRGAM(10),BRDCOSX(10),BRDCOSY(10),BRDCOSZ[10],BRX(10),BRY(10),BRZ[10],BRT(10),EBRTOT[6],NBREM[6]
	COMMON/CASRSB/ECASB[400],XCASB[400],YCASB[400],ZCASB[400],DRXB[400],DRYB[400],DRZB[400],TTB1(400),NFLGFB[400],NFLGPPB[400],IEVNTLB
	COMMON/CASRSE/ECASE(400),XCASE(400),YCASE(400),ZCASE(400),DRXCE(400),DRYCE(400),DRZCE(400),TCASE(400),NFLGFE(400),NFLGPPE(400),IEVENTE
	COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
	COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
	DIMENSION XS(150000),YS(150000),ZS(150000),TS(150000),ES(150000),DCX(150000),DCY(150000),DCZ[150000],NFLGFC(150000),NFLGPPC(150000),NFLGBRMC(150000)
	DIMENSION TEMP(20000)
	# ----------------------------------------------------------------------   
	#   RELATIVISTIC KINEMATICS
	#   ELECTRIC AND MAGNETIC FIELDS  PARALLEL TO Z-AXIS      
	#   TRACKS DELTA ELECTRONS AND UPDATES ARRAYS CONTAINING POSITION AND 
	#   TIME OF THERMALISED ELECTRONS.
	#   CALCULATES NUMBER OF PRODUCED ELECTRONS PER PRIMARY DELTA AND OTHER
	#   HIGHER FANO FACTORS
	#   RANGE CALCULATION IS ACCURATE ONLY FOR ANISOTROPIC X-SECTIONS.
	# ----------------------------------------------------------------------
	# VARYING ENERGY STEPS
	if(EFINAL <= 140000.):
	:
	ESTEP1=(EFINAL-16000.0)/float(4000)
	else:
	ESTEP1=20.0
	ESTEP2=(EFINAL-92000.0)/float(4000)
	# endif
	NPRINT=0 
	J300=300
	J20000=20000
	API=numpy.arccos(-1.00)
	SMALL=1.0D-20
	EMAX=0.00
	TMAX1=0.00
	RDUM=RSTART
	CONST9=CONST3*0.010
	DO 25 I=1,300
	25 TIME[I]=0.00
	DO 26 I=1,30
	26 ICOLL[I]=0
	DO 27 I=1,512
	27 ICOLN[I]=0
	NREAL=0                                                           
	NNULL=0                                                           
	NETOT=0
	NEXCTOT=0
	NITOT=0
	NMXADD=0
	NTMPFLG=0
	BP=EFIELD*EFIELD*CONST1                                           
	F1=EFIELD*CONST2                                                  
	F2=EFIELD*CONST3
	F4=2.00*API
	THETA1=THETA
	PHI1=PHI
	NEOVFL=0
	# CALCULATE MAXIMUM COLLISION FREQUENCY
	TLIM=0.0
	DO 111 J=1,20000
	TEMP[J]=TCFN[J]+TCF[J]
	if(TLIM < TEMP[J]:
	) TLIM=TEMP[J] 
	111 CONTINUE
	# START OF PRIMARY DELTA LOOP
	J1=0
	DO 210 J11=1,NDELTA 
	J1=J1+1
	NPRIME=J1      
	NGEXC1=0
	NGEXC2=0
	NGEXC3=0
	NGEXC4=0
	NGEXC5=0
	NGEXC6=0
	#     INITIAL DIRECTION COSINES FOR ELECTRON BEAM                
	DCZ1=numpy.cos(THETA1) 
	DCX1=numpy.sin(THETA1)*numpy.cos(PHI1)                                      
	DCY1=numpy.sin(THETA1)*numpy.sin(PHI1)
	NFLGFF=0
	NFLGPPP=0
	NFLGBRMM=0
	NFLGHIGH=0
	EST1=ESTART
	# INITIAL VELOCITY
	E1=ESTART
	#     VTOT=CONST9*math.sqrt(E1)
	GAM1=(EMS+E1)/EMS
	GAM12=GAM1
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.0D-12
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT      
	X=0.00    
	Y=0.00    
	Z=0.00                                           
	K1=0   
	KEXC=0
	NSTEXC=0
	NEXCNUL=0
	NCLUS=0
	NELEC=0
	NEGION=0
	TLAST=0.00
	ST=0.00
	TDASH=0.00
	if(IMIP == 2):
	GO TO 1
	if(IMIP > 2):
	:
	# READIN FIRST ELECTRON FROM BETA DECAY OR XRAY UNTHERMALISED CLUSTERS
	CALL CASRES(J11,IBADTOT,IBAD1)
	#  SKIP IF BAD EVENT
	if(IBAD1 == 1):
	:
	J1=J1-1
	GO TO 210
	# endif
	else if(IMIP == 1) :
	# READ IN FIRST ELECTRON FROM MIP INTERACTION
	CALL CASREM(J11)
	EST1=ECAS[1]
	EST2=EST1
	# endif
	X=XCAS[1]
	Y=YCAS[1]
	Z=ZCAS[1]
	ST=TT1[1]
	TS[1]=TT1[1]
	E1=ECAS[1]
	DCZ1=DRZS[1]
	DCY1=DRYS[1]
	DCX1=DRXS[1]
	NFLGFF=NFLGF[1]
	NFLGPPP=NFLGPP[1]
	NFLGBRMM=0
	NFLGHIGH=NFLGFF
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	#     VTOT=CONST9*math.sqrt(E1)
	VTOT=BET1*VC*1.0D-12
	#
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# PUT REMAINDER OF ELECTRONS INTO CLUSTER STORE
	ISDUM=0
	DO 35 IST=2,IEVNTL
	ISDUM=ISDUM+1
	XS[ISDUM]=XCAS[IST]
	YS[ISDUM]=YCAS[IST]
	ZS[ISDUM]=ZCAS[IST]
	TS[ISDUM]=TT1[IST]
	ES[ISDUM]=ECAS[IST]
	DCX[ISDUM]=DRXS[IST]
	DCY[ISDUM]=DRYS[IST]
	DCZ[ISDUM]=DRZS[IST]
	NFLGFC[ISDUM]=NFLGF[IST]
	NFLGPPC[ISDUM]=NFLGPP[IST]
	NFLGBRMC[ISDUM]=0
	NCLUS=ISDUM
	if(NFLGF[IST]:
	> NFLGHIGH) NFLGHIGH=NFLGF[IST]
	35 CONTINUE
	GAM12=GAM1
	# START OF LOOP FOR NEWLY CREATED ELECTRONS                             
	1 CONTINUE 
	R1=DRAND48(RDUM)
	T=-math.log(R1)/TLIM+TDASH
	TDASH=T
	#     AP=DCZ1*F2*math.sqrt(E1)
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	AP=DCZ1*EFIELD*BET1*VC*1.0D-10
	BP1=BP/GAM1
	913  print(3X,' AFTER STORE NREAL=',I10,' E1=',E12.3,' T=',E12.3,' AP=',E12.3,' BP=',E12.3,' DCZ1=',E12.3)
	#     E=E1+(AP+BP*T)*T       
	E=E1+(AP+BP1*T)*T
	if(E < 0.00):
	:
	if(NPRINT == 0):
	WRITE(6,913)NREAL,E1,T,AP,BP,DCZ1 
	NPRINT=1
	E=0.0010
	# endif                                                   
	# INSERT NEW ALGORITHM TO FIND IE FOR VARYING ENERGY STEP          
	if(IMIP == 1):
	:                                     
	IE=int(E/ESTEP)+1                                               
	else:
	if(EFINAL <= 20000.):
	:
	IE=int(E/ESTEP)+1
	else if(EFINAL <= 140000.) :
	if(E <= 16000.):
	:
	 IE=int(E)+1
	else:
	 IE=16000+int((E-16000.)/ESTEP1)
	# endif
	else:
	if(E <= 12000.):
	:
	 IE=int(E)+1
	else if(E <= 92000.) :
	 IE=12000+int((E-12000.)/ESTEP1)
	else:
	 IE=16000+int((E-92000.)/ESTEP2)
	# endif
	# endif
	# endif 
	IE=DMIN0(IE,J20000)                                            
	#                                                                       
	#     TEST FOR #real OR NULL COLLISION                                   
	#                                                                       
	R5=DRAND48(RDUM)
	TEST1=TCF[IE]/TLIM                                                
	if(R5 <= TEST1):
	GO TO 137                                         
	NNULL=NNULL+1                
	TEST2=TEMP[IE]/TLIM
	if(R5 < TEST2):
	:
	# TEST FOR NULL LEVELS
	if(NPLAST == 0):
	GO TO 1
	R2=DRAND48(RDUM) 
	I=0
	888  I=I+1
	if(CFN[IE][I]:
	< R2) GO TO 888  
	# INCREMENT NULL LEVEL SUM
	NEXCNUL=NEXCNUL+1
	ICOLNN[I]=ICOLNN[I]+1
	# STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION AND DISSOCIATION FROM 
	#    NULL EXCITATION  
	# NOTE: SMALL APPROX USED POSITION OF PREVIOUS COLLISION
	XSTN[NEXCNUL]=X
	YSTN[NEXCNUL]=Y
	ZSTN[NEXCNUL]=Z
	TSTN[NEXCNUL]=ST
	IDNUL[NEXCNUL]=I
	GO TO 1       
	else:
	# NULL
	GO TO 1
	# endif                                                   
	#                                                                       
	#  CALCULATE DIRECTION COSINES AND POSITIONS AT INSTANT BEFORE COLLISION
	137 T2=T*T
	GAM2=(EMS+E)/EMS
	BET2=math.sqrt(1.00-1.00/(GAM2*GAM2))
	GAM12=(GAM1+GAM2)/2.00
	if(E > EMAX):
	EMAX=E
	if(T > TMAX1):
	TMAX1=T
	TDASH=0.00  
	NREAL=NREAL+1
	WBT=WB*T/GAM12
	#     WBT=WB*T      
	WBR=WB/GAM12
	COSWT=numpy.cos(WBT)
	SINWT=numpy.sin(WBT)                                                   
	#     CONST6=math.sqrt(E1/E)
	CONST6=BET1/BET2
	CX2=CX1*COSWT-CY1*SINWT
	CY2=CY1*COSWT+CX1*SINWT
	#     VTOT=CONST9*math.sqrt(E)
	VTOT=VC*BET2*1.0D-12                    
	DCX2=CX2/VTOT                                                     
	DCY2=CY2/VTOT                                                     
	#     DCZ2=DCZ1*CONST6+EFIELD*T*CONST5/math.sqrt(E) 
	DCZ2=DCZ1*CONST6+EFIELD*T*2.0D10*CONST1/(VC*BET2)
	#     CONST7=CONST9*math.sqrt(E1)   
	CONST7=VC*BET1*1.0D-12            
	A=T*CONST7                                                        
	#     DX=(CX1*SINWT-CY1*(1.00-COSWT))/WB 
	DX=(CX1*SINWT-CY1*(1.00-COSWT))/WBR                              
	X=X+DX           
	#     DY=(CY1*SINWT+CX1*(1.00-COSWT))/WB                               
	DY=(CY1*SINWT+CX1*(1.00-COSWT))/WBR                              
	Y=Y+DY    
	#     Z=Z+DCZ1*A+T2*F1
	Z=Z+DCZ1*A+T2*F1/GAM12
	ST=ST+T
	IT=int(T+1.00)                                                  
	IT=DMIN0[IT][J300]                                                
	TIME[IT]=TIME[IT]+1.00                                           
	# --------------------------------------------------------------------- 
	#     DETERMINATION OF #real COLLISION TYPE                              
	# --------------------------------------------------------------------- 
	R2=DRAND48(RDUM)
	I=0                                                               
	140 I=I+1 
	if(I <= 0 or I > 512):
	:
	WRITE(6,945) I
	945 print(' BAD  SELECTION I=',I8)
	sys.exit()
	# endif
	if(CF[IE][I]:
	< R2) GO TO 140        
	#************************************************************
	# CHECK IF BREMSSTRAHLUNG
	if(IZBR[I]:
	!= 0 and LBRM == 1) :
	NFLGBRMM=1
	IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1
	ICOLN[I]=ICOLN[I]+1
	DO 141 KNGS=1,NGAS
	if(IPT == (KNGS*5):
	-1) GO TO 142
	141  CONTINUE
	142  IATOMNO=IZBR[I] 
	CALL BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
	NBREM[KNGS]=NBREM[KNGS]+1
	EBRTOT[KNGS]=EBRTOT[KNGS]+EGAMMA
	#      WRITE(6,668) EGAMMA,J11   
	# 668 print(' BREM EGAMMA=','%.4f' % ,' EVENT NO=',I5)
	# GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
	E1=EOUT
	DCX1=EDCX
	DCY1=EDCY
	DCZ1=EDCZ
	# RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE : STORE CONVERTED 
	# ELECTRONS IN COMMON/CASRSB/
	#              
	CALL BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
	# BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
	if(ILOW == 1):
	GO TO 190
	# 
	# STORE BREMSSTRAHLUNG DATA IN CLUSTER STORE
	#
	DO 890 KBR=1,IEVNTLB
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif     
	ES[NCLUS]=ECASB[KBR]
	XS[NCLUS]=XCASB[KBR]
	YS[NCLUS]=YCASB[KBR]
	ZS[NCLUS]=ZCASB[KBR]
	TS[NCLUS]=TTB1[KBR]
	DCX[NCLUS]=DRXB[KBR]
	DCY[NCLUS]=DRYB[KBR]
	DCZ[NCLUS]=DRZB[KBR]
	NFLGFC[NCLUS]=NFLGFB[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPB[KBR]
	NFLGBRMC[NCLUS]=2
	890  CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 190
	# endif
	891 CONTINUE
	#****************************************************************
	#     S1=RGAS[I]  
	S1=1.00+GAM2*(RGAS[I]-1.00)                                    
	EI=EIN[I]
	if(E < EI):
	:
	EI=E-0.00010
	# endif                                                          
	if(IPN[I]:
	== 0) GO TO 666
	# ATTACHMENT       
	if(IPN[I]:
	== -1) :
	NETOT=NETOT+1
	NITOT=NITOT+1
	NELEC=NELEC+1
	NEGION=NEGION+1
	IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1
	ICOLN[I]=ICOLN[I]+1 
	IT=int(T+1.00)
	IT=DMIN0[IT][J300]
	TIME[IT]=TIME[IT]+1.00
	GO TO 335
	# endif   
	EISTR=EI
	if(IONMODEL[I]:
	> 0) :
	# CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
	# FIVE DIFFERENT MODELS
	CALL IONSPLIT(I,E,EI,ESEC) 
	GO TO 544
	# endif
	R9=DRAND48(RDUM)
	#    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
	ESEC=WPL[I]*TAN(R9*ATAN((E-EI)/(2.00*WPL[I]))) 
	ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
	544 CONTINUE
	EI=ESEC+EI 
	# STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
	# OF SECONDARY IONISATION ELECTRON
	NCLUS=NCLUS+1
	NMXADD=MAX[NCLUS][NMXADD]
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL 
	546   print(2X,' def STOPPED: . NCLUS=',I7,' NREAL =',I10)
	sys.exit()
	# endif     
	XS[NCLUS]=X       
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	ES[NCLUS]=ESEC        
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	NTMPFLG=1
	NCLTMP=NCLUS
	# RANDOMISE SECONDARY ELECTRON DIRECTION
	#     R3=drand48(RDUM)
	#     F3=1.0-2.00*R3
	#     THETA0=DACOS(F3)
	#     F6=DCOS(THETA0)
	#     F5=DSIN(THETA0)
	#     R4=drand48(RDUM)
	#     PHI0=F4*R4
	#     F8=DSIN(PHI0)
	#     F9=DCOS(PHI0)               
	#     DCX[NCLUS]=F9*F5
	#     DCY[NCLUS]=F8*F5
	#     DCZ[NCLUS]=F6     
	#*********************************************************
	if(IECASC == 0):
	GO TO 333
	if(LEGAS[I]:
	== 0) GO TO 333
	# USE COMPLETE CASCADE FOR ELECTRON IONISATION
	KG1=NEGAS[I]
	LG1=LEGAS[I]
	IGSHEL=IESHELL[I]
	CALL CASCADEE(J11,KG1,LG1,X,Y,Z,ST,ESEC,IGSHEL)
	#
	# STORE CASCADE IN CLUSTER STORE
	#
	ETSUM=0.0
	DO 844 KBR=1,IEVENTE
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	:
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif
	ES[NCLUS]=ECASE[KBR]
	ETSUM=ETSUM+ES[NCLUS]
	XS[NCLUS]=XCASE[KBR]
	YS[NCLUS]=YCASE[KBR]
	ZS[NCLUS]=ZCASE[KBR]
	TS[NCLUS]=TCASE[KBR]
	DCX[NCLUS]=DRXCE[KBR]
	DCY[NCLUS]=DRYCE[KBR]
	DCZ[NCLUS]=DRZCE[KBR]
	NFLGFC[NCLUS]=NFLGFE[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPE[KBR]
	NFLGBRMC[NCLUS]=NFLGBRMM
	844 CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 666
	#*********************************************************
	# STORE POSSIBLE SHELL EMISSSIONS BY AUGER OR FLUORESCENCE
	333 if (EISTR > 30.0) :
	# TEST IF FLUORESCENCE EMISSION
	IFLTST=0:
	if(WKLM[I]:
	> 0.0) :
	R9=DRAND48(RDUM)
	if(R9 < WKLM[I]:
	) IFLTST=1
	# endif
	if(IFLTST == 0):
	:
	# AUGER EMISSION WITHOUT FLUORESCENCE
	NAUG=NC0[I]
	EAVAUG=EC0[I]/float(NAUG)
	DO 700 JFL=1,NC0[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)      
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	700   CONTINUE
	else:
	# AUGER EMISSION AND FLUORESCENCE
	if(NG2[I]:
	== 0) GO TO 702
	NAUG=NG2[I]
	EAVAUG=EG2[I]/float(NAUG)
	DO 701 JFL=1,NG2[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	701   CONTINUE
	702   if(NG1[I] == 0) GO TO 704
	NAUG=NG1[I]
	EAVAUG=EG1[I]/float(NAUG)
	R9=DRAND48(RDUM)
	DFL=-math.log(R9)*DSTFL[I]
	DO 703 JFL=1,NG1[I]
	NCLUS=NCLUS+1
	R3=DRAND48(RDUM)
	THEFL=numpy.arccos(1.0-2.00*R3)
	R4=DRAND48(RDUM)
	PHIFL=F4*R4
	XS[NCLUS]=X+DFL*numpy.sin(THEFL)*numpy.cos(PHIFL)
	YS[NCLUS]=Y+DFL*numpy.sin(THEFL)*numpy.sin(PHIFL)
	ZS[NCLUS]=Z+DFL*numpy.cos(THEFL)
	NFLGFC[NCLUS]=NFLGHIGH+1
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	NFLGHIGH=NFLGFC[NCLUS]
	703   CONTINUE
	704   CONTINUE
	# endif
	# endif 
	#                                                                       
	#  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
	#   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
	#
	666 IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1 
	ICOLN[I]=ICOLN[I]+1   
	# IF EXCITATION : ADD PROBABILITY,PENFRA(1,I), OF TRANSFER TO GIVE   
	# IONISATION OF THE OTHER GASES IN MIXTURE 
	if(IPEN == 0 or NGAS == 1):
	GO TO 5          
	if(PENFRA[1][I] != 0.0):
	:
	RAN=DRAND48(RDUM)
	if(RAN > PENFRA[1][I]):
	GO TO 5
	NCLUS=NCLUS+1  
	# ENTER HERE POSSIBLE DELOCALISATION LENGTH FOR PENNING TRANSFER
	if(PENFRA[2][I] == 0.0):
	:
	XS[NCLUS]=X      
	YS[NCLUS]=Y
	ZS[NCLUS]=Z   
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	GO TO 667
	# endif
	ASIGN=1.0
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	XS[NCLUS]=X-math.log(RAN)*PENFRA[2][I]*ASIGN
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	YS[NCLUS]=Y-math.log(RAN)*PENFRA[2][I]*ASIGN
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	ZS[NCLUS]=Z-math.log(RAN)*PENFRA[2][I]*ASIGN
	667  RAN=DRAND48(RDUM)           
	TS[NCLUS]=ST-math.log(RAN)*PENFRA[3][I] 
	# ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
	ES[NCLUS]=1.0
	DCX[NCLUS]=DCX1
	DCY[NCLUS]=DCY1
	DCZ[NCLUS]=DCZ1
	GO TO 6
	# endif
	#     GO TO 6 
	# CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
	5  if(IPN[I] == 0) :
	if((RGAS[I]:
	*EIN[I]) > 4.0) :
	KEXC=KEXC+1
	if(KEXC > 150000):
	: 
	 WRITE(6,548) KEXC 
	548     print(2X,' def STOPPED: . KEXC=',I7)
	 sys.exit()
	# endif
	# FIND GAS IN WHICH EXCITATION OCCURED AND INCREMENT COUNTER
	if(I <= IDG1):
	: 
	 NGEXC1=NGEXC1+1
	else if(I <= IDG2) :
	 NGEXC2=NGEXC2+1
	else if(I <= IDG3) :
	 NGEXC3=NGEXC3+1
	else if(I <= IDG4) :
	 NGEXC4=NGEXC4+1
	else if(I <= IDG5) :
	 NGEXC5=NGEXC5+1
	else if(I <= IDG6) :
	 NGEXC6=NGEXC6+1
	else:
	 WRITE(6,9911) 
	9911    print(' def STOPPED: BAD GAS ID IN MONTE')
	 sys.exit()
	# endif
	NEXCTOT=NEXCTOT+1
	NSTEXC=NSTEXC+1
	XSTEXC[KEXC]=X
	YSTEXC[KEXC]=Y
	ZSTEXC[KEXC]=Z
	TSTEXC[KEXC]=ST
	# endif
	# endif 
	6  S2=(S1*S1)/(S1-1.00) 
	# ANISOTROPIC SCATTERING
	R3=DRAND48(RDUM)     
	if(INDEX[I]:
	== 1) :
	R31=DRAND48(RDUM)
	F3=1.00-R3*ANGCT[IE][I]        
	if(R31 > PSCT[IE][I]:
	) F3=-F3     
	else if (INDEX[I] == 2) :
	EPSI=PSCT[IE][I]
	F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3)))  
	else:     
	# ISOTROPIC SCATTERING                                                 
	F3=1.00-2.00*R3  
	# endif
	THETA0=numpy.arccos(F3)                                                  
	R4=DRAND48(RDUM)
	PHI0=F4*R4                                                        
	F8=numpy.sin(PHI0)                                                     
	F9=numpy.cos(PHI0)                                                     
	if(E < EI):
	EI=0.00                                              
	ARG1=1.00-S1*EI/E                                                
	ARG1=DMAX1[ARG1][SMALL]                                            
	D=1.00-F3*math.sqrt(ARG1)                                            
	E1=E*(1.00-EI/(S1*E)-2.00*D/S2) 
	E1=DMAX1[E1][SMALL]                                                
	Q=math.sqrt((E/E1)*ARG1)/S1                                           
	Q=DMIN1[Q][1.00]                                                  
	THETA=numpy.arcsin(Q*numpy.sin(THETA0))                                       
	F6=numpy.cos(THETA)                                                    
	U=(S1-1.00)*(S1-1.00)/ARG1                                      
	CSQD=F3*F3                                                        
	if(F3 < 0.00 and CSQD > U):
		F6=-1.00*F6                        
	F5=numpy.sin(THETA)                                                    
	DCZ2=DMIN1[DCZ2][1.00]   
	ARGZ=math.sqrt(DCX2*DCX2+DCY2*DCY2)
	if(ARGZ == 0.00):
	:
	DCZ1=F6         
	DCX1=F9*F5                             
	DCY1=F8*F5
	if(NTMPFLG == 1):
	:
	# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
	F5S=F5*math.sqrt(E1/ES[NCLTMP])
	if(F5S >= 1.0):
	F5S=0.999
	THSEC=numpy.arcsin(F5S)
	F5S=numpy.sin(THSEC)
	F6S=numpy.cos(THSEC)
	if(F6 < 0.0):
	F6S=-F6S
	PHIS=PHI0+API   
	if(PHIS > F4):
	PHIS=PHI0-F4
	F8S=numpy.sin(PHIS)
	F9S=numpy.cos(PHIS)
	DCZ[NCLTMP]=F6S
	DCX[NCLTMP]=F9S*F5S
	DCY[NCLTMP]=F8S*F5S
	NTMPFLG=0
	# endif
	GO TO 190
	# endif      
	DCZ1=DCZ2*F6+ARGZ*F5*F8   
	DCY1=DCY2*F6+(F5/ARGZ)*(DCX2*F9-DCY2*DCZ2*F8)                     
	DCX1=DCX2*F6-(F5/ARGZ)*(DCY2*F9+DCX2*DCZ2*F8) 
	if(NTMPFLG == 1):
	:
	# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
	F5S=F5*math.sqrt(E1/ES[NCLTMP])
	if(F5S >= 1.0):
	F5S=0.999          
	THSEC=numpy.arcsin(F5S)
	F5S=numpy.sin(THSEC)
	F6S=numpy.cos(THSEC)
	if(F6 < 0.0):
	F6S=-F6S
	PHIS=PHI0+API   
	if(PHIS > F4):
	PHIS=PHI0-F4
	F8S=numpy.sin(PHIS)
	F9S=numpy.cos(PHIS)
	DCZ[NCLTMP]=DCZ2*F6S+ARGZ*F5S*F8S                               
	DCY[NCLTMP]=DCY2*F6S+(F5S/ARGZ)*(DCX2*F9S-DCY2*DCZ2*F8S)        
	DCX[NCLTMP]=DCX2*F6S-(F5S/ARGZ)*(DCY2*F9S+DCX2*DCZ2*F8S)
	NTMPFLG=0
	# endif 
	190 CONTINUE  
	#     VTOT=CONST9*math.sqrt(E1)
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.0D-12
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# TEST IF ELECTRON IS THERMALISED
	if(E1 > ETHRM):
	GO TO 1
	# STORE POSITION AND TIME OF THERMALISED ELECTRON
	191 CONTINUE
	K1=K1+1
	XST[K1]=X
	YST[K1]=Y
	ZST[K1]=Z
	TST[K1]=ST
	NFGF[K1]=NFLGFF
	NFGPP[K1]=NFLGPPP
	NFGBR[K1]=NFLGBRMM
	TTIME[K1]=ST-TLAST
	NELEC=NELEC+1
	NETOT=NETOT+1
	#     WRITE(6,777) XST[K1],YST[K1],ZST[K1],TST[K1],NFGF[K1],NFGPP[K1],
	#    /NFGBR[K1],NELEC,NETOT,K1
	# 777 print(' XST=','%.4f' % ,' YST=','%.4f' % ,' ZST=','%.4f' % ,' TST=','%.4f' % ,/,
	#    /' NFGF=',I4,' NFGPP=',I4,' NFGBR=',I4,' NELEC=',I4,' NETOT=',I4,
	#    /' K1=',I4)
	335 if(K1 == 150000) GO TO 889
	if(NELEC == (NCLUS+1):
	) :
	# LAST ELECTRON IN CLUSTER, DO STATISTICS ON PRIMARY
	CALL STATS(J11,J1)
	GO TO 210 
	# endif
	# GET NEW IONISATION ELECTRON FROM STORE
	X=XS[NELEC]
	Y=YS[NELEC]
	Z=ZS[NELEC]
	ST=TS[NELEC]
	NFLGFF=NFLGFC[NELEC]
	NFLGPPP=NFLGPPC[NELEC]
	NFLGBRMM=NFLGBRMC[NELEC]
	TLAST=TS[NELEC]
	E1=ES[NELEC]
	DCX1=DCX[NELEC]
	DCY1=DCY[NELEC]
	DCZ1=DCZ[NELEC] 
	#     IF(NELEC > 94) WRITE(6,766) X,Y,Z,ST,E1,DCX1,DCY1,DCZ1,NELEC
	# 766 print(' X=','%.4f' % ,' Y=','%.4f' % ,' Z=','%.4f' % ,' T=','%.4f' % ,/,' E=',
	#    /'%.4f' % ,' DCX=','%.4f' % ,' DCY=','%.4f' % ,' DCZ=','%.4f' % ,' NELEC=',I6,/)
	# STORE ALREADY THERMALISED ELECTRONS
	if(E1 < ETHRM):
	GO TO 191 
	GO TO 1  
	# MAIN LOOP # end   
	210 CONTINUE
	# RESET NUMBER OF EVENTS FOR BAD EVENTS
	if(IMIP > 2):
	NDELTA=NDELTA-IBADTOT
	#
	WRITE(6,887) EMAX,NEOVFL
	887 print(' EMAX=','%.7f' % ,' NEOVFL =',I5)
	if(EMAX > EFINAL):
	:
	WRITE(6,989) EFINAL,EMAX
	989 print('INCREASE ENERGY LIMIT FROM','%.6f' % ,' EV TO AT LEAST','%.6f' % ,' EV.')
	sys.exit()
	# endif                                         
	return 
	889 NLEFT=NCLUS-NELEC
	WRITE(6,992) NPRIME,NLEFT,NCLUS
	992 print(3(/),' WARNING STOPPED: AFTER NPRIME=',I6,' LAST PRIMARY HAS AT LEAST ',I6,' SECONDARIES LEFT TO TRACK, OUT OF ',I6,' ELECTRONS ALREADY IN CLUSTER')
	sys.exit()
	return
	# end
def MONTEFB():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)                                         
	COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	COMMON/INPT1/NDVEC
	COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
	COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE 
	COMMON/BFLD/EOVB,WB,BTHETA,BMAG                                   
	COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),    RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA[3,512]
	COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST
	COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL, NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT  
	COMMON/RLTVY/BET[2000],GAM(20000),VC,EMS
	COMMON/STTS/XST(150000),YST(150000),ZST(150000),TST(150000),TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,NEGION,EST1,EST2
	COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),TSTEXC(150000),NSTEXC
	COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),TSTN(150000),IDNUL(150000),NEXCNUL
	COMMON/IONC/DOUBLE(6,20000),CMINIXSC[6],CMINEXSC[6],ECLOSS[6],WPLN[6],ICOUNT,AVPFRAC(3,6)
	COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),EG2(512),WKLM(512),DSTFL(512)
	COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512) 
	COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO 
	COMMON/CASRS/ECAS(400),XCAS(400),YCAS(400),ZCAS(400),DRXS(400),DRYS(400),DRZS(400),TT1(400),NFLGF(400),NFLGPP(400),IEVNTL
	COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	COMMON/BREMG/EBRGAM(10),BRDCOSX(10),BRDCOSY(10),BRDCOSZ[10],BRX(10),BRY(10),BRZ[10],BRT(10),EBRTOT[6],NBREM[6]
	COMMON/CASRSB/ECASB[400],XCASB[400],YCASB[400],ZCASB[400],DRXB[400],DRYB[400],DRZB[400],TTB1(400),NFLGFB[400],NFLGPPB[400],IEVNTLB
	COMMON/CASRSE/ECASE(400),XCASE(400),YCASE(400),ZCASE(400),DRXCE(400),DRYCE(400),DRZCE(400),TCASE(400),NFLGFE(400),NFLGPPE(400),IEVENTE
	COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
	COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
	DIMENSION XS(150000),YS(150000),ZS(150000),TS(150000),ES(150000),DCX(150000),DCY(150000),DCZ[150000],NFLGFC(150000),NFLGPPC(150000),NFLGBRMC(150000)           
	DIMENSION TEMP(20000)   
	# -------------------------------------------------------------------  
	#  RELATIVISTIC VERSION
	#  ELECTRIC FIELD ALONG Z-AXIS MAGNETIC FIELD ALONG  X-AXIS.
	#  TRACKS DELTA ELECTRONS AND UPDATES ARRAYS CONTAINING POSITION AND
	#  TIME OF THERMALISED ELECTRONS.
	#  CALCULATES NUMBER OF PRODUCED ELECTRONS PER PRIMARY DELTA AND OTHER
	#  HIGHER FANO FACTORS .
	# ------------------------------------------------------------------- 
	# VARYING ENERGY STEPS
	if(EFINAL <= 140000.):
	:
	ESTEP1=(EFINAL-16000.0)/float(4000)
	else:
	ESTEP1=20.0
	ESTEP2=(EFINAL-92000.0)/float(4000)
	# endif
	NPRINT=0
	J20000=20000
	J300=300
	API=numpy.arccos(-1.00)
	SMALL=1.0D-20         
	EMAX=0.00                                            
	TMAX1=0.00                                                       
	RDUM=RSTART                                                       
	CONST9=CONST3*0.010
	DO 25 I=1,300
	25 TIME[I]=0.00
	DO 26 I=1,30
	26 ICOLL[I]=0
	DO 27 I=1,512
	27 ICOLN[I]=0
	NREAL=0                                                           
	NNULL=0
	NETOT=0
	NEXCTOT=0
	NITOT=0
	NMXADD=0
	NTMPFLG=0
	THETA1=THETA
	PHI1=PHI
	F4=2.00*API
	NEOVFL=0
	# CALCULATE MAXIMUM COLLISION FREQUENCY
	TLIM=0.0
	DO 111 J=1,20000
	TEMP[J]=TCFN[J]+TCF[J]
	if(TLIM < TEMP[J]:
	) TLIM=TEMP[J] 
	111 CONTINUE
	J1=0
	# START OF PRIMARY EVENT LOOP
	DO 210 J11=1,NDELTA
	J1=J1+1
	NPRIME=J1   
	NGEXC1=0
	NGEXC2=0
	NGEXC3=0
	NGEXC4=0
	NGEXC5=0
	NGEXC6=0
	#     INITIAL DIRECTION COSINES                                         
	DCZ1=numpy.cos(THETA1) 
	DCX1=numpy.sin(THETA1)*numpy.cos(PHI1)                                      
	DCY1=numpy.sin(THETA1)*numpy.sin(PHI1) 
	NFLGFF=0
	NFLGPPP=0
	NFLGBRMM=0
	NFLGHIGH=0
	EST1=ESTART
	# INITIAL VELOCITY,TIME AND POSITION
	E1=ESTART
	GAM1=(EMS+E1)/EMS
	GAM12=GAM1
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.0D-12
	#     VTOT=CONST9*math.sqrt(E1)       
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT      
	X=0.00
	Y=0.00
	Z=0.00 
	K1=0
	KEXC=0
	NSTEXC=0
	NEXCNUL=0
	NCLUS=0
	NELEC=0
	NEGION=0
	TLAST=0.00
	ST=0.00
	TDASH=0.00
	if(IMIP == 2):
	GO TO 1
	if(IMIP > 2):
	:
	# READ IN FIRST ELECTRON FROM BETA DECAY OR XRAY UNTHERMALISED CLUSTERS
	CALL CASRES(J11,IBADTOT,IBAD1)
	#  SKIP IF BAD EVENT
	if(IBAD1 == 1):
	:
	J1=J1-1
	GO TO 210
	# endif 
	else if(IMIP == 1) :
	# READ IN FIRST ELECTRON FROM MIP INTERACTION
	CALL CASREM(J11)
	EST1=ECAS[1]
	EST2=EST1
	# endif
	X=XCAS[1]
	Y=YCAS[1]
	Z=ZCAS[1]
	ST=TT1[1]
	TS[1]=TT1[1]
	E1=ECAS[1]
	DCZ1=DRZS[1]
	DCY1=DRYS[1]
	DCX1=DRXS[1]
	NFLGFF=NFLGF[1]
	NFLGPPP=NFLGPP[1]
	NFLGBRMM=0
	NFLGHIGH=NFLGFF
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=VC*BET1*1.0D-12
	#     VTOT=CONST9*math.sqrt(E1)
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# PUT REMAINDER OF ELECTRONS INTO CLUSTER STORE
	ISDUM=0
	DO 35 IST=2,IEVNTL
	ISDUM=ISDUM+1
	XS[ISDUM]=XCAS[IST]
	YS[ISDUM]=YCAS[IST]
	ZS[ISDUM]=ZCAS[IST]
	TS[ISDUM]=TT1[IST]
	ES[ISDUM]=ECAS[IST]
	DCX[ISDUM]=DRXS[IST]
	DCY[ISDUM]=DRYS[IST]
	DCZ[ISDUM]=DRZS[IST]
	NFLGFC[ISDUM]=NFLGF[IST]
	NFLGPPC[ISDUM]=NFLGPP[IST]
	NFLGBRMC[ISDUM]=0
	NCLUS=ISDUM
	if(NFLGFC[IST]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[IST]
	35 CONTINUE
	GAM12=GAM1
	# START OF LOOP FOR NEWLY CREATED ELECTRONS                             
	1 CONTINUE                                                          
	R1=DRAND48(RDUM)
	T=-math.log(R1)/TLIM+TDASH
	TDASH=T
	WBT=WB*T/GAM12
	#     WBT=WB*T
	COSWT=numpy.cos(WBT)
	SINWT=numpy.sin(WBT)
	DZ=GAM12*(CZ1*SINWT+(EOVB-CY1)*(1.00-COSWT))/WB
	#     DZ=(CZ1*SINWT+(EOVB-CY1)*(1.00-COSWT))/WB 
	E=E1+DZ*EFIELD*100.00
	GAM2=(EMS+E)/EMS
	BET2=math.sqrt(1.00-1.00/(GAM2*GAM2))
	#913  print(3X,' AFTER STORE NREAL=',I10,' DZ=','%.3f' %,'E1=','%.3f' %,' COS
	#    /WT=','%.3f' %,' SINWT=','%.3f' %,' WBT=','%.3f' %,' CY1=','%.3f' %)   
	if(E < 0.00):
	:
	#      IF(NPRINT == 0) WRITE(6,913)NREAL,DZ,E1,COSWT,SINWT,WBT,CY1
	#      NPRINT=1  
	E=0.0010
	# endif                                                   
	# INSERT NEW ALGORITHM TO FIND IE FOR VARYING ENERGY STEP          
	if(IMIP == 1):
	:                                     
	IE=int(E/ESTEP)+1                                               
	else:
	if(EFINAL <= 20000.):
	:
	IE=int(E/ESTEP)+1
	else if(EFINAL <= 140000.) :
	if(E <= 16000.):
	:
	IE=int(E)+1
	else:
	IE=16000+int((E-16000.)/ESTEP1)
	# endif
	else:
	if(E <= 12000.):
	:
	IE=int(E)+1
	else if(E <= 92000.) :
	IE=12000+int((E-12000.)/ESTEP1)
	else:
	IE=16000+int((E-92000.)/ESTEP2)
	# endif
	# endif
	# endif 
	IE=DMIN0(IE,J20000)                                            
	#                                                                       
	#     TEST FOR #real OR NULL COLLISION                                   
	#                                                                       
	R5=DRAND48(RDUM)
	TEST1=TCF[IE]/TLIM                                                
	if(R5 <= TEST1):
	GO TO 137                                        
	NNULL=NNULL+1                     
	TEST2=TEMP[IE]/TLIM
	if(R5 < TEST2):
	:
	# TEST FOR NULL LEVELS
	if(NPLAST == 0):
	GO TO 1
	R2=DRAND48(RDUM) 
	I=0
	888  I=I+1
	if(CFN[IE][I]:
	< R2) GO TO 888
	# INCREMENT NULL LEVEL SUM
	NEXCNUL=NEXCNUL+1
	ICOLNN[I]=ICOLNN[I]+1
	# STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION AND DISSOCIATION FROM 
	#    NULL EXCITATION
	# NOTE: SMALL APPROX USED POSITION OF PREVIOUS #real COLLISION
	XSTN[NEXCNUL]=X
	YSTN[NEXCNUL]=Y
	ZSTN[NEXCNUL]=Z
	TSTN[NEXCNUL]=ST
	IDNUL[NEXCNUL]=I                            
	GO TO 1     
	else:
	# NULL
	GO TO 1
	# endif                                                     
	#                                                                       
	#  CALCULATE DIRECTION COSINES AND POSITIONS AT INSTANT BEFORE COLLISION
	137 T2=T*T
	if(E > EMAX):
	EMAX=E
	if(T > TMAX1):
	TMAX1=T
	TDASH=0.00 
	NREAL=NREAL+1
	# CALC VELOCITY
	CX2=CX1
	CY2=(CY1-EOVB)*COSWT+CZ1*SINWT+EOVB
	CZ2=CZ1*COSWT-(CY1-EOVB)*SINWT
	# CALC DIRECTION COSINES
	VTOT=math.sqrt(CX2*CX2+CY2*CY2+CZ2*CZ2)
	DCX2=CX2/VTOT
	DCY2=CY2/VTOT
	DCZ2=CZ2/VTOT                                                     
	# CALC NEW POSITION                                                
	X=X+CX1*T                                                         
	Y=Y+EOVB*T+GAM12*((CY1-EOVB)*SINWT+CZ1*(1.00-COSWT))/WB
	Z=Z+DZ 
	GAM12=(GAM1+GAM2)/2.00         
	ST=ST+T
	IT=int(T+1.00)                                                  
	IT=DMIN0[IT][J300]                                               
	TIME[IT]=TIME[IT]+1.00                                           
	# --------------------------------------------------------------------- 
	#     DETERMINATION OF #real COLLISION TYPE                              
	# --------------------------------------------------------------------- 
	R2=DRAND48(RDUM)
	I=0                                                               
	140 I=I+1                                                             
	if(CF[IE][I]:
	< R2) GO TO 140      
	#************************************************************
	# CHECK IF BREMSSTRAHLUNG
	if(IZBR[I]:
	!= 0 and LBRM == 1) :
	NFLGBRMM=1
	IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1
	ICOLN[I]=ICOLN[I]+1
	DO 141 KNGS=1,NGAS
	if(IPT == (KNGS*5):
	-1) GO TO 142
	141  CONTINUE
	142  IATOMNO=IZBR[I] 
	CALL BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
	NBREM[KNGS]=NBREM[KNGS]+1
	EBRTOT[KNGS]=EBRTOT[KNGS]+EGAMMA
	#      WRITE(6,668) EGAMMA,J11   
	# 668 print(' BREM EGAMMA=','%.4f' % ,' EVENT NO=',I5)
	# GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
	E1=EOUT
	DCX1=EDCX
	DCY1=EDCY
	DCZ1=EDCZ
	# RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE : STORE CONVERTED
	# ELECTRONS IN COMMON/CASRSB/
	# 
	CALL BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
	# BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
	if(ILOW == 1):
	GO TO 190
	# 
	# STORE BREMSSTARHLUNG DATA IN CLUSTER STORE
	#
	DO 890 KBR=1,IEVNTLB
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif     
	ES[NCLUS]=ECASB[KBR]
	XS[NCLUS]=XCASB[KBR]
	YS[NCLUS]=YCASB[KBR]
	ZS[NCLUS]=ZCASB[KBR]
	TS[NCLUS]=TTB1[KBR]
	DCX[NCLUS]=DRXB[KBR]
	DCY[NCLUS]=DRYB[KBR]
	DCZ[NCLUS]=DRZB[KBR]
	NFLGFC[NCLUS]=NFLGFB[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPB[KBR]
	NFLGBRMC[NCLUS]=2
	890  CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 190
	# endif
	891 CONTINUE
	#****************************************************************
	#     S1=RGAS[I]                   
	S1=1.00+GAM2*(RGAS[I]-1.00)  
	EI=EIN[I]
	if(E < EI):
	:
	EI=E-0.00010
	# endif                                                          
	if(IPN[I]:
	== 0) GO TO 666
	# ATTACHMENT       
	if(IPN[I]:
	== -1) :
	NETOT=NETOT+1
	NITOT=NITOT+1
	NELEC=NELEC+1
	NEGION=NEGION+1
	IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1
	ICOLN[I]=ICOLN[I]+1 
	IT=int(T+1.00)
	IT=DMIN0[IT][J300]
	TIME[IT]=TIME[IT]+1.00
	GO TO 335
	# endif   
	EISTR=EI
	if(IONMODEL[I]:
	> 0) :
	# CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
	# FIVE DIFFERENT MODELS
	CALL IONSPLIT(I,E,EI,ESEC)
	GO TO 544
	# endif
	R9=DRAND48(RDUM)
	#    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
	ESEC=WPL[I]*TAN(R9*ATAN((E-EI)/(2.00*WPL[I]))) 
	ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
	544 CONTINUE
	EI=ESEC+EI 
	# STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
	# OF SECONDARY IONISATION ELECTRON 
	NCLUS=NCLUS+1
	NMXADD=MAX[NCLUS][NMXADD]
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL
	546   print(2X,' def STOPPED: . NCLUS=',I7,' NREAL=',I10)
	sys.exit()
	# endif     
	XS[NCLUS]=X       
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	ES[NCLUS]=ESEC 
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	NTMPFLG=1
	NCLTMP=NCLUS
	# RANDOMISE SECONDARY ELECTRON DIRECTION
	#     R3=drand48(RDUM)
	#     F3=1.0-2.00*R3
	#     THETA0=DACOS(F3)
	#     F6=DCOS(THETA0)
	#     F5=DSIN(THETA0)
	#     R4=drand48(RDUM)
	#     PHI0=F4*R4
	#     F8=DSIN(PHI0)
	#     F9=DCOS(PHI0)               
	#     DCX[NCLUS]=F9*F5
	#     DCY[NCLUS]=F8*F5
	#     DCZ[NCLUS]=F6    
	#*********************************************************
	if(IECASC == 0):
	GO TO 333
	if(LEGAS[I]:
	== 0) GO TO 333
	# USE COMPLETE CASCADE FOR ELECTRON IONISATION
	KG1=NEGAS[I]
	LG1=LEGAS[I]
	IGSHEL=IESHELL[I]
	CALL CASCADEE(J11,KG1,LG1,X,Y,Z,ST,ESEC,IGSHEL)
	#
	# STORE CASCADE IN CLUSTER STORE
	#
	ETSUM=0.0
	DO 844 KBR=1,IEVENTE
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	:
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif
	ES[NCLUS]=ECASE[KBR]
	ETSUM=ETSUM+ES[NCLUS]
	XS[NCLUS]=XCASE[KBR]
	YS[NCLUS]=YCASE[KBR]
	ZS[NCLUS]=ZCASE[KBR]
	TS[NCLUS]=TCASE[KBR]
	DCX[NCLUS]=DRXCE[KBR]
	DCY[NCLUS]=DRYCE[KBR]
	DCZ[NCLUS]=DRZCE[KBR]
	NFLGFC[NCLUS]=NFLGFE[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPE[KBR]
	NFLGBRMC[NCLUS]=NFLGBRMM
	844 CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 666
	#*********************************************************
	# STORE POSSIBLE SHELL EMISSIONS AUGER OR FLUORESCENCE 
	333 if(EISTR > 30.0) :
	# TEST IF FLUORESCENCE EMISSION
	IFLTST=0:
	if(WKLM[I]:
	> 0.0) :
	R9=DRAND48(RDUM)
	if(R9 < WKLM[I]:
	) IFLTST=1
	# endif
	if(IFLTST == 0):
	:
	# AUGER EMISSION WITHOUT FLUORESCENCE
	NAUG=NC0[I]
	EAVAUG=EC0[I]/float(NAUG)
	DO 700 JFL=1,NC0[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	700   CONTINUE 
	else:
	# AUGER EMISSION AND FLUORESENCE 
	if(NG2[I]:
	== 0) GO TO 702
	NAUG=NG2[I]
	EAVAUG=EG2[I]/float(NAUG)
	DO 701 JFL=1,NG2[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	701   CONTINUE
	702   if(NG1[I] == 0) GO TO 704
	NAUG=NG1[I]
	EAVAUG=EG1[I]/float(NAUG)
	R9=DRAND48(RDUM)
	DFL=-math.log(R9)*DSTFL[I]
	DO 703 JFL=1,NG1[I]
	NCLUS=NCLUS+1
	R3=DRAND48(RDUM)
	THEFL=numpy.arccos(1.0-2.00*R3)
	R4=DRAND48(RDUM)
	PHIFL=F4*R4
	XS[NCLUS]=X+DFL*numpy.sin(THEFL)*numpy.cos(PHIFL)
	YS[NCLUS]=Y+DFL*numpy.sin(THEFL)*numpy.sin(PHIFL)
	ZS[NCLUS]=Z+DFL*numpy.cos(THEFL)
	NFLGFC[NCLUS]=NFLGHIGH+1
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	NFLGHIGH=NFLGFC[NCLUS]
	703   CONTINUE
	704   CONTINUE
	# endif
	# endif
	#                                                                       
	#  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
	#   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
	#
	666 IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1 
	ICOLN[I]=ICOLN[I]+1      
	# IF EXCITATION : ADD PROBABILITY ,PENFRA(1,I), OF TRANSFER TO GIVE 
	# IONISATION OF THE OTHER GASES IN MIXTURE              
	if(IPEN == 0 or NGAS == 1):
	GO TO 5          
	if(PENFRA[1][I] != 0.0):
	:
	RAN=DRAND48(RDUM) 
	if(RAN > PENFRA[1][I]):
	GO TO 5
	NCLUS=NCLUS+1    
	# ENTER HERE POSSIBLE DELOCALISATION LENGTH FOR PENNING TRANSFER
	if(PENFRA[2][I] == 0.0):
	:
	XS[NCLUS]=X  
	YS[NCLUS]=Y    
	ZS[NCLUS]=Z
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	GO TO 667
	# endif
	ASIGN=1.0
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	XS[NCLUS]=X-math.log(RAN)*PENFRA[2][I]*ASIGN
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	YS[NCLUS]=Y-math.log(RAN)*PENFRA[2][I]*ASIGN
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN
	ZS[NCLUS]=Z-math.log(RAN)*PENFRA[2][I]*ASIGN
	667  RAN=DRAND48(RDUM)
	TS[NCLUS]=ST-math.log(RAN)*PENFRA[3][I]
	# ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
	ES[NCLUS]=1.0 
	DCX[NCLUS]=DCX1
	DCY[NCLUS]=DCY1
	DCZ[NCLUS]=DCZ1
	GO TO 6
	# endif
	#     GO TO 6
	# CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
	5  if(IPN[I] == 0) :
	if((RGAS[I]:
	*EIN[I]) > 4.0) :
	KEXC=KEXC+1
	if(KEXC > 150000):
	: 
	WRITE(6,548) KEXC
	548     print(2X,' def STOPPED: . KEXC=',I7)
	sys.exit()
	# endif
	# FIND GAS IN WHICH EXCITATION OCCURED AND INCREMENT COUNTER
	if(I <= IDG1):
	: 
	NGEXC1=NGEXC1+1
	else if(I <= IDG2) :
	NGEXC2=NGEXC2+1
	else if(I <= IDG3) :
	NGEXC3=NGEXC3+1
	else if(I <= IDG4) :
	NGEXC4=NGEXC4+1
	else if(I <= IDG5) :
	NGEXC5=NGEXC5+1
	else if(I <= IDG6) :
	NGEXC6=NGEXC6+1
	else:
	WRITE(6,9911) 
	9911    print(' def STOPPED: BAD GAS ID IN MONTE')
	sys.exit()
	# endif
	NEXCTOT=NEXCTOT+1
	NSTEXC=NSTEXC+1
	XSTEXC[KEXC]=X
	YSTEXC[KEXC]=Y
	ZSTEXC[KEXC]=Z
	TSTEXC[KEXC]=ST
	# endif
	# endif 
	6  S2=(S1*S1)/(S1-1.00) 
	#  ANISOTROPIC SCATTERING
	R3=DRAND48(RDUM) 
	if(INDEX[I]:
	== 1) :
	R31=DRAND48(RDUM)
	F3=1.00-R3*ANGCT[IE][I]      
	if(R31 > PSCT[IE][I]:
	)  F3=-F3
	else if(INDEX[I] == 2) :
	EPSI=PSCT[IE][I]
	F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3)))
	else: 
	# ISOTROPIC SCATTERING                   
	F3=1.00-2.00*R3  
	# endif
	THETA0=numpy.arccos(F3)                                                  
	R4=DRAND48(RDUM)
	PHI0=F4*R4                                                        
	F8=numpy.sin(PHI0)                                                     
	F9=numpy.cos(PHI0)                                                     
	if(E < EI):
	EI=0.00                                              
	ARG1=1.00-S1*EI/E                                                
	ARG1=DMAX1[ARG1][SMALL]                                            
	D=1.00-F3*math.sqrt(ARG1)                                            
	E1=E*(1.00-EI/(S1*E)-2.00*D/S2) 
	E1=DMAX1[E1][SMALL]                                                
	Q=math.sqrt((E/E1)*ARG1)/S1                                           
	Q=DMIN1[Q][1.00]                                                  
	THETA=numpy.arcsin(Q*numpy.sin(THETA0))                                       
	F6=numpy.cos(THETA)                                                    
	U=(S1-1.00)*(S1-1.00)/ARG1                                      
	CSQD=F3*F3                                                        
	if(F3 < 0.00 and CSQD > U):
		F6=-1.00*F6                        
	F5=numpy.sin(THETA)                                                    
	DCZ2=DMIN1[DCZ2][1.00]                                            
	ARGZ=math.sqrt(DCX2*DCX2+DCY2*DCY2)
	if(ARGZ == 0.00):
	:
	DCZ1=F6         
	DCX1=F9*F5                             
	DCY1=F8*F5 
	if(NTMPFLG == 1):
	:
	# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
	F5S=F5*math.sqrt(E1/ES[NCLTMP])
	if(F5S > 1.0):
	F5S=1.0
	THSEC=numpy.arcsin(F5S)
	F5S=numpy.sin(THSEC)
	F6S=numpy.cos(THSEC)
	if(F6 < 0.0):
	F6S=-F6S
	PHIS=PHI0+API   
	if(PHIS > F4):
	PHIS=PHI0-F4
	F8S=numpy.sin(PHIS)
	F9S=numpy.cos(PHIS)
	DCZ[NCLTMP]=F6S
	DCX[NCLTMP]=F9S*F5S
	DCY[NCLTMP]=F8S*F5S
	NTMPFLG=0
	# endif
	GO TO 190
	# endif                                            
	DCZ1=DCZ2*F6+ARGZ*F5*F8                                           
	DCY1=DCY2*F6+(F5/ARGZ)*(DCX2*F9-DCY2*DCZ2*F8)                     
	DCX1=DCX2*F6-(F5/ARGZ)*(DCY2*F9+DCX2*DCZ2*F8) 
	if(NTMPFLG == 1):
	:
	# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
	F5S=F5*math.sqrt(E1/ES[NCLTMP])
	if(F5S > 1.0):
	F5S=1.0            
	THSEC=numpy.arcsin(F5S)
	F5S=numpy.sin(THSEC)
	F6S=numpy.cos(THSEC)
	if(F6 < 0.0):
	F6S=-F6S
	PHIS=PHI0+API   
	if(PHIS > F4):
	PHIS=PHI0-F4
	F8S=numpy.sin(PHIS)
	F9S=numpy.cos(PHIS)
	DCZ[NCLTMP]=DCZ2*F6S+ARGZ*F5S*F8S                               
	DCY[NCLTMP]=DCY2*F6S+(F5S/ARGZ)*(DCX2*F9S-DCY2*DCZ2*F8S)        
	DCX[NCLTMP]=DCX2*F6S-(F5S/ARGZ)*(DCY2*F9S+DCX2*DCZ2*F8S)
	NTMPFLG=0
	# endif 
	190 CONTINUE 
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.D-12 
	#     VTOT=CONST9*math.sqrt(E1)
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# TEST IF ELECTRON IS THERMALISED
	if(E1 > ETHRM):
	GO TO 1
	# STORE POSITION AND TIME OF THERMALISED ELECTRON
	191 CONTINUE
	K1=K1+1
	XST[K1]=X
	YST[K1]=Y
	ZST[K1]=Z
	TST[K1]=ST
	NFGF[K1]=NFLGFF
	NFGPP[K1]=NFLGPPP
	NFGBR[K1]=NFLGBRMM
	TTIME[K1]=ST-TLAST
	NELEC=NELEC+1
	NETOT=NETOT+1
	335 if(K1 == 150000) GO TO 889
	if(NELEC == (NCLUS+1):
	) :
	# LAST ELECTRON IN CLUSTER , DO STATISTICS ON CLUSTER  
	CALL STATS(J11,J1)
	GO TO 210
	# endif 
	# GET NEW IONISATION ELECTRON FROM STORE
	X=XS[NELEC]
	Y=YS[NELEC]
	Z=ZS[NELEC]
	ST=TS[NELEC]
	NFLGFF=NFLGFC[NELEC]
	NFLGPPP=NFLGPPC[NELEC]
	NFLGBRMM=NFLGBRMC[NELEC]
	TLAST=TS[NELEC] 
	E1=ES[NELEC]
	DCX1=DCX[NELEC]
	DCY1=DCY[NELEC]
	DCZ1=DCZ[NELEC]  
	if(E1 < ETHRM):
	GO TO 191  
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.D-12 
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	GO TO 1                                    
	#  MAIN LOOP # end 
	210 CONTINUE
	# RESET NUMBER OF EVENTS FOR BAD EVENTS
	if(IMIP > 2):
	NDELTA=NDELTA-IBADTOT
	#
	WRITE(6,887) EMAX,NEOVFL
	887 print(' EMAX=','%.7f' % ,' NEOVFL =',I5)
	if(EMAX > EFINAL):
	:
	WRITE(6,989) EFINAL,EMAX
	989 print('INCREASE ENERGY LIMIT FROM','%.6f' % ,' EV TO AT LEAST','%.6f' % ,' EV.')
	sys.exit()
	# endif                                         
	return 
	889 NLEFT=NCLUS-NELEC
	WRITE(6,992) NPRIME,NLEFT,NCLUS
	992 print(3(/),' WARNING STOPPED: AFTER NPRIME=',I6,' LAST PRIMARY HAS AT LEAST ',I6,' SECONDARIES LEFT TO TRACK,OUT OF ',I6,' ELECTRONS ALREADY IN CLUSTER')
	sys.exit()
	return
	# end                                                   
def MONTEFC():
	# IMPLICIT #real*8 (A-H,O-Z) 
	# IMPLICIT #integer*8 (I-N)                                        
	COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	COMMON/INPT1/NDVEC
	COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
	COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE  
	COMMON/BFLD/EOVB,WB,BTHETA,BMAG
	COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),    RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA[3,512]
	COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST
	COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL, NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT  
	COMMON/RLTVY/BET[2000],GAM(20000),VC,EMS
	COMMON/STTS/XST(150000),YST(150000),ZST(150000),TST(150000),TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,NEGION,EST1,EST2
	COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),TSTEXC(150000),NSTEXC
	COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),TSTN(150000),IDNUL(150000),NEXCNUL
	COMMON/IONC/DOUBLE(6,20000),CMINIXSC[6],CMINEXSC[6],ECLOSS[6],WPLN[6],ICOUNT,AVPFRAC(3,6)
	COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),EG2(512),WKLM(512),DSTFL(512)
	COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512) 
	COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO
	COMMON/CASRS/ECAS(400),XCAS(400),YCAS(400),ZCAS(400),DRXS(400),DRYS(400),DRZS(400),TT1(400),NFLGF(400),NFLGPP(400),IEVNTL     
	COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
	COMMON/BREMG/EBRGAM(10),BRDCOSX(10),BRDCOSY(10),BRDCOSZ[10],BRX(10),BRY(10),BRZ[10],BRT(10),EBRTOT[6],NBREM[6] 
	COMMON/CASRSB/ECASB[400],XCASB[400],YCASB[400],ZCASB[400],DRXB[400],DRYB[400],DRZB[400],TTB1(400),NFLGFB[400],NFLGPPB[400],IEVNTLB
	COMMON/CASRSE/ECASE(400),XCASE(400),YCASE(400),ZCASE(400),DRXCE(400),DRYCE(400),DRZCE(400),TCASE(400),NFLGFE(400),NFLGPPE(400),IEVENTE     
	COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
	COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
	DIMENSION XS(150000),YS(150000),ZS(150000),TS(150000),ES(150000),DCX(150000),DCY(150000),DCZ[150000],NFLGFC(150000),NFLGPPC(150000),NFLGBRMC(150000)           
	DIMENSION TEMP(20000) 
	# ------------------------------------------------------------------- 
	#   RELATIVISTIC VERSION  
	#   CALCULATES COLLISION EVENTS AND UPDATES DIFFUSION AND VELOCITY.
	#   THIS ROUTINE HANDLES TERMINATIONS AT FIXED DRIFT TIMES. 
	#   SOLVES MOTION IN COORDINATE SYSTEM WITH BFIELD ALIGNED TO X-AXIS
	#   ELECTRIC FIELD AT AN ANGLE BTHETA IN THE X-Z PLANE.
	#   THE RESULTS FOR THE VELOCITY VECTORS  ARE : 
	#   ROTATED INTO THE STANDARD COORDINATE FRAME WITH THE ELECTRIC FIELD 
	#   ALONG THE Z-AXIS AND THE BFIELD AT AN ANGLE BTHETA TO THE ELECTRIC
	#   FIELD IN THE X-Z PLANE  
	# -------------------------------------------------------------------
	# VARYING ENERGY STEPS
	if(EFINAL <= 140000.):
	:
	ESTEP1=(EFINAL-16000.0)/float(4000)
	else:
	ESTEP1=20.0
	ESTEP2=(EFINAL-92000.0)/float(4000)
	# endif
	NPRINT=0 
	J20000=20000
	J300=300
	API=numpy.arccos(-1.00)
	SMALL=1.0D-20
	EMAX=0.00
	TMAX1=0.00
	RDUM=RSTART
	CONST9=CONST3*0.010
	DO 25 I=1,300
	25 TIME[I]=0.00
	DO 26 I=1,30
	26 ICOLL[I]=0
	DO 27 I=1,512
	27 ICOLN[I]=0
	NREAL=0           
	NNULL=0                                                           
	NETOT=0 
	NEXCTOT=0
	NITOT=0
	NMXADD=0
	NTMPFLG=0
	# CALC ROTATION MATRIX ANGLES
	RCS=numpy.cos((BTHETA-90.00)*API/180.00)
	RSN=numpy.sin((BTHETA-90.00)*API/180.00)
	# 
	RTHETA=BTHETA*API/180.00
	EFZ100=EFIELD*100.00*numpy.sin(RTHETA)
	EFX100=EFIELD*100.00*numpy.cos(RTHETA)
	F1=EFIELD*CONST2*numpy.cos(RTHETA)
	F4=2.00*API
	EOVBR=EOVB*numpy.sin(RTHETA)
	THETA1=THETA
	PHI1=PHI
	# CALCULATE MAXIMUM COLLISION FREQUENCY
	TLIM=0.0
	DO 111 J=1,20000
	TEMP[J]=TCFN[J]+TCF[J] 
	if(TLIM < TEMP[J]:
	) TLIM=TEMP[J] 
	111 CONTINUE
	NEOVFL=0
	J1=0
	# START OF PRIMARY EVENT LOOP
	DO 210 J11=1,NDELTA
	J1=J1+1
	NPRIME=J1
	NGEXC1=0
	NGEXC2=0
	NGEXC3=0
	NGEXC4=0
	NGEXC5=0
	NGEXC6=0
	#     INITIAL DIRECTION COSINES 
	if(THETA1 == (API/2.0):
	or NDVEC != 1) :
	#  ONLY ALLOW CASE WHERE DELTA IS ALONG E-FIELD DIRECTION
	WRITE(6,22) 
	22  print(2(/),3X,'def STOPPED: ONLY ALLOWED TO HAVE DELTA ELECTRON PRALLEL TO E-FIELD IN CASE WITH ARBITRARY ANGLE FOR B-FIELD')  
	sys.exit()
	# endif
	# FIX DELTA TO E - FIELD DIRECTION
	PHI1=0.00
	THETA1=(API/2.0)-RTHETA
	DCZ1=numpy.cos(THETA1)                                                 
	DCX1=numpy.sin(THETA1)*numpy.cos(PHI1)                                      
	DCY1=numpy.sin(THETA1)*numpy.sin(PHI1) 
	NFLGFF=0
	NFLGPPP=0
	NFLGBRMM=0
	NFLGHIGH=0
	EST1=ESTART
	# INITIAL VELOCITY
	E1=ESTART
	GAM1=(EMS+E1)/EMS
	GAM12=GAM1
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.0D-12
	#     VTOT=CONST9*math.sqrt(E1)
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT 
	X=0.00
	Y=0.00
	Z=0.00
	K1=0
	KEXC=0
	NSTEXC=0
	NEXCNUL=0
	NCLUS=0
	NELEC=0
	NEGION=0
	TLAST=0.00
	ST=0.00
	TDASH=0.00  
	if(IMIP == 2):
	GO TO 1
	if(IMIP > 2):
	:
	# READIN FIRST ELECTRON FROM BETA DECAY OR X-RAY UNTHERMALISED CLUSTERS
	CALL CASRES(J11,IBADTOT,IBAD1)
	#  SKIP BAD EVENT
	if(IBAD1 == 1):
	:
	J1=J1-1
	GO TO 210
	# endif
	else if(IMIP == 1) :
	# READ IN FIRST ELECTRON FROM MIP INTERACTION
	CALL CASREM(J11)
	EST1=ECAS[1]
	EST2=EST1
	# endif
	X=XCAS[1]
	Y=YCAS[1]
	Z=ZCAS[1]
	ST=TT1[1]
	TS[1]=TT1[1]
	E1=ECAS[1]
	DCZ1=DRZS[1]
	DCY1=DRYS[1]
	DCX1=DRXS[1]
	NFLGFF=NFLGF[1]
	NFLGPPP=NFLGPP[1]
	NFLGBRMM=0
	NFLGHIGH=NFLGFF
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.0D-12
	#     VTOT=CONST9*math.sqrt(E1)
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# PUT REMAINDER OF ELECTRONS INTO CLUSTER STORE
	ISDUM=0
	DO 35 IST=2,IEVNTL
	ISDUM=ISDUM+1
	XS[ISDUM]=XCAS[IST]
	YS[ISDUM]=YCAS[IST]
	ZS[ISDUM]=ZCAS[IST]
	TS[ISDUM]=TT1[IST]
	ES[ISDUM]=ECAS[IST]
	DCX[ISDUM]=DRXS[IST]
	DCY[ISDUM]=DRYS[IST]
	DCZ[ISDUM]=DRZS[IST]
	NFLGFC[ISDUM]=NFLGF[IST]
	NFLGPPC[ISDUM]=NFLGPP[IST]
	NFLGBRMC[ISDUM]=0
	NCLUS=ISDUM
	if(NFLGFC[IST]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[IST]
	35 CONTINUE
	GAM12=GAM1
	# START OF LOOP FOR NEW ELECTRONS                                       
	1 CONTINUE 
	R1=DRAND48(RDUM)
	T=-math.log(R1)/TLIM+TDASH
	TDASH=T
	WBT=WB*T/GAM12
	#     WBT=WB*T
	COSWT=numpy.cos(WBT)
	SINWT=numpy.sin(WBT)
	DZ=GAM12*(CZ1*SINWT+(EOVBR-CY1)*(1.00-COSWT))/WB
	#     DZ=(CZ1*SINWT+(EOVBR-CY1)*(1.00-COSWT))/WB
	DX=CX1*T+F1*T*T/GAM12
	#     DX=CX1*T+F1*T*T
	E=E1+DZ*EFZ100+DX*EFX100
	GAM2=(EMS+E)/EMS
	BET2=math.sqrt(1.00-1.00/(GAM2+GAM2))
	if(E < 0.00):
	:
	E=0.0010
	# endif                                                   
	# INSERT NEW ALGORITHM TO FIND IE FOR VARYING ENERGY STEP          
	if(IMIP == 1):
	:                                     
	IE=int(E/ESTEP)+1                                               
	else:
	if(EFINAL <= 20000.):
	:
	IE=int(E/ESTEP)+1
	else if(EFINAL <= 140000.) :
	if(E <= 16000.):
	:
	 IE=int(E)+1
	else:
	 IE=16000+int((E-16000.)/ESTEP1)
	# endif
	else:
	if(E <= 12000.):
	:
	 IE=int(E)+1
	else if(E <= 92000.) :
	 IE=12000+int((E-12000.)/ESTEP1)
	else:
	 IE=16000+int((E-92000.)/ESTEP2)
	# endif
	# endif
	# endif 
	IE=DMIN0(IE,J20000)                                            
	#                                                                       
	#     TEST FOR #real OR NULL COLLISION                                   
	#                                                                       
	R5=DRAND48(RDUM)
	TEST1=TCF[IE]/TLIM                                                
	if(R5 <= TEST1):
	GO TO 137                                         
	NNULL=NNULL+1       
	TEST2=TEMP[IE]/TLIM                      
	if(R5 < TEST2):
	:
	# TEST FOR NULL LEVELS
	if(NPLAST == 0):
	GO TO 1
	R2=DRAND48(RDUM) 
	I=0
	888  I=I+1
	if(CFN[IE][I]:
	< R2) GOTO 888
	# INCREMENT NULL LEVEL SUM
	NEXCNUL=NEXCNUL+1
	ICOLNN[I]=ICOLNN[I]+1
	# STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION AND DISSOCIATION FROM 
	#   NULL EXCITATION
	# NOTE: SMALL APPROX USED POSITION OF PREVIOUS #real COLLISION
	XSTN[NEXCNUL]=X
	YSTN[NEXCNUL]=Y
	ZSTN[NEXCNUL]=Z
	TSTN[NEXCNUL]=ST
	IDNUL[NEXCNUL]=I               
	GO TO 1         
	else:
	# NULL
	GO TO 1
	# endif                                                 
	#                                                                       
	#  CALCULATE DIRECTION COSINES AND POSITIONS AT INSTANT BEFORE COLLISION
	137 T2=T*T
	if(E > EMAX):
	EMAX=E
	if(T > TMAX1):
	TMAX1=T
	TDASH=0.00
	NREAL=NREAL+1  
	# CALC VELOCITY
	#     CX2=CX1+2.0*F1*T        
	CX2=CX1+2.0*F1*T/GAM12
	CY2=(CY1-EOVBR)*COSWT+CZ1*SINWT+EOVBR
	CZ2=CZ1*COSWT-(CY1-EOVBR)*SINWT
	# CALC DIRECTION COSINES
	VTOT=math.sqrt(CX2*CX2+CY2*CY2+CZ2*CZ2)
	DCX2=CX2/VTOT
	DCY2=CY2/VTOT
	DCZ2=CZ2/VTOT                                                     
	# CALC NEW POSITION                                                
	X=X+DX                                                            
	Y=Y+EOVBR*T+GAM12*((CY1-EOVBR)*SINWT+CZ1*(1.00-COSWT))/WB
	#     Y=Y+EOVBR*T+((CY1-EOVBR)*SINWT+CZ1*(1.00-COSWT))/WB
	Z=Z+DZ          
	GAM12=(GAM1+GAM2)/2.00
	ST=ST+T
	IT=int(T+1.00)                                                  
	IT=DMIN0[IT][J300]                                               
	TIME[IT]=TIME[IT]+1.00                                           
	# --------------------------------------------------------------------- 
	#     DETERMINATION OF #real COLLISION TYPE                              
	# --------------------------------------------------------------------- 
	R2=DRAND48(RDUM)
	I=0                                                               
	140 I=I+1                                                             
	if(CF[IE][I]:
	< R2) GO TO 140     
	#************************************************************
	# CHECK IF BREMSSTRAHLUNG
	if(IZBR[I]:
	!= 0 and LBRM == 1) :
	NFLGBRMM=1
	IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1
	ICOLN[I]=ICOLN[I]+1
	DO 141 KNGS=1,NGAS
	if(IPT == (KNGS*5):
	-1) GO TO 142
	141  CONTINUE
	142  IATOMNO=IZBR[I] 
	CALL BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
	NBREM[KNGS]=NBREM[KNGS]+1
	EBRTOT[KNGS]=EBRTOT[KNGS]+EGAMMA
	#      WRITE(6,668) EGAMMA,J11   
	# 668 print(' BREM EGAMMA=','%.4f' % ,' EVENT NO=',I5)
	# GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
	E1=EOUT
	DCX1=EDCX
	DCY1=EDCY
	DCZ1=EDCZ
	# RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE : STORE CONVERTED
	# ELECTRONS IN COMMON/CASRSB/
	# 
	CALL BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
	# BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
	if(ILOW == 1):
	GO TO 190
	# 
	# STORE BREMSSTRAHLUNG DATA IN CLUSTER STORE
	DO 890 KBR=1,IEVNTLB
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif     
	ES[NCLUS]=ECASB[KBR]
	XS[NCLUS]=XCASB[KBR]
	YS[NCLUS]=YCASB[KBR]
	ZS[NCLUS]=ZCASB[KBR]
	TS[NCLUS]=TTB1[KBR]
	DCX[NCLUS]=DRXB[KBR]
	DCY[NCLUS]=DRYB[KBR]
	DCZ[NCLUS]=DRZB[KBR]
	NFLGFC[NCLUS]=NFLGFB[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPB[KBR]
	NFLGBRMC[NCLUS]=2
	890  CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 190
	# endif
	891 CONTINUE
	#****************************************************************
	#     S1=RGAS[I]                                                        
	S1=1.00+GAM2*(RGAS[I]-1.00)                                     
	EI=EIN[I]
	if(E < EI):
	:
	EI=E-0.00010
	# endif                                                          
	if(IPN[I]:
	== 0) GO TO 666
	# ATTACHMENT       
	if(IPN[I]== -1) :
    	NETOT=NETOT+1
    	NITOT=NITOT+1
    	NELEC=NELEC+1
    	NEGION=NEGION+1
    	IPT=IARRY[I]
    	ICOLL[IPT]=ICOLL[IPT]+1
    	ICOLN[I]=ICOLN[I]+1 
    	IT=int(T+1.00)
    	IT=DMIN0[IT][J300]
    	TIME[IT]=TIME[IT]+1.00
    	GO TO 335
	# endif    
	EISTR=EI                                   
	if(IONMODEL[I]> 0):
    	# CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
    	# FIVE DIFFERENT MODELS
    	CALL IONSPLIT(I,E,EI,ESEC) 
    	GO TO 544
	# endif               
	R9=DRAND48(RDUM)
	#    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
	ESEC=WPL[I]*TAN(R9*ATAN((E-EI)/(2.00*WPL[I]))) 
	ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
	544 CONTINUE
	EI=ESEC+EI 
	# STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
	# OF SECONDARY IONISATION ELECTRON 
	NCLUS=NCLUS+1
	NMXADD=MAX[NCLUS][NMXADD]
	if(NCLUS > 150000):
	: 
	WRITE(6,546) NCLUS,NREAL 
	546   print(2X,' def STOPPED: . NCLUS=',I7,' NREAL=',I10)
	sys.exit()
	# endif     
	XS[NCLUS]=X       
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	ES[NCLUS]=ESEC 
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM         
	NTMPFLG=1
	NCLTMP=NCLUS
	# RANDOMISE SECONDARY ELECTRON DIRECTION
	#     R3=drand48(RDUM)
	#     F3=1.0-2.00*R3
	#     THETA0=DACOS(F3)
	#     F6=DCOS(THETA0)
	#     F5=DSIN(THETA0)
	#     R4=drand48(RDUM)
	#     PHI0=F4*R4
	#     F8=DSIN(PHI0)
	#     F9=DCOS(PHI0)               
	#     DCX[NCLUS]=F9*F5
	#     DCY[NCLUS]=F8*F5
	#     DCZ[NCLUS]=F6    
	#*********************************************************
	if(IECASC == 0):
	GO TO 333
	if(LEGAS[I]:
	== 0) GO TO 333
	# USE COMPLETE CASCADE FOR ELECTRON IONISATION
	KG1=NEGAS[I]
	LG1=LEGAS[I]
	IGSHEL=IESHELL[I]
	CALL CASCADEE(J11,KG1,LG1,X,Y,Z,ST,ESEC,IGSHEL)
	#
	# STORE CASCADE IN CLUSTER STORE
	#
	ETSUM=0.0
	DO 844 KBR=1,IEVENTE
	NCLUS=NCLUS+1
	if(NCLUS > 150000):
	:
	WRITE(6,546) NCLUS,NREAL
	sys.exit()
	# endif
	ES[NCLUS]=ECASE[KBR]
	ETSUM=ETSUM+ES[NCLUS]
	XS[NCLUS]=XCASE[KBR]
	YS[NCLUS]=YCASE[KBR]
	ZS[NCLUS]=ZCASE[KBR]
	TS[NCLUS]=TCASE[KBR]
	DCX[NCLUS]=DRXCE[KBR]
	DCY[NCLUS]=DRYCE[KBR]
	DCZ[NCLUS]=DRZCE[KBR]
	NFLGFC[NCLUS]=NFLGFE[KBR]+NFLGHIGH
	NFLGPPC[NCLUS]=NFLGPPE[KBR]
	NFLGBRMC[NCLUS]=NFLGBRMM
	844 CONTINUE
	if(NFLGFC[NCLUS]:
	> NFLGHIGH) NFLGHIGH=NFLGFC[NCLUS]
	GO TO 666
	#*********************************************************
	# STORE POSSIBLE SHELL EMISSIONS AUGER OR FLUORESCENCE 
	333 if(EISTR > 30.0) :
	# TEST IF FLUORESCENCE EMISSION
	IFLTST=0:
	if(WKLM[I]:
	> 0.0) :
	R9=DRAND48(RDUM)
	if(R9 < WKLM[I]:
	) IFLTST=1
	# endif
	if(IFLTST == 0):
	:
	# AUGER EMISSION WITHOUT FLUORESCENCE
	NAUG=NC0[I]
	EAVAUG=EC0[I]/float(NAUG)
	DO 700 JFL=1,NC0[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	TS[NCLUS]=ST
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	700   CONTINUE 
	else:
	# AUGER EMISSION AND FLUORESENCE 
	if(NG2[I]:
	== 0) GO TO 702
	NAUG=NG2[I]
	EAVAUG=EG2[I]/float(NAUG)
	DO 701 JFL=1,NG2[I]
	NCLUS=NCLUS+1
	XS[NCLUS]=X
	YS[NCLUS]=Y
	ZS[NCLUS]=Z
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	701   CONTINUE
	702   if(NG1[I] == 0) GO TO 704
	NAUG=NG1[I]
	EAVAUG=EG1[I]/float(NAUG)
	R9=DRAND48(RDUM)
	DFL=-math.log(R9)*DSTFL[I]
	DO 703 JFL=1,NG1[I]
	NCLUS=NCLUS+1
	R3=DRAND48(RDUM)
	THEFL=numpy.arccos(1.0-2.00*R3)
	R4=DRAND48(RDUM)
	PHIFL=F4*R4
	XS[NCLUS]=X+DFL*numpy.sin(THEFL)*numpy.cos(PHIFL)
	YS[NCLUS]=Y+DFL*numpy.sin(THEFL)*numpy.sin(PHIFL)
	ZS[NCLUS]=Z+DFL*numpy.cos(THEFL)
	NFLGFC[NCLUS]=NFLGHIGH+1
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	TS[NCLUS]=ST
	ES[NCLUS]=EAVAUG
	R3=DRAND48(RDUM)
	F3=1.0-2.00*R3
	THETA0=numpy.arccos(F3)
	F6=numpy.cos(THETA0)
	F5=numpy.sin(THETA0)
	R4=DRAND48(RDUM)
	PHI0=F4*R4
	F8=numpy.sin(PHI0)
	F9=numpy.cos(PHI0)               
	DCX[NCLUS]=F9*F5
	DCY[NCLUS]=F8*F5
	DCZ[NCLUS]=F6
	NFLGHIGH=NFLGFC[NCLUS]
	703   CONTINUE
	704   CONTINUE
	# endif
	# endif
	#
	#  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
	#   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
	#
	666 IPT=IARRY[I]
	ICOLL[IPT]=ICOLL[IPT]+1 
	ICOLN[I]=ICOLN[I]+1   
	# IF EXCITATION : ADD PROBABILITY ,PENFRA(1,I), OF TRANSFER TO GIVE 
	# IONISATION OF THE OTHER GASES IN MIXTURE            
	if(IPEN == 0 or NGAS == 1):
	GO TO 5                
	if(PENFRA[1][I] != 0.0):
	:
	RAN=DRAND48(RDUM)
	if(RAN > PENFRA[1][I]):
	GO TO 5
	NCLUS=NCLUS+1
	# ENTER HERE POSSIBLE DELOCALISATION LENGTH FOR PENNING TRANSFER
	if(PENFRA[2][I] == 0.0):
	:
	XS[NCLUS]=X             
	YS[NCLUS]=Y    
	ZS[NCLUS]=Z
	NFLGFC[NCLUS]=NFLGFF
	NFLGPPC[NCLUS]=NFLGPPP
	NFLGBRMC[NCLUS]=NFLGBRMM
	GO TO 667
	# endif
	ASIGN=1.0
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN  
	XS[NCLUS]=X-math.log(RAN)*PENFRA[2][I]*ASIGN
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN 
	YS[NCLUS]=Y-math.log(RAN)*PENFRA[2][I]*ASIGN 
	RAN=DRAND48(RDUM)
	RAN1=DRAND48(RDUM)
	if(RAN1 < 0.5):
	ASIGN=-ASIGN  
	ZS[NCLUS]=Z-math.log(RAN)*PENFRA[2][I]*ASIGN
	667  RAN=DRAND48(RDUM)
	TS[NCLUS]=ST-math.log(RAN)*PENFRA[3][I]
	# ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
	ES[NCLUS]=1.0
	DCX[NCLUS]=DCX1
	DCY[NCLUS]=DCY1
	DCZ[NCLUS]=DCZ1
	GO TO 6
	# endif
	#     GO TO 6 
	# CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
	5  if(IPN[I] == 0) :
	if((RGAS[I]:
	*EIN[I]) > 4.0) :
	KEXC=KEXC+1
	if(KEXC > 150000):
	: 
	 WRITE(6,548) KEXC
	548     print(2X,' def STOPPED: . KEXC=',I7)
	 sys.exit()
	# endif
	# FIND GAS IN WHICH EXCITATION OCCURED AND INCREMENT COUNTER
	if(I <= IDG1):
	: 
	 NGEXC1=NGEXC1+1
	else if(I <= IDG2) :
	 NGEXC2=NGEXC2+1
	else if(I <= IDG3) :
	 NGEXC3=NGEXC3+1
	else if(I <= IDG4) :
	 NGEXC4=NGEXC4+1
	else if(I <= IDG5) :
	 NGEXC5=NGEXC5+1
	else if(I <= IDG6) :
	 NGEXC6=NGEXC6+1
	else:
	 WRITE(6,9911) 
	9911    print(' def STOPPED: BAD GAS ID IN MONTE')
	 sys.exit()
	# endif
	NEXCTOT=NEXCTOT+1
	NSTEXC=NSTEXC+1
	XSTEXC[KEXC]=X
	YSTEXC[KEXC]=Y
	ZSTEXC[KEXC]=Z
	TSTEXC[KEXC]=ST
	# endif
	# endif 
	6  S2=(S1*S1)/(S1-1.00) 
	#  ANISOTROPIC SCATTERING 
	R3=DRAND48(RDUM)
	if(INDEX[I]:
	== 1) :
	R31=DRAND48(RDUM)
	F3=1.00-R3*ANGCT[IE][I]       
	if(R31 > PSCT[IE][I]:
	) F3=-F3   
	else if(INDEX[I] == 2) :
	EPSI=PSCT[IE][I]
	F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3)))   
	else:
	# ISOTROPIC SCATTERING        
	F3=1.00-2.00*R3  
	# endif
	THETA0=numpy.arccos(F3)                                                  
	R4=DRAND48(RDUM)
	PHI0=F4*R4                                                        
	F8=numpy.sin(PHI0)                                                     
	F9=numpy.cos(PHI0)                                                     
	if(E < EI):
	EI=0.00                                              
	ARG1=1.00-S1*EI/E                                                
	ARG1=DMAX1[ARG1][SMALL]                                            
	D=1.00-F3*math.sqrt(ARG1)                                            
	E1=E*(1.00-EI/(S1*E)-2.00*D/S2) 
	E1=DMAX1[E1][SMALL]                                                
	Q=math.sqrt((E/E1)*ARG1)/S1                                           
	Q=DMIN1[Q][1.00]                                                  
	THETA=numpy.arcsin(Q*numpy.sin(THETA0))                                       
	F6=numpy.cos(THETA)                                                    
	U=(S1-1.00)*(S1-1.00)/ARG1                                      
	CSQD=F3*F3                                                        
	if(F3 < 0.00 and CSQD > U):
		F6=-1.00*F6                        
	F5=numpy.sin(THETA)                                                    
	DCZ2=DMIN1[DCZ2][1.00]                                            
	ARGZ=math.sqrt(DCX2*DCX2+DCY2*DCY2)
	if(ARGZ == 0.00):
		DCZ1=F6         
		DCX1=F9*F5                             
		DCY1=F8*F5 
		if(NTMPFLG == 1):
			# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
			F5S=F5*math.sqrt(E1/ES[NCLTMP])
			if(F5S > 1.0):
			F5S=1.0
			THSEC=numpy.arcsin(F5S)
			F5S=numpy.sin(THSEC)
			F6S=numpy.cos(THSEC)
			if(F6 < 0.0):
			F6S=-F6S
			PHIS=PHI0+API   
			if(PHIS > F4):
			PHIS=PHI0-F4
			F8S=numpy.sin(PHIS)
			F9S=numpy.cos(PHIS)
			DCZ[NCLTMP]=F6S
			DCX[NCLTMP]=F9S*F5S
			DCY[NCLTMP]=F8S*F5S
			NTMPFLG=0
		# endif
		pass
		# endif                                            
	else:
		DCZ1=DCZ2*F6+ARGZ*F5*F8                                           
		DCY1=DCY2*F6+(F5/ARGZ)*(DCX2*F9-DCY2*DCZ2*F8)                     
		DCX1=DCX2*F6-(F5/ARGZ)*(DCY2*F9+DCX2*DCZ2*F8) 
		if(NTMPFLG == 1):
			# USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
			F5S=F5*math.sqrt(E1/ES[NCLTMP])
			if(F5S > 1.0):
				F5S=1.0            
			THSEC=numpy.arcsin(F5S)
			F5S=numpy.sin(THSEC)
			F6S=numpy.cos(THSEC)
			if(F6 < 0.0):
				F6S=-F6S
			PHIS=PHI0+API   
			if(PHIS > F4):
				PHIS=PHI0-F4
			F8S=numpy.sin(PHIS)
			F9S=numpy.cos(PHIS)
			DCZ[NCLTMP]=DCZ2*F6S+ARGZ*F5S*F8S                               
			DCY[NCLTMP]=DCY2*F6S+(F5S/ARGZ)*(DCX2*F9S-DCY2*DCZ2*F8S)        
			DCX[NCLTMP]=DCX2*F6S-(F5S/ARGZ)*(DCY2*F9S+DCX2*DCZ2*F8S)
			NTMPFLG=0
		# endif 
	#190 CONTINUE  
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.E-12
	#     VTOT=CONST9*math.sqrt(E1)
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	# TEST IF ELECTRON IS THERMALISED
	if(E1 > ETHRM):
		GO TO 1
	191 CONTINUE
	# STORE POSITION AND TIME OF THERMALISED ELECTRONS
	K1=K1+1
	# ROTATE INTO COORDINATE SYSTEM WITH EFIELD ALONG Z
	ZR=Z*RCS-X*RSN
	YR=Y
	XR=Z*RSN+X*RCS          
	XST[K1]=XR
	YST[K1]=YR
	ZST[K1]=ZR
	TST[K1]=ST
	NFGF[K1]=NFLGFF
	NFGPP[K1]=NFLGPPP
	NFGBR[K1]=NFLGBRMM
	TTIME[K1]=ST-TLAST
	NELEC=NELEC+1
	NETOT=NETOT+1
	335 
	if(K1 == 150000):
		GO TO 889
	if(NELEC == (NCLUS+1)):
		# LAST ELECTRON IN CLUSTER. DO STATISTICS ON CLUSTER
		STATS(J11,J1) 
		GO TO 210      
	# endif
	# GET NEW IONISATION ELECTRON FROM STORE
	X=XS[NELEC]
	Y=YS[NELEC]
	Z=ZS[NELEC]
	ST=TS[NELEC]
	NFLGFF=NFLGFC[NELEC]
	NFLGPPP=NFLGPPC[NELEC]
	NFLGBRMM=NFLGBRMC[NELEC]
	TLAST=TS[NELEC]
	E1=ES[NELEC]
	DCX1=DCX[NELEC]
	DCY1=DCY[NELEC]
	DCZ1=DCZ[NELEC]
	if(E1 < ETHRM):
		GO TO 191
	GAM1=(EMS+E1)/EMS
	BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
	VTOT=BET1*VC*1.E-12
	CX1=DCX1*VTOT
	CY1=DCY1*VTOT
	CZ1=DCZ1*VTOT
	GO TO 1  
	# MAIN LOOP # end
	210 CONTINUE
	# RESET NUMBER OF EVENTS FOR BAD EVENTS
	if(IMIP > 2):
		NDELTA=NDELTA-IBADTOT
		print(' EMAX=','%.7f' % EMAX,' NEOVFL =',NEOVFL)
	if(EMAX > EFINAL):
		print('INCREASE ENERGY LIMIT FROM','%.6f' % EFINAL,' EV TO AT LEAST','%.6f' % EMAX,' EV.')
		sys.exit()
	# endif                                         
	return
	889 NLEFT=NCLUS-NELEC
	print('\n\n\n WARNING STOPPED: AFTER NPRIME=',NPRIME,' LAST PRIMARY HAS AT LEAST ',NLEFT,' SECONDARIES LEFT TO TRACK. OUT OF ',NCLUS,' ELECTRONS ALREADY IN CLUSTER')
	sys.exit()
	return
	# end                                                  