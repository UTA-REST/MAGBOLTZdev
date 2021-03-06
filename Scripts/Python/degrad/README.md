
# GasSimulator 
The aim of this repo is to build a tool and a semi-automated algorithm, to convert FORTRAN code to python<br>

## RECENT <br>
broken into rough modules:<br>
Globals in : <br>
* conf.py
* casrs.py
* Inthrm1.py

Structure :
* degrad1.py + Setup.py + Density.py + Mixerc.py + Mixer.py + Cascdat.py + Gasmix.py + Fldist.py + Abso.py + Stats.py +Stats2.py + Printer.py + Mipcalc.py + Control0.py + Control.py + Shake.py + Casstoree.py + Casstore.py + Outputc.py + Casres.py + CsstfbN.py + Compress.py + Bremscasc.py + Controlb.py + Calcb.py + Cascadee.py + Controle.py + CalcbN.py + csstfNe.py + Compresse.py + Splitn.py + Montefc.py + Montefx.py + csstfN.py + Calcn.py + Gasmixc.py + cgasn.py + gasn.py 
<br>
Added f2py interface example code in testing directory. Code file -> ftype .
Terminal Screenshot -> Screenshot <br>

magboltz.py is the lastest conversion <br>

### Features of change.py currently : <br>
1.map arithematical operators from FORTRAN to corresponding in python <br>
2.map logical operators from FORTRAN to corresponsing operators in python <br>
3.retain comments as comments<br>
4.map dabs,dsqrt,dlog,dexp functions correctly<br>
5.replace FORTRAN do to Python for-loop<br>
6.replace irrelevant conditions like endif <br>
7.add : after function definition<br>
8.remove datatype declarations<br>

### TODO
* Make globals by namespace
* document the technique to replicate logic in python
  * namespace variables are same in order despite of the variable name
  * each function has only unique variable names
* use a new documentation framework because slate is taking time to load
* re-write tests
* formulate graphs to be plotted
* setup a debugger environment for fortran- with complete tutorial


## Installing F2Py<br>

    cd testing/F2PY-2.45.241_1926<br>
    sudo python setup.py install<br>
    cd ../scipy_distutils-0.3.3_34.586<br>
    sudo python setup.py install<br>

## Using input interface of degrad <br>
### Installation 
 
    sudo pip3 install --user pyqt5  
    sudo apt-get install python3-pyqt5  
    sudo apt-get install pyqt5-dev-tools
    sudo apt-get install qttools5-dev-tools
    
### Tutorial PyQt5
<ul>
<li> 
	<a href="http://zetcode.com/gui/pyqt5/firstprograms/"> http://zetcode.com/gui/pyqt5/firstprograms/</a>

</ul>

## Notes
### WRITE FORMAT
   A - text string<br>
   D - double precision numbers, exponent notation<br>
   E - real numbers, exponent notation<br>
   F - real numbers, fixed point format<br>
   I - integer<br>
   X - horizontal skip (space)<br>
   / - vertical skip (newline)<br>

