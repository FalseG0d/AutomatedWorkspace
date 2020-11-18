import sys
from commands.rolling_backup import rolling_backup
from commands.clone import clone

def main():
      args = sys.argv[1:]

      if args[0]=="rolling_backup":
            args=sys.argv[2:]
            rolling_backup(args)
      elif args[0]=="clone":
            args=sys.argv[2:]
            clone(args)
      else:
            print("Command Not Recognized")


if __name__ == '__main__':
    main()