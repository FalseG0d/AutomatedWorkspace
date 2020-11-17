import sys
from modules.scheduler import Scheduler

def main():
      args = sys.argv[1:]

      len_args=len(args)

      if len_args==0:
            working_dir="."
            target_dir="F:\Backups\Rolling"
            interval=5
      elif len_args==1:
            working_dir="."
            target_dir="F:\Backups\Rolling"
            interval=int(args[0])
      elif len_args==2:
            working_dir="."
            target_dir=args[0]
            interval=int(args[1])
      elif len_args==3:
            working_dir=args[0]
            target_dir=args[1]
            interval=int(args[2])
            
      if working_dir==target_dir:
            print("Invalid Target Directory")
            return
            
      sc=Scheduler(interval=interval,start=0,pwd=working_dir,twd=target_dir)


if __name__ == '__main__':
    main()