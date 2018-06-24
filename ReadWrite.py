#This python script contains all of the Read/Write routines for Langevin simulations
#
#Steven Large
#June 4th 2018

import os

def WriteTrajectory(Path,Filename,Data):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')

	for index in range(len(Data)):
		file1.write("%lf\n" % Data[index])

	file1.close()


def WriteCorrelation(Path,Filename,CorrArray,LagTime):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')
	for index in range(len(CorrArray)):
		file1.write("%lf\t%lf\n" % (LagTime[index],CorrArray[index]))
	file1.close()


def WriteFriction(Path,Filename,GeneralizedFriction,Lambda):

	CompleteName = os.path.join(Path,Filename)

	file1 = open(CompleteName,'w')
	file1.write('%lf\t%lf\n' % (Lambda,GeneralizedFriction))
	file1.close()



