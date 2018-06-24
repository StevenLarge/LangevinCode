#This python script generates an equilibrium trajectory of a Langevin system and then estimates the force autocorrelation function
#
#Steven Large
#June 14th 2018

import os
import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD
#import seaborn as sns
=======
import seaborn as sns
>>>>>>> 4b5dc44734ef40de40b844d30abdaa518108eb92

import LangevinPropagator
from Parameters import *
import ReadWrite


def CalculateFriction(CorrArray,LagTime):

	Friction = 0

	for index in range(len(CorrArray)-1):
		Friction += 0.5*(CorrArray[index+1] + CorrArray[index])*dt

	return Friction


ForceTracker = []

MaxLag = 25							#Maximum simulated time lag for correlation function
<<<<<<< HEAD
TotalStatistics = 10000 			#Total number of statistics obtained for each lag time
=======
TotalStatistics = 10000000 			#Total number of statistics obtained for each lag time
>>>>>>> 4b5dc44734ef40de40b844d30abdaa518108eb92
StatCount = 0
ForceAccumulator = 0	 			#Accumulator variable for calculating the average force

position = 0
velocity = 0
CP = 0
time = 0

ForceArray = []
CorrArray = []
LagTime = []

Equilibration = 100

WritePath = "Friction"
WriteName_Friction = "GeneralizedFriction.dat"
WriteName_Correlation = "ForceCorrelation.dat"


#----- Equilibrate the initial conditions -----#

while time < Equilibration:
	time,position,velocity = LangevinPropagator.Equilibration(time,position,velocity,CP)

time = 0 																					#Reset the time variable


#----- Initialize the force array with equilibrium values -----#

while time < MaxLag:
	time,position,velocity = LangevinPropagator.Equilibration(time,position,velocity,CP)
	Force = -k*(position - CP)
	ForceArray.insert(0,Force)
	CorrArray.append(0.0)
	LagTime.append(time)


#----- Obtain TotalStatistics number of data points for each lag time in the correlation function -----#

while StatCount < TotalStatistics:

	time,position,velocity = LangevinPropagator.Equilibration(time,position,velocity,CP)
	Force = -k*(position - CP)
	ForceAccumulator += Force

	ForceArray.pop(len(ForceArray)-1)
	ForceArray.insert(0,Force)

	for index in range(len(ForceArray)):
		CorrArray[index] += ForceArray[0]*ForceArray[index]

	StatCount += 1

MeanForce = ForceAccumulator/TotalStatistics 												#Calculate Mean force sampled

for index in range(len(CorrArray)):
	CorrArray[index] = (CorrArray[index] - MeanForce*MeanForce)/TotalStatistics 			#Normalize the Correlation Array and subtract off the mean squared force

Friction = CalculateFriction(CorrArray,LagTime) 											#Calculate the generalized friction by integrating the correlation function

<<<<<<< HEAD
print("\n\n\tGeneralized Friction --> " + str(Friction) + "\n\n")
=======
print "\n\n\tGeneralized Friction --> " + str(Friction) + "\n\n"
>>>>>>> 4b5dc44734ef40de40b844d30abdaa518108eb92

ReadWrite.WriteCorrelation(WritePath,WriteName_Correlation,CorrArray,LagTime)
ReadWrite.WriteFriction(WritePath,WriteName_Friction,Friction,CP)

<<<<<<< HEAD
#sns.set(style='darkgrid',color_codes=True,palette='muted')
=======
sns.set(style='darkgrid',color_codes=True,palette='muted')
>>>>>>> 4b5dc44734ef40de40b844d30abdaa518108eb92

fig,ax = plt.subplots(1,2)

ax[0].plot(LagTime,CorrArray,linewidth=3.0)
ax[0].set_xlabel(r'Lag time $t$',fontsize=16)
ax[0].set_ylabel(r'$\langle\delta f(0)\delta f(t)\rangle_{\lambda}$',fontsize=16)

ax[1].plot(LagTime,CorrArray,linewidth=3.0)
ax[1].set_yscale('log')

ax[0].set_title(r"Linear Scale",fontsize=16)
<<<<<<< HEAD
ax[1].set_title(r"SemiLog-y Scale",fontsize=16)
=======
ax[1].set_title(r"Log-Log Scale",fontsize=16)
>>>>>>> 4b5dc44734ef40de40b844d30abdaa518108eb92

plt.show()
plt.close()


