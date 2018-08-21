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


| Variable | Number of Inputs | Input Type |               Description                |
|----------|------------------|------------|------------------------------------------|
| NGASN    |                6 | int        | Number to define which gas(between 1-80) |
|          |                  |            | see Gas-List for identifying numbers     |
|          |                  |            |                                          |
|          |                  |            |                                          |

* Input Gas Parameters (Input Card 3)


| Variable | Number of Inputs | Input Type |              Description              |
|----------|------------------|------------|---------------------------------------|
| FRAC     |                6 | float .4f  | Percentage fraction of gas in mixture |
|          |                  |            |                                       |
| TEMPC    |                1 | float .4f  | Temperature of Gas in Centigrade      |
|          |                  |            |                                       |
| TORR     |                1 | float .4f  | Pressure of Gas in Torr               |
|          |                  |            |                                       |

* Input Field values (Input Card 4)

| Variable | Input Type |                        Description                        |
|----------|------------|-----------------------------------------------------------|
| EFIELD   | float .3f  | Electric Field in Volts/cm                                |
|          |            |                                                           |
| BMAG     | float .3f  | Magnetic Field in Kilo Gauss                              |
|          |            |                                                           |
| BTHETA   | float .3f  | Angle between electric and magnetic fields in degrees     |
|          |            |                                                           |
| IWRITE   | int        | = 0 Standard Output                                       |
|          |            | = 1 then                                                  |
|          |            | Line 1: Output no. of electrons and no. of excitations    |
|          |            | for each event                                            |
|          |            | Line 2 : Output X,Y,Z and T for each thermalised electron |
|          |            | = 2 then                                                  |
|          |            | Line 1: Output no. of electrons and no. of excitations    |
|          |            | for each event                                            |
|          |            | Line 2: Outputs X,Y,Z and T for each thermalised electron |
|          |            | Line 3: Outputs X,Y,Z and T for each excitation           |
|          |            |                                                           |
| IPEN     | int        | = 0 No Penning transfers                                  |
|          |            | = 1 Penning transfers allowed                             |
|          |            |                                                           |
|          |            |                                                           |

* (Input Card 5) 

| Variable | Input type |                        Description                        |
|----------|------------|-----------------------------------------------------------|
| DETEFF   | float .3f  | Detection efficiency of photons. Used for calculation of  |
|          |            | FANO factors for combined electron and photon detection   |
|          |            | in pure noble gases (Between 0.0 - 100.0)                 |
|          |            |                                                           |
| EXCWGHT  | float .3f  | Weight given to excitation events in FANO calculation     |
|          |            | with respect to ionisation. Typically 0.5 - 0.6           |
|          |            | Use weight given by SQRT((Fele)/(Fexc))                   |
|          |            | Fele = Electron FANO factor                               |
|          |            | Fexc = Electron FANO factor                               |
|          |            |                                                           |
| KGAS     | int        | Gas identifier for which gas in mixture has Beta decayed. |
|          |            | Identifier Numbers : NGAS1 etc.                           |
|          |            |                                                           |
| LGAS     | int        | If molecular gas : LGAS identifies the component atom in  |
|          |            | the molecule which has Beta decayed :                     |
|          |            | E.g. in CO2 1=Carbon 2=Oxygen                             |
|          |            | in CF4 1=Carbon 2=Fluorine                                |
|          |            |                                                           |
| ICMP     | int        | =0 No Compton Scattering                                  |
|          |            | =1 Include Compton Scattering                             |
|          |            |                                                           |
| IRAY     | int        | =0 No Rayleigh Scattering                                 |
|          |            | =1 Include Rayleigh Scattering                            |
|          |            |                                                           |
| IPAP     | int        | =0 No pair production                                     |
|          |            | =1 Include pair production                                |
|          |            |                                                           |
| IBRM     | int        | =0 No Bremsstrahlung                                      |
|          |            | =1 Include Bremsstrahlung                                 |
|          |            |                                                           |
| IECASC   | int        | =0 Use parameterised cascade for 2nd to n^(th) generation |
|          |            | of electron ionising collisions.                          |
|          |            | =1 Use exact cascade for 2nd to nth generation of         |
|          |            | electron ionising collisions.                             |
|          |            |                                                           |


