# Open-Source Degrad and MAGBOLTZ

Magboltz and Degrad Software in Fortran.

Author: Stephen Biagi

http://magboltz.web.cern.ch/magboltz/

___

Magboltz solves the Boltzmann transport equations with numerical integration in order to simulate the interactions of electrons in gas mixtures under the influence of electric and magnetic fields.

Degrad calculates the cluster size distribution and primary cluster distribution in gas mixtures for minimum ionizing particles and X-rays.

Both of these programs were originally made in Fortran, the code is available in the links bellow.

The goal of this project is to:
- Develop and test a fully-functional python API for joint functionality of Magboltz and Degrad with optional GUI controls.
- Design optimized python implementations of their processes, joint functionality.
- Implement extensive reports of the results and complement with detailed documentation.
- Extend the interface and code modularity to allow for new functionality related to the calculation to be implemented.

Check out the 2018 GSoC project here: http://hepsoftwarefoundation.org/gsoc/2018/proposal_OpenSourceGasSim.html 

R&D of gaseous detectors requires simulations like those provided by Magboltz and Degrad. An open-source, modernized and optimized incarnation of this software would be employed in many existing R&D efforts.


In this repository, we are testing enhancements the user interface and improvements aimed at improving the running time of Degrad and Magboltz. Being built on Fortran77, and having its database integrated in the code, there is opportunity for enhancement of the functionality and modularization by the use of modern programming languages and algorithms. Moreover, that having the code connected to a user friendly GUI will encourage development of an open source version of the code.

---

# About MAGBOLTZ

[Documentation]

(http://cyclo.mit.edu/drift/www/aboutMagboltz.html)

[Article in sciencedirect]

(https://www.sciencedirect.com/science/article/pii/S0168900298012339?via%3Dihub)

The MAGBOLTZ program computes drift gas properties by numerically integrating the Boltzmann transport equation -- i.e., simulating an electron bouncing around inside a gas. By tracking how far this electron propagates, one can compute the drift velocity. By including a magnetic field, one can also calculate the Lorentz angle.

http://cyclo.mit.edu/drift/www/aboutMagboltz.html

## About our wrapper

A first step of this project, is a python wrapper to Magboltz.


## Running Instructions

REQUIREMENTS:

Please note that this python code was written using python 2.7.12.
Please also note that you might need to install gfortran to run the magboltz code.

To run this program you will need to do the following,

1) open a terminal, go to the directory where the code is
2) type "python Main.py"
3) fill inputs and press run


Alternatively,

$ gfortran <magboltz ... .f>
$ ./a.out

type in the inputs in order, hitting enter after each one.

## Current plans for Magboltz

Currently Magboltz uses a set of arrays as its database. A more modular database system is being built.
It is possible that the current Magboltz Gas functions may be minimized to a single standardized gas function dependent on the gas evaluated. This standardized gas function is expected to enhance the running times.
