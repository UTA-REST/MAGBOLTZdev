---
title: Degrad Documentation

language_tabs: # must be one of https://git.io/vQNgJ
  - shell
  - fortran
  - python
  - javascript

toc_footers:
  - <a href='#'>Sign Up for a Developer Key</a>
  - <a href='https://github.com/lord/slate'>Documentation Powered by Slate</a>

includes:
  - errors

search: true
---

# Introduction

Welcome to Degrad! This program can be used to give cluster size distribution and primary cluster distribution in gas mixtures for ionising particles. The spatial distribution of the thermalised electron is given and plotted as a cumulated sum. The individual events can also be output using control word, IWRITE, so that a more detailed analysis can be performed with other detector simulation programs.

Ionising particle clusters are created with a start position of the primart electron in X Y and Z of (0,0,0). It is easy to transform and pace the generated clusters on a track with the calculated primary cluster spacing along the track given by a poisson distribution.

There is at the moment no facility to allow the density effect, which may change the cluster size at energies above minimum ionising. However, the  density effect is expected to be small above minimum ionising. The dE/dX is also calculated for the ionising particle energy.

We have language bindings in Shell, Fortran, and Python! You can view code in the dark area to the right, and you can switch the programming language of the examples with the tabs in the top right.

This documentation page was created with [Slate](https://github.com/lord/slate). 

# Using

Degrad is written in python3 and FORTRAN

> To run Degrad, use this code:

```shell
# to run fortran code
gfortran degrad3.3.f 
./a.out

# to run python
python3 degrad1.py 

# With shell, you can just run the input interface if you have python3 and qt5 installed on your machine
cd UI/
python3 MAIN.py
```


> Make sure you're in the same directory as the file you're executing.

The input interface for degrad UI has been written in pyqt-5. main.ui contains the ui structure of the interface, created in the qt-designer. 
Kittn uses API keys to allow access to the API. You can register a new Kittn API key at our [developer portal](http://example.com/developers).

Kittn expects for the API key to be included in all API requests to the server in a header that looks like the following:


<aside class="notice">
Make sure you're in the same directory as the file you're executing.
</aside>

# Function Documentation

## DEGRADE()

```fortran
      PROGRAM DEGRADE                                                   
      IMPLICIT REAL*8 (A-H,O-Z)
      IMPLICIT INTEGER*8 (I-N)
      COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,
     /RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE
      COMMON/BFLD/EOVB,WB,BTHETA,BMAG
 1    CALL SETUP(LAST)                                                  
      IF(LAST.EQ.1) GO TO 99
      CALL DENSITY
      CALL CASCDAT
      CALL MIXERC
      CALL MIXER
C CALCULATE FLUORESCENCE ABSORPTION DISTANCES 
      CALL FLDIST
      CALL PRINTER
      IF(IMIP.EQ.1) CALL MIPCALC
C IF MIP OR ELECTRON BEAM SKIP DIRECT CASCADE CALCULATION
      IF(IMIP.LE.2) GO TO 10
      ICON=IMIP-2
C  ICON=1 XRAY,   ICON=2 BETA DECAY , ICON=3 DOUBLE BETA DECAY  
      CALL CONTROL0(NEVENT,ESTART,ICON)
C CALCULATE AND OUTPUT AVERAGES FROM SHELLS
      CALL OUTPUTC(NEVENT,IMIP)
C AFTER ALL SHELL EMISSIONS THERMALISE ELECTRONS
  10  IF(BMAG.EQ.0.0D0) CALL MONTEFE
      IF(BMAG.NE.0.0D0) THEN
       IF(BTHETA.EQ.0.0D0.OR.BTHETA.EQ.180.0D0) THEN
        CALL MONTEFA
        ELSE IF(BTHETA.EQ.90.0D0) THEN
        CALL MONTEFB
        ELSE
        CALL MONTEFC
       ENDIF
      ENDIF
      CALL STATS2
      CALL OUTPUT 
      GO TO 1
  99  STOP                                                             
      END
```

```python
def DEGRADE():
  # IMPLICIT #real*8 (A-H,O-Z)
  # IMPLICIT #integer*8 (I-N)
  global TMAX,SMALL,API,ESTART,THETA,PHI
  global TCFMAX #array size 10
  global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE,EOVB,WB,BTHETA,BMAG
  SETUP(LAST)
  if(LAST == 1):
    sys.exit()
  DENSITY()
  CASCDAT()
  MIXERC()
  MIXER()
  # CALCULATE FLUORESCENCE ABSORPTION DISTANCES 
  FLDIST()
  PRINTER()
  if(IMIP == 1):
    MIPCALC()
  # if MIP OR ELECTRON BEAM SKIP DIRECT CASCADE CALCULATION
  if(IMIP <= 2):
    PASSING 
  else:
    ICON=IMIP-2
    #  ICON=1 XRAY,   ICON=2 BETA DECAY , ICON=3 DOUBLE BETA DECAY  
    CONTROL0(NEVENT,ESTART,ICON)
    # CALCULATE AND OUTPUT AVERAGES FROM SHELLS
    OUTPUTC(NEVENT,IMIP)
    # AFTER ALL SHELL EMISSIONS THERMALISE ELECTRONS
  if(BMAG == 0.00):
    MONTEFE()
  if(BMAG != 0.00):
    if(BTHETA == 0.00 or BTHETA == 180.00):
      MONTEFA()
    else if(BTHETA == 90.00) :
      MONTEFB()
    else:
      MONTEFC()
    # endif
  # endif
  STATS2()
  OUTPUT()
  DEGRADE()
  sys.exit()
  # end
```

This is the main function which calls all the subroutines.

### Arguments

Argument | Description
--------- | -----------
no arguments | 

## MIXER()
* The function fills arrays of collision frequency
* Store counting ionisation X-Section in array CMINIXSC[6] at minimum ionising energy
* Initialisations 
* Calculate and store energy grid(X-Ray,Beta or Particles)
* If EFINAL <=20000
* If EFINAL in range(20000,140000)
* Else

```fortran
        SUBROUTINE MIXER                                                  
        IMPLICIT REAL*8 (A-H,O-Z)
        IMPLICIT INTEGER*8 (I-N)                                         
        CHARACTER*25 NAMEG,NAME1,NAME2,NAME3,NAME4,NAME5,NAME6
        COMMON/RATIO/AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC(6)              
        CHARACTER*50 DSCRPT,SCRP1(300),SCRP2(300),SCRP3(300),SCRP4(300),
       /SCRP5(300),SCRP6(300)   
        CHARACTER*50 DSCRPTN,SCRPN1(10),SCRPN2(10),SCRPN3(10),SCRPN4(10),
       /SCRPN5(10),SCRPN6(10)                          
        COMMON/GASN/NGASN(6) 
        COMMON/MIX1/QELM(20000),QSUM(20000),QION(6,20000),QIN1(250,20000),
       /QIN2(250,20000),QIN3(250,20000),QIN4(250,20000),QIN5(250,20000),
       /QIN6(250,20000),QSATT(20000)             
        COMMON/MIX2/E(20000),EROOT(20000),QTOT(20000),QREL(20000),
       /QINEL(20000),QEL(20000)
        COMMON/MIX3/NIN1,NIN2,NIN3,NIN4,NIN5,NIN6,LION(6),LIN1(250),
       /LIN2(250),LIN3(250),LIN4(250),LIN5(250),LIN6(250),ALION(6),
       /ALIN1(250),ALIN2(250),ALIN3(250),ALIN4(250),ALIN5(250),ALIN6(250)
        COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
        COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
        COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,
       /RSTART,EFIELD,ETHRM,ECUT,NDELTA,IMIP,IWRITE                    
        COMMON/LARGE/CF(20000,512),EIN(512),TCF(20000),IARRY(512),
       /RGAS(512),IPN(512),WPL(512),IZBR(512),IPLAST,PENFRA(3,512)  
        COMMON/LARGEN/CFN(20000,60),TCFN(20000),SCLENUL(60),NPLAST    
        COMMON/ANIS/PSCT(20000,512),ANGCT(20000,512),INDEX(512),NISO
        COMMON/FRED/FCION(20000),FCATT(20000)
        COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC            
        COMMON/MRATIO/VAN1,VAN2,VAN3,VAN4,VAN5,VAN6,VAN
        COMMON/IONC/DOUBLE(6,20000),CMINIXSC(6),CMINEXSC(6),ECLOSS(6),
       /WPLN(6),ICOUNT,AVPFRAC(3,6)
        COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),EG2(512)
       /,WKLM(512),EFL(512)
        COMMON/COMP/LCMP,LCFLG,LRAY,LRFLG,LPAP,LPFLG,LBRM,LBFLG,LPEFLG
        COMMON/NAMES/NAMEG(6)
        COMMON/IDEXC/NGEXC1,NGEXC2,NGEXC3,NGEXC4,NGEXC5,NGEXC6,IDG1,IDG2,
       /IDG3,IDG4,IDG5,IDG6      
        COMMON/SCRIP/DSCRPT(512),DSCRPTN(60)
        COMMON/IONMOD/ESPLIT(512,20),IONMODEL(512)
        COMMON/RLTVY/BET(20000),GAM(20000),VC,EMS                        
        DIMENSION Q1(6,20000),Q2(6,20000),Q3(6,20000),Q4(6,20000),
       /Q5(6,20000),Q6(6,20000)
        DIMENSION E1(6),E2(6),E3(6),E4(6),E5(6),E6(6),EI1(250),EI2(250),
       /EI3(250),EI4(250),EI5(250),EI6(250)
        DIMENSION QATT(6,20000),EION(6)         
        DIMENSION PEQEL1(6,20000),PEQEL2(6,20000),PEQEL3(6,20000),
       /PEQEL4(6,20000),PEQEL5(6,20000),PEQEL6(6,20000)
        DIMENSION PEQIN1(250,20000),PEQIN2(250,20000),PEQIN3(250,20000),  
       /PEQIN4(250,20000),PEQIN5(250,20000),PEQIN6(250,20000)
        DIMENSION PENFRA1(3,250),PENFRA2(3,250),PENFRA3(3,250),
       /PENFRA4(3,250),PENFRA5(3,250),PENFRA6(3,250)
        DIMENSION KIN1(250),KIN2(250),KIN3(250),KIN4(250),KIN5(250),
       /KIN6(250)
        DIMENSION KEL1(6),KEL2(6),KEL3(6),KEL4(6),KEL5(6),KEL6(6)
        DIMENSION EION1(30),EION2(30),EION3(30),EION4(30),EION5(30),
       /EION6(30)
        DIMENSION QION1(30,20000),QION2(30,20000),QION3(30,20000),
       /QION4(30,20000),QION5(30,20000),QION6(30,20000)
        DIMENSION PEQION1(30,20000),PEQION2(30,20000),PEQION3(30,20000),
       /PEQION4(30,20000),PEQION5(30,20000),PEQION6(30,20000)
        DIMENSION LEGAS1(30),LEGAS2(30),LEGAS3(30),LEGAS4(30),LEGAS5(30),
       /LEGAS6(30)
        DIMENSION IESHEL1(30),IESHEL2(30),IESHEL3(30),IESHEL4(30),
       /IESHEL5(30),IESHEL6(30) 
        DIMENSION EB1(30),EB2(30),EB3(30),EB4(30),EB5(30),EB6(30)
        DIMENSION NC01(30),NC02(30),NC03(30),NC04(30),NC05(30),NC06(30)
        DIMENSION EC01(30),EC02(30),EC03(30),EC04(30),EC05(30),EC06(30)
        DIMENSION NG11(30),NG12(30),NG13(30),NG14(30),NG15(30),NG16(30)
        DIMENSION EG11(30),EG12(30),EG13(30),EG14(30),EG15(30),EG16(30)
        DIMENSION NG21(30),NG22(30),NG23(30),NG24(30),NG25(30),NG26(30)
        DIMENSION EG21(30),EG22(30),EG23(30),EG24(30),EG25(30),EG26(30)
        DIMENSION WK1(30),WK2(30),WK3(30),WK4(30),WK5(30),WK6(30)
        DIMENSION EFL1(30),EFL2(30),EFL3(30),EFL4(30),EFL5(30),EFL6(30)
        DIMENSION IZBR1(250),IZBR2(250),IZBR3(250),IZBR4(250),IZBR5(250),
       /IZBR6(250)
        DIMENSION QATT1(8,20000),QATT2(8,20000),QATT3(8,20000),
       /QATT4(8,20000),QATT5(8,20000),QATT6(8,20000) 
        DIMENSION QNUL1(10,20000),QNUL2(10,20000),QNUL3(10,20000),
       /QNUL4(10,20000),QNUL5(10,20000),QNUL6(10,20000),SCLN1(10),
       /SCLN2(10),SCLN3(10),SCLN4(10),SCLN5(10),SCLN6(10)  
        DIMENSION ESPLIT1(5,20),ESPLIT2(5,20),ESPLIT3(5,20),ESPLIT4(5,20),
       /ESPLIT5(5,20),ESPLIT6(5,20)
  C                                                                       
  C  ---------------------------------------------------------------------
  C                                                                       
  C     SUBROUTINE MIXER FILLS ARRAYS OF COLLISION FREQUENCY              
  C     CAN HAVE A MIXTURE OF UP TO 6 GASES                               
  C                                                                       
  C     MOD: STORE COUNTING IONISATION X-SECTION IN ARRAY CMINIXSC(6)
  C          AT MINIMUM IONISING ENERGY                                 
  C  ---------------------------------------------------------------------
  C                                                             
        NISO=0
        NIN1=0                                                            
        NIN2=0                                                            
        NIN3=0                                                            
        NIN4=0
        NIN5=0
        NIN6=0
        NION1=0
        NION2=0
        NION3=0
        NION4=0
        NION5=0
        NION6=0
        NATT1=0
        NATT2=0
        NATT3=0
        NATT4=0
        NATT5=0
        NATT6=0
        NUL1=0
        NUL2=0
        NUL3=0
        NUL4=0
        NUL5=0
        NUL6=0
        DO 2 J=1,6  
        NAMEG(J)='-------------------------'                              
        KEL1(J)=0
        KEL2(J)=0
        KEL3(J)=0
        KEL4(J)=0
        KEL5(J)=0
        KEL6(J)=0                       
        DO 1 I=1,20000                                                    
        Q1(J,I)=0.0D0                                                     
        Q2(J,I)=0.0D0                                                     
        Q3(J,I)=0.0D0                                                     
        Q4(J,I)=0.0D0
        Q5(J,I)=0.0D0
        Q6(J,I)=0.0D0
        DOUBLE(J,I)=0.0D0    
      1 CONTINUE                                                          
        E1(J)=0.0D0                                                       
        E2(J)=0.0D0                                                       
        E3(J)=0.0D0                                                       
        E4(J)=0.0D0 
        E5(J)=0.0D0
      2 E6(J)=0.0D0
        DO 222 J=1,30
        IESHEL1(J)=0
        IESHEL2(J)=0
        IESHEL3(J)=0
        IESHEL4(J)=0
        IESHEL5(J)=0
        IESHEL6(J)=0
        LEGAS1(J)=0
        LEGAS2(J)=0
        LEGAS3(J)=0
        LEGAS4(J)=0
        LEGAS5(J)=0
        LEGAS6(J)=0
        EION1(J)=0.0D0
        EION2(J)=0.0D0
        EION3(J)=0.0D0
        EION4(J)=0.0D0
        EION5(J)=0.0D0
        EION6(J)=0.0D0
        EB1(J)=0.0D0
        EB2(J)=0.0D0
        EB3(J)=0.0D0
        EB4(J)=0.0D0
        EB5(J)=0.0D0
        EB6(J)=0.0D0
        EC01(J)=0.0D0
        EC02(J)=0.0D0
        EC03(J)=0.0D0
        EC04(J)=0.0D0
        EC05(J)=0.0D0
        EC06(J)=0.0D0
        EG11(J)=0.0D0
        EG12(J)=0.0D0
        EG13(J)=0.0D0
        EG14(J)=0.0D0
        EG15(J)=0.0D0
        EG16(J)=0.0D0
        EG21(J)=0.0D0
        EG22(J)=0.0D0
        EG23(J)=0.0D0
        EG24(J)=0.0D0
        EG25(J)=0.0D0
        EG26(J)=0.0D0
        WK1(J)=0.0D0
        WK2(J)=0.0D0
        WK3(J)=0.0D0
        WK4(J)=0.0D0
        WK5(J)=0.0D0
        WK6(J)=0.0D0
        EFL1(J)=0.0D0
        EFL2(J)=0.0D0
        EFL3(J)=0.0D0
        EFL4(J)=0.0D0
        EFL5(J)=0.0D0
        EFL6(J)=0.0D0
        NC01(J)=0
        NC02(J)=0
        NC03(J)=0
        NC04(J)=0
        NC05(J)=0
        NC06(J)=0
        NG11(J)=0
        NG12(J)=0
        NG13(J)=0
        NG14(J)=0
        NG15(J)=0
        NG16(J)=0
        NG21(J)=0
        NG22(J)=0
        NG23(J)=0
        NG24(J)=0
        NG25(J)=0
        NG26(J)=0
        DO 222 I=1,20000
        QION1(J,I)=0.0D0
        QION2(J,I)=0.0D0
        QION3(J,I)=0.0D0
        QION4(J,I)=0.0D0
        QION5(J,I)=0.0D0
        QION6(J,I)=0.0D0
    222 CONTINUE
        DO 223 K=1,8
        DO 223 I=1,20000
        QATT1(K,I)=0.0
        QATT2(K,I)=0.0
        QATT3(K,I)=0.0
        QATT4(K,I)=0.0
        QATT5(K,I)=0.0
        QATT6(K,I)=0.0
    223 CONTINUE
        DO 224 K=1,10
        DO 224 I=1,20000
        QNUL1(K,I)=0.0
        QNUL2(K,I)=0.0
        QNUL3(K,I)=0.0
        QNUL4(K,I)=0.0
        QNUL5(K,I)=0.0
        QNUL6(K,I)=0.0
    224 CONTINUE 
        DO 225 I=1,512
        IONMODEL(I)=0
        DO 225 K=1,20
        ESPLIT(I,K)=0.0
    225 CONTINUE   
  C CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
        IF(EFINAL.LE.20000.0) THEN
         ESTEP=EFINAL/DFLOAT(NSTEP)
         EHALF=ESTEP/2.0D0
         E(1)=EHALF
         GAM(1)=(EMS+E(1))/EMS
         BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
         DO 3 I=2,20000
         AJ=DFLOAT(I-1)
         E(I)=EHALF+ESTEP*AJ
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
      3  EROOT(I)=DSQRT(E(I))
         EROOT(1)=DSQRT(EHALF)     
        ELSE IF(EFINAL.GT.20000.0.AND.EFINAL.LE.140000.) THEN
         ESTEP=1.0
         EHALF=0.5
         E(1)=EHALF
         GAM(1)=(EMS+E(1))/EMS
         BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
         DO 31 I=2,16000
         AJ=DFLOAT(I-1)
         E(I)=EHALF+ESTEP*AJ
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
     31  EROOT(I)=DSQRT(E(I))
         EROOT(1)=DSQRT(EHALF)
         ESTEP1=(EFINAL-16000.0)/DFLOAT(4000)
         DO 32 I=16001,20000
         AJ=DFLOAT(I-16000)
         E(I)=16000.0+AJ*ESTEP1
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
     32  EROOT(I)=DSQRT(E(I))
        ELSE
         ESTEP=1.0
         EHALF=0.5
         E(1)=EHALF
         GAM(1)=(EMS+E(1))/EMS
         BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
         DO 33 I=2,12000
         AJ=DFLOAT(I-1)
         E(I)=EHALF+ESTEP*AJ
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
     33  EROOT(I)=DSQRT(E(I))
         EROOT(1)=DSQRT(EHALF)
         ESTEP1=20.0
         DO 34 I=12001,16000
         AJ=DFLOAT(I-12000)
         E(I)=12000.0+AJ*ESTEP1
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
     34  EROOT(I)=DSQRT(E(I))
         ESTEP2=(EFINAL-92000.0)/DFLOAT(4000)
         DO 35 I=16001,20000
         AJ=DFLOAT(I-16000)
         E(I)=92000.0+AJ*ESTEP2
         GAM(I)=(EMS+E(I))/EMS
         BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
     35  EROOT(I)=DSQRT(E(I))
        ENDIF
  C
        DO 4 I=1,250
        IZBR1(I)=0
        IZBR2(I)=0
        IZBR3(I)=0
        IZBR4(I)=0
        IZBR5(I)=0
        IZBR6(I)=0
        KIN1(I)=0
        KIN2(I)=0
        KIN3(I)=0
        KIN4(I)=0
        KIN5(I)=0
      4 KIN6(I)=0
        DO 6 I=1,512 
      6 INDEX(I)=0                                               
  C                                                                       
  C   CALL GAS CROSS-SECTIONS 
        CALL GASMIX(NGASN(1),Q1,QIN1,NIN1,E1,EI1,NAME1,VIRIAL1,EB1,
       /PEQEL1,PEQIN1,PENFRA1,KEL1,KIN1,QION1,PEQION1,EION1,NION1,QATT1,
       /NATT1,QNUL1,NUL1,SCLN1,NC01,EC01,WK1,EFL1,NG11,EG11,NG21,EG21,
       /IZBR1,LEGAS1,IESHEL1,IONMODL1,ESPLIT1,SCRP1,SCRPN1) 
        IF(NGAS.EQ.1) GO TO 10 
        CALL GASMIX(NGASN(2),Q2,QIN2,NIN2,E2,EI2,NAME2,VIRIAL2,EB2,
       /PEQEL2,PEQIN2,PENFRA2,KEL2,KIN2,QION2,PEQION2,EION2,NION2,QATT2,
       /NATT2,QNUL2,NUL2,SCLN2,NC02,EC02,WK2,EFL2,NG12,EG12,NG22,EG22,
       /IZBR2,LEGAS2,IESHEL2,IONMODL2,ESPLIT2,SCRP2,SCRPN2) 
        IF(NGAS.EQ.2) GO TO 10 
        CALL GASMIX(NGASN(3),Q3,QIN3,NIN3,E3,EI3,NAME3,VIRIAL3,EB3,
       /PEQEL3,PEQIN3,PENFRA3,KEL3,KIN3,QION3,PEQION3,EION3,NION3,QATT3,
       /NATT3,QNUL3,NUL3,SCLN3,NC03,EC03,WK3,EFL3,NG13,EG13,NG23,EG23,
       /IZBR3,LEGAS3,IESHEL3,IONMODL3,ESPLIT3,SCRP3,SCRPN3) 
        IF(NGAS.EQ.3) GO TO 10 
        CALL GASMIX(NGASN(4),Q4,QIN4,NIN4,E4,EI4,NAME4,VIRIAL4,EB4,
       /PEQEL4,PEQIN4,PENFRA4,KEL4,KIN4,QION4,PEQION4,EION4,NION4,QATT4,
       /NATT4,QNUL4,NUL4,SCLN4,NC04,EC04,WK4,EFL4,NG14,EG14,NG24,EG24,
       /IZBR4,LEGAS4,IESHEL4,IONMODL4,ESPLIT4,SCRP4,SCRPN4)
        IF(NGAS.EQ.4) GO TO 10 
        CALL GASMIX(NGASN(5),Q5,QIN5,NIN5,E5,EI5,NAME5,VIRIAL5,EB5,
       /PEQEL5,PEQIN5,PENFRA5,KEL5,KIN5,QION5,PEQION5,EION5,NION5,QATT5,
       /NATT5,QNUL5,NUL5,SCLN5,NC05,EC05,WK5,EFL5,NG15,EG15,NG25,EG25,
       /IZBR5,LEGAS5,IESHEL5,IONMODL5,ESPLIT5,SCRP5,SCRPN5)
        IF(NGAS.EQ.5) GO TO 10 
        CALL GASMIX(NGASN(6),Q6,QIN6,NIN6,E6,EI6,NAME6,VIRIAL6,EB6,
       /PEQEL6,PEQIN6,PENFRA6,KEL6,KIN6,QION6,PEQION6,EION6,NION6,QATT6,
       /NATT6,QNUL6,NUL6,SCLN6,NC06,EC06,WK6,EFL6,NG16,EG16,NG26,EG26,
       /IZBR6,LEGAS6,IESHEL6,IONMODL6,ESPLIT6,SCRP6,SCRPN6) 
     10 CONTINUE                                                          
  C ---------------------------------------------------------------       
  C  CORRECTION OF NUMBER DENSITY DUE TO VIRIAL COEFFICIENT               
  C  CAN BE PROGRAMMED HERE NOT YET IMPLEMENTED.                          
  C-----------------------------------------------------------------      
  C-----------------------------------------------------------------      
  C     CALCULATION OF COLLISION FREQUENCIES FOR AN ARRAY OF              
  C     ELECTRON ENERGIES IN THE RANGE ZERO TO EFINAL        
  C                                                                     
  C     L=5*N-4    ELASTIC NTH GAS                                        
  C     L=5*N-3    IONISATION NTH GAS                               
  C     L=5*N-2    ATTACHMENT NTH GAS                                  
  C     L=5*N-1    INELASTIC NTH GAS    
  C     L=5*N      SUPERELASTIC NTH GAS                    
  C---------------------------------------------------------------   
        DO 700 IE=1,20000  
        FCION(IE)=0.0D0
        FCATT(IE)=0.0D0
  C
        NP=1 
        IDG1=1
        NEGAS(NP)=1  
        LEGAS(NP)=0
        IESHELL(NP)=0                                               
        CF(IE,NP)=Q1(2,IE)*VAN1*BET(IE)
        PSCT(IE,NP)=0.5D0
        ANGCT(IE,NP)=1.0D0    
        INDEX(NP)=0 
  C   ELASTIC ANG  
        IF(KEL1(2).EQ.1) THEN
         PSCT1=PEQEL1(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2  
         INDEX(NP)=1   
        ENDIF 
        IF(KEL1(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL1(2,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 12                                   
        RGAS1=1.0D0+E1(2)/2.0D0                                           
        RGAS(NP)=RGAS1                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0 
        L=1                                                      
        IARRY(NP)=L 
        IZBR(NP)=0
        DSCRPT(NP)=SCRP1(2)  
        NAMEG(1)=NAME1
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,1)=0.0
        AVPFRAC(2,1)=0.0
        AVPFRAC(3,1)=0.0
        CMINEXSC(1)=E1(4)*AN1                                        
        CMINIXSC(1)=E1(5)*AN1
        ECLOSS(1)=E1(3)
        WPLN(1)=E1(6)
     12 IF(EFINAL.LT.E1(3)) GO TO 30
        IF(NION1.GT.1) GO TO 20  
        NP=NP+1
        IDG1=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q1(5,IE)*VAN1*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(1,IE)=Q1(3,IE)/Q1(5,IE)-1.0D0
        ELSE                                    
         CF(IE,NP)=Q1(3,IE)*VAN1*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=1 
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C 
        IF(ICOUNT.EQ.1) THEN
         IF(KEL1(5).EQ.1) THEN
          PSCT1=PEQEL1(5,IE) 
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL1(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL1(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL1(3).EQ.1) THEN
          PSCT1=PEQEL1(3,IE) 
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL1(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL1(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C
        WPL(NP)=EB1(1)
        NC0(NP)=NC01(1)
        EC0(NP)=EC01(1)
        NG1(NP)=NG11(1)
        EG1(NP)=EG11(1)
        NG2(NP)=NG21(1)
        EG2(NP)=EG21(1)
        WKLM(NP)=WK1(1)
        EFL(NP)=EFL1(1)
        IF(IE.GT.1) GO TO 30                                     
        RGAS(NP)=RGAS1                                                    
        EIN(NP)=E1(3)/RGAS1
        IPN(NP)=1 
        L=2                                                      
        IARRY(NP)=L 
        IZBR(NP)=0
        DSCRPT(NP)=SCRP1(3) 
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        IONMODEL(NP)=IONMODL1
        DO 19 K=1,20
     19 ESPLIT(NP,K)=ESPLIT1(IONMODL1,K) 
        GO TO 30
     20 DO 25 KION=1,NION1
        NP=NP+1
        IDG1=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        CF(IE,NP)=QION1(KION,IE)*VAN1*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5D0
        ANGCT(IE,NP)=1.0D0
        INDEX(NP)=0 
        NEGAS(NP)=1
        LEGAS(NP)=LEGAS1(KION)
        IESHELL(NP)=IESHEL1(KION)
  C                           
        IF(KEL1(3).EQ.1) THEN
         PSCT1=PEQION1(KION,IE) 
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL1(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION1(KION,IE)
         INDEX(NP)=2
        ENDIF
  C
        WPL(NP)=EB1(KION)
        NC0(NP)=NC01(KION)
        EC0(NP)=EC01(KION)
        NG1(NP)=NG11(KION)
        EG1(NP)=EG11(KION)
        NG2(NP)=NG21(KION)
        EG2(NP)=EG21(KION)
        WKLM(NP)=WK1(KION)
        EFL(NP)=EFL1(KION)
        IF(IE.GT.1) GO TO 25                                     
        RGAS(NP)=RGAS1                                                    
        EIN(NP)=EION1(KION)/RGAS1
  C 
        IPN(NP)=1 
        L=2                                                      
        IARRY(NP)=L 
        IZBR(NP)=0
        DSCRPT(NP)=SCRP1(2+KION) 
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        IONMODEL(NP)=IONMODL1
        DO 24 K=1,20
     24 ESPLIT(NP,K)=ESPLIT1(IONMODL1,K) 
     25 CONTINUE   
     30 IF(EFINAL.LT.E1(4)) GO TO 40   
        IF(NATT1.GT.1) GO TO 551                                   
        NP=NP+1
        IDG1=NP                                                           
        CF(IE,NP)=Q1(4,IE)*VAN1*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP) 
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 40
        NEGAS(NP)=1
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0                                     
        RGAS(NP)=RGAS1                                                   
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1              
        L=3                                           
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP1(3+NION1)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0 
        GO TO 40
    551 DO 552 JJ=1,NATT1 
        NP=NP+1
        IDG1=NP
        CF(IE,NP)=QATT1(JJ,IE)*VAN1*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 552
        NEGAS(NP)=1
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS1
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=3
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP1(2+NION1+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
    552 CONTINUE
     40 IF(NIN1.EQ.0) GO TO 60                                           
        DO 50 J=1,NIN1
        NP=NP+1
        IDG1=NP      
        NEGAS(NP)=1
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=QIN1(J,IE)*VAN1*BET(IE)
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR1(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KIN1(J).EQ.1) THEN   
         PSCT1=PEQIN1(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1   
        ENDIF
        IF(KIN1(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN1(J,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 50                                     
        RGAS(NP)=RGAS1                                                    
        EIN(NP)=EI1(J)/RGAS1
        L=4
        IF(EI1(J).LT.0.0D0) L=5                                           
        IPN(NP)=0  
        IARRY(NP)=L
        IZBR(NP)=IZBR1(J)
        DSCRPT(NP)=SCRP1(4+NION1+NATT1+J)
        PENFRA(1,NP)=PENFRA1(1,J)
        PENFRA(2,NP)=PENFRA1(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA1(3,J)
        IF(PENFRA(1,NP).GT.AVPFRAC(1,1)) THEN 
         AVPFRAC(1,1)=PENFRA(1,NP)
         AVPFRAC(2,1)=PENFRA(2,NP)
         AVPFRAC(3,1)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN1) CMINEXSC(1)=CMINEXSC(1)*AVPFRAC(1,1)
     50 CONTINUE    
  C                                                    
     60 IF(NGAS.EQ.1) GO TO 600
        NP=NP+1
        IDG2=NP  
        NEGAS(NP)=2
        LEGAS(NP)=0
        IESHELL(NP)=0                                                 
        CF(IE,NP)=Q2(2,IE)*VAN2*BET(IE)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KEL2(2).EQ.1) THEN
         PSCT1=PEQEL2(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL2(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL2(2,IE)
         INDEX(NP)=2 
        ENDIF 
  C
        IF(IE.GT.1) GO TO 62                                     
        RGAS2=1.0D0+E2(2)/2.0D0                                           
        RGAS(NP)=RGAS2                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0
        L=6                                                          
        IARRY(NP)=L      
        IZBR(NP)=0
        DSCRPT(NP)=SCRP2(2)  
        NAMEG(2)=NAME2
        PENFRA(1,NP)=0.0 
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,2)=0.0
        AVPFRAC(2,2)=0.0
        AVPFRAC(3,2)=0.0                        
        CMINEXSC(2)=E2(4)*AN2                                        
        CMINIXSC(2)=E2(5)*AN2
        ECLOSS(2)=E2(3)
        WPLN(2)=E2(6)
     62 IF(EFINAL.LT.E2(3)) GO TO 130  
        IF(NION2.GT.1) GO TO 70                                   
        NP=NP+1
        IDG2=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q2(5,IE)*VAN2*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(2,IE)=Q2(3,IE)/Q2(5,IE)-1.0D0
        ELSE                             
         CF(IE,NP)=Q2(3,IE)*VAN2*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=2
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(ICOUNT.EQ.1) THEN
         IF(KEL2(5).EQ.1) THEN
          PSCT1=PEQEL2(5,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL2(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL2(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL2(3).EQ.1) THEN
          PSCT1=PEQEL2(3,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL2(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL2(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C
        WPL(NP)=EB2(1)
        NC0(NP)=NC02(1)
        EC0(NP)=EC02(1)
        NG1(NP)=NG12(1)
        EG1(NP)=EG12(1)
        NG2(NP)=NG22(1)
        EG2(NP)=EG22(1)
        WKLM(NP)=WK2(1)
        EFL(NP)=EFL2(1)
        IF(IE.GT.1) GO TO 130                                      
        RGAS(NP)=RGAS2                                                    
        EIN(NP)=E2(3)/RGAS2 
        IPN(NP)=1  
        L=7                                                        
        IARRY(NP)=L
        IZBR(NP)=0      
        DSCRPT(NP)=SCRP2(3)     
        PENFRA(1,NP)=0.0 
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0  
        IONMODEL(NP)=IONMODL2
        DO 69 K=1,20
     69 ESPLIT(NP,K)=ESPLIT2(IONMODL2,K) 
        GO TO 130                                       
     70 DO 80 KION=1,NION2
        NP=NP+1
        IDG2=NP
        CF(IE,NP)=QION2(KION,IE)*VAN2*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
        NEGAS(NP)=2
        LEGAS(NP)=LEGAS2(KION)
        IESHELL(NP)=IESHEL2(KION)
  C
        IF(KEL2(3).EQ.1) THEN
         PSCT1=PEQION2(KION,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL2(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION2(KION,IE)
         INDEX(NP)=2
        ENDIF
  C
        WPL(NP)=EB2(KION)
        NC0(NP)=NC02(KION)
        EC0(NP)=EC02(KION)
        NG1(NP)=NG12(KION)
        EG1(NP)=EG12(KION)
        NG2(NP)=NG22(KION)
        EG2(NP)=EG22(KION)
        WKLM(NP)=WK2(KION)
        EFL(NP)=EFL2(KION)
        IF(IE.GT.1) GO TO 80                                      
        RGAS(NP)=RGAS2                                                    
        EIN(NP)=EION2(KION)/RGAS2 
  C
        IPN(NP)=1  
        L=7                                                        
        IARRY(NP)=L
        IZBR(NP)=0      
        DSCRPT(NP)=SCRP2(2+KION)     
        PENFRA(1,NP)=0.0 
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0       
        IONMODEL(NP)=IONMODL2
        DO 79 K=1,20
     79 ESPLIT(NP,K)=ESPLIT2(IONMODL2,K) 
     80 CONTINUE                                  
    130 IF(EFINAL.LT.E2(4)) GO TO 140    
        IF(NATT2.GT.1) GO TO 561                                 
        NP=NP+1
        IDG2=NP                                                           
        CF(IE,NP)=Q2(4,IE)*VAN2*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)  
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 140
        NEGAS(NP)=2
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0                                  
        RGAS(NP)=RGAS2                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1            
        L=8                                              
        IARRY(NP)=L
        IZBR(NP)=0      
        DSCRPT(NP)=SCRP2(3+NION2)   
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0        
        GO TO 140
    561 DO 562 JJ=1,NATT2
        NP=NP+1
        IDG2=NP
        CF(IE,NP)=QATT2(JJ,IE)*VAN2*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 562
        NEGAS(NP)=2
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS2
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=8
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP2(2+NION2+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
    562 CONTINUE                                 
    140 IF(NIN2.EQ.0) GO TO 160                                           
        DO 150 J=1,NIN2
        NP=NP+1
        IDG2=NP    
        NEGAS(NP)=2
        LEGAS(NP)=0
        IESHELL(NP)=0                                                   
        CF(IE,NP)=QIN2(J,IE)*VAN2*BET(IE)
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR2(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KIN2(J).EQ.1) THEN
         PSCT1=PEQIN2(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KIN2(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN2(J,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 150                                    
        RGAS(NP)=RGAS2                                                   
        EIN(NP)=EI2(J)/RGAS2
        L=9 
        IF(EI2(J).LT.0.0D0) L=10                                          
        IPN(NP)=0         
        IARRY(NP)=L
        IZBR(NP)=IZBR2(J)
        DSCRPT(NP)=SCRP2(4+NION2+NATT2+J)
        PENFRA(1,NP)=PENFRA2(1,J)
        PENFRA(2,NP)=PENFRA2(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA2(3,J)
        IF(PENFRA(1,NP).GT.AVPFRAC(1,2)) THEN 
         AVPFRAC(1,2)=PENFRA(1,NP)
         AVPFRAC(2,2)=PENFRA(2,NP)
         AVPFRAC(3,2)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN2) CMINEXSC(2)=CMINEXSC(2)*AVPFRAC(1,2)
    150 CONTINUE     
  C                                                   
    160 IF(NGAS.EQ.2) GO TO 600
        NP=NP+1
        IDG3=NP              
        NEGAS(NP)=3
        LEGAS(NP)=0
        IESHELL(NP)=0                                             
        CF(IE,NP)=Q3(2,IE)*VAN3*BET(IE)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C      
        IF(KEL3(2).EQ.1) THEN
         PSCT1=PEQEL3(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF 
        IF(KEL3(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL3(2,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 162                                     
        RGAS3=1.0D0+E3(2)/2.0D0                                           
        RGAS(NP)=RGAS3                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0  
        L=11                                                        
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP3(2)
        NAMEG(3)=NAME3
        PENFRA(1,NP)=0.0 
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,3)=0.0
        AVPFRAC(2,3)=0.0
        AVPFRAC(3,3)=0.0
        CMINEXSC(3)=E3(4)*AN3                                   
        CMINIXSC(3)=E3(5)*AN3 
        ECLOSS(3)=E3(3)
        WPLN(3)=E3(6)
    162 IF(EFINAL.LT.E3(3)) GO TO 230 
        IF(NION3.GT.1) GO TO 170                                    
        NP=NP+1
        IDG3=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q3(5,IE)*VAN3*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(3,IE)=Q3(3,IE)/Q3(5,IE)-1.0D0
        ELSE                              
         CF(IE,NP)=Q3(3,IE)*VAN3*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=3
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(ICOUNT.EQ.1) THEN
         IF(KEL3(5).EQ.1) THEN
          PSCT1=PEQEL3(5,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL3(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL3(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL3(3).EQ.1) THEN
          PSCT1=PEQEL3(3,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL3(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL3(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C 
        WPL(NP)=EB3(1)
        NC0(NP)=NC03(1)
        EC0(NP)=EC03(1)
        NG1(NP)=NG13(1)
        EG1(NP)=EG13(1)
        NG2(NP)=NG23(1)
        EG2(NP)=EG23(1)
        WKLM(NP)=WK3(1)
        EFL(NP)=EFL3(1)
        IF(IE.GT.1) GO TO 230                                            
        RGAS(NP)=RGAS3                                                    
        EIN(NP)=E3(3)/RGAS3 
        IPN(NP)=1
        L=12                                                           
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP3(3) 
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0 
        IONMODEL(NP)=IONMODL3
        DO 169 K=1,20
    169 ESPLIT(NP,K)=ESPLIT3(IONMODL3,K) 
        GO TO 230  
    170 DO 180 KION=1,NION3                                         
        NP=NP+1
        IDG3=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        CF(IE,NP)=QION3(KION,IE)*VAN3*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
        NEGAS(NP)=3
        LEGAS(NP)=LEGAS3(KION)
        IESHELL(NP)=IESHEL3(KION)
  C
        IF(KEL3(3).EQ.1) THEN
         PSCT1=PEQION3(3,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL3(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION3(KION,IE)
         INDEX(NP)=2
        ENDIF
  C 
        WPL(NP)=EB3(KION)
        NC0(NP)=NC03(KION)
        EC0(NP)=EC03(KION)
        NG1(NP)=NG13(KION)
        EG1(NP)=EG13(KION)
        NG2(NP)=NG23(KION)
        EG2(NP)=EG23(KION)
        WKLM(NP)=WK3(KION)
        EFL(NP)=EFL3(KION)
        IF(IE.GT.1) GO TO 180                                            
        RGAS(NP)=RGAS3                                                    
        EIN(NP)=EION3(KION)/RGAS3 
  C
        IPN(NP)=1
        L=12                                                           
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP3(2+KION) 
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0    
        IONMODEL(NP)=IONMODL3
        DO 179 K=1,20
    179 ESPLIT(NP,K)=ESPLIT3(IONMODL3,K) 
    180 CONTINUE                                        
    230 IF(EFINAL.LT.E3(4)) GO TO 240      
        IF(NATT3.GT.1) GO TO 571                               
        NP=NP+1
        IDG3=NP                                                           
        CF(IE,NP)=Q3(4,IE)*VAN3*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 240
        NEGAS(NP)=3
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0                                            
        RGAS(NP)=RGAS3                                                   
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1 
        L=13                                                        
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP3(3+NION3)
        PENFRA(1,NP)=0.0 
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0        
        GO TO 240
    571 CONTINUE
        DO 572 JJ=1,NATT3
        NP=NP+1
        IDG3=NP
        CF(IE,NP)=QATT3(JJ,IE)*VAN3*BET(IE)  
        FCATT(IE)=FCATT(IE)+CF(IE,NP)      
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 572
        NEGAS(NP)=3
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS3
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=13
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP3(2+NION3+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
    572 CONTINUE                           
    240 IF(NIN3.EQ.0) GO TO 260                                           
        DO 250 J=1,NIN3 
        NP=NP+1
        IDG3=NP      
        NEGAS(NP)=3
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=QIN3(J,IE)*VAN3*BET(IE)
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR3(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KIN3(J).EQ.1) THEN
         PSCT1=PEQIN3(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KIN3(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN3(J,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 250                                     
        RGAS(NP)=RGAS3                                                    
        EIN(NP)=EI3(J)/RGAS3
        L=14
        IF(EI3(J).LT.0.0D0) L=15                                          
        IPN(NP)=0
        IARRY(NP)=L
        IZBR(NP)=IZBR3(J)
        DSCRPT(NP)=SCRP3(4+NION3+NATT3+J)
        PENFRA(1,NP)=PENFRA3(1,J)
        PENFRA(2,NP)=PENFRA3(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA3(3,J)  
        IF(PENFRA(1,NP).GT.AVPFRAC(1,3)) THEN 
         AVPFRAC(1,3)=PENFRA(1,NP)
         AVPFRAC(2,3)=PENFRA(2,NP)
         AVPFRAC(3,3)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN3) CMINEXSC(3)=CMINEXSC(3)*AVPFRAC(1,3)   
    250 CONTINUE             
  C                  
    260 IF(NGAS.EQ.3) GO TO 600  
        NP=NP+1
        IDG4=NP      
        NEGAS(NP)=4
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=Q4(2,IE)*VAN4*BET(IE) 
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KEL4(2).EQ.1) THEN
         PSCT1=PEQEL4(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1  
        ENDIF
        IF(KEL4(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL4(2,IE)
         INDEX(NP)=2
        ENDIF 
  C
        IF(IE.GT.1) GO TO 262                                    
        RGAS4=1.0D0+E4(2)/2.0D0                                           
        RGAS(NP)=RGAS4                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0
        L=16                                                          
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP4(2)
        NAMEG(4)=NAME4 
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,4)=0.0 
        AVPFRAC(2,4)=0.0
        AVPFRAC(3,4)=0.0
        CMINEXSC(4)=E4(4)*AN4                                       
        CMINIXSC(4)=E4(5)*AN4
        ECLOSS(4)=E4(3)
        WPLN(4)=E4(6)
    262 IF(EFINAL.LT.E4(3)) GO TO 330  
        IF(NION4.GT.1) GO TO 270                                   
        NP=NP+1
        IDG4=NP  
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q4(5,IE)*VAN4*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(4,IE)=Q4(3,IE)/Q4(5,IE)-1.0D0
        ELSE                                                         
         CF(IE,NP)=Q4(3,IE)*VAN4*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=4
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0  
  C
        IF(ICOUNT.EQ.1) THEN
         IF(KEL4(5).EQ.1) THEN
          PSCT1=PEQEL4(5,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL4(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL4(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL4(3).EQ.1) THEN
          PSCT1=PEQEL4(3,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL4(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL4(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C
        WPL(NP)=EB4(1)
        NC0(NP)=NC04(1)
        EC0(NP)=EC04(1)
        NG1(NP)=NG14(1)
        EG1(NP)=EG14(1)
        NG2(NP)=NG24(1)
        EG2(NP)=EG24(1)
        WKLM(NP)=WK4(1)
        EFL(NP)=EFL4(1)
        IF(IE.GT.1) GO TO 330                                     
        RGAS(NP)=RGAS4                                                    
        EIN(NP)=E4(3)/RGAS4 
        IPN(NP)=1  
        L=17                                                        
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP4(3)   
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0 
        PENFRA(3,NP)=0.0  
        IONMODEL(NP)=IONMODL4
        DO 269 K=1,20
    269 ESPLIT(NP,K)=ESPLIT4(IONMODL4,K) 
        GO TO 330
    270 DO 280 KION=1,NION4                                       
        NP=NP+1
        IDG4=NP
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        CF(IE,NP)=QION4(KION,IE)*VAN4*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0  
        NEGAS(NP)=4
        LEGAS(NP)=LEGAS4(KION)
        IESHELL(NP)=IESHEL4(KION)
  C
        IF(KEL4(3).EQ.1) THEN
         PSCT1=PEQION4(KION,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL4(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION4(KION,IE)
         INDEX(NP)=2
        ENDIF
  C 
        WPL(NP)=EB4(KION)
        NC0(NP)=NC04(KION)
        EC0(NP)=EC04(KION)
        NG1(NP)=NG14(KION)
        EG1(NP)=EG14(KION)
        NG2(NP)=NG24(KION)
        EG2(NP)=EG24(KION)
        WKLM(NP)=WK4(KION)
        EFL(NP)=EFL4(KION)
        IF(IE.GT.1) GO TO 280                                     
        RGAS(NP)=RGAS4                                                    
        EIN(NP)=EION4(KION)/RGAS4
  C 
        IPN(NP)=1  
        L=17                                                        
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP4(2+KION)   
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0 
        PENFRA(3,NP)=0.0  
        IONMODEL(NP)=IONMODL4
        DO 279 K=1,20
    279 ESPLIT(NP,K)=ESPLIT4(IONMODL4,K) 
    280 CONTINUE                                       
    330 IF(EFINAL.LT.E4(4)) GO TO 340          
        IF(NATT4.GT.1) GO TO 581                           
        NP=NP+1
        IDG4=NP                                                           
        CF(IE,NP)=Q4(4,IE)*VAN4*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 340  
        NEGAS(NP)=4
        LEGAS(NP)=0
        IESHELL(NP)=0      
        INDEX(NP)=0                             
        RGAS(NP)=RGAS4                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1 
        L=18                                                        
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP4(3+NION4)
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0        
        GO TO 340
    581 DO 582 JJ=1,NATT4
        NP=NP+1
        IDG4=NP
        CF(IE,NP)=QATT4(JJ,IE)*VAN4*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP) 
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 582
        NEGAS(NP)=4
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS4
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=18
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP4(2+NION4+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
    582 CONTINUE                                    
    340 IF(NIN4.EQ.0) GO TO 360                                           
        DO 350 J=1,NIN4 
        NP=NP+1
        IDG4=NP
        NEGAS(NP)=4
        LEGAS(NP)=0
        IESHELL(NP)=0
        CF(IE,NP)=QIN4(J,IE)*VAN4*BET(IE)
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR4(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KIN4(J).EQ.1) THEN
         PSCT1=PEQIN4(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KIN4(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN4(J,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 350        
        RGAS(NP)=RGAS4                                                    
        EIN(NP)=EI4(J)/RGAS4
        L=19
        IF(EI4(J).LT.0.0D0) L=20                                          
        IPN(NP)=0         
        IARRY(NP)=L
        IZBR(NP)=IZBR4(J)
        DSCRPT(NP)=SCRP4(4+NION4+NATT4+J)
        PENFRA(1,NP)=PENFRA4(1,J)
        PENFRA(2,NP)=PENFRA4(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA4(3,J)
        IF(PENFRA(1,NP).GT.AVPFRAC(1,4)) THEN 
         AVPFRAC(1,4)=PENFRA(1,NP)
         AVPFRAC(2,4)=PENFRA(2,NP)
         AVPFRAC(3,4)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN4) CMINEXSC(4)=CMINEXSC(4)*AVPFRAC(1,4)
    350 CONTINUE             
  C                                           
    360 IF(NGAS.EQ.4) GO TO 600  
        NP=NP+1
        IDG5=NP      
        NEGAS(NP)=5
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=Q5(2,IE)*VAN5*BET(IE) 
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KEL5(2).EQ.1) THEN 
         PSCT1=PEQEL5(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL5(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL5(2,IE)
         INDEX(NP)=2
        ENDIF
  C 
        IF(IE.GT.1) GO TO 362                                    
        RGAS5=1.0D0+E5(2)/2.0D0                                           
        RGAS(NP)=RGAS5                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0
        L=21                                                          
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP5(2) 
        NAMEG(5)=NAME5    
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,5)=0.0
        AVPFRAC(2,5)=0.0
        AVPFRAC(3,5)=0.0
        CMINEXSC(5)=E5(4)*AN5                                    
        CMINIXSC(5)=E5(5)*AN5
        ECLOSS(5)=E5(3)
        WPLN(5)=E5(6)
    362 IF(EFINAL.LT.E5(3)) GO TO 430  
        IF(NION5.GT.1) GO TO 370                                   
        NP=NP+1
        IDG5=NP  
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q5(5,IE)*VAN5*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(5,IE)=Q5(3,IE)/Q5(5,IE)-1.0D0
        ELSE                                                         
         CF(IE,NP)=Q5(3,IE)*VAN5*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=5
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0 
  C
        IF(ICOUNT.EQ.1) THEN
         IF(KEL5(5).EQ.1) THEN
          PSCT1=PEQEL5(5,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL5(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL5(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL5(3).EQ.1) THEN
          PSCT1=PEQEL5(3,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1
         ENDIF
         IF(KEL5(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL5(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C 
        WPL(NP)=EB5(1)     
        NC0(NP)=NC05(1)
        EC0(NP)=EC05(1)
        NG1(NP)=NG15(1)
        EG1(NP)=EG15(1)
        NG2(NP)=NG25(1)
        EG2(NP)=EG25(1)
        WKLM(NP)=WK5(1)
        EFL(NP)=EFL5(1)
        IF(IE.GT.1) GO TO 430                                    
        RGAS(NP)=RGAS5                                                    
        EIN(NP)=E5(3)/RGAS5 
        IPN(NP)=1
        L=22                                                          
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP5(3)  
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0 
        IONMODEL(NP)=IONMODL5
        DO 369 K=1,20
    369 ESPLIT(NP,K)=ESPLIT5(IONMODL5,K) 
        GO TO 430       
    370 DO 380 KION=1,NION5                                   
        NP=NP+1
        IDG5=NP  
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        CF(IE,NP)=QION5(KION,IE)*VAN5*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0 
        NEGAS(NP)=5
        LEGAS(NP)=LEGAS5(KION)
        IESHELL(NP)=IESHEL5(KION)
  C
        IF(KEL5(3).EQ.1) THEN
         PSCT1=PEQION5(KION,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL5(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION5(KION,IE)
         INDEX(NP)=2
        ENDIF
  C
        WPL(NP)=EB5(KION)      
        NC0(NP)=NC05(KION)
        EC0(NP)=EC05(KION)
        NG1(NP)=NG15(KION)
        EG1(NP)=EG15(KION)
        NG2(NP)=NG25(KION)
        EG2(NP)=EG25(KION)
        WKLM(NP)=WK5(KION)
        EFL(NP)=EFL5(KION)
        IF(IE.GT.1) GO TO 380                                    
        RGAS(NP)=RGAS5                                                    
        EIN(NP)=EION5(KION)/RGAS5
  C 
        IPN(NP)=1
        L=22                                                          
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP5(2+KION)  
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0 
        IONMODEL(NP)=IONMODL5
        DO 379 K=1,20
    379 ESPLIT(NP,K)=ESPLIT5(IONMODL5,K) 
    380 CONTINUE
    430 IF(EFINAL.LT.E5(4)) GO TO 440                 
        IF(NATT5.GT.1) GO TO 591                    
        NP=NP+1
        IDG5=NP                                                           
        CF(IE,NP)=Q5(4,IE)*VAN5*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 440
        NEGAS(NP)=5
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0                                     
        RGAS(NP)=RGAS5                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1             
        L=23                                            
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP5(3+NION5)  
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0 
        PENFRA(3,NP)=0.0        
        GO TO 440
    591 DO 592 JJ=1,NATT5
        NP=NP+1
        IDG5=NP
        CF(IE,NP)=QATT5(JJ,IE)*VAN5*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 592
        NEGAS(NP)=5
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS5
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=23
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP5(2+NION5+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
    592 CONTINUE                                  
    440 IF(NIN5.EQ.0) GO TO 460                                           
        DO 450 J=1,NIN5 
        NP=NP+1
        IDG5=NP      
        NEGAS(NP)=5
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=QIN5(J,IE)*VAN5*BET(IE) 
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR5(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(KIN5(J).EQ.1) THEN
         PSCT1=PEQIN5(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KIN5(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN5(J,IE)
         INDEX(NP)=2
        ENDIF  
  C        
        IF(IE.GT.1) GO TO 450
        RGAS(NP)=RGAS5                                                    
        EIN(NP)=EI5(J)/RGAS5
        L=24
        IF(EI5(J).LT.0.0D0) L=25                                          
        IPN(NP)=0         
        IARRY(NP)=L
        IZBR(NP)=IZBR5(J)
        DSCRPT(NP)=SCRP5(4+NION5+NATT5+J)
        PENFRA(1,NP)=PENFRA5(1,J)
        PENFRA(2,NP)=PENFRA5(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA5(3,J)
        IF(PENFRA(1,NP).GT.AVPFRAC(1,5)) THEN 
         AVPFRAC(1,5)=PENFRA(1,NP)
         AVPFRAC(2,5)=PENFRA(2,NP)
         AVPFRAC(3,5)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN5) CMINEXSC(5)=CMINEXSC(5)*AVPFRAC(1,5)
    450 CONTINUE             
  C                                           
    460 IF(NGAS.EQ.5) GO TO 600  
        NP=NP+1
        IDG6=NP      
        NEGAS(NP)=6
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=Q6(2,IE)*VAN6*BET(IE)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0 
  C
        IF(KEL6(2).EQ.1) THEN
         PSCT1=PEQEL6(2,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KEL6(2).EQ.2) THEN
         PSCT(IE,NP)=PEQEL6(2,IE)
         INDEX(NP)=2
        ENDIF
  C  
        IF(IE.GT.1) GO TO 462                                    
        RGAS6=1.0D0+E6(2)/2.0D0                                           
        RGAS(NP)=RGAS6                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=0
        L=26                                                          
        IARRY(NP)=L
        IZBR(NP)=0  
        DSCRPT(NP)=SCRP6(2) 
        NAMEG(6)=NAME6  
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        AVPFRAC(1,6)=0.0
        AVPFRAC(2,6)=0.0
        AVPFRAC(3,6)=0.0
        CMINEXSC(6)=E6(4)*AN6                                       
        CMINIXSC(6)=E6(5)*AN6
        ECLOSS(6)=E6(3)
        WPLN(6)=E6(6)
    462 IF(EFINAL.LT.E6(3)) GO TO 530      
        IF(NION6.GT.1) GO TO 470                               
        NP=NP+1 
        IDG6=NP 
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        IF(ICOUNT.EQ.1) THEN
         CF(IE,NP)=Q6(5,IE)*VAN6*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
         DOUBLE(6,IE)=Q6(3,IE)/Q6(5,IE)-1.0D0
        ELSE                                                         
         CF(IE,NP)=Q6(3,IE)*VAN6*BET(IE)
         FCION(IE)=FCION(IE)+CF(IE,NP)
        ENDIF
        NEGAS(NP)=6
        LEGAS(NP)=0
        IESHELL(NP)=0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
  C
        IF(ICOUNT.EQ.1) THEN
         IF(KEL6(5).EQ.1) THEN
          PSCT1=PEQEL6(5,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1      
         ENDIF
         IF(KEL6(5).EQ.2) THEN
          PSCT(IE,NP)=PEQEL6(5,IE)
          INDEX(NP)=2
         ENDIF
        ELSE
         IF(KEL6(3).EQ.1) THEN
          PSCT1=PEQEL6(3,IE)
          CALL ANGCUT(PSCT1,ANGC,PSCT2)
          ANGCT(IE,NP)=ANGC
          PSCT(IE,NP)=PSCT2
          INDEX(NP)=1      
         ENDIF
         IF(KEL6(3).EQ.2) THEN
          PSCT(IE,NP)=PEQEL6(3,IE)
          INDEX(NP)=2
         ENDIF
        ENDIF
  C
        WPL(NP)=EB6(1)
        NC0(NP)=NC06(1)
        EC0(NP)=EC06(1)
        NG1(NP)=NG16(1)
        EG1(NP)=EG16(1)
        NG2(NP)=NG26(1)
        EG2(NP)=EG26(1)
        WKLM(NP)=WK6(1)
        EFL(NP)=EFL6(1)
        IF(IE.GT.1) GO TO 530                                     
        RGAS(NP)=RGAS6                                                    
        EIN(NP)=E6(3)/RGAS6 
        IPN(NP)=1             
        L=27                                             
        IARRY(NP)=L
        IZBR(NP)=0  
        DSCRPT(NP)=SCRP6(3)
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0    
        GO TO 530  
    470 DO 480 KION=1,NION6    
        NP=NP+1
        IDG6=NP  
  C CHOOSE BETWEEN COUNTING AND GROSS IONISATION X-SECTION
        CF(IE,NP)=QION6(KION,IE)*VAN6*BET(IE)
        FCION(IE)=FCION(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0
        NEGAS(NP)=6
        LEGAS(NP)=LEGAS6(KION)
        IESHELL(NP)=IESHEL6(KION)
  C
        IF(KEL6(3).EQ.1) THEN
         PSCT1=PEQION6(KION,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1      
        ENDIF
        IF(KEL6(3).EQ.2) THEN
         PSCT(IE,NP)=PEQION6(KION,IE)
         INDEX(NP)=2
        ENDIF
  C
        WPL(NP)=EB6(KION)
        NC0(NP)=NC06(KION)
        EC0(NP)=EC06(KION)
        NG1(NP)=NG16(KION)
        EG1(NP)=EG16(KION)
        NG2(NP)=NG26(KION)
        EG2(NP)=EG26(KION)
        WKLM(NP)=WK6(KION)
        EFL(NP)=EFL6(KION)
        IF(IE.GT.1) GO TO 480                                     
        RGAS(NP)=RGAS6                                                    
        EIN(NP)=EION6(KION)/RGAS6 
        IPN(NP)=1             
        L=27                                             
        IARRY(NP)=L
        IZBR(NP)=0  
        DSCRPT(NP)=SCRP6(2+KION)
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0    
        IONMODEL(NP)=IONMODL6
        DO 479 K=1,20
    479 ESPLIT(NP,K)=ESPLIT6(IONMODL6,K) 
    480 CONTINUE                                 
    530 IF(EFINAL.LT.E6(4)) GO TO 540                  
        IF(NATT6.GT.1) GO TO 590                   
        NP=NP+1
        IDG6=NP                                                           
        CF(IE,NP)=Q6(4,IE)*VAN6*BET(IE) 
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 540 
        NEGAS(NP)=6
        LEGAS(NP)=0
        IESHELL(NP)=0       
        INDEX(NP)=0                            
        RGAS(NP)=RGAS6                                                    
        EIN(NP)=0.0D0                                                     
        IPN(NP)=-1
        L=28                                                          
        IARRY(NP)=L
        IZBR(NP)=0  
        DSCRPT(NP)=SCRP6(3+NION6) 
        PENFRA(1,NP)=0.0  
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0        
        GO TO 540
    590 DO 602 JJ=1,NATT6
        NP=NP+1
        IDG6=NP
        CF(IE,NP)=QATT6(JJ,IE)*VAN6*BET(IE)
        FCATT(IE)=FCATT(IE)+CF(IE,NP)
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        IF(IE.GT.1) GO TO 602
        NEGAS(NP)=6
        LEGAS(NP)=0
        IESHELL(NP)=0
        INDEX(NP)=0
        RGAS(NP)=RGAS6
        EIN(NP)=0.0D0
        IPN(NP)=-1
        L=28
        IARRY(NP)=L
        IZBR(NP)=0
        DSCRPT(NP)=SCRP6(2+NION6+JJ)
        PENFRA(1,NP)=0.0
        PENFRA(2,NP)=0.0
        PENFRA(3,NP)=0.0
        IONMODEL(NP)=IONMODL6
        DO 601 K=1,20
    601 ESPLIT(NP,K)=ESPLIT6(IONMODL6,K)  
    602 CONTINUE                                    
    540 IF(NIN6.EQ.0) GO TO 560                                           
        DO 550 J=1,NIN6 
        NP=NP+1
        IDG6=NP      
        NEGAS(NP)=6
        LEGAS(NP)=0
        IESHELL(NP)=0                                                     
        CF(IE,NP)=QIN6(J,IE)*VAN6*BET(IE)
  C NO X-SECTION FOR BREMSSTRAHLUNG IF LBRM=0
        IF(IZBR6(J).NE.0.AND.LBRM.EQ.0) CF(IE,NP)=0.0
        PSCT(IE,NP)=0.5
        ANGCT(IE,NP)=1.0
        INDEX(NP)=0 
  C
        IF(KIN6(J).EQ.1) THEN
         PSCT1=PEQIN6(J,IE)
         CALL ANGCUT(PSCT1,ANGC,PSCT2)
         ANGCT(IE,NP)=ANGC
         PSCT(IE,NP)=PSCT2
         INDEX(NP)=1
        ENDIF
        IF(KIN6(J).EQ.2) THEN
         PSCT(IE,NP)=PEQIN6(J,IE)
         INDEX(NP)=2
        ENDIF
  C
        IF(IE.GT.1) GO TO 550          
        RGAS(NP)=RGAS6                                                    
        EIN(NP)=EI6(J)/RGAS6
        L=29
        IF(EI6(J).LT.0.0D0) L=30                                          
        IPN(NP)=0         
        IARRY(NP)=L
        IZBR(NP)=IZBR6(J)  
        DSCRPT(NP)=SCRP6(4+NION6+NATT6+J)
        PENFRA(1,NP)=PENFRA6(1,J)
        PENFRA(2,NP)=PENFRA6(2,J)*1.D-6/DSQRT(3.0D0)
        PENFRA(3,NP)=PENFRA6(3,J)
        IF(PENFRA(1,NP).GT.AVPFRAC(1,6)) THEN 
         AVPFRAC(1,6)=PENFRA(1,NP)
         AVPFRAC(2,6)=PENFRA(2,NP)
         AVPFRAC(3,6)=PENFRA(3,NP)
        ENDIF
        IF(J.EQ.NIN6) CMINEXSC(6)=CMINEXSC(6)*AVPFRAC(1,6) 
    550 CONTINUE                                                     
    560 CONTINUE     
  C                                                                       
    600 CONTINUE                                                          
        IPLAST=NP  
  C ----------------------------------------------------------------      
  C   CAN INCREASE ARRAY SIZE UP TO 1740 IF MORE COMPLEX MIXTURES USED.
  C   1740 = 6 * 290 ( 6 = MAX NO OF GASES. 290 = MAX NO OF LEVELS )    
  C ------------------------------------------------------------------    
        IF(IPLAST.GT.512) WRITE(6,992)                                    
    992 FORMAT(/,/,6X,'WARNING TOO MANY LEVELS IN CALCULATION. CAN INCREAS
       /E THE ARRAY SIZES FROM 512 UP TO 1740 MAXIMUM',/)                 
        IF(IPLAST.GT.512) STOP                                            
  C --------------------------------------------------------------------  
  C     CALCULATION OF TOTAL COLLISION FREQUENCY                          
  C --------------------------------------------------------------------- 
        TCF(IE)=0.0D0                                                     
        DO 610 IL=1,IPLAST                                                
        TCF(IE)=TCF(IE)+CF(IE,IL)
        IF(CF(IE,IL).LT.0.0D0) WRITE(6,776) CF(IE,IL),IE,IL,IARRY(IL),EIN
       /(IL),E(IE) 
    776 FORMAT('MODI WARNING NEGATIVE COLLISION FREQUENCY =',D12.3,' IE =',I6,
       /' IL =',I3,' IARRY=',I5,' EIN=',D12.4,' ENERGY=',D12.4)         
   610  CONTINUE                                                          
        DO 620 IL=1,IPLAST                                                
        IF(TCF(IE).EQ.0.0D0) GO TO 615                                    
        CF(IE,IL)=CF(IE,IL)/TCF(IE)                                       
        GO TO 620                                                         
   615  CF(IE,IL)=0.0D0                                                   
   620  CONTINUE                                                          
        DO 630 IL=2,IPLAST                                                
        CF(IE,IL)=CF(IE,IL)+CF(IE,IL-1)                                   
   630  CONTINUE                   
  C FIX ROUNDING ERRORS AT HIGHEST VALUE
        CF(IE,IPLAST)=1.0D0
  C
  C     FCATT(IE)=FCATT(IE)*EROOT(IE)
  C     FCION(IE)=FCION(IE)*EROOT(IE)                                     
  C     TCF(IE)=TCF(IE)*EROOT(IE)   
        FCATT(IE)=FCATT(IE)*1.0D-10  
        FCION(IE)=FCION(IE)*1.0D-10                                       
        TCF(IE)=TCF(IE)*1.0D-10   
  C CALCULATION OF NULL COLLISION FREQUENCIES
        NP=0
        NPLAST=0
        IF((NUL1+NUL2+NUL3+NUL4+NUL5+NUL6).EQ.0) GO TO 699
        IF(NUL1.GT.0) THEN
         DO 631 J=1,NUL1
         NP=NP+1
         SCLENUL(NP)=SCLN1(J)
         DSCRPTN(NP)=SCRPN1(J)
    631  CFN(IE,NP)=QNUL1(J,IE)*VAN1*SCLENUL(NP)*BET(IE)
        ENDIF
        IF(NUL2.GT.0) THEN
         DO 632 J=1,NUL2
         NP=NP+1
         SCLENUL(NP)=SCLN2(J)
         DSCRPTN(NP)=SCRPN2(J)
    632  CFN(IE,NP)=QNUL2(J,IE)*VAN2*SCLENUL(NP)*BET(IE)
        ENDIF
        IF(NUL3.GT.0) THEN
         DO 633 J=1,NUL3
         NP=NP+1
         SCLENUL(NP)=SCLN3(J)
         DSCRPTN(NP)=SCRPN3(J)
    633  CFN(IE,NP)=QNUL3(J,IE)*VAN3*SCLENUL(NP)*BET(IE)
        ENDIF
        IF(NUL4.GT.0) THEN
         DO 634 J=1,NUL4
         NP=NP+1
         SCLENUL(NP)=SCLN4(J)
         DSCRPTN(NP)=SCRPN4(J)
    634  CFN(IE,NP)=QNUL4(J,IE)*VAN4*SCLENUL(NP)*BET(IE)
        ENDIF
        IF(NUL5.GT.0) THEN
         DO 635 J=1,NUL5
         NP=NP+1
         SCLENUL(NP)=SCLN5(J)
         DSCRPTN(NP)=SCRPN5(J)
    635  CFN(IE,NP)=QNUL5(J,IE)*VAN5*SCLENUL(NP)*BET(IE)
        ENDIF
        IF(NUL6.GT.0) THEN
         DO 636 J=1,NUL6
         NP=NP+1
         SCLENUL(NP)=SCLN6(J)
         DSCRPTN(NP)=SCRPN6(J)
    636  CFN(IE,NP)=QNUL6(J,IE)*VAN6*SCLENUL(NP)*BET(IE)
        ENDIF
        NPLAST=NP
  C SUM NULL COLLISIONS
        TCFN(IE)=0.0
        DO 640 IL=1,NPLAST
        TCFN(IE)=TCFN(IE)+CFN(IE,IL)
        IF(CFN(IE,IL).LT.0.0) WRITE(6,779) CFN(IE,IL),IE,IL
    779 FORMAT(' WARNING NEGATIVE NULL COLLISION REQUENCY =',D12.3,
       /' IE =',I6,' IL =',I3)
    640 CONTINUE
        DO 642 IL=1,NPLAST
        IF(TCFN(IE).EQ.0.0D0) GO TO 641
        CFN(IE,IL)=CFN(IE,IL)/TCFN(IE)
        GO TO 642
    641 CFN(IE,IL)=0.0D0
    642 CONTINUE
        TCFN(IE)=TCFN(IE)*1.0D-10
        IF(NPLAST.EQ.1) GO TO 699
        DO 643 IL=2,NPLAST
        CFN(IE,IL)=CFN(IE,IL)+CFN(IE,IL-1)
    643 CONTINUE
  C FIX ROUNDING ERRORS AT HIGHEST VALUE
        CFN(IE,NPLAST)=1.0D0 
    699 CONTINUE
    700 CONTINUE 
  C     WRITE(6,841) (INDEX(J),J, J=1,IPLAST)
  C 841 FORMAT(2X,' INDEX=',I3,' J=',I3)                   
  C  SET ANISOTROPIC FLAG IF ANISOTROPIC SCATTERING DATA IS DETECTED
        KELSUM=0
        DO 701 J=1,6
   701  KELSUM=KELSUM+KEL1(J)+KEL2(J)+KEL3(J)+KEL4(J)+KEL5(J)+KEL6(J)
        DO 702 J=1,250
   702  KELSUM=KELSUM+KIN1(J)+KIN2(J)+KIN3(J)+KIN4(J)+KIN5(J)+KIN6(J)
        IF(KELSUM.GT.0) NISO=1  
  C     IF(NISO.EQ.1) WRITE(6,7765) NISO
  C7765 FORMAT(3X,' ANISOTROPIC SCATTERING DETECTED NISO=',I5)         
  C -------------------------------------------------------------------   
  C   CALCULATE NULL COLLISION FREQUENCY                                  
  C -------------------------------------------------------------------   
        BP=EFIELD*EFIELD*CONST1                                           
        F2=EFIELD*CONST3                                                  
        ELOW=TMAX*(TMAX*BP-F2*DSQRT(0.5D0*EFINAL))/ESTEP-1.0D0            
        ELOW=DMIN1(ELOW,SMALL)                                            
        EHI=TMAX*(TMAX*BP+F2*DSQRT(0.5D0*EFINAL))/ESTEP+1.0D0
        IF(EHI.GT.20000.0) EHI=20000.0
        JONE=1
        JLARGE=20000  
        DO 810 I=1,10                                                     
        JLOW=20000-2000*(11-I)+1+DINT(ELOW)                               
        JHI=20000-2000*(10-I)+DINT(EHI)
        JLOW=DMAX0(JLOW,JONE)                                         
        JHI=DMIN0(JHI,JLARGE)
        DO 800 J=JLOW,JHI
        IF(TCF(J).GE.TCFMAX(I)) TCFMAX(I)=TCF(J)                          
    800 CONTINUE                                                          
    810 CONTINUE  
  C---------------------------------------------------------------------
  C FIND MAXIMUM COLLISION FREQUENCY
  C     TLIM=TCFMAX(1)
  C     DO 835 I=1,10
  C 835 IF(TLIM.LT.TCFMAX(I)) TLIM=TCFMAX(I)
  C     TCFMAX1=TLIM  
        TLIM=0.0
        DO 835 I=1,20000
    835 IF(TLIM.LT.TCF(I)) TLIM=TCF(I)
        TCFMAX1=TLIM                                                    
  C -------------------------------------------------------------------   
  C   CROSS SECTION DATA FOR INTEGRALS IN  OUTPUT               
  C --------------------------------------------------------------------- 
        DO 900 I=1,NSTEP                                               
        QTOT(I)=AN1*Q1(1,I)+AN2*Q2(1,I)+AN3*Q3(1,I)+AN4*Q4(1,I)+
       /AN5*Q5(1,I)+AN6*Q6(1,I)            
        QEL(I)=AN1*Q1(2,I)+AN2*Q2(2,I)+AN3*Q3(2,I)+AN4*Q4(2,I)+
       /AN5*Q5(2,I)+AN6*Q6(2,I)             
  C                                                                       
        QION(1,I)=Q1(3,I)*AN1   
        IF(NION1.GT.1) THEN
         DO 811 KION=1,NION1
    811  QION(1,I)=QION1(KION,I)*AN1
        ENDIF                                           
        QION(2,I)=Q2(3,I)*AN2                                             
        IF(NION2.GT.1) THEN
         DO 812 KION=1,NION2
    812  QION(2,I)=QION2(KION,I)*AN2
        ENDIF                                           
        QION(3,I)=Q3(3,I)*AN3                                             
        IF(NION3.GT.1) THEN
         DO 813 KION=1,NION3
    813  QION(3,I)=QION3(KION,I)*AN3
        ENDIF                                           
        QION(4,I)=Q4(3,I)*AN4
        IF(NION4.GT.1) THEN
         DO 814 KION=1,NION4
    814  QION(4,I)=QION4(KION,I)*AN4
        ENDIF                                           
        QION(5,I)=Q5(3,I)*AN5
        IF(NION5.GT.1) THEN
         DO 815 KION=1,NION5
    815  QION(5,I)=QION5(KION,I)*AN5
        ENDIF                                           
        QION(6,I)=Q6(3,I)*AN6                                             
        IF(NION6.GT.1) THEN
         DO 816 KION=1,NION6
    816  QION(6,I)=QION6(KION,I)*AN6
        ENDIF                                           
        QATT(1,I)=Q1(4,I)*AN1                                             
        QATT(2,I)=Q2(4,I)*AN2                                             
        QATT(3,I)=Q3(4,I)*AN3                                             
        QATT(4,I)=Q4(4,I)*AN4
        QATT(5,I)=Q5(4,I)*AN5
        QATT(6,I)=Q6(4,I)*AN6                                             
  C                                                                       
        QREL(I)=0.0D0                                                     
        QSATT(I)=0.0D0                                                   
        QSUM(I)=0.0D0                                                     
        DO 855 J=1,NGAS                                                   
        QSUM(I)=QSUM(I)+QION(J,I)+QATT(J,I)                               
        QSATT(I)=QSATT(I)+QATT(J,I)                                       
    855 QREL(I)=QREL(I)+QION(J,I)-QATT(J,I)                               
  C                                                                       
        IF(NIN1.EQ.0) GO TO 865                                           
        DO 860 J=1,NIN1                                                   
    860 QSUM(I)=QSUM(I)+QIN1(J,I)*AN1                                     
    865 IF(NIN2.EQ.0) GO TO 875                                           
        DO 870 J=1,NIN2                                                   
    870 QSUM(I)=QSUM(I)+QIN2(J,I)*AN2                                     
    875 IF(NIN3.EQ.0) GO TO 885                                           
        DO 880 J=1,NIN3                                                   
    880 QSUM(I)=QSUM(I)+QIN3(J,I)*AN3                                     
    885 IF(NIN4.EQ.0) GO TO 895                                           
        DO 890 J=1,NIN4                                                   
    890 QSUM(I)=QSUM(I)+QIN4(J,I)*AN4                                     
    895 IF(NIN5.EQ.0) GO TO 898 
        DO 896 J=1,NIN5
    896 QSUM(I)=QSUM(I)+QIN5(J,I)*AN5
    898 IF(NIN6.EQ.0) GO TO 900
        DO 899 J=1,NIN6
    899 QSUM(I)=QSUM(I)+QIN6(J,I)*AN6                                     
  C                                                                       
   900  CONTINUE                                                          
  C                                                                       
        RETURN                                                            
        END 
```
## SETUP()

```fortran
      SUBROUTINE SETUP(LAST)                                            
      IMPLICIT REAL*8 (A-H,O-Z) 
      IMPLICIT INTEGER*8 (I-N) 
      INTEGER*4 NSEED                                       
      COMMON/INPT/NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
      COMMON/CNSTS/ECHARG,EMASS,AMU,PIR2
      COMMON/INPT2/KGAS,LGAS,DETEFF,EXCWGHT
      COMMON/INPT1/NDVEC                                
      COMMON/CNSTS1/CONST1,CONST2,CONST3,CONST4,CONST5                  
      COMMON/RATIO/AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC(6)               
      COMMON/GASN/NGASN(6)                                 
      COMMON/SETP/TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX(10),TCFMAX1,
     /RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE
      COMMON/SET2/DRXINIT,DRYINIT,DRZINIT
      COMMON/BFLD/EOVB,WB,BTHETA,BMAG 
      COMMON/IONC/DOUBLE(6,20000),CMINIXSC(6),CMINEXSC(6),ECLOSS(6),
     /WPLN(6),ICOUNT,AVPFRAC(3,6)
      COMMON/MRATIO/VAN1,VAN2,VAN3,VAN4,VAN5,VAN6,VAN
      COMMON/OUTPT/ICOLL(30),NETOT,NPRIME,TMAX1,TIME(300),NNULL,
     /NITOT,ICOLN(512),ICOLNN(60),NREAL,NEXCTOT
      COMMON/PRIM3/MSUM(10000),MCOMP(10000),MRAYL(10000),MPAIR(10000),
     /MPHOT(10000),MVAC(10000)
      COMMON/RLTVY/BET(20000),GAM(20000),VC,EMS 
      COMMON/COMP/ICMP,ICFLG,IRAY,IRFLG,IPAP,IPFLG,IBRM,IBFLG,LPEFLG 
      COMMON/MIX2/E(20000),EROOT(20000),QTOT(20000),QREL(20000),
     /QINEL(20000),QEL(20000)
      COMMON/PLOT/NXPL10(31),NYPL10(31),NZPL10(31),NXPL40(31),
     /NYPL40(31),NZPL40(31),NXPL100(31),NYPL100(31),NZPL100(31),
     /NXPL400(31),NYPL400(31),NZPL400(31),NXPL1000(31),NYPL1000(31),
     /NZPL1000(31),NXPL2(31),NYPL2(31),NZPL2(31),NXPL4000(31),
     /NYPL4000(31),NZPL4000(31),NXPL10000(31),NYPL10000(31),
     /NZPL10000(31),NXPL40000(31),NYPL40000(31),NZPL40000(31),
     /NXPL100000(31),NYPL100000(31),NZPL100000(31),NRPL2(31),NRPL10(31),
     /NRPL40(31),NRPL100(31),NRPL400(31),NRPL1000(31),NRPL4000(31),
     /NRPL10000(31),NRPL40000(31),NRPL100000(31),NEPL1(100),
     /NEPL10(100),NEPL100(100),MELEC(1000),MELEC3(1000),MELEC10(1000),
     /MELEC30(1000),MELEC100(1000),MELEC300(1000)
      COMMON/BREMG/EBRGAM(10),BRDCOSX(10),BRDCOSY(10),BRDCOSZ(10),
     /BRX(10),BRY(10),BRZ(10),BRT(10),EBRTOT(6),NBREM(6)
      COMMON/CLUS/XAV(100000),YAV(100000),ZAV(100000),TAV(100000),
     /XYAV(100000),XYZAV(100000),DX(100000),DY(100000),DZ(100000),
     /DT(100000),DXY(100000),DXYZ(100000),NCL(100000),FARX1(100000)
     /,FARY1(100000),FARZ1(100000),FARXY1(100000),RMAX1(100000),
     /TSUM(100000),XNEG(100000), 
     /YNEG(100000),ZNEG(100000),EDELTA(100000),EDELTA2(100000),
     /NCLEXC(100000)
      COMMON/KSEED/NSEED
      COMMON/ECASC/NEGAS(512),LEGAS(512),IESHELL(512),IECASC
C                                                                       
C   NEW UPDATE OF CONSTANTS 2010
C
      API=DACOS(-1.0D0)                                                 
      ARY=13.60569253D0                                              
      PIR2=8.7973554297D-17                                       
      ECHARG=1.602176565D-19                                            
      EMASS=9.10938291D-31                     
      EMS=510998.928D0
      VC=299792458.0D0                       
      AMU=1.660538921D-27                                             
      BOLTZ=8.6173324D-5     
      BOLTZJ=1.3806488D-23                                              
      AWB=1.758820088D10                                              
      ALOSCH=2.6867805D19      
      RE=2.8179403267D-13    
      ALPH=137.035999074
      HBAR=6.58211928D-16                                     
      EOVM=DSQRT(2.0D0*ECHARG/EMASS)*100.0D0                            
      ABZERO=273.15D0                                                   
      ATMOS=760.0D0                                                     
      CONST1=AWB/2.0D0*1.0D-19                                          
      CONST2=CONST1*1.0D-02                                             
      CONST3=DSQRT(0.2D0*AWB)*1.0D-09                                   
      CONST4=CONST3*ALOSCH*1.0D-15                                      
      CONST5=CONST3/2.0D0
      TWOPI=2.0D0*API
      NANISO=2
      DO 55 K=1,6
      NBREM(K)=0
      EBRTOT(K)=0.0
   55 CONTINUE
      ICFLG=0
      IRFLG=0
      IPFLG=0
      IBFLG=0
      LPEFLG=0
C  --------------------------------------------       
C                                                                       
C      READ IN OUTPUT CONTROL AND INTEGRATION DATA                      
C                                                                       
      READ(5,2) NGAS,NEVENT,IMIP,NDVEC,NSEED,ESTART,ETHRM,ECUT    
    2 FORMAT(5I10,3F10.5)  
      ICOUNT=0
      IF(IMIP.EQ.1) ICOUNT=1 
      IF(NGAS.EQ.0) GO TO 99 
      IF(ESTART.GT.3.0D6.AND.IMIP.EQ.3) THEN
      WRITE(6,664) ESTART
  664 FORMAT(' PROGRAM STOPPED: X-RAY ENERGY=',D12.3,'EV. MAXIMUM ENERGY
     / 3.0MEV')
       STOP 
      ENDIF
      IF(IMIP.NE.1.AND.NEVENT.GT.10000) THEN 
       WRITE(6,665) NEVENT
  665  FORMAT(' PROGRAM STOPPED NUMBER OF EVENTS =',I7,' LARGER THAN ARR
     /AY LIMIT OF 10000')
       STOP
      ENDIF
      IF(IMIP.EQ.1.AND.NEVENT.GT.100000) THEN
       WRITE(6,666) NEVENT
  666  FORMAT(' PROGRAM STOPPED NUMBER OF EVENTS =',I7,' LARGER THAN ARR
     /AY LIMIT OF 100000')
       STOP
      ENDIF
C 
C   GAS IDENTIFIERS 
C
      READ(5,3) NGASN(1),NGASN(2),NGASN(3),NGASN(4),NGASN(5),NGASN(6)
    3 FORMAT(6I5)        
C      
C      GAS PARAMETERS
C
      READ(5,4) FRAC(1),FRAC(2),FRAC(3),FRAC(4),FRAC(5),FRAC(6),TEMPC,
     /TORR                        
    4 FORMAT(8F10.4)      
C                                                  
C      FIELD VALUES                                                    
C                                                                       
      READ(5,5) EFIELD,BMAG,BTHETA,IWRITE,IPEN                         
    5 FORMAT(3F10.3,2I5)
      READ(5,6) DETEFF,EXCWGHT,KGAS,LGAS,ICMP,IRAY,IPAP,IBRM,IECASC 
    6 FORMAT(2F10.3,7I5)
C     WRITE(6,656) IWRITE
C 656 FORMAT(' IWRITE=',I3)  
      IF(IWRITE.NE.0) OPEN(UNIT=50,FILE='DEGRAD.OUT')
C CALCULATE EFINAL FOR DELTAS OR XRAYS 
C INCREASED EFINAL CAUSED BY ELECTRIC FIELD 
      EBIG=0.05*ESTART/1000. 
      EFINAL=ESTART*1.0001+760.0*EBIG/TORR*(TEMPC+ABZERO)/293.15*EFIELD
      IF(EFINAL.LT.(1.01*ESTART)) EFINAL=1.01*ESTART 
C   CHECK INPUT
      TOTFRAC=0.0D0
      IF(NGAS.EQ.0.OR.NGAS.GT.6) GO TO 999
      DO 10 J=1,NGAS
      IF(NGASN(J).EQ.0.OR.FRAC(J).EQ.0.0D0) GO TO 999
   10 TOTFRAC=TOTFRAC+FRAC(J)
      IF(DABS(TOTFRAC-100.0D0).GT.1.D-6) GO TO 999
      LAST=0
      TMAX=100.0D0  
      NOUT=10  
      NSTEP=20000
C INITIAL ANGLES
      IF(NDVEC.EQ.1) THEN
       PHI=0.0D0                                
       THETA=0.0D0 
      ELSE IF(NDVEC.EQ.(-1)) THEN
       PHI=0.0D0
       THETA=DACOS(-1.D0)
      ELSE IF(NDVEC.EQ.0) THEN
       PHI=0.0D0
       THETA=API/2.0  
      ELSE IF(NDVEC.EQ.2) THEN
       R3=drand48(RDUM)
C  Self Added
C       PRINT * , RDUM
       PHI=TWOPI*R3
       R4=drand48(RDUM)
       THETA=DACOS(1.0D0-2.0D0*R4)  
      ELSE 
       WRITE(6,992) NDVEC
  992  FORMAT(/,2X,'DIRECTION OF BEAM NOT DEFINED NDVEC =',I5)
       STOP      
      ENDIF
C INITIAL DIRECTION COSINES FOR CASCADE CALCULATION
      DRZINIT=DCOS(THETA)
      DRXINIT=DSIN(THETA)*DCOS(PHI)
      DRYINIT=DSIN(THETA)*DSIN(PHI)
C ZERO COMMON BLOCKS OF OUTPUT RESULTS
      DO 64 J=1,10000
      MSUM(J)=0
      MCOMP(J)=0
      MRAYL(J)=0
      MPAIR(J)=0
      MPHOT(J)=0
   64 MVAC(J)=0
      DO 65 J=1,300                                                     
   65 TIME(J)=0.0D0                                                     
      DO 70 K=1,30                                                      
   70 ICOLL(K)=0  
      DO 80 K=1,512
   80 ICOLN(K)=0                 
      DO 81 K=1,60
   81 ICOLNN(K)=0                                       
      DO 100 K=1,10                                                     
  100 TCFMAX(K)=0.0D0   
C ZERO PLOT ARRAYS
      DO 110 K=1,31
      NXPL2(K)=0
      NYPL2(K)=0
      NZPL2(K)=0
      NXPL10(K)=0
      NYPL10(K)=0
      NZPL10(K)=0
      NXPL40(K)=0
      NYPL40(K)=0
      NZPL40(K)=0
      NXPL100(K)=0
      NYPL100(K)=0
      NZPL100(K)=0
      NXPL400(K)=0
      NYPL400(K)=0
      NZPL400(K)=0
      NXPL1000(K)=0
      NYPL1000(K)=0
      NZPL1000(K)=0
      NXPL4000(K)=0
      NYPL4000(K)=0
      NZPL4000(K)=0
      NXPL10000(K)=0
      NYPL10000(K)=0
      NZPL10000(K)=0
      NXPL40000(K)=0
      NYPL40000(K)=0
      NZPL40000(K)=0
      NXPL100000(K)=0
      NYPL100000(K)=0
      NZPL100000(K)=0
      NRPL2(K)=0
      NRPL10(K)=0
      NRPL40(K)=0
      NRPL100(K)=0
      NRPL400(K)=0
      NRPL1000(K)=0
      NRPL4000(K)=0
      NRPL10000(K)=0
      NRPL40000(K)=0
  110 NRPL100000(K)=0
      DO 111 K=1,100
      NEPL1(K)=0
      NEPL10(K)=0
  111 NEPL100(K)=0
      DO 112 K=1,1000
      MELEC(K)=0
      MELEC3(K)=0
      MELEC10(K)=0
      MELEC30(K)=0
      MELEC100(K)=0
  112 MELEC300(K)=0
C ZERO ARRAYS
      DO 113 KS=1,100000
      XAV(KS)=0.0
      YAV(KS)=0.0
      ZAV(KS)=0.0
      TAV(KS)=0.0
      XYAV(KS)=0.0
      XYZAV(KS)=0.0
      DX(KS)=0.0
      DY(KS)=0.0
      DZ(KS)=0.0
      DT(KS)=0.0
      DXY(KS)=0.0
      DXYZ(KS)=0.0
      FARX1(KS)=0.0
      FARY1(KS)=0.0
      FARZ1(KS)=0.0
      FARXY1(KS)=0.0
      RMAX1(KS)=0.0
      TSUM(KS)=0.0
      XNEG(KS)=0.0
      YNEG(KS)=0.0
      ZNEG(KS)=0.0
      EDELTA(KS)=0.0
      EDELTA2(KS)=0.0
      NCL(KS)=0
      NCLEXC(KS)=0
  113 CONTINUE
C ----------------------------------------------------  
C IF NSEED = 0 THEN USE STANDARD SEED VALUE =54217137
      IF(NSEED.NE.0) CALL RM48IN(NSEED,0,0)                           
C-----------------------------------------------      
C
      CORR=ABZERO*TORR/(ATMOS*(ABZERO+TEMPC)*100.0D0)                   
      AKT=(ABZERO+TEMPC)*BOLTZ
      AN1=FRAC(1)*CORR*ALOSCH                                           
      AN2=FRAC(2)*CORR*ALOSCH                                           
      AN3=FRAC(3)*CORR*ALOSCH                                           
      AN4=FRAC(4)*CORR*ALOSCH
      AN5=FRAC(5)*CORR*ALOSCH
      AN6=FRAC(6)*CORR*ALOSCH                                           
      AN=100.0D0*CORR*ALOSCH                                            
C     VAN1=FRAC(1)*CORR*CONST4*1.0D15                                   
C     VAN2=FRAC(2)*CORR*CONST4*1.0D15                                   
C     VAN3=FRAC(3)*CORR*CONST4*1.0D15                                   
C     VAN4=FRAC(4)*CORR*CONST4*1.0D15
C     VAN5=FRAC(5)*CORR*CONST4*1.0D15
C     VAN6=FRAC(6)*CORR*CONST4*1.0D15                                   
C     VAN=100.0D0*CORR*CONST4*1.0D15
      VAN1=FRAC(1)*CORR*ALOSCH*VC                                   
      VAN2=FRAC(2)*CORR*ALOSCH*VC                                   
      VAN3=FRAC(3)*CORR*ALOSCH*VC                                  
      VAN4=FRAC(4)*CORR*ALOSCH*VC
      VAN5=FRAC(5)*CORR*ALOSCH*VC
      VAN6=FRAC(6)*CORR*ALOSCH*VC                                  
      VAN=100.0D0*CORR*ALOSCH*VC
C CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
      IF(EFINAL.LE.20000.0) THEN
       ESTEP=EFINAL/DFLOAT(NSTEP)
       EHALF=ESTEP/2.0D0
       E(1)=EHALF
       GAM(1)=(EMS+E(1))/EMS
       BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
       DO 203 I=2,20000
       AJ=DFLOAT(I-1)
       E(I)=EHALF+ESTEP*AJ
       GAM(I)=(EMS+E(I))/EMS
  203  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
      ELSE IF(EFINAL.GT.20000.0.AND.EFINAL.LE.140000.) THEN
       ESTEP=1.0
       EHALF=0.5
       E(1)=EHALF
       GAM(1)=(EMS+E(1))/EMS
       BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
       DO 231 I=2,16000
       AJ=DFLOAT(I-1)
       E(I)=EHALF+ESTEP*AJ
       GAM(I)=(EMS+E(I))/EMS
  231  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
       ESTEP1=(EFINAL-16000.0)/DFLOAT(4000)
       DO 232 I=16001,20000
       AJ=DFLOAT(I-16000)
       E(I)=16000.0+AJ*ESTEP1
       GAM(I)=(EMS+E(I))/EMS
  232  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
      ELSE
       ESTEP=1.0
       EHALF=0.5
       E(1)=EHALF
       GAM(1)=(EMS+E(1))/EMS
       BET(1)=DSQRT(1.0D0-1.0D0/(GAM(1)*GAM(1)))
       DO 233 I=2,12000
       AJ=DFLOAT(I-1)
       E(I)=EHALF+ESTEP*AJ
       GAM(I)=(EMS+E(I))/EMS
  233  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
       ESTEP1=20.0
       DO 234 I=12001,16000
       AJ=DFLOAT(I-12000)
       E(I)=12000.0+AJ*ESTEP1
       GAM(I)=(EMS+E(I))/EMS
  234  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
       ESTEP2=(EFINAL-92000.0)/DFLOAT(4000)
       DO 235 I=16001,20000
       AJ=DFLOAT(I-16000)
       E(I)=92000.0+AJ*ESTEP2
       GAM(I)=(EMS+E(I))/EMS
  235  BET(I)=DSQRT(1.0D0-1.0D0/(GAM(I)*GAM(I)))
      ENDIF
C  RADIANS PER PICOSECOND                                        
      WB=AWB*BMAG*1.0D-12 
C   METRES PER PICOSECOND
      IF(BMAG.EQ.0.0D0) RETURN
      EOVB=EFIELD*1.D-9/BMAG
      RETURN
  999 WRITE(6,87) NGAS,(J,NGASN(J),FRAC(J),J=1,6) 
   87 FORMAT(3(/),4X,' ERROR IN GAS INPUT : NGAS=',I5,6(/,2X,' N=',I3,' 
     /NGAS=',I5,' FRAC=',F8.3))                                         
   99 LAST=1                                                            
      RETURN                                                            
      END 
```

```python
def SETUP(LAST):
	#IMPLICIT #real*8 (A-H,O-Z) 
	#IMPLICIT #integer*8 (I-N) 
	#integer*4 NSEED                                       
	global NGAS,NSTEP,NANISO,EFINAL,ESTEP,AKT,ARY,TEMPC,TORR,IPEN
	global ECHARG,EMASS,AMU,PIR2
	global KGAS,LGAS,DETEFF,EXCWGHT
	global NDVEC,CONST1,CONST2,CONST3,CONST4,CONST5                  
	global AN1,AN2,AN3,AN4,AN5,AN6,AN,FRAC #=[0 for x in range[6]]               
	global NGASN #=[0 for x in range[6]]                                 
	global TMAX,SMALL,API,ESTART,THETA,PHI,TCFMAX #=[0 for x in range(10)]
	global TCFMAX1,RSTART,EFIELD,ETHRM,ECUT,NEVENT,IMIP,IWRITE
	global DRXINIT,DRYINIT,DRZINIT
	global EOVB,WB,BTHETA,BMAG 
	global DOUBLE #=[[0 for x in range[6]] for y in range(20000)]
	global AVPFRAC #=[[0 for x in range(3)] for y in range(6)]
	global CMINIXSC #=[0 for x in range[6]]
	global CMINEXSC #=[0 for x in range[6]]
	global ECLOSS #=[0 for x in range[6]]
	global WPLN #=[0 for x in range[6]]
	global ICOUNT
	global OVAN1,VAN2,VAN3,VAN4,VAN5,VAN6,VAN
	global ICOLL#=[0 for x in range(30)]
	global NETOT,NPRIME,TMAX1
	global TIME #=[0 for x in range(300)]
	global NNULL,NITOT
	global ICOLN #=[0 for x i range(512)]
	global ICOLNN#=[0 for x in range(60)]
	global NREAL,NEXCTOT
	global MSUM#=[0 for x in range(10000)]
	global MCOMP#=[0 for x in range(10000)]
	global MRAYL#=[0 for x in range(10000)]
	global MPAIR#=[0 for x in range(10000)]
	global MPHOT#=[0 for x in range(10000)]
	global MVAC#=[0 for x in range(10000)]
	global BET#=[0 for x in range(2000)]
	global GAM#=[0 for x in range(20000)]
	global VC,EMS 
	global ICMP,ICFLG,IRAY,IRFLG,IPAP,IPFLG,IBRM,IBFLG,LPEFLG 
	global E #=[0 for x in range(20000)]
	global EROOT #=[0 for x in range(20000)]
	global QTOT #=[0 for x in range(20000)]
	global QREL #=[0 for x in range(20000)]
	global QINEL #=[0 for x in range(20000)]
	global QEL #=[0 for x in range(20000)]
	global NXPL10#=[0 for x in range(31)]
	global NYPL10#=[0 for x in range(31)]
	global NZPL10#=[0 for x in range(31)]
	global NXPL40#=[0 for x in range(31)]
	global NYPL40#=[0 for x in range(31)]
	global NZPL40#=[0 for x in range(31)]
	global NXPL100#=[0 for x in range(31)]
	global NYPL100#=[0 for x in range(31)]
	global NZPL100#=[0 for x in range(31)]
	global NXPL400#=[0 for x in range(31)]
	global NYPL400#=[0 for x in range(31)]
	global NZPL400#=[0 for x in range(31)]
	global NXPL1000#=[0 for x in range(31)]
	global NYPL1000#=[0 for x in range(31)]
	global NZPL1000#=[0 for x in range(31)]
	global NXPL2#=[0 for x in range(31)]
	global NYPL2#=[0 for x in range(31)]
	global NZPL2#=[0 for x in range(31)]
	global NXPL4000#=[0 for x in range(31)]
	global NYPL4000#=[0 for x in range(31)]
	global NZPL4000#=[0 for x in range(31)]
	global NXPL10000#=[0 for x in range(31)]
	global NYPL10000#=[0 for x in range(31)]
	global NZPL10000#=[0 for x in range(31)]
	global NXPL40000#=[0 for x in range(31)]
	global NYPL40000#=[0 for x in range(31)]
	global NZPL40000#=[0 for x in range(31)]
	global NXPL100000#=[0 for x in range(31)]
	global NYPL100000#=[0 for x in range(31)]
	global NZPL100000#=[0 for x in range(31)]
	global NRPL2#=[0 for x in range(31)]
	global NRPL10#=[0 for x in range(31)]
	global NRPL40#=[0 for x in range(31)]
	global NRPL100#=[0 for x in range(31)]
	global NRPL400#=[0 for x in range(31)]
	global NRPL1000#=[0 for x in range(31)]
	global NRPL4000#=[0 for x in range(31)]
	global NRPL10000#=[0 for x in range(31)]
	global NRPL40000#=[0 for x in range(31)]
	global NRPL100000#=[0 for x in range(31)]
	global NEPL1#=[0 for x in range(100)]
	global NEPL10#=[0 for x in range(100)]
	global NEPL100#=[0 for x in range(100)]
	global MELEC#=[0 for x in range(1000)]
	global MELEC3#=[0 for x in range(1000)]
	global MELEC10#=[0 for x in range(1000)]
	global MELEC30#=[0 for x in range(1000)]
	global MELEC100#=[0 for x in range(1000)]
	global MELEC300#=[0 for x in range(1000)]
	global EBRGAM#=[0 for x in range(10)]
	global BRDCOSX# =[0 for x in range(10)]
	global BRDCOSY# =[0 for x in range(10)]
	global BRDCOSZ# =[0 for x in range(10)]
	global BRX#=[0 for x in range(10)]
	global BRY#=[0 for x in range(10)]
	global BRZ#=[0 for x in range(10)]
	global BRT#=[0 for x in range(10)]
	global EBRTOT#=[0 for x in range[6]]
	global NBREM#=[0 for x in range[6]]
	global XAV#=[0 for x in range(100000)]
	global YAV#=[0 for x in range(100000)]
	global ZAV#=[0 for x in range(100000)]
	global TAV#=[0 for x in range(100000)]
	global XYAV#=[0 for x in range(100000)]
	global XYZAV#=[0 for x in range(100000)]
	global DX#=[0 for x in range(100000)]
	global DY#=[0 for x in range(100000)] 
	global DZ#=[0 for x in range(100000)]
	global DT#=[0 for x in range(100000)]
	global DXY#=[0 for x in range(100000)]
	global DXYZ#=[0 for x in range(100000)]
	global NCL#=[0 for x in range(100000)]
	global FARX1#=[0 for x in range(100000)]
	global FARY1#=[0 for x in range(100000)]
	global FARZ1#=[0 for x in range(100000)]
	global FARXY1#=[0 for x in range(100000)]
	global RMAX1#=[0 for x in range(100000)]
	global TSUM#=[0 for x in range(100000)]
	global XNEG#=[0 for x in range(100000)]
	global YNEG#=[0 for x in range(100000)]
	global ZNEG#=[0 for x in range(100000)]
	global EDELTA#[100000]
	global EDELTA2#=[0 for x in range(100000)]
	global NCLEXC#=[0 for x in range(100000)]
	global NSEED
	global NEGAS#=[0 for x in range(512)]
	global LEGAS#=[0 for x in range(512)]
	global IESHELL#=[0 for x in range(512)]
	global IECASC
	#                                                                       
	#   NEW UPDATE OF CONSTANTS 2010
	#
	API=numpy.arccos(-1.00)                                                 
	ARY=13.605692530                                              
	PIR2=8.7973554297*(10**-17)
	ECHARG=1.602176565*(10**-19)                                         
	EMASS=9.10938291*(10**-31)                     
	EMS=510998.9280
	VC=299792458.00                       
	AMU=1.660538921*(10**-27)                                             
	BOLTZ=8.6173324*(10**-5)    
	BOLTZJ=1.3806488*(10**-23)                                              
	AWB=1.758820088*(10**10)                                             
	ALOSCH=2.6867805*(10**19)     
	RE=2.8179403267*(10**-13)    
	ALPH=137.035999074
	HBAR=6.58211928*(10**-16)                                     
	EOVM=math.sqrt(2.00*ECHARG/EMASS)*100.00                            
	ABZERO=273.150                                                   
	ATMOS=760.00                                                     
	CONST1=AWB/2.00*1.0*(10**-19)                                          
	CONST2=CONST1*1.0*(10**-02)                                             
	CONST3=math.sqrt(0.20*AWB)*1.0*(10**-9)                                   
	CONST4=CONST3*ALOSCH*1.0*(10**-15)                                      
	CONST5=CONST3/2.00
	TWOPI=2.00*API
	NANISO=2
	for K in range(1,6):
		NBREM[K]=0
		EBRTOT[K]=0.0
	ICFLG=0
	IRFLG=0
	IPFLG=0
	IBFLG=0
	LPEFLG=0
	#  --------------------------------------------       
	#                                                                       
	#      READ IN OUTPUT CONTROL AND INTEGRATION DATA                      
	#                                                                       
	NGAS=int(input())
	NEVENT=int(input())
	IMIP=int(input())
	NDVEC=int(input())
	NSEED=int(input())
	ESTART=float(input())
	ETHRM=float(input())
	ECUT=float(input())
	ICOUNT=0
	if(IMIP == 1):
		ICOUNT=1 
	if(NGAS == 0):  #yet to figure out 
		LAST=1
		return  
	if(ESTART > 3.0*(10**6) and IMIP == 3):
		print(' SUBROUTINE STOPPED: X-RAY ENERGY=','%.3f' % ESTART,'EV. MAXIMUM ENERGY 3.0MEV')
		sys.exit() 
	# endif
	if(IMIP != 1 and NEVENT > 10000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',NEVENT,' LARGER THAN ARRAY LIMIT OF 10000')
		sys.exit()
	# endif
	if(IMIP == 1 and NEVENT > 100000):
		print(' SUBROUTINE STOPPED: NUMBER OF EVENTS =',NEVENT,' LARGER THAN ARRAY LIMIT OF 100000')
		sys.exit()
	# endif
	# 
	#   GAS IDENTifIERS 
	#
	for i in range(1,6):
		NGASN[i]=int(input())
	#      
	#      GAS PARAMETERS
	#
	for i in range(1,6):
		FRAC[i]=round(float(input()),4)  			#print(8'%.4f' %)      
	TEMPC=round(float(input()),4)  					#print(8'%.4f' %)      
	TORR=round(float(input()),4)                  	#print(8'%.4f' %)      

       
	#print(8'%.4f' %)      
	#                                                  
	#      FIELD VALUES                                                    
	#                                                                       
	EFIELD=round(float(input()),3)  			#print(3'%.3f' % ,2I5)
	BMAG=round(float(input()),3)			#print(3'%.3f' % ,2I5)
	BTHETA=round(float(input()),3)			#print(3'%.3f' % ,2I5)
	IWRITE=int(input())			#print(3'%.3f' % ,2I5)
	IPEN=int(input())                    			#print(3'%.3f' % ,2I5)     
	
	DETEFF=round(float(input()),3)      	# print(2'%.3f' % ,7I5)
	EXCWGHT=round(float(input()),3)			# print(2'%.3f' % ,7I5)			
	KGAS=int(input())						# print(2'%.3f' % ,7I5)
	LGAS=int(input())						# print(2'%.3f' % ,7I5)
	ICMP=int(input())						# print(2'%.3f' % ,7I5)
	IRAY=int(input())						# print(2'%.3f' % ,7I5)
	IPAP=int(input())						# print(2'%.3f' % ,7I5)
	IBRM=int(input())						# print(2'%.3f' % ,7I5)
	IECASC =int(input())					# print(2'%.3f' % ,7I5)
	#     WRITE(6,656) IWRITE
	# 656 print(' IWRITE=',I3)  
	if(IWRITE != 0):
		OPEN(UNIT=50,FILE='DEGRAD.OUT')  #yet to be
	# CALCULATE EFINAL FOR DELTAS OR XRAYS 
	# INCREASED EFINAL CAUSED BY ELECTRIC FIELD 
	EBIG=0.05*ESTART/1000. 
	EFINAL=ESTART*1.0001+760.0*EBIG/TORR*(TEMPC+ABZERO)/293.15*EFIELD
	if(EFINAL < (1.01*ESTART)):
		EFINAL=1.01*ESTART 
	#   CHECK INPUT
	TOTFRAC=0.00
	if(NGAS == 0 or NGAS > 6):
			GOTO999()
	for J in range(1,NGAS):
		if(NGASN[J]== 0 or FRAC[J] == 0.00):
			GOTO999()
		TOTFRAC=TOTFRAC+FRAC[J]
	if(abs(TOTFRAC-100.00)> 1*(10**-6)):
		GOTO999()
	LAST=0
	TMAX=100.00  
	NOUT=10  
	NSTEP=20000
	# INITIAL ANGLES
	if(NDVEC): #22594
		PHI=0
		THETA=0
	else if(NDVEC==-1):
		PHI=0
		THETA=numpy.arccos(-1)
	else if(NDVEC==0):
		PHI=0.0
		THETA=API/2.0
	else if(NDVEC==2):
		R3=DRAND48(0.0,1.0)
		PHI=TWOPI*R3
		R4=DRAND48(1.5, 1.9)
		THETA=numpy.arccos(1.0-2.0*R4)
	else :
		print('DIRECTION OF BEAM NOT DEFINED NDVEC =',NDVEC)
		sys.exit()

	# INITIAL DIRECTION COSINES FOR CASCADE CALCULATION
	DRZINIT= numpy.cos(THETA)
	DRXINIT= numpy.sin(THETA)*numpy.cos(PHI)
	DRYINIT=numpy.sin(THETA)*numpy.sin(PHI)
	# ZERO COMMON BLOCKS OF OUTPUT RESULTS
	for J in range(1,10000):
		MSUM[J]=0
		MCOMP[J]=0
		MRAYL[J]=0
		MPAIR[J]=0
		MPHOT[J]=0
		MVAC[J]=0

	for J in range(1,300):
		TIME[J]=0
	for K in range(1,30):
		ICOLL[K]=0
	for K in range(1,512):
		ICOLN[K]=0
	for K in range(1,60):
		ICOLNN[K]=0
	for in range(1,10):
		TCFMAX[K]=float(0)
	# ZERO PLOT ARRAYS
	for K in range(1,31):
		NXPL2[K]=0
		NYPL2[K]=0
		NZPL2[K]=0
		NXPL10[K]=0
		NYPL10[K]=0
		NZPL10[K]=0
		NXPL40[K]=0
		NYPL40[K]=0
		NZPL40[K]=0
		NXPL100[K]=0
		NYPL100[K]=0
		NZPL100[K]=0
		NXPL400[K]=0
		NYPL400[K]=0
		NZPL400[K]=0
		NXPL1000[K]=0
		NYPL1000[K]=0
		NZPL1000[K]=0
		NXPL4000[K]=0
		NYPL4000[K]=0
		NZPL4000[K]=0
		NXPL10000[K]=0
		NYPL10000[K]=0
		NZPL10000[K]=0
		NXPL40000[K]=0
		NYPL40000[K]=0
		NZPL40000[K]=0
		NXPL100000[K]=0
		NYPL100000[K]=0
		NZPL100000[K]=0
		NRPL2[K]=0
		NRPL10[K]=0
		NRPL40[K]=0
		NRPL100[K]=0
		NRPL400[K]=0
		NRPL1000[K]=0
		NRPL4000[K]=0
		NRPL10000[K]=0
		NRPL40000[K]=0
		NRPL100000[K]=0 #22678
	for K in range(1,100):
		NEPL1[K]=0
		NEPL10[K]=0
		NEPL100[K]=0
	for K in range(1,1000):
		MELEC[K]=0
		MELEC3[K]=0
		MELEC10[K]=0
		MELEC30[K]=0
		MELEC100[K]=0
		MELEC300[K]=0 #22689
	# C ZERO ARRAYS
	for KS in range(1,100000):
		XAV[KS]=0.0
		YAV[KS]=0.0
		ZAV[KS]=0.0
		TAV[KS]=0.0
		XYAV[KS]=0.0
		XYZAV[KS]=0.0
		DX[KS]=0.0
		DY[KS]=0.0
		DZ[KS]=0.0
		DT[KS]=0.0
		DXY[KS]=0.0
		DXYZ[KS]=0.0
		FARX1[KS]=0.0
		FARY1[KS]=0.0
		FARZ1[KS]=0.0
		FARXY1[KS]=0.0
		RMAX1[KS]=0.0
		TSUM[KS]=0.0
		XNEG[KS]=0.0
		YNEG[KS]=0.0
		ZNEG[KS]=0.0
		EDELTA[KS]=0.0
		EDELTA2[KS]=0.0
		NCL[KS]=0
		NCLEXC[KS]=0 ##22716 #22915
	# ----------------------------------------------------  
	# if NSEED = 0 : USE STANDARD SEED VALUE =54217137
	if(NSEED != 0):
		RM48(NSEED,0,0)                           
	#-----------------------------------------------      
	#
	CORR=ABZERO*TORR/(ATMOS*(ABZERO+TEMPC)*100.00)                    #check precision
	AKT=(ABZERO+TEMPC)*BOLTZ
	AN1=FRAC[1]CORR*ALOSCH                                           
	AN2=FRAC[2]CORR*ALOSCH                                           
	AN3=FRAC[3]CORR*ALOSCH                                           
	AN4=FRAC[4]CORR*ALOSCH
	AN5=FRAC[5]CORR*ALOSCH
	AN6=FRAC[6]CORR*ALOSCH                                           
	AN=float(100.00*CORR*ALOSCH)
	AN=100.00*CORR*ALOSCH                                            
	#VAN1=FRAC[1]*CORR*CONST4*1.0D15                                   
	#VAN2=FRAC[2]*CORR*CONST4*1.0D15                                   
	#VAN3=FRAC(3)*CORR*CONST4*1.0D15                                   
	#VAN4=FRAC[4]*CORR*CONST4*1.0D15
	#VAN5=FRAC[5]*CORR*CONST4*1.0D15
	#VAN6=FRAC[6]*CORR*CONST4*1.0D15                                   
	#VAN=100.00*CORR*CONST4*1.0D15
	VAN1=FRAC[1]*CORR*ALOSCH*VC                                   
	VAN2=FRAC[2]*CORR*ALOSCH*VC                                   
	VAN3=FRAC[3]*CORR*ALOSCH*VC                                  
	VAN4=FRAC[4]*CORR*ALOSCH*VC
	VAN5=FRAC[5]*CORR*ALOSCH*VC
	VAN6=FRAC[6]*CORR*ALOSCH*VC                                  
	VAN=float(100.00*CORR*ALOSCH*VC)    #22745 #22945
	# CALCULATE AND STORE ENERGY GRID FOR XRAYS BETAS OR PARTICLES
	 
	if(EFINAL <= 20000.0):
		ESTEP=float(EFINAL/float(NSTEP))
		EHALF=float(ESTEP/2.00)
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))  #ifcontinues
		for I in range(2,20000):                      #ifcontinues
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	else if(EFINAL > 20000.0 and EFINAL <= 140000.) :
		ESTEP=1.0
		EHALF=0.5
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for i in range(2,16000):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))   #22768 #22968  
		ESTEP1=(EFINAL-16000.0)/float(4000)
		for I in range(16001,2000):
			AJ=float(I-16000)
			E[I]=16000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]=math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	else:
		ESTEP=1.0
		EHALF=0.5
		E[1]=EHALF
		GAM[1]=(EMS+E[1])/EMS
		BET[1]=math.sqrt(1.00-1.00/(GAM[1]*GAM[1]))
		for I in range(2,12000):
			AJ=float(I-1)
			E[I]=EHALF+ESTEP*AJ
			GAM[I]=(EMS+E[I])/EMS
			BET[I]math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
		ESTEP1=20.0
		for I in range(12001,16000):
			AJ=float(I-12000)
			E[I]=12000.0+AJ*ESTEP1
			GAM[I]=(EMS+E[I])/EMS
			BET[I]math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
		ESTEP2=(EFINAL-92000.0)/float(4000)
		for I in range(16001,20000):
			AJ=float(I-16000)
			E[I]=92000.0+AJ*ESTEP2
			GAM[I]=(EMS+E[I])/EMS
			BET[I]math.sqrt(1.00-1.00/(GAM[I]*GAM[I]))
	# endif
	#  RADIANS PER PICOSECOND                                        
	WB=AWB*BMAG*1.0*(10**-12 )
	#   METRES PER PICOSECOND
	if(BMAG == 0.00):
		return
	EOVB=EFIELD*1*(10**-9)/BMAG
	return
	print(' ERROR IN GAS INPUT : NGAS=',NGAS,'\n')
	for J in range(1,6):
		print(' N=',J,' NGAS=',NGASN[J],' FRAC=',FRAC[J])
	LAST=1                                                            
	return                                                            
	# end                                                               
```

The SETUP() function handles the gas inputs

### Arguments

| Argument |          Description          |
|----------|-------------------------------|
| LAST     | 1 -> end the program          |
|          | 0 -> keep the Program running |
|          |                               |

### Pseudo Code

* (Input Card 1)

| Variables |                          Description                          |
|-----------|---------------------------------------------------------------|
| NGAS      | Number of Gases                                               |
|           |                                                               |
| NEVENT    | Event Number                                                  |
|           |                                                               |
| IMIP      | = 1 Mips Simulation  (dE/dX, Clusters)                        |
|           | = 2 Electron Beam  (Total Absorption)                         |
|           | = 3 X-ray                                                     |
|           | = 4 Beta Decay                                                |
|           | = 5 Double Beta Decay                                         |
|           |                                                               |
| NDVEC     | = 2 Mip X-ray or Beta in Random Direction                     |
|           | = 1 Mip X-ray or Beta Direction Parallel to E-field (Z)       |
|           | =-1 Mip X-ray or Beta Direction Anti Parallel to E-field (-z) |
|           | = 0 Mip X-ray or Beta in Random Direction in X-y Plane        |
|           |                                                               |
| NSEED     | = 0 Uses Standard Seed Value = 54217137                       |
|           | != 0 Uses Value of NSEED as Seed Value                        |
|           |                                                               |
| ESTART    | Starting energy of the chosen IMIP ( MIP                      |
|           | electron,beta Decay or X-ray Energy in eV).                   |
|           | Note Double Beta Decay Energy Is to Be Entered as the         |
|           | Energy of Each Beta (0.5 Times Total Decay Energy)            |
|           | (if X-ray Max Energy=2.0 MeV)                                 |
|           |                                                               |
| ETHRM     | Electrons Tracked Until They Fall to This Energy eV.          |
|           | for Fast Calculation the Thermalisation Energy Should         |
|           | Be Set to the Lowest Ionisation Potential in the Gas Mixture. |
|           | for More Accurate Thermalisation Range the Thermalisation     |
|           | Energy Should Be Set to the Lowest Excitation Energy in       |
|           | Pure Noble Gases or to 2.0 eV for Mixtures With Molecular Gas |
|           |                                                               |
| ECUT      | For Mips only. Applies Energy Cut in eV to Give the           |
|           | Maximum Allowed Primary Cluster Energy ( Should Be Set        |
|           | to Less Than 10000 eV to Give Maximum Primary Cluster Size)   |
|           | of Typically 400 Electrons                                    |
|           |                                                               |

* If number of gases is 0, then LAST =1 ( and end the program)
* If X-Ray and Start energy ESTART > 3 MeV then stop program
* Stop if event limit NEVENT exceeded
  * non-MIPS Simulation:Limit for number of events = 10000 
  * MIPS Simulation: Limit for number of events = 100000
* Input Gas Identifiers (Input Card 2)


| Variable | Number of Inputs |               Description                |
|----------|------------------|------------------------------------------|
| NGASN    |                6 | Number to define which gas(between 1-80) |
|          |                  | see Gas-List for identifying numbers     |
|          |                  |                                          |

* Input Gas Parameters (Input Card 3)


| Variable | Number of Inputs |              Description              |
|----------|------------------|---------------------------------------|
| FRAC     |                6 | Percentage fraction of gas in mixture |
|          |                  |                                       |
| TEMP     |                1 | Temperature of Gas in Centigrade      |
|          |                  |                                       |
| TORR     |                1 | Pressure of Gas in Torr               |
|          |                  |                                       |

* Input Field values (Input Card 4)

| Variable |                        Description                        |
|----------|-----------------------------------------------------------|
| EFIELD   | Electric Field in Volts/cm                                |
|          |                                                           |
| BMAG     | Magnetic Field in Kilo Gauss                              |
|          |                                                           |
| BTHETA   | Angle between electric and magnetic fields in degrees     |
|          |                                                           |
| IWRITE   | = 0 Standard Output                                       |
|          | = 1 then                                                  |
|          | Line 1: Output no. of electrons and no. of excitations    |
|          | for each event                                            |
|          | Line 2 : Output X,Y,Z and T for each thermalised electron |
|          | = 2 then                                                  |
|          | Line 1: Output no. of electrons and no. of excitations    |
|          | for each event                                            |
|          | Line 2: Outputs X,Y,Z and T for each thermalised electron |
|          | Line 3: Outputs X,Y,Z and T for each excitation           |
|          |                                                           |
| IPEN     | = 0 No Penning transfers                                  |
|          | = 1 Penning transfers allowed                             |
|          |                                                           |

* (Input Card 5) 

| Variable | Input type |                Description                |
|----------|------------|-------------------------------------------|
| DETEFF   | float .3f  | Detection efficiency of photons. Used for |
|          |            | calculation of FANO factors for combined  |
|          |            | electron and photon detection in pure     |
|          |            | noble gases (Between 0.0 - 100.0)         |
|          |            |                                           |
| EXCWGHT  | float .3f  | Weight given to excitation events in      |
|          |            | FANO calculation with respect to          |
|          |            | ionisation. Typically 0.5 - 0.6           |
|          |            | Use weight given by SQRT((Fele)/(Fexc))   |
|          |            | Fele = Electron FANO factor               |
|          |            | Fexc = Electron FANO factor               |
|          |            |                                           |
| KGAS     | int        | Gas identifier for which gas in mixture   |
|          |            | has Beta decayed.                         |
|          |            | Identifier Numbers : NGAS1 etc.           |
|          |            |                                           |
| LGAS     | int        | If molecular gas : LGAS identifies        |
|          |            | the component atom in the molecule        |
|          |            | which has Beta decayed :                  |
|          |            | E.g. in CO2 1 = Carbon 2 = Oxygen         |
|          |            | in CF4 1 = Carbon 2 = Fluorine            |
|          |            |                                           |
| LCMP     | int        | =0 No Compton Scattering                  |
|          |            | =1 Include Compton Scattering             |
|          |            |                                           |
| LRAY     | int        | =0 No Rayleigh Scattering                 |
|          |            | =1 Include Rayleigh Scattering            |
|          |            |                                           |
| LPAP     | int        | =0 No pair production                     |
|          |            | =1 Include pair production                |
|          |            |                                           |
| LBRM     | int        | =0 No Bremsstrahlung                      |
|          |            | =1 Include Bremsstrahlung                 |
|          |            |                                           |
| IECASC   | int        | =0 Use parameterised cascade for          |
|          |            | 2nd to n^(th) generation of electron      |
|          |            | ionising collisions.                      |
|          |            | =1 Use exact cascade for 2nd to nth       |
|          |            | generation of electron ionising           |
|          |            | collisions.                               |
|          |            |                                           |# Kittens

## Get All Kittens

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get()
```

```shell
curl "http://example.com/api/kittens"
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let kittens = api.kittens.get();
```

> The above command returns JSON structured like this:

```json
[
  {
    "id": 1,
    "name": "Fluffums",
    "breed": "calico",
    "fluffiness": 6,
    "cuteness": 7
  },
  {
    "id": 2,
    "name": "Max",
    "breed": "unknown",
    "fluffiness": 5,
    "cuteness": 10
  }
]
```

This endpoint retrieves all kittens.

### HTTP Request

`GET http://example.com/api/kittens`

### Query Parameters

Parameter | Default | Description
--------- | ------- | -----------
include_cats | false | If set to true, the result will also include cats.
available | true | If set to false, the result will include kittens that have already been adopted.

<aside class="success">
Remember — a happy kitten is an authenticated kitten!
</aside>

## Get a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.get(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.get(2)
```

```shell
curl "http://example.com/api/kittens/2"
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.get(2);
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "name": "Max",
  "breed": "unknown",
  "fluffiness": 5,
  "cuteness": 10
}
```

This endpoint retrieves a specific kitten.

<aside class="warning">Inside HTML code blocks like this one, you can't use Markdown, so use <code>&lt;code&gt;</code> blocks to denote code.</aside>

### HTTP Request

`GET http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to retrieve

## Delete a Specific Kitten

```ruby
require 'kittn'

api = Kittn::APIClient.authorize!('meowmeowmeow')
api.kittens.delete(2)
```

```python
import kittn

api = kittn.authorize('meowmeowmeow')
api.kittens.delete(2)
```

```shell
curl "http://example.com/api/kittens/2"
  -X DELETE
  -H "Authorization: meowmeowmeow"
```

```javascript
const kittn = require('kittn');

let api = kittn.authorize('meowmeowmeow');
let max = api.kittens.delete(2);
```

> The above command returns JSON structured like this:

```json
{
  "id": 2,
  "deleted" : ":("
}
```

This endpoint deletes a specific kitten.

### HTTP Request

`DELETE http://example.com/kittens/<ID>`

### URL Parameters

Parameter | Description
--------- | -----------
ID | The ID of the kitten to delete

