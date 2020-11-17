import sched, time
from modules.handler import rolling_backup

s = sched.scheduler(time.time, time.sleep)

class Scheduler:
    def __init__(self,interval,start,pwd,twd):
        self.interval=interval*60
        self.start=start
        self.func=rolling_backup

        self.src=pwd
        self.dest=twd

        s.enter(interval, start, self.rolling_backup, (s,))
        s.run()

    def rolling_backup(self,sc):
        self.func(self.src,self.dest)
        s.enter(self.interval, self.start, self.rolling_backup, (sc,))