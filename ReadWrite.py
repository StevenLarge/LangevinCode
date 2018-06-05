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



