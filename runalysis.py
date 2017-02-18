import os
#import time
#import numpy
#import datetime
#import dateutil.parser as dp
import tcxparser as tp
import matplotlib.pyplot as plt


FILEDIRECTORY='./data'
FILENAME='act1.tcx'
FILEPATH=os.path.join(FILEDIRECTORY, FILENAME)

dictd={}
TCX=tp.TCXParser(FILEPATH)

#Change getdata function to Recursion, to lower complexity.---Done
#Remove Global variables.
#Pass TCX as input in getdata
#Start ploting

def old_getdata():
    "Return a dictionary contains all the data from an xml file, having as key a tupple with Lap#,Trackpoint# combination"
    dictd={}
    global TCX
    for i in range(0,len(TCX.activity.Lap)):
        for j in range (0,len(TCX.activity.Lap[i].Track.Trackpoint)):
            dictd[i,j]=[TCX.activity.Lap[i].Track.Trackpoint[j].Time,TCX.activity.Lap[i].Track.Trackpoint[j].DistanceMeters,\
            TCX.activity.Lap[i].Track.Trackpoint[j].HeartRateBpm.Value]
        return dictd


def getdata(n=0,m=0):
    """
    Store tcx data in a dictionary having for key a Lap#,measurement# tupple.
    """
    try:
        global TCX
        global dictd
        dictd[n,m]=[TCX.activity.Lap[n].Track.Trackpoint[m].Time,TCX.activity.Lap[n].Track.Trackpoint[m].DistanceMeters,\
                    TCX.activity.Lap[n].Track.Trackpoint[m].HeartRateBpm.Value]
        if n==len(TCX.activity.Lap)-1:
            if m == len(TCX.activity.Lap[n].Track.Trackpoint)-1:
                return dictd
            else:
                return getdata(n,m+1)
        elif n<len(TCX.activity.Lap)-1:
            if m == len(TCX.activity.Lap[n].Track.Trackpoint)-1:
                return getdata(n+1,0)
            else:
                return getdata(n,m+1)
        else:
            raise Exception('General exceptions..')
    except ValueError as e:
        print('Value Error!?')

#Test my data in dict
#test_case=old_getdata(FILEPATH)
test_case=getdata()
print test_case

def plot_hr_dis(TCX):
    #Create time list from dict for the x axis

    for i in range(0, len(TCX.hr_values())):
        plt.bar(i,TCX.hr_values()[i],1.1, color="brown")
        #plt.plot(i,TCX.hr_values()[i],'b.')
    plt.axis([0, 550, 100, 180])
    plt.title('Heart Rate Values in relevant time')
    plt.ylabel('Heart Rate Values (bpm)')
    plt.xlabel('Time xsec')
    plt.show()

#Test my plot
#plot_hr_dis(TCX)

