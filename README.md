# MAGBOLTZdev

In this repository, we decided to enhance the user experiance and the running time of the MAGBOLTZ code. Being built on Fortran77, and having its database integrated in its code, we believe that the MAGBOLTZ code can be enhanced by the use of modern programming languages and modern algorithms. Moreover, we also believe that having the code connected to a user friendly GUI would improve its usabilty.

# Running Instructions

REQUIREMENTS:

Please note that this python code was written using python 2.7.12.
Please also note that you might need to install gfortran to run the magboltz code.

To run this program you will need to do the following,

1) open a terminal, go to the directory where the code is
2) type "python run.py"
3) fill inputs and press run


Alternatively,

$ gfortran <magboltz ... .f>
$ ./a.out

type in the inputs in order, hitting enter after each one.

# About MAGBOLTZ

The MAGBOLTZ program computes drift gas properties by "numerically integrating the Boltzmann transport equation"-- i.e., simulating an electron bouncing around inside a gas. By tracking how far the virtual electron propagates, the program can compute the drift velocity. By including a magnetic field, the program can also calculate the Lorentz angle.

Taken from - http://cyclo.mit.edu/drift/www/aboutMagboltz.html

# About our wrapper

As a first step of this project, we decided to build a wrapper to the MAGBOLTZ code. This wrapper will enhance the user experiance as the user will have a GUI to interact with. 

# Current plans

Given that Magboltz uses an inefficient huge set of arrays as its database, we decided to build a better database system as well as modernizing the functions that call those databases. The current Magboltz "Gas functions" can be minimized to a single standardized gas function that operates depending on the gas given. This standardized gas function should dramatically enhance the running times, as well as enhance the user experiance with the whole system.
