#This python script contains the Langevin dynamics propogation routines
#
#Steven Large
#June 4th 2018

import os
from math import *
import numpy as np
import random

from Parameters import *

#The Langevin integrator used in this script comes from the reference
#D.A. Sivak, J.D. Chodera, & G.E. Crooks, J. Phys. Chem. B, 2014


#----- Langevin integrator for a constant control parameter value -----

def Equilibration(time,position,velocity,CP):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*HarmonicForce(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*HarmonicForce(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity 


#----- Langevin integrator for a dynamic control parameter -----	

def Langevin(time,position,velocity,CP,CPVel):

	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1) 
	velocity = velocity + 0.5*dt*HarmonicForce(position,CP)/m
	position = position + 0.5*dt*velocity
		
	time += dt

	NewCP = CP + CPVel*dt
	WorkStep = CalcWork(position,NewCP,CP)
	CP = NewCP

	position = position + 0.5*dt*velocity 
	velocity = velocity + 0.5*dt*HarmonicForce(position,CP)/m
	velocity = sqrt(a)*velocity + sqrt((1-a)/(beta*m))*random.gauss(0,1)

	return time, position, velocity, CP, WorkStep 
	

#----- Force due to quadratic confining potential -----

def HarmonicForce(position,CP):

	return -k*(position - CP)


#----- Energy of a particular particle position due to harmonic trap -----

def HarmonicEnergy(position,CP):

	return 0.5*k*(position - CP)*(position - CP)


#----- Work done during an update to the control parameter -----

def CalcWork(position,NewCP,OldCP):

	EnergyOld = HarmonicEnergy(position,OldCP)
	EnergyNew = HarmonicEnergy(position,NewCP)

	Work = EnergyNew - EnergyOld

	return Work	

