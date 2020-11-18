import sys,os
from modules.handler import clone_from_dir
from dotenv import load_dotenv

def clone(args):
    len_args=len(args)
    src=args[0]
    cwd=os.getcwd()
    
    if ":" not in src:
        load_dotenv()
        perm_back=str(os.getenv('Permanent_Backup'))
        src=perm_back+src

    if len_args==1:
        dest="."
    
    elif len_args==2:
        dest=cwd+"\\"+args[1]
        
    clone_from_dir(src=src,dest=dest)


if __name__ == '__main__':
    main()