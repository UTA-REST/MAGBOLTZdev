## FLDIST()
* Calculates fluorescence average absorption distance and loads into arrays

### Arguments

| Argument | Description |
|----------|-------------|
| NONE     | -           |
|          |             |

```fortran
      SUBROUTINE FLDIST
      IMPLICIT REAL*8 (A-H,O-Z)
      IMPLICIT INTEGER*8 (I-N)
      COMMON/IONFL/NC0(512),EC0(512),NG1(512),EG1(512),NG2(512),
     /EG2(512),WKLM(512),EFL(512)
C CALCULATE FLUORESCENCE AVERAGE ABSORPTION DISTANCE AND LOAD INTO ARRAY
	  ! PRINT *,"INSIDE FLDIST"
	  ! CALL SLEEP(2)
      DO 1 I=1,512
      EPH=EFL(I)
      ! PRINT *,EPH
      IF(EPH.EQ.0.0) GO TO 1
      JF=3
      ! PRINT *,IDUM
      ! PAUSE 1
      CALL ABSO(JF,EPH,IDUM,KDUM,LDUM,DIST)
      EFL(I)=DIST
    1 CONTINUE
      RETURN
      END
```

```python
def FLDIST():
	# IMPLICIT #real*8 (A-H,O-Z)
	# IMPLICIT #integer*8 (I-N)
	# COMMON/IONFL/
	global NC0#(512)
	global EC0#(512)
	global NG1#(512)
	global EG1#(512)
	global NG2#(512)
	global EG2#(512)
	global WKLM#(512)
	global EFL#(512)	
	NC0=conf.NC0
	EC0=conf.EC0
	NG1=conf.NG1
	EG1=conf.EG1
	NG2=conf.NG2
	EG2=conf.EG2
	WKLM=conf.WKLM
	EFL=conf.EFL
	# CALCULATE FLUORESCENCE AVERAGE ABSORPTION DISTANCE AND LOAD INTO ARRAY
	for I in range(1,512+1):
		EPH=EFL[I]
		if(EPH == 0.0):
			continue
		JF=3
		ABSO(JF,EPH,IDUM,KDUM,LDUM,DIST)
		EFL[I]=DIST

	conf.NC0=NC0
	conf.EC0=EC0
	conf.NG1=NG1
	conf.EG1=EG1
	conf.NG2=NG2
	conf.EG2=EG2
	conf.WKLM=WKLM
	conf.EFL=EFL
	return
	# end
```

