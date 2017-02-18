import os
import tcxparser as tp


class ttd():
    def __init__(self,cpath=''):
        FILEDIRECTORY='./data'
        FILENAME='act1.tcx'
        FILEPATH=os.path.join(FILEDIRECTORY, FILENAME)
        if cpath:
            FILEPATH=cpath
        self.TCX_object=tp.TCXParser(FILEPATH)
        self.dict_data={}
        self.getdata()

    def getdata(self,n=0,m=0):
        """
        Store tcx data in a dictionary having a (#Lap,#measurement#) tuple as a key.
        """
        TCX=self.TCX_object
        dictd=self.dict_data
        try:
            dictd[n,m]=[TCX.activity.Lap[n].Track.Trackpoint[m].Time,TCX.activity.Lap[n].Track.Trackpoint[m].DistanceMeters,\
                        TCX.activity.Lap[n].Track.Trackpoint[m].HeartRateBpm.Value]
            if n==len(TCX.activity.Lap)-1:
                if m == len(TCX.activity.Lap[n].Track.Trackpoint)-1:
                    return dictd
                else:
                    return self.getdata(n,m+1)
            elif n<len(TCX.activity.Lap)-1:
                if m == len(TCX.activity.Lap[n].Track.Trackpoint)-1:
                    return self.getdata(n+1,0)
                else:
                    return self.getdata(n,m+1)
            else:
                raise Exception('General exceptions..')
        except ValueError as e:
            print('Value Error!?')
