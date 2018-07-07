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

### HTTP Request

```shell
do something
```

`DELETE http://example.com/kittens/<ID>`

### Arguments

Argument | Description
--------- | -----------
no arguments | 

