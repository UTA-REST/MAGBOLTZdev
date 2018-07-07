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
