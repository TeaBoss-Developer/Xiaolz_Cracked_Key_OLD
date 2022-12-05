import datetime

def time_alert(begin_time,endtime):
    if (int(float(endtime))*1000 > int(float(begin_time))*1000):
        value = (int(float(endtime))*1000) - (int(float(begin_time))*1000)
        day = int(value/(24*3600*1000))
        buf = value%(24*3600*1000)
        hours = int(buf/(3600*1000))
        buf1 = buf%(3600*1000)
        min = int(buf1/(60*1000))
        buf2 = buf1%(60*1000)
        s = int(buf2/1000)
        ms = s%1000
        return(str(day)+" "+str(hours)+" "+str(min)+" "+str(s)+" "+str(ms))
    if (int(float(endtime))*1000 < int(float(begin_time))*1000):
        value = (int(float(endtime))*1000) - (int(float(begin_time))*1000)
        day = int(value/(24*3600*1000))
        buf = value%(24*3600*1000)
        hours = int(buf/(3600*1000))
        buf1 = buf%(3600*1000)
        min = int(buf1/(60*1000))
        buf2 = buf1%(60*1000)
        s = int(buf2/1000)
        ms = s%1000
        return("-"+str(day)+" -"+str(hours)+" -"+str(min)+" -"+str(s)+" -"+str(ms))
def gethour():
    a = str(datetime.datetime.now())
    return(a[11:13])
def gettime():
    return(int(datetime.datetime.now().timestamp()))
