#This python script contains all of the plotting routines for Langevin simualtions
#
#Steven Large
#June 4th 2018

import os
import matplotlib.pyplot as plt
#import seaborn as sns
from Parameters import *

def PlotSimulationData(Position_Eq,Velocity_Eq,CP_Eq,Position,Velocity,CP):

	#sns.set(style='darkgrid',color_codes=True)

	TimeRange = []
	time = 0

	for index in range(len(Position_Eq)):
		TimeRange.append(time)
		time += dt

	fig,ax = plt.subplots(2,3)

	ax[0,0].plot(TimeRange,Position_Eq,color='b',linewidth=1.5,alpha=0.6)
	ax[0,1].plot(TimeRange,Velocity_Eq,color='g',linewidth=1.5,alpha=0.6)
	ax[0,2].plot(TimeRange,CP_Eq,color='r',linewidth=1.5,alpha=0.6)

	ax[1,0].plot(TimeRange,Position,color='b',linewidth=1.5,alpha=0.6)
	ax[1,1].plot(TimeRange,Velocity,color='g',linewidth=1.5,alpha=0.6)
	ax[1,2].plot(TimeRange,CP,color='r',linewidth=1.5,alpha=0.6)

	ax[0,0].set_title(r"Position equilibration",fontsize=16)
	ax[0,1].set_title(r"Velocity equilibration",fontsize=16)
	ax[0,2].set_title(r"$\lambda$ equilibration",fontsize=16)

	ax[1,0].set_title(r"Position dynamics",fontsize=16)
	ax[1,1].set_title(r"Velocity dynamics",fontsize=16)
	ax[1,2].set_title(r"$\lambda$ dynamics",fontsize=16)

	ax[1,0].set_xlabel(r"Time $t$",fontsize=16)
	ax[1,0].set_ylabel(r"Position $x$",fontsize=16)

	ax[1,1].set_ylabel(r"Velocity $\dot{x}$",fontsize=16)

	ax[1,2].set_ylabel(r"Control parameter $\lambda$",fontsize=16)	

	plt.savefig("Plots/TrajectoryData.pdf",fmt="pdf")

	plt.show()
	plt.close()



