import os
import matplotlib.pyplot as plt
from tcx2dict import *

FILEDIRECTORY='./example_data'
FILENAME='act1.tcx'
FILEPATH=os.path.join(FILEDIRECTORY, FILENAME)

#Write a function for the heart rate zone grouping
#make it a class
#add some methods

def plot_test(Dict):
    "Plot HR vs Distance in Bars And simple diagram"
    x=[]
    y=[]
    for key in sorted(Dict):
        x.append(int(Dict[key][1]))
        y.append(int(Dict[key][2]))
    plt.subplot(2,1, 1)
    plt.bar(x,y,10,color="brown")
    plt.subplot(2,1, 2)
    plt.plot(x,y,'r-')
    #plt.axis([0, 6000, 0, 200])
    plt.title('Heart Rate Values vs Distance')
    plt.ylabel('Heart Rate Values (bpm)')
    plt.xlabel('Distance (m)')
    plt.show()

def HRperZone(Dict):
    # Pie chart of HR Zones
    labels = 'Zone 1', 'Zone 2', 'Zone 3', 'Zone 4','Zone 5','Danger'
    zone1=0
    zone2=0
    zone3=0
    zone4=0
    zone5=0
    zone6=0

    def get_autopct(values):
        def cs_autopct(apct):
            suma = sum(values)
            perc = int(round(apct*suma/100.0))
            return '{p:.2f}%  ({v:d})'.format(p=apct,v=perc)
        return cs_autopct

    for key in Dict:
        if int(Dict[key][2])   < 135: zone1+=1
        elif int(Dict[key][2]) < 147: zone2+=1
        elif int(Dict[key][2]) < 159: zone3+=1
        elif int(Dict[key][2]) < 172: zone4+=1
        elif int(Dict[key][2]) < 183: zone5+=1
        else: zone6+=1

    sizes = [zone1, zone2, zone3, zone4,zone5,zone6]
    explode = (0, 0.3, 0, 0,0,0.6)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct=get_autopct(sizes),shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()


#E=ttd(FILEPATH).dict_data
#plot_test(E)
#HRperZone(E)



