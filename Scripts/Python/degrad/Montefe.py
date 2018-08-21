import conf
import numpy
import math 
import sys
def MONTEFE():                                                
      # IMPLICIT #real*8 (A-H,O-Z)
      # IMPLICIT #integer*8 (I-N)                                         
      # global /INPT/
      global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
      # global /INPT1/
      global NDVEC
      # global /CNSTS1/
      global CONST1,CONST2,CONST3,CONST4,CONST5                  
      # global /SETP/
      global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX#(10)
      global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                    
      # global /LARGE/
      global CF#(20000,512)
      global EIN#(512)
      global TCF#(20000)
      global IARRY#(512),
      global RGAS#(512)
      global IPN#(512)
      global WPL#(512)
      global IZBR#(512)
      global IPLAST,PENFRA#[3,512]
      # global /LARGEN/
      global CFN#(20000,60),
      global TCFN#(20000)
      global SCLENUL#(60)
      global NPLAST
      # global /OUTPT/
      global ICOLL#(30)
      global NETOT,NPRIME,TMAX1,TIME#(300)
      global NNULL,NITOT,ICOLN#(512)
      global ICOLNN#(60)
      global NREAL,NEXCTOT 
      # global /RLTVY/
      global BET#(20000)
      global GAM#(20000)
      global VC,EMS
      # global /STTS/
      global XST#(150000)
      global YST#(150000)
      global ZST#(150000)
      global TST#(150000),
      global TTIME#(150000)
      global NFGF#(150000)
      global NFGPP#(150000)
      global NFGBR#(150000)
      global NELEC,NEGION,EST1,EST2
      # global /STEXC/
      global XSTEXC#(150000)
      global YSTEXC#(150000)
      global ZSTEXC#(150000),
      global TSTEXC#(150000)
      global NSTEXC
      # global /STEXCNUL/
      global XSTN#(150000)
      global YSTN#(150000)
      global ZSTN#(150000),
      global TSTN#(150000)
      global IDNUL#(150000)
      global NEXCNUL
      # global /IONC/
      global DOUBLE#(6,20000)
      global CMINIXSC#[6]
      global CMINEXSC#[6]
      global ECLOSS#[6],
      global WPLN#[6]
      global ICOUNT,AVPFRAC#(3,6) 
      # global /IONFL/
      global NC0#(512)
      global EC0#(512)
      global NG1#(512)
      global EG1#(512)
      global NG2#(512),
      global EG2#(512)
      global WKLM#(512)
      global DSTFL#(512)
      # global /IONMOD/
      global ESPLIT#(512,20)
      global IONMODEL#(512)
      # global /ANIS/
      global PSCT#(20000,512)
      global ANGCT#(20000,512)
      global INDEX#(512)
      global NISO
      # global /CASRS/
      global ECAS#(400)
      global XCAS#(400)
      global YCAS#(400)
      global ZCAS#(400)
      global DRXS#(400),
      global DRYS#(400)
      global DRZS#(400)
      global TT1#(400)
      global NFLGF#(400)
      global NFLGPP#(400)
      global IEVNTL
      # global /COMP/
      global LCMPLCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
      # global /BREMG/
      global EBRGAM#(10)
      global BRDCOSX#(10)
      global BRDCOSY#(10)
      global BRDCOSZ#[10],
      global BRX#(10)
      global BRY#(10)
      global BRZ#[10]
      global BRT#(10)
      global EBRTOT#[6]
      global NBREM#[6]
      # global /CASRSB/
      global ECASB#[400]
      global XCASB#[400]
      global YCASB#[400]
      global ZCASB#[400],
      global DRXB#[400]
      global DRYB#[400]
      global DRZB#[400]
      global TTB1#(400)
      global NFLGFB#[400]
      global NFLGPPB#[400],
      global IEVNTLB
      # global /CASRSE/
      global ECASE#(400)
      global XCASE#(400)
      global YCASE#(400)
      global ZCASE#(400),
      global DRXCE#(400)
      global DRYCE#(400)
      global DRZCE#(400)
      global TCASE#(400),
      global NFLGFE#(400)
      global NFLGPPE#(400)
      global IEVENTE
      # global /ECASC/
      global NEGAS#(512)
      global LEGAS#(512)
      global IESHELL#(512)
      global IECASC
      # global /IDEXC/
      global NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
      NGAS=conf.NGAS
      NSTEP=conf.NSTEP
      NANISO=conf.NANISO
      EFINAL=conf.EFINAL
      ESTEP=conf.ESTEP
      AKT=conf.AKT
      ARY=conf.ARY
      TEMPC=conf.TEMPC
      TORR=conf.TORR
      IPEN=conf.IPEN
      NDVEC=conf.NDVEC
      CONST1=conf.CONST1
      CONST2=conf.CONST2
      CONST3=conf.CONST3
      CONST4=conf.CONST4
      CONST5=conf.CONST5                  
      TMAX=conf.TMAX
      SMALL=conf.SMALL
      API=conf.API
      ESTART=conf.ESTART
      THETA=conf.THETA
      PHI=conf.PHI
      TCFMAX=conf.TCFMAX
      TCFMAX1=conf.TCFMAX1
      RSTART=conf.RSTART
      EFIELD=conf.EFIELD
      ETHRM=conf.ETHRM
      ECUT=conf.ECUT
      NDELTA=conf.NEVENT
      IMIP=conf.IMIP
      IWRITE=conf.IWRITE                    
      CF=conf.CF
      EIN=conf.EIN
      TCF=conf.TCF
      IARRY=conf.IARRY
      RGAS=conf.RGAS
      IPN=conf.IPN
      WPL=conf.WPL
      IZBR=conf.IZBR
      IPLAST=conf.IPLAST
      PENFRA=conf.PENFRA
      CFN=conf.CFN
      TCFN=conf.TCFN
      SCLENUL=conf.SCLENUL
      NPLAST=conf.NPLAST
      ICOLL=conf.ICOLL
      NETOT=conf.NETOT
      NPRIME=conf.NPRIME
      TMAX1=conf.TMAX1
      TIME=conf.TIME
      NNULL=conf.NNULL
      NITOT=conf.NITOT
      ICOLN=conf.ICOLN
      ICOLNN=conf.ICOLNN
      NREAL=conf.NREAL
      NEXCTOT =conf.NEXCTOT 
      BET=conf.BET
      GAM=conf.GAM
      VC=conf.VC
      EMS=conf.EMS
      XST=conf.XST
      YST=conf.YST
      ZST=conf.ZST
      TST=conf.TST
      TTIME=conf.TTIME
      NFGF=conf.NFGF
      NFGPP=conf.NFGPP
      NFGBR=conf.NFGBR
      NELEC=conf.NELEC
      NEGION=conf.NEGION
      EST1=conf.EST1
      EST2=conf.EST2
      XSTEXC=conf.XSTEXC
      YSTEXC=conf.YSTEXC
      ZSTEXC=conf.ZSTEXC
      TSTEXC=conf.TSTEXC
      NSTEXC=conf.NSTEXC
      XSTN=conf.XSTN
      YSTN=conf.YSTN
      ZSTN=conf.ZSTN
      TSTN=conf.TSTN
      IDNUL=conf.IDNUL
      NEXCNUL=conf.NEXCNUL
      DOUBLE=conf.DOUBLE
      CMINIXSC=conf.CMINIXSC
      CMINEXSC=conf.CMINEXSC
      ECLOSS=conf.ECLOSS
      WPLN=conf.WPLN
      ICOUNT=conf.ICOUNT
      AVPFRAC=conf.AVPFRAC
      NC0=conf.NC0
      EC0=conf.EC0
      NG1=conf.NG1
      EG1=conf.EG1
      NG2=conf.NG2
      EG2=conf.EG2
      WKLM=conf.WKLM
      DSTFL=conf.DSTFL
      ESPLIT=conf.ESPLIT
      IONMODEL=conf.IONMODEL
      PSCT=conf.PSCT
      ANGCT=conf.ANGCT
      INDEX=conf.INDEX
      NISO=conf.NISO
      ECAS=conf.ECAS
      XCAS=conf.XCAS
      YCAS=conf.YCAS
      ZCAS=conf.ZCAS
      DRXS=conf.DRXS
      DRYS=conf.DRYS
      DRZS=conf.DRZS
      TT1=conf.TT1
      NFLGF=conf.NFLGF
      NFLGPP=conf.NFLGPP
      IEVNTL=conf.IEVNTL
      LCMPLCFLG=conf.LCMPLCFLG
      LRAY=conf.LRAY
      LRFLG=conf.LRFLG
      LPAP=conf.LPAP
      LPFLG=conf.LPFLG
      LBRM=conf.LBRM
      LBFLG=conf.LBFLG
      LPEFLG=conf.LPEFLG
      EBRGAM=conf.EBRGAM
      BRDCOSX=conf.BRDCOSX
      BRDCOSY=conf.BRDCOSY
      BRDCOSZ=conf.BRDCOSZ
      BRX=conf.BRX
      BRY=conf.BRY
      BRZ=conf.BRZ
      BRT=conf.BRT
      EBRTOT=conf.EBRTOT
      NBREM=conf.NBREM
      ECASB=conf.ECASB
      XCASB=conf.XCASB
      YCASB=conf.YCASB
      ZCASB=conf.ZCASB
      DRXB=conf.DRXB
      DRYB=conf.DRYB
      DRZB=conf.DRZB
      TTB1=conf.TTB1
      NFLGFB=conf.NFLGFB
      NFLGPPB=conf.NFLGPPB
      IEVNTLB=conf.IEVNTLB
      ECASE=conf.ECASE
      XCASE=conf.XCASE
      YCASE=conf.YCASE
      ZCASE=conf.ZCASE
      DRXCE=conf.DRXCE
      DRYCE=conf.DRYCE
      DRZCE=conf.DRZCE
      TCASE=conf.TCASE
      NFLGFE=conf.NFLGFE
      NFLGPPE=conf.NFLGPPE
      IEVENTE=conf.IEVENTE
      NEGAS=conf.NEGAS
      LEGAS=conf.LEGAS
      IESHELL=conf.IESHELL
      IECASC=conf.IECASC
      NGEXC1=conf.NGEXC1
      NGEXC2=conf.NGEXC2
      NGEXC3=conf.NGEXC3
      NGEXC4=conf.NGEXC4
      NGEXC5=conf.NGEXC5
      NGEXC6=conf.NGEXC6
      IDG1=conf.IDG1
      IDG2=conf.IDG2
      IDG3=conf.IDG3
      IDG4=conf.IDG4
      IDG5=conf.IDG5
      IDG6=conf.IDG6
      # DIMENSION 
      XS=numpy.zeros((150000+1))
      YS=numpy.zeros((150000+1))
      ZS=numpy.zeros((150000+1))
      TS=numpy.zeros((150000+1))
      ES=numpy.zeros((150000+1))
      DCX=numpy.zeros((150000+1))
      DCY=numpy.zeros((150000+1))
      DCZ=numpy.zeros((150000+1))
      NFLGFC=numpy.zeros((150000+1))
      NFLGPPC=numpy.zeros((150000+1))
      NFLGBRMC=numpy.zeros((150000+1))
      # DIMENSION 
      TEMP=numpy.zeros((20000+1))
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
      for I in range(1,300+1):
            TIME[I]=0.00
      for I in range(1,30+1):
            ICOLL[I]=0
      for I in range(1,512+1):
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
      for J in range(1,20000+1):
            TEMP[J]=TCFN[J]+TCF[J] 
            if(TLIM < TEMP[J]):
                  TLIM=TEMP[J] 
            # 111 CONTINUE
      NEOVFL=0
      J1=0
      # START OF PRIMARY EVENT LOOP 
      print("NDELTA= ",NDELTA,conf.NEVENT)
      for J11 in range(1,int(NDELTA)+1):
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
                              flag1=0
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
                  for IST in range(2,IEVNTL+1):
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
                        # 35 CONTINUE

                  # START OF LOOP FOR NEWLY CREATED ELECTRONS
            # 1 CONTINUE
            flag1=1
            flag210=0
            while(flag1):  
                  flag1=0                                                       
                  R1=random.uniform(RDUM)
                  T=-math.log(R1)/TLIM+TDASH
                  TDASH=T
                  #     AP=DCZ1*F2*DSQRT(E1)
                  GAM1=(EMS+E1)/EMS
                  BET1=math.sqrt(1.00-1.00/(GAM1*GAM1))
                  AP=DCZ1*EFIELD*BET1*VC*1.0e-10
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
                  IE=min(IE,J20000)                                            
                  #                                                                       
                  #     TEST FOR REAL OR NULL COLLISION                                   
                  #                                                                       
                  R5=random.uniform(RDUM)
                  TEST1=TCF[IE]/TLIM                                               
                  if(R5 <= TEST1):
                        pass
                  else:
                        NNULL=NNULL+1                          
                        TEST2=TEMP[IE]/TLIM
                        if(R5 < TEST2):
                              # TEST FOR NULL LEVELS
                              if(NPLAST == 0):
                                    flag1=1
                                    continue
                              R2=random.uniform(RDUM) 
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
                              # NOTE:  SMALL APPROX USED POSITION OF PREVIOUS REAL COLLISION
                              XSTN[NEXCNUL]=X
                              YSTN[NEXCNUL]=Y
                              ZSTN[NEXCNUL]=Z
                              TSTN[NEXCNUL]=ST
                              IDNUL[NEXCNUL]=I      
                              flag1=1
                              continue
                        else:
                              # NULL 
                              flag1=1
                              continue
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
                  #     CONST6=DSQRT(E1/E)
                  GAM2=(EMS+E)/EMS
                  GAM12=(GAM1+GAM2)/2.00
                  BET2=math.sqrt(1.00-1.00/(GAM2*GAM2))   
                  CONST6=BET1/BET2                                             
                  DCX2=DCX1*CONST6                                                  
                  DCY2=DCY1*CONST6                                                  
                  #     DCZ2=DCZ1*CONST6+EFIELD*T*CONST5/DSQRT(E) 
                  DCZ2=DCZ1*CONST6+EFIELD*T*2.0e10*CONST1/(VC*BET2)
                  #     CONST7=CONST9*DSQRT(E1)  
                  CONST7=VC*BET1*1.0e-12                          
                  A=T*CONST7                                                        
                  X=X+DCX1*A                                                        
                  Y=Y+DCY1*A
                  Z=Z+DCZ1*A+T2*F1/GAM12
                  #     Z=Z+DCZ1*A+T2*F1     
                  ST=ST+T
                  IT=int(T+1.00)                                                  
                  IT=min(IT,J300)                                               
                  TIME[IT]=TIME[IT]+1.00                                           
                  # --------------------------------------------------------------------- 
                  #     DETERMINATION OF REAL COLLISION TYPE                              
                  # --------------------------------------------------------------------- 
                  R2=random.uniform(RDUM)
                  I=0                                                               
                  flag140=1
                  while(flag140):
                        flag140=0
                        I=I+1                                                             
                        if(CF[IE][I]< R2):
                              flag140=1
                              break
                  #************************************************************
                  # CHECK IF BREMSSTRAHLUNG
                  if(IZBR[I]!= 0 and LBRM == 1) :
                        NFLGBRMM=1
                  IPT=IARRY[I]
                  ICOLL[IPT]=ICOLL[IPT]+1
                  ICOLN[I]=ICOLN[I]+1
                  for KNGS in range(1,NGAS+1):
                        if(IPT == (KNGS*5)-1):
                              break
                        # 141  CONTINUE
                  # 142  
                  IATOMNO=IZBR[I] 
                  BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,EGAMMA,GDCX,GDCY,GDCZ)
                  NBREM[KNGS]=NBREM[KNGS]+1
                  EBRTOT[KNGS]=EBRTOT[KNGS]+EGAMMA
                  # GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
                  E1=EOUT
                  DCX1=EDCX
                  DCY1=EDCY
                  DCZ1=EDCZ
                  # RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE THEN STORE CONVERTED 
                  # ELECTRONS IN global /CASRSB/
                  #
                  BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
                  # BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
                  flag191=0
                  if(ILOW == 1):
                        pass
                  else:
                        #    
                        #  STORE BREMSSTRAHLUNG DATA IN CLUSTER STORE
                        # 
                        ETSUM=0.0     
                        for KBR in range(1,IEVNTLB+1):
                              NCLUS=NCLUS+1
                              if(NCLUS > 150000):
                                    print('   SUBROUTINE STOPPED . NCLUS=',NCLUS,' NREAL=',NREAL)
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
                              # 890  CONTINUE 
                        if(NFLGFC[NCLUS]> NFLGHIGH):
                              NFLGHIGH=NFLGFC[NCLUS]
                              pass
                        else:
                              # endif                
                              # 891 CONTINUE  
                              #*****************************************************************
                              #     S1=RGAS[I]   
                              S1=1.00+GAM2*(RGAS[I]-1.00)                                    
                              EI=EIN[I]
                              #     WRITE(6,8890) EIN[I],I
                              #8890 FORMAT(' EIN=',D12.4,' I=',I3)
                              if(E < EI):
                                    EI=E-0.00010
                              # endif                                                          
                              if(IPN[I]== 0):
                                    # GO TO 666
                                    pass
                              else:
                                    flag335=0
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
                                          IT=min(IT,J300)
                                          TIME[IT]=TIME[IT]+1.00
                                          flag335=1
                                    # endif
                                    if(flag335):
                                          # 335 Copied it form the end till here 
                                          if(K1 == 150000):
                                                # GO TO 889
                                                # 889 
                                                NLEFT=NCLUS-NELEC
                                                # WRITE(6,992) NPRIME,NLEFT,NCLUS
                                                # 992 
                                                print('\n\n\n WARNING STOPPED AFTER NPRIME=',NPRIME,' LAST PRIMARY HAS AT LEAST ',NLEFT,' SECONDARIES LEFT TO TRACK OUT OF ',NCLUS,' ELECTRONS ALREADY IN CLUSTER') 
                                                sys.exit()                      
                                                return                                                            
                                                # end
                                          # CATCH SINGLE ELECTRON CLUSTER THAT WAS ATTACHED.
                                          #     if(NELEC == 1 and NCLUS == 0) GO TO 210 
                                          #
                                          if(NELEC == (NCLUS+1)) :
                                                #       WRITE(6,884) NELEC,NCLUS,NEGION,J11
                                                # 884 FORMAT(' NELEC=',I6,' NCLUS=',I6,' NEGION=',I3,' J11=',I6)
                                                # LAST ELECTRON IN CLUSTER DO STATISTICS OVER PRIMARY CLUSTER
                                                STATS(J11,J1)
                                                # GO TO 210
                                                flag210=1

                                          # endif
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
                                                      pass
                                                else:                       
                                                      # GO TO 1   
                                                      continue
                                          # endif

                                    EISTR=EI
                                    if(IONMODEL[I]> 0) : 
                                          # CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
                                          # FIVE DIFFERENT MODELS
                                          IONSPLIT(I,E,EI,ESEC)
                                          # GO TO 544
                                          pass
                                    else:
                                          # endif
                                          R9=random.uniform(RDUM)
                                          #    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
                                          ESEC=WPL[I]*numpy.tan(R9*numpy.arctan((E-EI)/(2.00*WPL[I])))
                                          ESEC=WPL[I]*(ESEC/WPL[I])**0.9524
                                    # 544 CONTINUE
                                    EI=ESEC+EI 
                                    # STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
                                    # OF SECONDARY IONISATION ELECTRONS
                                    NCLUS=NCLUS+1
                                    NMXADD=MAX(NCLUS,NMXADD)
                                    if(NCLUS > 150000):
                                          # WRITE(6,546) NCLUS,NREAL
                                          # 546  
                                          print('   SUBROUTINE STOPPED . NCLUS=',NCLUS,' NREAL=',NREAL)
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
                                    #     F3=1.0-2.0D0*R3
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
                                    flag666=0
                                    if(IECASC == 0):
                                          # GO TO 333
                                          pass
                                    else:
                                          if(LEGAS[I]== 0):
                                                # GO TO 333
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
                                                for KBR in range(1,IEVENTE+1):
                                                      NCLUS=NCLUS+1
                                                      if(NCLUS > 150000):
                                                            print('   SUBROUTINE STOPPED . NCLUS=',NCLUS,' NREAL=',NREAL)
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
                                                      # 844 CONTINUE
                                                if(NFLGFC[NCLUS]> NFLGHIGH):
                                                      NFLGHIGH=NFLGFC[NCLUS]
                                                flag666=1
                                                #*********************************************************
                                                # STORE POSSIBLE SHELL EMISSIONS AUGER OR FLUORESCENCE 
                                    # 333 
                                    if(flag666):
                                          pass
                                    else:
                                          if(EISTR > 30.0) :
                                                #      WRITE(6,8891) EISTR
                                                #8891  FORMAT(' EISTR=',D12.4)
                                                # TEST IF FLUORESCENCE EMISSION
                                                IFLTST=0
                                                if(WKLM[I]> 0.0):
                                                      R9=random.uniform(RDUM)
                                                if(R9 < WKLM[I]):
                                                      IFLTST=1
                                          # endif
                                          if(IFLTST == 0):
                                                # AUGER EMISSION WITHOUT FLUORESCENCE
                                                NAUG=NC0[I]
                                                EAVAUG=EC0[I]/float(NAUG)
                                                for JFL in range(1,NC0[I]+1):
                                                      NCLUS=NCLUS+1
                                                      XS[NCLUS]=X
                                                      YS[NCLUS]=Y
                                                      ZS[NCLUS]=Z
                                                      TS[NCLUS]=ST
                                                      NFLGFC[NCLUS]=NFLGFF
                                                      NFLGPPC[NCLUS]=NFLGPPP
                                                      NFLGBRMC[NCLUS]=NFLGBRMM
                                                      ES[NCLUS]=EAVAUG
                                                      R3=random.uniform(RDUM)
                                                      F3=1.0-2.00*R3
                                                      THETA0=numpy.arccos(F3)
                                                      F6=numpy.cos(THETA0)
                                                      F5=numpy.sin(THETA0)
                                                      R4=random.uniform(RDUM)
                                                      PHI0=F4*R4
                                                      F8=numpy.sin(PHI0)
                                                      F9=numpy.cos(PHI0)               
                                                      DCX[NCLUS]=F9*F5
                                                      DCY[NCLUS]=F8*F5
                                                      DCZ[NCLUS]=F6
                                                      # 700   CONTINUE 
                                          else:
                                                # AUGER EMISSION AND FLUORESENCE 
                                                if(NG2[I]== 0):
                                                      # GO TO 702
                                                      pass
                                                else:
                                                      NAUG=NG2[I]
                                                      EAVAUG=EG2[I]/float(NAUG)
                                                      for JFL in range(1,NG2[I]+1):
                                                            NCLUS=NCLUS+1
                                                            XS[NCLUS]=X
                                                            YS[NCLUS]=Y
                                                            ZS[NCLUS]=Z
                                                            NFLGFC[NCLUS]=NFLGFF
                                                            NFLGPPC[NCLUS]=NFLGPPP
                                                            NFLGBRMC[NCLUS]=NFLGBRMM
                                                            TS[NCLUS]=ST
                                                            ES[NCLUS]=EAVAUG
                                                            R3=random.uniform(RDUM)
                                                            F3=1.0-2.00*R3
                                                            THETA0=numpy.arccos(F3)
                                                            F6=numpy.cos(THETA0)
                                                            F5=numpy.sin(THETA0)
                                                            R4=random.uniform(RDUM)
                                                            PHI0=F4*R4
                                                            F8=numpy.sin(PHI0)
                                                            F9=numpy.cos(PHI0)               
                                                            DCX[NCLUS]=F9*F5
                                                            DCY[NCLUS]=F8*F5
                                                            DCZ[NCLUS]=F6
                                                            # 701   CONTINUE
                                                # 702   
                                                if(NG1[I] == 0):
                                                      # GO TO 704
                                                      pass
                                                else:
                                                      NAUG=NG1[I]
                                                      EAVAUG=EG1[I]/float(NAUG)
                                                      R9=random.uniform(RDUM)
                                                      DFL=-math.log(R9)*DSTFL[I]
                                                      for JFL in range(1,NG1[I]+1):
                                                            NCLUS=NCLUS+1
                                                            R3=random.uniform(RDUM)
                                                            THEFL=numpy.arccos(1.0-2.00*R3)
                                                            R4=random.uniform(RDUM)
                                                            PHIFL=F4*R4
                                                            XS[NCLUS]=X+DFL*numpy.sin(THEFL)*numpy.cos(PHIFL)
                                                            YS[NCLUS]=Y+DFL*numpy.sin(THEFL)*numpy.sin(PHIFL)
                                                            ZS[NCLUS]=Z+DFL*numpy.cos(THEFL)
                                                            NFLGFC[NCLUS]=NFLGHIGH+1
                                                            NFLGPPC[NCLUS]=NFLGPPP
                                                            NFLGBRMC[NCLUS]=NFLGBRMM
                                                            TS[NCLUS]=ST
                                                            ES[NCLUS]=EAVAUG
                                                            R3=random.uniform(RDUM)
                                                            F3=1.0-2.00*R3
                                                            THETA0=numpy.arccos(F3)
                                                            F6=numpy.cos(THETA0)
                                                            F5=numpy.sin(THETA0)
                                                            R4=random.uniform(RDUM)
                                                            PHI0=F4*R4
                                                            F8=numpy.sin(PHI0)
                                                            F9=numpy.cos(PHI0)               
                                                            DCX[NCLUS]=F9*F5
                                                            DCY[NCLUS]=F8*F5
                                                            DCZ[NCLUS]=F6
                                                            NFLGHIGH=NFLGFC[NCLUS]
                                                            # 703   CONTINUE
                                                # 704   CONTINUE
                                                # endif
                                          # endif
                                          #                                                                       
                                          #  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
                                          #   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
                                          #
                                          # 666 
                              IPT=IARRY[I]
                              ICOLL[IPT]=ICOLL[IPT]+1 
                              ICOLN[I]=ICOLN[I]+1 
                              # IF EXCITATION THEN ADD PROBABILITY ,PENFRA(1,I),OF TRANSFER TO GIVE   
                              # IONISATION OF THE OTHER GASES IN MIXTURE
                              flag6=0
                              if(IPEN == 0 or NGAS == 1):
                                    # GO TO 5
                                    pass
                              else:
                                    if(PENFRA[1][I] != 0.0):
                                          RAN=random.uniform(RDUM)
                                          if(RAN > PENFRA[1][I]):
                                                # GO TO 5
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
                                                else:
                                                      # endif
                                                      ASIGN=1.0
                                                      RAN=random.uniform(RDUM)
                                                      RAN1=random.uniform(RDUM)
                                                      if(RAN1 < 0.5):
                                                            ASIGN=-ASIGN
                                                      XS[NCLUS]=X-math.log(RAN)*PENFRA[2][I]*ASIGN
                                                      RAN=random.uniform(RDUM)
                                                      RAN1=random.uniform(RDUM)
                                                      if(RAN1 < 0.5):
                                                            ASIGN=-ASIGN
                                                      YS[NCLUS]=Y-math.log(RAN)*PENFRA[2][I]*ASIGN
                                                      RAN=random.uniform(RDUM)
                                                      RAN1=random.uniform(RDUM)
                                                      if(RAN1 < 0.5):
                                                            ASIGN=-ASIGN
                                                      ZS[NCLUS]=Z-math.log(RAN)*PENFRA[2][I]*ASIGN
                                                # 667  
                                                RAN=random.uniform(RDUM)
                                                TS[NCLUS]=ST-math.log(RAN)*PENFRA[3][I]
                                                # ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
                                                ES[NCLUS]=1.0
                                                DCX[NCLUS]=DCX1
                                                DCY[NCLUS]=DCY1
                                                DCZ[NCLUS]=DCZ1
                                                flag6=1
                                          # endif 
                                          #      GO TO 6 
                                          # CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
                              # 5 
                              if(flag6): 
                                    if(IPN[I] == 0) :
                                          if((RGAS[I]*EIN[I]) > 4.0) :
                                                KEXC=KEXC+1
                                          if(KEXC > 150000):
                                                # WRITE(6,548) KEXC
                                                # 548     
                                                print('   SUBROUTINE STOPPED . KEXC=',KEXC)
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
                                                # WRITE(6,9911) 
                                                # 9911    
                                                print(' SUBROUTINE STOPPED BAD GAS ID IN MONTE')
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
                              R3=random.uniform(RDUM)
                              if(INDEX[I]== 1):
                                    R31=random.uniform(RDUM)
                              F3=1.00-R3*ANGCT(IE,I)          
                              if(R31 > PSCT[IE][I]):
                                    F3=-F3
                              elif(INDEX[I] == 2) :
                                    EPSI=PSCT(IE,I)
                                    F3=1.00-(2.00*R3*(1.00-EPSI)/(1.00+EPSI*(1.00-2.00*R3))) 
                              else: 
                                    # ISOTROPIC SCATTERING                                             
                                    F3=1.00-2.00*R3
                              # endif
                              THETA0=numpy.arccos(F3)
                              R4=random.uniform(RDUM)
                              PHI0=F4*R4                                                        
                              F8=numpy.sin(PHI0)                                                     
                              F9=numpy.cos(PHI0)                                                     
                              if(E < EI):
                                    EI=0.00                                              
                              ARG1=1.00-S1*EI/E                                                
                              ARG1=max(ARG1,SMALL)                                            
                              D=1.00-F3*math.sqrt(ARG1)                                            
                              E1=E*(1.00-EI/(S1*E)-2.00*D/S2) 
                              E1=max(E1,SMALL)                                                
                              Q=math.sqrt((E/E1)*ARG1)/S1                                           
                              Q=min(Q,1.00)                                                  
                              THETA=numpy.arcsin(Q*numpy.sin(THETA0))                                       
                              F6=numpy.cos(THETA)                                                    
                              U=(S1-1.00)*(S1-1.00)/ARG1                                      
                              CSQD=F3*F3                                                        
                              if(F3 < 0.00 and CSQD > U):
                                    F6=-1.00*F6                        
                              F5=numpy.sin(THETA)                                                    
                              DCZ2=min(DCZ2,1.00)                                            
                              ARGZ=math.sqrt(DCX2*DCX2+DCY2*DCY2)
                              flag190=0
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
                                    flag190=1
                              # endif                                            
                              if(flag190):
                                    # GO TO 190
                                    pass
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
                        flag1=1
                        continue  
                  # STORE POSITION AND TIME OF ELECTRON AND COLLISION HISTORY
                  # 191 CONTINUE
                  flag191=1
                  while(flag191):
                        flag191=0
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
                        # 335  
                        if(K1 == 150000):
                              # GO TO 889
                              # 889 
                              NLEFT=NCLUS-NELEC
                              # WRITE(6,992) NPRIME,NLEFT,NCLUS
                              # 992 
                              print(3*'\n',' WARNING STOPPED AFTER NPRIME= %d LAST PRIMARY HAS AT LEAST %d SECONDARIES LEFT TO TRACK OUT OF %d ELECTRONS ALREADY IN CLUSTER'%(NPRIME,NLEFT,NCLUS)) 
                              # sys.exit()  
                              # doing this if so that updating conf variables can be collapsed by indentation in sublime
                              if(1):   
                                    conf.NGAS=NGAS
                                    conf.NSTEP=NSTEP
                                    conf.NANISO=NANISO
                                    conf.EFINAL=EFINAL
                                    conf.ESTEP=ESTEP
                                    conf.AKT=AKT
                                    conf.ARY=ARY
                                    conf.TEMPC=TEMPC
                                    conf.TORR=TORR
                                    conf.IPEN=IPEN
                                    conf.NDVEC=NDVEC
                                    conf.CONST1=CONST1
                                    conf.CONST2=CONST2
                                    conf.CONST3=CONST3
                                    conf.CONST4=CONST4
                                    conf.CONST5=CONST5
                                    conf.TMAX=TMAX
                                    conf.SMALL=SMALL
                                    conf.API=API
                                    conf.ESTART=ESTART
                                    conf.THETA=THETA
                                    conf.PHI=PHI
                                    conf.TCFMAX=TCFMAX
                                    conf.TCFMAX1=TCFMAX1
                                    conf.RSTART=RSTART
                                    conf.EFIELD=EFIELD
                                    conf.ETHRM=ETHRM
                                    conf.ECUT=ECUT
                                    conf.NDELTA=NDELTA
                                    conf.IMIP=IMIP
                                    conf.IWRITE=IWRITE                    
                                    conf.CF=CF
                                    conf.EIN=EIN
                                    conf.TCF=TCF
                                    conf.IARRY=IARRY
                                    conf.RGAS=RGAS
                                    conf.IPN=IPN
                                    conf.WPL=WPL
                                    conf.IZBR=IZBR
                                    conf.IPLAST=IPLAST
                                    conf.PENFRA=PENFRA
                                    conf.CFN=CFN
                                    conf.TCFN=TCFN
                                    conf.SCLENUL=SCLENUL
                                    conf.NPLAST=NPLAST
                                    conf.ICOLL=ICOLL
                                    conf.NETOT=NETOT
                                    conf.NPRIME=NPRIME
                                    conf.TMAX1=TMAX1
                                    conf.TIME=TIME
                                    conf.NNULL=NNULL
                                    conf.NITOT=NITOT
                                    conf.ICOLN=ICOLN
                                    conf.ICOLNN=ICOLNN
                                    conf.NREAL=NREAL
                                    conf.NEXCTOT =NEXCTOT 
                                    conf.BET=BET
                                    conf.GAM=GAM
                                    conf.VC=VC
                                    conf.EMS=EMS
                                    conf.XST=XST
                                    conf.YST=YST
                                    conf.ZST=ZST
                                    conf.TST=TST
                                    conf.TTIME=TTIME
                                    conf.NFGF=NFGF
                                    conf.NFGPP=NFGPP
                                    conf.NFGBR=NFGBR
                                    conf.NELEC=NELEC
                                    conf.NEGION=NEGION
                                    conf.EST1=EST1
                                    conf.EST2=EST2
                                    conf.XSTEXC=XSTEXC
                                    conf.YSTEXC=YSTEXC
                                    conf.ZSTEXC=ZSTEXC
                                    conf.TSTEXC=TSTEXC
                                    conf.NSTEXC=NSTEXC
                                    conf.XSTN=XSTN
                                    conf.YSTN=YSTN
                                    conf.ZSTN=ZSTN
                                    conf.TSTN=TSTN
                                    conf.IDNUL=IDNUL
                                    conf.NEXCNUL=NEXCNUL
                                    conf.DOUBLE=DOUBLE
                                    conf.CMINIXSC=CMINIXSC
                                    conf.CMINEXSC=CMINEXSC
                                    conf.ECLOSS=ECLOSS
                                    conf.WPLN=WPLN
                                    conf.ICOUNT=ICOUNT
                                    conf.AVPFRAC=AVPFRAC
                                    conf.NC0=NC0
                                    conf.EC0=EC0
                                    conf.NG1=NG1
                                    conf.EG1=EG1
                                    conf.NG2=NG2
                                    conf.EG2=EG2
                                    conf.WKLM=WKLM
                                    conf.DSTFL=DSTFL
                                    conf.ESPLIT=ESPLIT
                                    conf.IONMODEL=IONMODEL
                                    conf.PSCT=PSCT
                                    conf.ANGCT=ANGCT
                                    conf.INDEX=INDEX
                                    conf.NISO=NISO
                                    conf.ECAS=ECAS
                                    conf.XCAS=XCAS
                                    conf.YCAS=YCAS
                                    conf.ZCAS=ZCAS
                                    conf.DRXS=DRXS
                                    conf.DRYS=DRYS
                                    conf.DRZS=DRZS
                                    conf.TT1=TT1
                                    conf.NFLGF=NFLGF
                                    conf.NFLGPP=NFLGPP
                                    conf.IEVNTL=IEVNTL
                                    conf.LCMPLCFLG=LCMPLCFLG
                                    conf.LRAY=LRAY
                                    conf.LRFLG=LRFLG
                                    conf.LPAP=LPAP
                                    conf.LPFLG=LPFLG
                                    conf.LBRM=LBRM
                                    conf.LBFLG=LBFLG
                                    conf.LPEFLG=LPEFLG
                                    conf.EBRGAM=EBRGAM
                                    conf.BRDCOSX=BRDCOSX
                                    conf.BRDCOSY=BRDCOSY
                                    conf.BRDCOSZ=BRDCOSZ
                                    conf.BRX=BRX
                                    conf.BRY=BRY
                                    conf.BRZ=BRZ
                                    conf.BRT=BRT
                                    conf.EBRTOT=EBRTOT
                                    conf.NBREM=NBREM
                                    conf.ECASB=ECASB
                                    conf.XCASB=XCASB
                                    conf.YCASB=YCASB
                                    conf.ZCASB=ZCASB
                                    conf.DRXB=DRXB
                                    conf.DRYB=DRYB
                                    conf.DRZB=DRZB
                                    conf.TTB1=TTB1
                                    conf.NFLGFB=NFLGFB
                                    conf.NFLGPPB=NFLGPPB
                                    conf.IEVNTLB=IEVNTLB
                                    conf.ECASE=ECASE
                                    conf.XCASE=XCASE
                                    conf.YCASE=YCASE
                                    conf.ZCASE=ZCASE
                                    conf.DRXCE=DRXCE
                                    conf.DRYCE=DRYCE
                                    conf.DRZCE=DRZCE
                                    conf.TCASE=TCASE
                                    conf.NFLGFE=NFLGFE
                                    conf.NFLGPPE=NFLGPPE
                                    conf.IEVENTE=IEVENTE
                                    conf.NEGAS=NEGAS
                                    conf.LEGAS=LEGAS
                                    conf.IESHELL=IESHELL
                                    conf.IECASC=IECASC
                                    conf.NGEXC1=NGEXC1
                                    conf.NGEXC2=NGEXC2
                                    conf.NGEXC3=NGEXC3
                                    conf.NGEXC4=NGEXC4
                                    conf.NGEXC5=NGEXC5
                                    conf.NGEXC6=NGEXC6
                                    conf.IDG1=IDG1
                                    conf.IDG2=IDG2
                                    conf.IDG3=IDG3
                                    conf.IDG4=IDG4
                                    conf.IDG5=IDG5
                                    conf.IDG6=IDG6                 
                              return 

                        # CATCH SINGLE ELECTRON CLUSTER THAT WAS ATTACHED.
                        #     if(NELEC == 1 and NCLUS == 0) GO TO 210 
                        #
                        if(NELEC == (NCLUS+1)) :
                              #       WRITE(6,884) NELEC,NCLUS,NEGION,J11
                              # 884 FORMAT(' NELEC=',I6,' NCLUS=',I6,' NEGION=',I3,' J11=',I6)
                              # LAST ELECTRON IN CLUSTER DO STATISTICS OVER PRIMARY CLUSTER
                              STATS(J11,J1)
                              # GO TO 210
                              flag1=0
                              flag210=1
                              break
                        # endif
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
                                    continue
                              flag1=1                       
                              break
                  # endif
                  #  MAIN LOOP END    
                  # 210 CONTINUE
                  if(flag210):
                        break
      # RESET NUMBER OF EVENTS FOR BAD EVENTS
      if(IMIP > 2):
            NDELTA=NDELTA-IBADTOT
      #
      # WRITE(6,887) EMAX,NEOVFL
      # 887 
      print(' EMAX= %.7f NEOVFL= %d'%(EMAX,NEOVFL))  
      if(EMAX > EFINAL):
            # WRITE(6,989) EFINAL,EMAX
            # 989 
            print('INCREASE ENERGY LIMIT FROM %.6f EV TO AT LEAST %.6f \n EV.'%(EFINAL,EMAX))
            # sys.exit()
            # doing if(1) so that updating conf variables can be collapsed by indentation in sublime
            if(1):
                  conf.NGAS=NGAS
                  conf.NSTEP=NSTEP
                  conf.NANISO=NANISO
                  conf.EFINAL=EFINAL
                  conf.ESTEP=ESTEP
                  conf.AKT=AKT
                  conf.ARY=ARY
                  conf.TEMPC=TEMPC
                  conf.TORR=TORR
                  conf.IPEN=IPEN
                  conf.NDVEC=NDVEC
                  conf.CONST1=CONST1
                  conf.CONST2=CONST2
                  conf.CONST3=CONST3
                  conf.CONST4=CONST4
                  conf.CONST5=CONST5
                  conf.TMAX=TMAX
                  conf.SMALL=SMALL
                  conf.API=API
                  conf.ESTART=ESTART
                  conf.THETA=THETA
                  conf.PHI=PHI
                  conf.TCFMAX=TCFMAX
                  conf.TCFMAX1=TCFMAX1
                  conf.RSTART=RSTART
                  conf.EFIELD=EFIELD
                  conf.ETHRM=ETHRM
                  conf.ECUT=ECUT
                  conf.NDELTA=NDELTA
                  conf.IMIP=IMIP
                  conf.IWRITE=IWRITE                    
                  conf.CF=CF
                  conf.EIN=EIN
                  conf.TCF=TCF
                  conf.IARRY=IARRY
                  conf.RGAS=RGAS
                  conf.IPN=IPN
                  conf.WPL=WPL
                  conf.IZBR=IZBR
                  conf.IPLAST=IPLAST
                  conf.PENFRA=PENFRA
                  conf.CFN=CFN
                  conf.TCFN=TCFN
                  conf.SCLENUL=SCLENUL
                  conf.NPLAST=NPLAST
                  conf.ICOLL=ICOLL
                  conf.NETOT=NETOT
                  conf.NPRIME=NPRIME
                  conf.TMAX1=TMAX1
                  conf.TIME=TIME
                  conf.NNULL=NNULL
                  conf.NITOT=NITOT
                  conf.ICOLN=ICOLN
                  conf.ICOLNN=ICOLNN
                  conf.NREAL=NREAL
                  conf.NEXCTOT =NEXCTOT 
                  conf.BET=BET
                  conf.GAM=GAM
                  conf.VC=VC
                  conf.EMS=EMS
                  conf.XST=XST
                  conf.YST=YST
                  conf.ZST=ZST
                  conf.TST=TST
                  conf.TTIME=TTIME
                  conf.NFGF=NFGF
                  conf.NFGPP=NFGPP
                  conf.NFGBR=NFGBR
                  conf.NELEC=NELEC
                  conf.NEGION=NEGION
                  conf.EST1=EST1
                  conf.EST2=EST2
                  conf.XSTEXC=XSTEXC
                  conf.YSTEXC=YSTEXC
                  conf.ZSTEXC=ZSTEXC
                  conf.TSTEXC=TSTEXC
                  conf.NSTEXC=NSTEXC
                  conf.XSTN=XSTN
                  conf.YSTN=YSTN
                  conf.ZSTN=ZSTN
                  conf.TSTN=TSTN
                  conf.IDNUL=IDNUL
                  conf.NEXCNUL=NEXCNUL
                  conf.DOUBLE=DOUBLE
                  conf.CMINIXSC=CMINIXSC
                  conf.CMINEXSC=CMINEXSC
                  conf.ECLOSS=ECLOSS
                  conf.WPLN=WPLN
                  conf.ICOUNT=ICOUNT
                  conf.AVPFRAC=AVPFRAC
                  conf.NC0=NC0
                  conf.EC0=EC0
                  conf.NG1=NG1
                  conf.EG1=EG1
                  conf.NG2=NG2
                  conf.EG2=EG2
                  conf.WKLM=WKLM
                  conf.DSTFL=DSTFL
                  conf.ESPLIT=ESPLIT
                  conf.IONMODEL=IONMODEL
                  conf.PSCT=PSCT
                  conf.ANGCT=ANGCT
                  conf.INDEX=INDEX
                  conf.NISO=NISO
                  conf.ECAS=ECAS
                  conf.XCAS=XCAS
                  conf.YCAS=YCAS
                  conf.ZCAS=ZCAS
                  conf.DRXS=DRXS
                  conf.DRYS=DRYS
                  conf.DRZS=DRZS
                  conf.TT1=TT1
                  conf.NFLGF=NFLGF
                  conf.NFLGPP=NFLGPP
                  conf.IEVNTL=IEVNTL
                  conf.LCMPLCFLG=LCMPLCFLG
                  conf.LRAY=LRAY
                  conf.LRFLG=LRFLG
                  conf.LPAP=LPAP
                  conf.LPFLG=LPFLG
                  conf.LBRM=LBRM
                  conf.LBFLG=LBFLG
                  conf.LPEFLG=LPEFLG
                  conf.EBRGAM=EBRGAM
                  conf.BRDCOSX=BRDCOSX
                  conf.BRDCOSY=BRDCOSY
                  conf.BRDCOSZ=BRDCOSZ
                  conf.BRX=BRX
                  conf.BRY=BRY
                  conf.BRZ=BRZ
                  conf.BRT=BRT
                  conf.EBRTOT=EBRTOT
                  conf.NBREM=NBREM
                  conf.ECASB=ECASB
                  conf.XCASB=XCASB
                  conf.YCASB=YCASB
                  conf.ZCASB=ZCASB
                  conf.DRXB=DRXB
                  conf.DRYB=DRYB
                  conf.DRZB=DRZB
                  conf.TTB1=TTB1
                  conf.NFLGFB=NFLGFB
                  conf.NFLGPPB=NFLGPPB
                  conf.IEVNTLB=IEVNTLB
                  conf.ECASE=ECASE
                  conf.XCASE=XCASE
                  conf.YCASE=YCASE
                  conf.ZCASE=ZCASE
                  conf.DRXCE=DRXCE
                  conf.DRYCE=DRYCE
                  conf.DRZCE=DRZCE
                  conf.TCASE=TCASE
                  conf.NFLGFE=NFLGFE
                  conf.NFLGPPE=NFLGPPE
                  conf.IEVENTE=IEVENTE
                  conf.NEGAS=NEGAS
                  conf.LEGAS=LEGAS
                  conf.IESHELL=IESHELL
                  conf.IECASC=IECASC
                  conf.NGEXC1=NGEXC1
                  conf.NGEXC2=NGEXC2
                  conf.NGEXC3=NGEXC3
                  conf.NGEXC4=NGEXC4
                  conf.NGEXC5=NGEXC5
                  conf.NGEXC6=NGEXC6
                  conf.IDG1=IDG1
                  conf.IDG2=IDG2
                  conf.IDG3=IDG3
                  conf.IDG4=IDG4
                  conf.IDG5=IDG5
                  conf.IDG6=IDG6
      # endif                                         
      return 
      # 889 
      NLEFT=NCLUS-NELEC
      # WRITE(6,992) NPRIME,NLEFT,NCLUS
      # 992 
      print(3*'\n',' WARNING STOPPED AFTER NPRIME= %d LAST PRIMARY HAS AT LEAST %d SECONDARIES LEFT TO TRACK OUT OF %d ELECTRONS ALREADY IN CLUSTER'%(NPRIME,NLEFT,NCLUS)) 
      # sys.exit()  
      # doing this if so that updating conf variables can be collapsed by indentation in sublime
      if(1):   
            conf.NGAS=NGAS
            conf.NSTEP=NSTEP
            conf.NANISO=NANISO
            conf.EFINAL=EFINAL
            conf.ESTEP=ESTEP
            conf.AKT=AKT
            conf.ARY=ARY
            conf.TEMPC=TEMPC
            conf.TORR=TORR
            conf.IPEN=IPEN
            conf.NDVEC=NDVEC
            conf.CONST1=CONST1
            conf.CONST2=CONST2
            conf.CONST3=CONST3
            conf.CONST4=CONST4
            conf.CONST5=CONST5
            conf.TMAX=TMAX
            conf.SMALL=SMALL
            conf.API=API
            conf.ESTART=ESTART
            conf.THETA=THETA
            conf.PHI=PHI
            conf.TCFMAX=TCFMAX
            conf.TCFMAX1=TCFMAX1
            conf.RSTART=RSTART
            conf.EFIELD=EFIELD
            conf.ETHRM=ETHRM
            conf.ECUT=ECUT
            conf.NDELTA=NDELTA
            conf.IMIP=IMIP
            conf.IWRITE=IWRITE                    
            conf.CF=CF
            conf.EIN=EIN
            conf.TCF=TCF
            conf.IARRY=IARRY
            conf.RGAS=RGAS
            conf.IPN=IPN
            conf.WPL=WPL
            conf.IZBR=IZBR
            conf.IPLAST=IPLAST
            conf.PENFRA=PENFRA
            conf.CFN=CFN
            conf.TCFN=TCFN
            conf.SCLENUL=SCLENUL
            conf.NPLAST=NPLAST
            conf.ICOLL=ICOLL
            conf.NETOT=NETOT
            conf.NPRIME=NPRIME
            conf.TMAX1=TMAX1
            conf.TIME=TIME
            conf.NNULL=NNULL
            conf.NITOT=NITOT
            conf.ICOLN=ICOLN
            conf.ICOLNN=ICOLNN
            conf.NREAL=NREAL
            conf.NEXCTOT =NEXCTOT 
            conf.BET=BET
            conf.GAM=GAM
            conf.VC=VC
            conf.EMS=EMS
            conf.XST=XST
            conf.YST=YST
            conf.ZST=ZST
            conf.TST=TST
            conf.TTIME=TTIME
            conf.NFGF=NFGF
            conf.NFGPP=NFGPP
            conf.NFGBR=NFGBR
            conf.NELEC=NELEC
            conf.NEGION=NEGION
            conf.EST1=EST1
            conf.EST2=EST2
            conf.XSTEXC=XSTEXC
            conf.YSTEXC=YSTEXC
            conf.ZSTEXC=ZSTEXC
            conf.TSTEXC=TSTEXC
            conf.NSTEXC=NSTEXC
            conf.XSTN=XSTN
            conf.YSTN=YSTN
            conf.ZSTN=ZSTN
            conf.TSTN=TSTN
            conf.IDNUL=IDNUL
            conf.NEXCNUL=NEXCNUL
            conf.DOUBLE=DOUBLE
            conf.CMINIXSC=CMINIXSC
            conf.CMINEXSC=CMINEXSC
            conf.ECLOSS=ECLOSS
            conf.WPLN=WPLN
            conf.ICOUNT=ICOUNT
            conf.AVPFRAC=AVPFRAC
            conf.NC0=NC0
            conf.EC0=EC0
            conf.NG1=NG1
            conf.EG1=EG1
            conf.NG2=NG2
            conf.EG2=EG2
            conf.WKLM=WKLM
            conf.DSTFL=DSTFL
            conf.ESPLIT=ESPLIT
            conf.IONMODEL=IONMODEL
            conf.PSCT=PSCT
            conf.ANGCT=ANGCT
            conf.INDEX=INDEX
            conf.NISO=NISO
            conf.ECAS=ECAS
            conf.XCAS=XCAS
            conf.YCAS=YCAS
            conf.ZCAS=ZCAS
            conf.DRXS=DRXS
            conf.DRYS=DRYS
            conf.DRZS=DRZS
            conf.TT1=TT1
            conf.NFLGF=NFLGF
            conf.NFLGPP=NFLGPP
            conf.IEVNTL=IEVNTL
            conf.LCMPLCFLG=LCMPLCFLG
            conf.LRAY=LRAY
            conf.LRFLG=LRFLG
            conf.LPAP=LPAP
            conf.LPFLG=LPFLG
            conf.LBRM=LBRM
            conf.LBFLG=LBFLG
            conf.LPEFLG=LPEFLG
            conf.EBRGAM=EBRGAM
            conf.BRDCOSX=BRDCOSX
            conf.BRDCOSY=BRDCOSY
            conf.BRDCOSZ=BRDCOSZ
            conf.BRX=BRX
            conf.BRY=BRY
            conf.BRZ=BRZ
            conf.BRT=BRT
            conf.EBRTOT=EBRTOT
            conf.NBREM=NBREM
            conf.ECASB=ECASB
            conf.XCASB=XCASB
            conf.YCASB=YCASB
            conf.ZCASB=ZCASB
            conf.DRXB=DRXB
            conf.DRYB=DRYB
            conf.DRZB=DRZB
            conf.TTB1=TTB1
            conf.NFLGFB=NFLGFB
            conf.NFLGPPB=NFLGPPB
            conf.IEVNTLB=IEVNTLB
            conf.ECASE=ECASE
            conf.XCASE=XCASE
            conf.YCASE=YCASE
            conf.ZCASE=ZCASE
            conf.DRXCE=DRXCE
            conf.DRYCE=DRYCE
            conf.DRZCE=DRZCE
            conf.TCASE=TCASE
            conf.NFLGFE=NFLGFE
            conf.NFLGPPE=NFLGPPE
            conf.IEVENTE=IEVENTE
            conf.NEGAS=NEGAS
            conf.LEGAS=LEGAS
            conf.IESHELL=IESHELL
            conf.IECASC=IECASC
            conf.NGEXC1=NGEXC1
            conf.NGEXC2=NGEXC2
            conf.NGEXC3=NGEXC3
            conf.NGEXC4=NGEXC4
            conf.NGEXC5=NGEXC5
            conf.NGEXC6=NGEXC6
            conf.IDG1=IDG1
            conf.IDG2=IDG2
            conf.IDG3=IDG3
            conf.IDG4=IDG4
            conf.IDG5=IDG5
            conf.IDG6=IDG6                 
      return                                                            
      # end
