#This is the primary driver for Langevin simulation code
#
#Steven Large
#June 4th 2018

import os
import matplotlib.pyplot as plt

import LangevinPropogator
import ReadWrite
import Plotting


#-----  These arrays track the position,velocity, and control parameter trajectories  -----

PositionTracker_Eq = []
VelocityTracker_Eq = []
CPTracker_Eq = []

PositionTracker = []
VelocityTracker = []
CPTracker = []

#-----  Initialize the system variables  -------

position = 0
CP = 0
velocity = 0
time = 0

#----- This is the equilibration time, 100 is somewhat arbitrary, this can be set differently, this is just to ensure that, on average
#----- each trajectory is initialized from an equilibrium ensemble of positions and velocities

EquilibrationTime = 100


#----- Protocol duration and the distance that the trap minimum moves -----

ProtocolDuration = 100
CPDistance = 10


#----- Write Paths and file names -----

WritePath = "Data"
WriteName_Position = "PositionTrajectory.dat"
WriteName_Velocity = "VelocityTrajectory.dat"
WriteName_CP = "CPTrajectory.dat"


#----- This is the constant velocity that the control parameter moves at -----

CPVel = CPDistance/float(ProtocolDuration)


#----- Equilibrate the initial state of the system -----

while time <= EquilibrationTime:
	time,position,velocity = LangevinPropogator.Equilibration(time,position,velocity,CP)
	PositionTracker_Eq.append(position)
	VelocityTracker_Eq.append(velocity)
	CPTracker_Eq.append(CP)


#----- Reset time to zero and initialize 'WorkAcc', which accumulates the work done by the control parameter over the protocol -----

time = 0
WorkAcc = 0

while time <= ProtocolDuration:
	time,position,velocity,CP,WorkStep = LangevinPropogator.Langevin(time,position,velocity,CP,CPVel)
	WorkAcc += WorkStep
	PositionTracker.append(position)
	VelocityTracker.append(velocity)
	CPTracker.append(CP)


#----- Plot trajectory data -----

Plotting.PlotSimulationData(PositionTracker_Eq,VelocityTracker_Eq,CPTracker_Eq,PositionTracker,VelocityTracker,CPTracker)


#----- Print the total work done in the protocol -----

print "TotalWork --> " + str(WorkAcc) + "\n"


#----- Write trajectory data to file -----

ReadWrite.WriteTrajectory(WritePath,WriteName_Position,PositionTracker)
ReadWrite.WriteTrajectory(WritePath,WriteName_Velocity,VelocityTracker)
ReadWrite.WriteTrajectory(WritePath,WriteName_CP,CPTracker)



