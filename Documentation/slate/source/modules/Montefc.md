## MONTEFC()
* Calculates collision events and updates diffusion and velocity.
* Handles terminations at fixed drfit times.
* Solves motion in coordinate system with Magnetic field aligned to X-axis and electric field at an angle `BTHETA` in the X-Z plane
* The results for velocity vectors are then rotated into the standard coordinate frame with the electric field along the Z-axis and magnetic field at an angle `BTHETA` to the electric field in X-Z plane.

### Arguments

| Argument | Description |
|----------|-------------|
| NONE     | -           |
|          |             |

### Pseudo Code


```fortran
      SUBROUTINE MONTEFC                                                
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
C ------------------------------------------------------------------- 
C   RELATIVISTIC VERSION  
C   CALCULATES COLLISION EVENTS AND UPDATES DIFFUSION AND VELOCITY.
C   THIS ROUTINE HANDLES TERMINATIONS AT FIXED DRIFT TIMES. 
C   SOLVES MOTION IN COORDINATE SYSTEM WITH BFIELD ALIGNED TO X-AXIS
C   ELECTRIC FIELD AT AN ANGLE BTHETA IN THE X-Z PLANE.
C   THE RESULTS FOR THE VELOCITY VECTORS  ARE THEN 
C   ROTATED INTO THE STANDARD COORDINATE FRAME WITH THE ELECTRIC FIELD 
C   ALONG THE Z-AXIS AND THE BFIELD AT AN ANGLE BTHETA TO THE ELECTRIC
C   FIELD IN THE X-Z PLANE  
C -------------------------------------------------------------------
C VARYING ENERGY STEPS
      IF(EFINAL.LE.140000.) THEN
        ESTEP1=(EFINAL-16000.0)/DFLOAT(4000)
      ELSE
        ESTEP1=20.0
        ESTEP2=(EFINAL-92000.0)/DFLOAT(4000)
      ENDIF
      NPRINT=0 
      J20000=20000
      J300=300
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
C CALC ROTATION MATRIX ANGLES
      RCS=DCOS((BTHETA-90.0D0)*API/180.0D0)
      RSN=DSIN((BTHETA-90.0D0)*API/180.0D0)
C 
      RTHETA=BTHETA*API/180.0D0
      EFZ100=EFIELD*100.0D0*DSIN(RTHETA)
      EFX100=EFIELD*100.0D0*DCOS(RTHETA)
      F1=EFIELD*CONST2*DCOS(RTHETA)
      F4=2.0D0*API
      EOVBR=EOVB*DSIN(RTHETA)
      THETA1=THETA
      PHI1=PHI
C CALCULATE MAXIMUM COLLISION FREQUENCY
      TLIM=0.0
      DO 111 J=1,20000
      TEMP(J)=TCFN(J)+TCF(J) 
      IF(TLIM.LT.TEMP(J)) TLIM=TEMP(J) 
  111 CONTINUE
      NEOVFL=0
      J1=0
C START OF PRIMARY EVENT LOOP
      DO 210 J11=1,NDELTA
      J1=J1+1
      NPRIME=J1
      NGEXC1=0
      NGEXC2=0
      NGEXC3=0
      NGEXC4=0
      NGEXC5=0
      NGEXC6=0
C     INITIAL DIRECTION COSINES 
      IF(THETA1.EQ.(API/2.0).OR.NDVEC.NE.1) THEN
C  ONLY ALLOW CASE WHERE DELTA IS ALONG E-FIELD DIRECTION
       WRITE(6,22) 
   22  FORMAT(2(/),3X,'PROGRAM STOPPED ONLY ALLOWED TO HAVE DELTA ELECTR
     /ON PRALLEL TO E-FIELD IN CASE WITH ARBITRARY ANGLE FOR B-FIELD')  
       STOP
      ENDIF
C FIX DELTA TO E - FIELD DIRECTION
      PHI1=0.0D0
      THETA1=(API/2.0)-RTHETA
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
      GAM1=(EMS+E1)/EMS
      GAM12=GAM1
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      VTOT=BET1*VC*1.0D-12
C     VTOT=CONST9*DSQRT(E1)
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
C READIN FIRST ELECTRON FROM BETA DECAY OR X-RAY UNTHERMALISED CLUSTERS
       CALL CASRES(J11,IBADTOT,IBAD1)
C  SKIP BAD EVENT
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
      VTOT=BET1*VC*1.0D-12
C     VTOT=CONST9*DSQRT(E1)
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
      IF(NFLGFC(IST).GT.NFLGHIGH) NFLGHIGH=NFLGFC(IST)
   35 CONTINUE
      GAM12=GAM1
C START OF LOOP FOR NEW ELECTRONS                                       
    1 CONTINUE 
      R1=drand48(RDUM)
      T=-DLOG(R1)/TLIM+TDASH
      TDASH=T
      WBT=WB*T/GAM12
C     WBT=WB*T
      COSWT=DCOS(WBT)
      SINWT=DSIN(WBT)
      DZ=GAM12*(CZ1*SINWT+(EOVBR-CY1)*(1.0D0-COSWT))/WB
C     DZ=(CZ1*SINWT+(EOVBR-CY1)*(1.0D0-COSWT))/WB
      DX=CX1*T+F1*T*T/GAM12
C     DX=CX1*T+F1*T*T
      E=E1+DZ*EFZ100+DX*EFX100
      GAM2=(EMS+E)/EMS
      BET2=DSQRT(1.0D0-1.0D0/(GAM2+GAM2))
      IF(E.LT.0.0D0) THEN
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
       IF(CFN(IE,I).LT.R2) GOTO 888
C INCREMENT NULL LEVEL SUM
       NEXCNUL=NEXCNUL+1
       ICOLNN(I)=ICOLNN(I)+1
C STORE X Y Z T ID FOR MOLECULAR LIGHT EMISSION AND DISSOCIATION FROM 
C   NULL EXCITATION
C NOTE: SMALL APPROX USED POSITION OF PREVIOUS REAL COLLISION
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
      IF(E.GT.EMAX) EMAX=E
      IF(T.GT.TMAX1) TMAX1=T
      TDASH=0.0D0
      NREAL=NREAL+1  
C CALC VELOCITY
C     CX2=CX1+2.0*F1*T        
      CX2=CX1+2.0*F1*T/GAM12
      CY2=(CY1-EOVBR)*COSWT+CZ1*SINWT+EOVBR
      CZ2=CZ1*COSWT-(CY1-EOVBR)*SINWT
C CALC DIRECTION COSINES
      VTOT=DSQRT(CX2*CX2+CY2*CY2+CZ2*CZ2)
      DCX2=CX2/VTOT
      DCY2=CY2/VTOT
      DCZ2=CZ2/VTOT                                                     
C CALC NEW POSITION                                                
      X=X+DX                                                            
      Y=Y+EOVBR*T+GAM12*((CY1-EOVBR)*SINWT+CZ1*(1.0D0-COSWT))/WB
C     Y=Y+EOVBR*T+((CY1-EOVBR)*SINWT+CZ1*(1.0D0-COSWT))/WB
      Z=Z+DZ          
      GAM12=(GAM1+GAM2)/2.0D0
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
 546   FORMAT(2X,' PROGRAM STOPPED . NCLUS=',I7,' NREAL=',I10)
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
C STORE POSSIBLE SHELL EMISSIONS AUGER OR FLUORESCENCE 
  333 IF(EISTR.GT.30.0) THEN
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
C AUGER EMISSION AND FLUORESENCE 
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
C IF EXCITATION THEN ADD PROBABILITY ,PENFRA(1,I), OF TRANSFER TO GIVE 
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
C  ANISOTROPIC SCATTERING 
      R3=drand48(RDUM)
      IF(INDEX(I).EQ.1) THEN
       R31=drand48(RDUM)
       F3=1.0D0-R3*ANGCT(IE,I)       
       IF(R31.GT.PSCT(IE,I)) F3=-F3   
      ELSE IF(INDEX(I).EQ.2) THEN
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
        IF(F5S.GT.1.0) F5S=1.0
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
       IF(F5S.GT.1.0) F5S=1.0            
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
      GAM1=(EMS+E1)/EMS
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      VTOT=BET1*VC*1.D-12
C     VTOT=CONST9*DSQRT(E1)
      CX1=DCX1*VTOT
      CY1=DCY1*VTOT
      CZ1=DCZ1*VTOT
C TEST IF ELECTRON IS THERMALISED
      IF(E1.GT.ETHRM) GO TO 1
  191 CONTINUE
C STORE POSITION AND TIME OF THERMALISED ELECTRONS
      K1=K1+1
C ROTATE INTO COORDINATE SYSTEM WITH EFIELD ALONG Z
      ZR=Z*RCS-X*RSN
      YR=Y
      XR=Z*RSN+X*RCS          
      XST(K1)=XR
      YST(K1)=YR
      ZST(K1)=ZR
      TST(K1)=ST
      NFGF(K1)=NFLGFF
      NFGPP(K1)=NFLGPPP
      NFGBR(K1)=NFLGBRMM
      TTIME(K1)=ST-TLAST
      NELEC=NELEC+1
      NETOT=NETOT+1
  335 IF(K1.EQ.150000) GO TO 889
      IF(NELEC.EQ.(NCLUS+1)) THEN
C LAST ELECTRON IN CLUSTER. DO STATISTICS ON CLUSTER
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
      IF(E1.LT.ETHRM) GO TO 191
      GAM1=(EMS+E1)/EMS
      BET1=DSQRT(1.0D0-1.0D0/(GAM1*GAM1))
      VTOT=BET1*VC*1.D-12
      CX1=DCX1*VTOT
      CY1=DCY1*VTOT
      CZ1=DCZ1*VTOT
      GO TO 1  
C MAIN LOOP END
  210 CONTINUE
C RESET NUMBER OF EVENTS FOR BAD EVENTS
      IF(IMIP.GT.2) NDELTA=NDELTA-IBADTOT
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
     / AT LEAST ',I6,' SECONDARIES LEFT TO TRACK. OUT OF ',I6,' ELECTRON
     /S ALREADY IN CLUSTER')
      STOP
      RETURN
      END                                                  

```

