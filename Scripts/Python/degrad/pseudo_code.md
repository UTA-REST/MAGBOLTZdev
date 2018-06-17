# Degrad Pseudo Code
## DEGRADE
* SETUP(LAST)
* If LAST==1 then STOP 
* DENSITY()
* CASCDAT()
* MIXERC()
* MIXER()
* FLDIST()
* If MIP simulation MIPCALC() 
* If MIP Simulation or electron beam simulation, then skip cascade calculation 
	* else :
		* CONTROL0(NEVENT,ESTART,ICON)
		* Calculate and output averages from shells
* If Magnetic Field == 0 then MONTEFA()
* If non-zero Magnetic Field then 
	* if Magnetic Field and Electric Field parallel or anti-parallel then MONTEFA()
	* else if Magnetic Field and Electric Field perpendicular then MONTEFB()
	* Any other angle between Magnetic Field and Electric Field then MONTEFC()
* STATS2()
* OUPUT()
* DEGRADE()
* STOP()

## MIXER 
* The function fills arrays of collision frequency
* Store counting ionisation X-Section in array CMINIXSC[6] at minimum ionising energy
* Initialisations 
*  


## CSSTFN (N:1-5 )
* Stores event data for N-th generation fluorescence
* Need to do globls for this 

## CALCNE (N:1-5)
* Using initial energy deposit and shell vacancy created at ISHELL :
	* Calculate Cascade in gas KGAS
	* Calculate Cascade in molecular component LGAS
* Stores photoelectron energy and angle 
* Get THET from ANGGEN function 
* Get DRXX,DRYY,DRZZ from DRCOS()
* Loop around cascade
	* Calculate energy of electron 
	* Stop if ion charge state > 28
	* Get a random emission angle 
	* Update()
		* Normalize
		* Save photon energy 
		* Random R3 and R4 
		* Find lowest vacancy 

## DRCOS
* Given direction Cosines and scattering by angle(theta,phi) 
* Calculate new direction cosines 

## ANGGEN
* Generate a random number y
* Do a Monte Carlo to return a converged theta

## SPLITN (N:1-5)
* SPLIT1 find a legitimate WPL and hence ESEC

## CALCBN (N:1-5)
* Calculate Cascade in KGAS and LGAS
* 
*
*
* same as CALCNE



