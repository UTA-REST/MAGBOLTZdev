## MONTEFA()
* Tracks DELTA electrons and updates arrays containing position and time of thermalised electrons.
* Calculates number of produced electrons per primary delta and other higher FANO factors.
* Range calculation accurate for anisotropic X-Sections

### Arguments

| Argument | Description |
|----------|-------------|
| NONE     | -           |
|          |             |

### Pseudo Code

```fortran
      SUBROUTINE MONTEFA                                               
      IMPLICIT REAL*8 (A-H,O-Z)
      IMPLICIT INTEGER*8 (I-N)                                         
      COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
      COMMON/INPT1/NDVEC
      COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
      COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,
     /RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE   
      COMMON/BFLD/EOVB,WB,BTHETA,BMAG                                   
      COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),    
     /RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA(3,512)
      COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST
      COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL,
     /NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT 
      COMMON/RLTVY/BET(20000),GAM(20000),VC,EMS
      COMMON/STTS/XST(150000),YST(150000),ZST(150000),TST(150000),
     /TTIME(150000),NFGF(150000),NFGPP(150000),NFGBR(150000),NELEC,
     /NEGION,EST1,EST2 
      COMMON/STEXC/XSTEXC(150000),YSTEXC(150000),ZSTEXC(150000),
     /TSTEXC(150000),NSTEXC
      COMMON/STEXCNUL/XSTN(150000),YSTN(150000),ZSTN(150000),
     /TSTN(150000),IDNUL(150000),NEXCNUL
      COMMON/IONC/DOUBLE(6,20000),CMINIXSC(6),CMINEXSC(6),ECLOSS(6),
     /WPLN(6),ICOUNT,AVPFRAC(3,6)
      COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),
     /EG2(512),WKLM(512),DSTFL(512)
      COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512) 
      COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO
      COMMON/CASRS/ECAS(400),XCAS(400),YCAS(400),ZCAS(400),DRXS(400),
     /DRYS(400),DRZS(400),TT1(400),NFLGF(400),NFLGPP(400),IEVNTL
      COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
      COMMON/BREMG/EBRGAM(10),BRDCOSX(10),BRDCOSY(10),BRDCOSZ(10),
     /BRX(10),BRY(10),BRZ(10),BRT(10),EBRTOT(6),NBREM(6)
      COMMON/CASRSB/ECASB(400),XCASB(400),YCASB(400),ZCASB(400),
     /DRXB(400),DRYB(400),DRZB(400),TTB1(400),NFLGFB(400),NFLGPPB(400),
     /IEVNTLB
      COMMON/CASRSE/ECASE(400),XCASE(400),YCASE(400),ZCASE(400),
     /DRXCE(400),DRYCE(400),DRZCE(400),TCASE(400),
     /NFLGFE(400),NFLGPPE(400),IEVENTE
      COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
      COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,
     /IDG1,IDG2,IDG3,IDG4,IDG5,IDG6
      DIMENSION XS(150000),YS(150000),ZS(150000),TS(150000),ES(150000),
     /DCX(150000),DCY(150000),DCZ(150000),
     /NFLGFC(150000),NFLGPPC(150000),NFLGBRMC(150000)
      DIMENSION TEMP(20000)
C ----------------------------------------------------------------------   
C   RELATIVISTIC KINEMATICS
C   ELECTRIC AND MAGNETIC FIELDS  PARALLEL TO Z-AXIS      
C   TRACKS DELTA ELECTRONS AND UPDATES ARRAYS CONTAINING POSITION AND 
C   TIME OF THERMALISED ELECTRONS.
C   CALCULATES NUMBER OF PRODUCED ELECTRONS PER PRIMARY DELTA AND OTHER
C   HIGHER FANO FACTORS
C   RANGE CALCULATION IS ACCURATE ONLY FOR ANISOTROPIC X-SECTIONS.
C ----------------------------------------------------------------------
C VARYING ENERGY STEPS
      IF(EFINAL.LE.140000.) THEN
        ESTEP1=(EFINAL-16000.0)/DFLOAT(4000)
      ELSE
        ESTEP1=20.0
        ESTEP2=(EFINAL-92000.0)/DFLOAT(4000)
      ENDIF
      NPRINT=0 
      J300=300
      J20000=20000
      API=DACOS(-1.0D0)
      SMALL=1.0D-20
      EMAX=0.0D0
      TMAX1=0.0D0
      RDUM=RSTART
      CONST9=CONST3*0.01D0
      DO 25 I=1,300
   25 TIME(I)=0.0D0
      DO 26 I=1,30
   26 ICOLL(I)=0
      DO 27 I=1,512
   27 ICOLN(I)=0
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
      F4=2.0D0*API
      THETA1=THETA
      PHI1=PHI
      NEOVFL=0
C CALCULATE MAXIMUM COLLISION FREQUENCY
      TLIM=0.0
      DO 111 J=1,20000
      TEMP(J)=TCFN(J)+TCF(J)
      IF(TLIM.LT.TEMP(J)) TLIM=TEMP(J) 
  111 CONTINUE
C START OF PRIMARY DELTA LOOP
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
C     INITIAL DIRECTION COSINES FOR ELECTRON BEAM                
      DCZ1=DCOS(THETA1) 
      DCX1=DSIN(THETA1)*DCOS(PHI1)                                      
      DCY1=DSIN(THETA1)*DSIN(PHI1)
      NFLGFF=0
      NFLGPPP=0
      NFLGBRMM=0
      NFLGHIGH=0
      EST1=ESTART
C INITIAL VELOCITY
      E1=ESTART
C     VTOT=CONST9*DSQRT(E1)
      GAM1=(EMS+E1)/EMS
      GAM12=GAM1
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      VTOT=BET1*VC*1.0D-12
      CX1=DCX1*VTOT
      CY1=DCY1*VTOT
      CZ1=DCZ1*VTOT      
      X=0.0D0    
      Y=0.0D0    
      Z=0.0D0                                           
      K1=0   
      KEXC=0
      NSTEXC=0
      NEXCNUL=0
      NCLUS=0
      NELEC=0
      NEGION=0
      TLAST=0.0D0
      ST=0.0D0
      TDASH=0.0D0
      IF(IMIP.EQ.2) GO TO 1
      IF(IMIP.GT.2) THEN
C READIN FIRST ELECTRON FROM BETA DECAY OR XRAY UNTHERMALISED CLUSTERS
       CALL CASRES(J11,IBADTOT,IBAD1)
C  SKIP IF BAD EVENT
       IF(IBAD1.EQ.1) THEN
        J1=J1-1
        GO TO 210
       ENDIF
      ELSE IF(IMIP.EQ.1) THEN
C READ IN FIRST ELECTRON FROM MIP INTERACTION
        CALL CASREM(J11)
        EST1=ECAS(1)
        EST2=EST1
      ENDIF
      X=XCAS(1)
      Y=YCAS(1)
      Z=ZCAS(1)
      ST=TT1(1)
      TS(1)=TT1(1)
      E1=ECAS(1)
      DCZ1=DRZS(1)
      DCY1=DRYS(1)
      DCX1=DRXS(1)
      NFLGFF=NFLGF(1)
      NFLGPPP=NFLGPP(1)
      NFLGBRMM=0
      NFLGHIGH=NFLGFF
      GAM1=(EMS+E1)/EMS
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
C     VTOT=CONST9*DSQRT(E1)
      VTOT=BET1*VC*1.0D-12
C
      CX1=DCX1*VTOT
      CY1=DCY1*VTOT
      CZ1=DCZ1*VTOT
C PUT REMAINDER OF ELECTRONS INTO CLUSTER STORE
      ISDUM=0
      DO 35 IST=2,IEVNTL
      ISDUM=ISDUM+1
      XS(ISDUM)=XCAS(IST)
      YS(ISDUM)=YCAS(IST)
      ZS(ISDUM)=ZCAS(IST)
      TS(ISDUM)=TT1(IST)
      ES(ISDUM)=ECAS(IST)
      DCX(ISDUM)=DRXS(IST)
      DCY(ISDUM)=DRYS(IST)
      DCZ(ISDUM)=DRZS(IST)
      NFLGFC(ISDUM)=NFLGF(IST)
      NFLGPPC(ISDUM)=NFLGPP(IST)
      NFLGBRMC(ISDUM)=0
      NCLUS=ISDUM
      IF(NFLGF(IST).GT.NFLGHIGH) NFLGHIGH=NFLGF(IST)
   35 CONTINUE
      GAM12=GAM1
C START OF LOOP FOR NEWLY CREATED ELECTRONS                             
    1 CONTINUE 
      R1=drand48(RDUM)
      T=-DLOG(R1)/TLIM+TDASH
      TDASH=T
C     AP=DCZ1*F2*DSQRT(E1)
      GAM1=(EMS+E1)/EMS
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      AP=DCZ1*EFIELD*BET1*VC*1.0D-10
      BP1=BP/GAM1
 913  FORMAT(3X,' AFTER STORE NREAL=',I10,' E1=',E12.3,' T=',E12.3,' AP=
     /',E12.3,' BP=',E12.3,' DCZ1=',E12.3)
C     E=E1+(AP+BP*T)*T       
      E=E1+(AP+BP1*T)*T
      IF(E.LT.0.0D0) THEN
       IF(NPRINT.EQ.0) WRITE(6,913)NREAL,E1,T,AP,BP,DCZ1 
       NPRINT=1
       E=0.001D0
      ENDIF                                                   
C INSERT NEW ALGORITHM TO FIND IE FOR VARYING ENERGY STEP          
      IF(IMIP.EQ.1) THEN                                     
       IE=DINT(E/ESTEP)+1                                               
      ELSE
       IF(EFINAL.LE.20000.) THEN
        IE=DINT(E/ESTEP)+1
       ELSE IF(EFINAL.LE.140000.) THEN
        IF(E.LE.16000.) THEN
         IE=DINT(E)+1
        ELSE
         IE=16000+DINT((E-16000.)/ESTEP1)
        ENDIF
       ELSE
        IF(E.LE.12000.) THEN
         IE=DINT(E)+1
        ELSE IF(E.LE.92000.) THEN
         IE=12000+DINT((E-12000.)/ESTEP1)
        ELSE
         IE=16000+DINT((E-92000.)/ESTEP2)
        ENDIF
       ENDIF
      ENDIF 
      IE=DMIN0(IE,J20000)                                            
C                                                                       
C     TEST FOR REAL OR NULL COLLISION                                   
C                                                                       
      R5=drand48(RDUM)
      TEST1=TCF(IE)/TLIM                                                
      IF(R5.LE.TEST1) GO TO 137                                         
      NNULL=NNULL+1                
      TEST2=TEMP(IE)/TLIM
      IF(R5.LT.TEST2) THEN
C TEST FOR NULL LEVELS
       IF(NPLAST.EQ.0) GO TO 1
       R2=drand48(RDUM) 
       I=0
  888  I=I+1
       IF(CFN(IE,I).LT.R2) GO TO 888  
C INCREMENT NULL LEVEL SUM
       NEXCNUL=NEXCNUL+1
       ICOLNN(I)=ICOLNN(I)+1
C STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION AND DISSOCIATION FROM 
C    NULL EXCITATION  
C NOTE: SMALL APPROX USED POSITION OF PREVIOUS COLLISION
       XSTN(NEXCNUL)=X
       YSTN(NEXCNUL)=Y
       ZSTN(NEXCNUL)=Z
       TSTN(NEXCNUL)=ST
       IDNUL(NEXCNUL)=I
       GO TO 1       
      ELSE
C NULL
       GO TO 1
      ENDIF                                                   
C                                                                       
C  CALCULATE DIRECTION COSINES AND POSITIONS AT INSTANT BEFORE COLLISION
  137 T2=T*T
      GAM2=(EMS+E)/EMS
      BET2=DSQRT(1.0D0-1.0D0/(GAM2*GAM2))
      GAM12=(GAM1+GAM2)/2.0D0
      IF(E.GT.EMAX) EMAX=E
      IF(T.GT.TMAX1) TMAX1=T
      TDASH=0.0D0  
      NREAL=NREAL+1
      WBT=WB*T/GAM12
C     WBT=WB*T      
      WBR=WB/GAM12
      COSWT=DCOS(WBT)
      SINWT=DSIN(WBT)                                                   
C     CONST6=DSQRT(E1/E)
      CONST6=BET1/BET2
      CX2=CX1*COSWT-CY1*SINWT
      CY2=CY1*COSWT+CX1*SINWT
C     VTOT=CONST9*DSQRT(E)
      VTOT=VC*BET2*1.0D-12                    
      DCX2=CX2/VTOT                                                     
      DCY2=CY2/VTOT                                                     
C     DCZ2=DCZ1*CONST6+EFIELD*T*CONST5/DSQRT(E) 
      DCZ2=DCZ1*CONST6+EFIELD*T*2.0D10*CONST1/(VC*BET2)
C     CONST7=CONST9*DSQRT(E1)   
      CONST7=VC*BET1*1.0D-12            
      A=T*CONST7                                                        
C     DX=(CX1*SINWT-CY1*(1.0D0-COSWT))/WB 
      DX=(CX1*SINWT-CY1*(1.0D0-COSWT))/WBR                              
      X=X+DX           
C     DY=(CY1*SINWT+CX1*(1.0D0-COSWT))/WB                               
      DY=(CY1*SINWT+CX1*(1.0D0-COSWT))/WBR                              
      Y=Y+DY    
C     Z=Z+DCZ1*A+T2*F1
      Z=Z+DCZ1*A+T2*F1/GAM12
      ST=ST+T
      IT=DINT(T+1.0D0)                                                  
      IT=DMIN0(IT,J300)                                                
      TIME(IT)=TIME(IT)+1.0D0                                           
C --------------------------------------------------------------------- 
C     DETERMINATION OF REAL COLLISION TYPE                              
C --------------------------------------------------------------------- 
      R2=drand48(RDUM)
      I=0                                                               
  140 I=I+1 
      IF(I.LE.0.OR.I.GT.512) THEN
      WRITE(6,945) I
  945 FORMAT(' BAD  SELECTION I=',I8)
      STOP
      ENDIF
      IF(CF(IE,I).LT.R2) GO TO 140        
C************************************************************
C CHECK IF BREMSSTRAHLUNG
      IF(IZBR(I).NE.0.AND.LBRM.EQ.1) THEN
       NFLGBRMM=1
       IPT=IARRY(I)
       ICOLL(IPT)=ICOLL(IPT)+1
       ICOLN(I)=ICOLN(I)+1
       DO 141 KNGS=1,NGAS
       IF(IPT.EQ.(KNGS*5)-1) GO TO 142
  141  CONTINUE
  142  IATOMNO=IZBR(I) 
       CALL BREMS(IATOMNO,E,DCX2,DCY2,DCZ2,EOUT,EDCX,EDCY,EDCZ,
     /EGAMMA,GDCX,GDCY,GDCZ)
       NBREM(KNGS)=NBREM(KNGS)+1
       EBRTOT(KNGS)=EBRTOT(KNGS)+EGAMMA
C      WRITE(6,668) EGAMMA,J11   
C 668 FORMAT(' BREM EGAMMA=',D12.4,' EVENT NO=',I5)
C GET  NEW DRCOS DRCOSY DRCOSX AND ENERGY OF ELECTRON
       E1=EOUT
       DCX1=EDCX
       DCY1=EDCY
       DCZ1=EDCZ
C RUN BREMSSTRAHLUNG GAMMA THROUGH CASCADE THEN STORE CONVERTED 
C ELECTRONS IN COMMON/CASRSB/
C              
       CALL BREMSCASC(J11,EGAMMA,X,Y,Z,ST,GDCX,GDCY,GDCZ,ILOW)
C BREMSSTRAHLUNG ENERGY TOO LOW TO IONISE
       IF(ILOW.EQ.1) GO TO 190
C 
C STORE BREMSSTRAHLUNG DATA IN CLUSTER STORE
C
       DO 890 KBR=1,IEVNTLB
       NCLUS=NCLUS+1
       IF(NCLUS.GT.150000) THEN 
        WRITE(6,546) NCLUS,NREAL
        STOP
       ENDIF     
       ES(NCLUS)=ECASB(KBR)
       XS(NCLUS)=XCASB(KBR)
       YS(NCLUS)=YCASB(KBR)
       ZS(NCLUS)=ZCASB(KBR)
       TS(NCLUS)=TTB1(KBR)
       DCX(NCLUS)=DRXB(KBR)
       DCY(NCLUS)=DRYB(KBR)
       DCZ(NCLUS)=DRZB(KBR)
       NFLGFC(NCLUS)=NFLGFB(KBR)+NFLGHIGH
       NFLGPPC(NCLUS)=NFLGPPB(KBR)
       NFLGBRMC(NCLUS)=2
  890  CONTINUE
       IF(NFLGFC(NCLUS).GT.NFLGHIGH) NFLGHIGH=NFLGFC(NCLUS)
       GO TO 190
      ENDIF
  891 CONTINUE
C****************************************************************
C     S1=RGAS(I)  
      S1=1.0D0+GAM2*(RGAS(I)-1.0D0)                                    
      EI=EIN(I)
      IF(E.LT.EI) THEN
      EI=E-0.0001D0
      ENDIF                                                          
      IF(IPN(I).EQ.0) GO TO 666
C ATTACHMENT       
      IF(IPN(I).EQ.-1) THEN
       NETOT=NETOT+1
       NITOT=NITOT+1
       NELEC=NELEC+1
       NEGION=NEGION+1
       IPT=IARRY(I)
       ICOLL(IPT)=ICOLL(IPT)+1
       ICOLN(I)=ICOLN(I)+1 
       IT=DINT(T+1.0D0)
       IT=DMIN0(IT,J300)
       TIME(IT)=TIME(IT)+1.0D0
       GO TO 335
      ENDIF   
      EISTR=EI
      IF(IONMODEL(I).GT.0) THEN
C CALCULATE SECONDARY ENERGY,ESEC,IN IONISATION COLLISION USING
C FIVE DIFFERENT MODELS
       CALL IONSPLIT(I,E,EI,ESEC) 
       GO TO 544
      ENDIF
      R9=drand48(RDUM)
C    USE OPAL PETERSON AND BEATY SPLITTING FACTOR.
      ESEC=WPL(I)*TAN(R9*ATAN((E-EI)/(2.0D0*WPL(I)))) 
      ESEC=WPL(I)*(ESEC/WPL(I))**0.9524
  544 CONTINUE
      EI=ESEC+EI 
C STORE POSITION ,ENERGY, DIRECTION COSINES AND TIME OF GENERATION
C OF SECONDARY IONISATION ELECTRON
      NCLUS=NCLUS+1
      NMXADD=MAX(NCLUS,NMXADD)
      IF(NCLUS.GT.150000) THEN 
       WRITE(6,546) NCLUS,NREAL 
 546   FORMAT(2X,' PROGRAM STOPPED . NCLUS=',I7,' NREAL =',I10)
       STOP
      ENDIF     
      XS(NCLUS)=X       
      YS(NCLUS)=Y
      ZS(NCLUS)=Z
      TS(NCLUS)=ST
      ES(NCLUS)=ESEC        
      NFLGFC(NCLUS)=NFLGFF
      NFLGPPC(NCLUS)=NFLGPPP
      NFLGBRMC(NCLUS)=NFLGBRMM
      NTMPFLG=1
      NCLTMP=NCLUS
C RANDOMISE SECONDARY ELECTRON DIRECTION
C     R3=drand48(RDUM)
C     F3=1.0-2.0D0*R3
C     THETA0=DACOS(F3)
C     F6=DCOS(THETA0)
C     F5=DSIN(THETA0)
C     R4=drand48(RDUM)
C     PHI0=F4*R4
C     F8=DSIN(PHI0)
C     F9=DCOS(PHI0)               
C     DCX(NCLUS)=F9*F5
C     DCY(NCLUS)=F8*F5
C     DCZ(NCLUS)=F6     
C*********************************************************
      IF(IECASC.EQ.0)GO TO 333
      IF(LEGAS(I).EQ.0) GO TO 333
C USE COMPLETE CASCADE FOR ELECTRON IONISATION
      KG1=NEGAS(I)
      LG1=LEGAS(I)
      IGSHEL=IESHELL(I)
      CALL CASCADEE(J11,KG1,LG1,X,Y,Z,ST,ESEC,IGSHEL)
C
C STORE CASCADE IN CLUSTER STORE
C
      ETSUM=0.0
      DO 844 KBR=1,IEVENTE
      NCLUS=NCLUS+1
      IF(NCLUS.GT.150000) THEN
       WRITE(6,546) NCLUS,NREAL
       STOP
      ENDIF
      ES(NCLUS)=ECASE(KBR)
      ETSUM=ETSUM+ES(NCLUS)
      XS(NCLUS)=XCASE(KBR)
      YS(NCLUS)=YCASE(KBR)
      ZS(NCLUS)=ZCASE(KBR)
      TS(NCLUS)=TCASE(KBR)
      DCX(NCLUS)=DRXCE(KBR)
      DCY(NCLUS)=DRYCE(KBR)
      DCZ(NCLUS)=DRZCE(KBR)
      NFLGFC(NCLUS)=NFLGFE(KBR)+NFLGHIGH
      NFLGPPC(NCLUS)=NFLGPPE(KBR)
      NFLGBRMC(NCLUS)=NFLGBRMM
  844 CONTINUE
      IF(NFLGFC(NCLUS).GT.NFLGHIGH) NFLGHIGH=NFLGFC(NCLUS)
      GO TO 666
C*********************************************************
C STORE POSSIBLE SHELL EMISSSIONS BY AUGER OR FLUORESCENCE
  333 IF (EISTR.GT.30.0) THEN
C TEST IF FLUORESCENCE EMISSION
       IFLTST=0
       IF(WKLM(I).GT.0.0) THEN
        R9=drand48(RDUM)
        IF(R9.LT.WKLM(I)) IFLTST=1
       ENDIF
       IF(IFLTST.EQ.0) THEN
C AUGER EMISSION WITHOUT FLUORESCENCE
        NAUG=NC0(I)
        EAVAUG=EC0(I)/DFLOAT(NAUG)
        DO 700 JFL=1,NC0(I)
        NCLUS=NCLUS+1
        XS(NCLUS)=X
        YS(NCLUS)=Y
        ZS(NCLUS)=Z
        TS(NCLUS)=ST
        NFLGFC(NCLUS)=NFLGFF
        NFLGPPC(NCLUS)=NFLGPPP
        NFLGBRMC(NCLUS)=NFLGBRMM
        ES(NCLUS)=EAVAUG
        R3=drand48(RDUM)
        F3=1.0-2.0D0*R3
        THETA0=DACOS(F3)
        F6=DCOS(THETA0)
        F5=DSIN(THETA0)      
        R4=drand48(RDUM)
        PHI0=F4*R4
        F8=DSIN(PHI0)
        F9=DCOS(PHI0)
        DCX(NCLUS)=F9*F5
        DCY(NCLUS)=F8*F5
        DCZ(NCLUS)=F6
  700   CONTINUE
       ELSE
C AUGER EMISSION AND FLUORESCENCE
        IF(NG2(I).EQ.0) GO TO 702
        NAUG=NG2(I)
        EAVAUG=EG2(I)/DFLOAT(NAUG)
        DO 701 JFL=1,NG2(I)
        NCLUS=NCLUS+1
        XS(NCLUS)=X
        YS(NCLUS)=Y
        ZS(NCLUS)=Z
        NFLGFC(NCLUS)=NFLGFF
        NFLGPPC(NCLUS)=NFLGPPP
        NFLGBRMC(NCLUS)=NFLGBRMM
        TS(NCLUS)=ST
        ES(NCLUS)=EAVAUG
        R3=drand48(RDUM)
        F3=1.0-2.0D0*R3
        THETA0=DACOS(F3)
        F6=DCOS(THETA0)
        F5=DSIN(THETA0)
        R4=drand48(RDUM)
        PHI0=F4*R4
        F8=DSIN(PHI0)
        F9=DCOS(PHI0)
        DCX(NCLUS)=F9*F5
        DCY(NCLUS)=F8*F5
        DCZ(NCLUS)=F6
  701   CONTINUE
  702   IF(NG1(I).EQ.0) GO TO 704
        NAUG=NG1(I)
        EAVAUG=EG1(I)/DFLOAT(NAUG)
        R9=drand48(RDUM)
        DFL=-DLOG(R9)*DSTFL(I)
        DO 703 JFL=1,NG1(I)
        NCLUS=NCLUS+1
        R3=drand48(RDUM)
        THEFL=DACOS(1.0-2.0D0*R3)
        R4=drand48(RDUM)
        PHIFL=F4*R4
        XS(NCLUS)=X+DFL*DSIN(THEFL)*DCOS(PHIFL)
        YS(NCLUS)=Y+DFL*DSIN(THEFL)*DSIN(PHIFL)
        ZS(NCLUS)=Z+DFL*DCOS(THEFL)
        NFLGFC(NCLUS)=NFLGHIGH+1
        NFLGPPC(NCLUS)=NFLGPPP
        NFLGBRMC(NCLUS)=NFLGBRMM
        TS(NCLUS)=ST
        ES(NCLUS)=EAVAUG
        R3=drand48(RDUM)
        F3=1.0-2.0D0*R3
        THETA0=DACOS(F3)
        F6=DCOS(THETA0)
        F5=DSIN(THETA0)
        R4=drand48(RDUM)
        PHI0=F4*R4
        F8=DSIN(PHI0)
        F9=DCOS(PHI0)
        DCX(NCLUS)=F9*F5
        DCY(NCLUS)=F8*F5
        DCZ(NCLUS)=F6
        NFLGHIGH=NFLGFC(NCLUS)
  703   CONTINUE
  704   CONTINUE
       ENDIF
      ENDIF 
C                                                                       
C  GENERATE SCATTERING ANGLES AND UPDATE  LABORATORY COSINES AFTER      
C   COLLISION ALSO UPDATE ENERGY OF ELECTRON.                           
C
  666 IPT=IARRY(I)
      ICOLL(IPT)=ICOLL(IPT)+1 
      ICOLN(I)=ICOLN(I)+1   
C IF EXCITATION THEN ADD PROBABILITY,PENFRA(1,I), OF TRANSFER TO GIVE   
C IONISATION OF THE OTHER GASES IN MIXTURE 
      IF(IPEN.EQ.0.OR.NGAS.EQ.1) GO TO 5          
      IF(PENFRA(1,I).NE.0.0) THEN
       RAN=drand48(RDUM)
       IF(RAN.GT.PENFRA(1,I)) GO TO 5
       NCLUS=NCLUS+1  
C ENTER HERE POSSIBLE DELOCALISATION LENGTH FOR PENNING TRANSFER
       IF(PENFRA(2,I).EQ.0.0) THEN
        XS(NCLUS)=X      
        YS(NCLUS)=Y
        ZS(NCLUS)=Z   
        NFLGFC(NCLUS)=NFLGFF
        NFLGPPC(NCLUS)=NFLGPPP
        NFLGBRMC(NCLUS)=NFLGBRMM
        GO TO 667
       ENDIF
       ASIGN=1.0
       RAN=drand48(RDUM)
       RAN1=drand48(RDUM)
       IF(RAN1.LT.0.5) ASIGN=-ASIGN
       XS(NCLUS)=X-DLOG(RAN)*PENFRA(2,I)*ASIGN
       RAN=drand48(RDUM)
       RAN1=drand48(RDUM)
       IF(RAN1.LT.0.5) ASIGN=-ASIGN
       YS(NCLUS)=Y-DLOG(RAN)*PENFRA(2,I)*ASIGN
       RAN=drand48(RDUM)
       RAN1=drand48(RDUM)
       IF(RAN1.LT.0.5) ASIGN=-ASIGN
       ZS(NCLUS)=Z-DLOG(RAN)*PENFRA(2,I)*ASIGN
  667  RAN=drand48(RDUM)           
       TS(NCLUS)=ST-DLOG(RAN)*PENFRA(3,I) 
C ASSIGN EXCESS ENERGY OF 1EV TO PENNING CREATED ELECTRON
       ES(NCLUS)=1.0
       DCX(NCLUS)=DCX1
       DCY(NCLUS)=DCY1
       DCZ(NCLUS)=DCZ1
       GO TO 6
      ENDIF
C     GO TO 6 
C CALCULATE SUM OF EXCITATION PER CLUSTER AND STORE EXCITATION X Y Z T
   5  IF(IPN(I).EQ.0) THEN
       IF((RGAS(I)*EIN(I)).GT.4.0) THEN
        KEXC=KEXC+1
        IF(KEXC.GT.150000) THEN 
         WRITE(6,548) KEXC 
 548     FORMAT(2X,' PROGRAM STOPPED . KEXC=',I7)
         STOP
        ENDIF
C FIND GAS IN WHICH EXCITATION OCCURED AND INCREMENT COUNTER
        IF(I.LE.IDG1) THEN 
         NGEXC1=NGEXC1+1
        ELSE IF(I.LE.IDG2) THEN
         NGEXC2=NGEXC2+1
        ELSE IF(I.LE.IDG3) THEN
         NGEXC3=NGEXC3+1
        ELSE IF(I.LE.IDG4) THEN
         NGEXC4=NGEXC4+1
        ELSE IF(I.LE.IDG5) THEN
         NGEXC5=NGEXC5+1
        ELSE IF(I.LE.IDG6) THEN
         NGEXC6=NGEXC6+1
        ELSE
         WRITE(6,9911) 
 9911    FORMAT(' PROGRAM STOPPED BAD GAS ID IN MONTE')
         STOP
        ENDIF
        NEXCTOT=NEXCTOT+1
        NSTEXC=NSTEXC+1
        XSTEXC(KEXC)=X
        YSTEXC(KEXC)=Y
        ZSTEXC(KEXC)=Z
        TSTEXC(KEXC)=ST
       ENDIF
      ENDIF 
   6  S2=(S1*S1)/(S1-1.0D0) 
C ANISOTROPIC SCATTERING
      R3=drand48(RDUM)     
      IF(INDEX(I).EQ.1) THEN
       R31=drand48(RDUM)
       F3=1.0D0-R3*ANGCT(IE,I)        
       IF(R31.GT.PSCT(IE,I)) F3=-F3     
      ELSE IF (INDEX(I).EQ.2) THEN
       EPSI=PSCT(IE,I)
       F3=1.0D0-(2.0D0*R3*(1.0D0-EPSI)/(1.0D0+EPSI*(1.0D0-2.0D0*R3)))  
      ELSE     
C ISOTROPIC SCATTERING                                                 
       F3=1.0D0-2.0D0*R3  
      ENDIF
      THETA0=DACOS(F3)                                                  
      R4=drand48(RDUM)
      PHI0=F4*R4                                                        
      F8=DSIN(PHI0)                                                     
      F9=DCOS(PHI0)                                                     
      IF(E.LT.EI) EI=0.0D0                                              
      ARG1=1.0D0-S1*EI/E                                                
      ARG1=DMAX1(ARG1,SMALL)                                            
      D=1.0D0-F3*DSQRT(ARG1)                                            
      E1=E*(1.0D0-EI/(S1*E)-2.0D0*D/S2) 
      E1=DMAX1(E1,SMALL)                                                
      Q=DSQRT((E/E1)*ARG1)/S1                                           
      Q=DMIN1(Q,1.0D0)                                                  
      THETA=DASIN(Q*DSIN(THETA0))                                       
      F6=DCOS(THETA)                                                    
      U=(S1-1.0D0)*(S1-1.0D0)/ARG1                                      
      CSQD=F3*F3                                                        
      IF(F3.LT.0.0D0.AND.CSQD.GT.U) F6=-1.0D0*F6                        
      F5=DSIN(THETA)                                                    
      DCZ2=DMIN1(DCZ2,1.0D0)   
      ARGZ=DSQRT(DCX2*DCX2+DCY2*DCY2)
      IF(ARGZ.EQ.0.0D0) THEN
       DCZ1=F6         
       DCX1=F9*F5                             
       DCY1=F8*F5
       IF(NTMPFLG.EQ.1) THEN
C USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
        F5S=F5*DSQRT(E1/ES(NCLTMP))
        IF(F5S.GE.1.0) F5S=0.999
        THSEC=DASIN(F5S)
        F5S=DSIN(THSEC)
        F6S=DCOS(THSEC)
        IF(F6.LT.0.0) F6S=-F6S
        PHIS=PHI0+API   
        IF(PHIS.GT.F4) PHIS=PHI0-F4
        F8S=DSIN(PHIS)
        F9S=DCOS(PHIS)
        DCZ(NCLTMP)=F6S
        DCX(NCLTMP)=F9S*F5S
        DCY(NCLTMP)=F8S*F5S
        NTMPFLG=0
       ENDIF
       GO TO 190
      ENDIF      
      DCZ1=DCZ2*F6+ARGZ*F5*F8   
      DCY1=DCY2*F6+(F5/ARGZ)*(DCX2*F9-DCY2*DCZ2*F8)                     
      DCX1=DCX2*F6-(F5/ARGZ)*(DCY2*F9+DCX2*DCZ2*F8) 
      IF(NTMPFLG.EQ.1) THEN
C USE FREE KINEMATICS FOR IONISATION SECONDARY ANGLES
       F5S=F5*DSQRT(E1/ES(NCLTMP))
       IF(F5S.GE.1.0) F5S=0.999          
       THSEC=DASIN(F5S)
       F5S=DSIN(THSEC)
       F6S=DCOS(THSEC)
       IF(F6.LT.0.0) F6S=-F6S
       PHIS=PHI0+API   
       IF(PHIS.GT.F4) PHIS=PHI0-F4
       F8S=DSIN(PHIS)
       F9S=DCOS(PHIS)
       DCZ(NCLTMP)=DCZ2*F6S+ARGZ*F5S*F8S                               
       DCY(NCLTMP)=DCY2*F6S+(F5S/ARGZ)*(DCX2*F9S-DCY2*DCZ2*F8S)        
       DCX(NCLTMP)=DCX2*F6S-(F5S/ARGZ)*(DCY2*F9S+DCX2*DCZ2*F8S)
       NTMPFLG=0
      ENDIF 
  190 CONTINUE  
C     VTOT=CONST9*DSQRT(E1)
      GAM1=(EMS+E1)/EMS
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      VTOT=BET1*VC*1.0D-12
      CX1=DCX1*VTOT
      CY1=DCY1*VTOT
      CZ1=DCZ1*VTOT
C TEST IF ELECTRON IS THERMALISED
      IF(E1.GT.ETHRM) GO TO 1
C STORE POSITION AND TIME OF THERMALISED ELECTRON
  191 CONTINUE
      K1=K1+1
      XST(K1)=X
      YST(K1)=Y
      ZST(K1)=Z
      TST(K1)=ST
      NFGF(K1)=NFLGFF
      NFGPP(K1)=NFLGPPP
      NFGBR(K1)=NFLGBRMM
      TTIME(K1)=ST-TLAST
      NELEC=NELEC+1
      NETOT=NETOT+1
C     WRITE(6,777) XST(K1),YST(K1),ZST(K1),TST(K1),NFGF(K1),NFGPP(K1),
C    /NFGBR(K1),NELEC,NETOT,K1
C 777 FORMAT(' XST=',D12.4,' YST=',D12.4,' ZST=',D12.4,' TST=',D12.4,/,
C    /' NFGF=',I4,' NFGPP=',I4,' NFGBR=',I4,' NELEC=',I4,' NETOT=',I4,
C    /' K1=',I4)
  335 IF(K1.EQ.150000) GO TO 889
      IF(NELEC.EQ.(NCLUS+1)) THEN
C LAST ELECTRON IN CLUSTER, DO STATISTICS ON PRIMARY
       CALL STATS(J11,J1)
       GO TO 210 
      ENDIF
C GET NEW IONISATION ELECTRON FROM STORE
      X=XS(NELEC)
      Y=YS(NELEC)
      Z=ZS(NELEC)
      ST=TS(NELEC)
      NFLGFF=NFLGFC(NELEC)
      NFLGPPP=NFLGPPC(NELEC)
      NFLGBRMM=NFLGBRMC(NELEC)
      TLAST=TS(NELEC)
      E1=ES(NELEC)
      DCX1=DCX(NELEC)
      DCY1=DCY(NELEC)
      DCZ1=DCZ(NELEC) 
C     IF(NELEC.GT.94) WRITE(6,766) X,Y,Z,ST,E1,DCX1,DCY1,DCZ1,NELEC
C 766 FORMAT(' X=',D12.4,' Y=',D12.4,' Z=',D12.4,' T=',D12.4,/,' E=',
C    /D12.4,' DCX=',D12.4,' DCY=',D12.4,' DCZ=',D12.4,' NELEC=',I6,/)
C STORE ALREADY THERMALISED ELECTRONS
      IF(E1.LT.ETHRM) GO TO 191 
      GO TO 1  
C MAIN LOOP END   
  210 CONTINUE
C RESET NUMBER OF EVENTS FOR BAD EVENTS
      IF(IMIP.GT.2) NDELTA=NDELTA-IBADTOT
C
      WRITE(6,887) EMAX,NEOVFL
  887 FORMAT(' EMAX=',D12.7,' NEOVFL =',I5)
      IF(EMAX.GT.EFINAL) THEN
      WRITE(6,989) EFINAL,EMAX
  989 FORMAT('INCREASE ENERGY LIMIT FROM',D12.6,' EV TO AT LEAST',D12.6,
     /' EV.')
      STOP
      ENDIF                                         
      RETURN 
  889 NLEFT=NCLUS-NELEC
      WRITE(6,992) NPRIME,NLEFT,NCLUS
  992 FORMAT(3(/),' WARNING STOPPED AFTER NPRIME=',I6,' LAST PRIMARY HAS
     / AT LEAST ',I6,' SECONDARIES LEFT TO TRACK, OUT OF ',I6,' ELECTRON
     /S ALREADY IN CLUSTER')
      STOP
      RETURN
      END

```