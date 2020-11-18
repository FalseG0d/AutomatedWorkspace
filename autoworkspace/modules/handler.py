import shutil,os
from datetime import datetime

def rolling_backup(src,dest):
    cwd=os.getcwd()
    
    project_name=cwd.split('\\')[-1]
    dest+="\\"+project_name
    
    cwd+="\\"
    
    if ':' in src:
        source=src
    else:
        source=cwd+src

    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")

    try:
        shutil.copytree(src=src,dst=dest)
        print("Backup Process Was Successfull: ",current_time)
        print("Source Folder: ",source)
        print("Destination Folder: ",dest)
    except err:
        print("Something Went Wrong In Creating The Backup At: ",current_time)
        print("Check Logs To View Last Backup:")
        print(err)


def clone_from_dir(src,dest):
    cwd=os.getcwd()
    project_name=src.split("\\")[-1]

    dest+="\\"+project_name

    if ":" not in dest:
        dest=cwd+"\\"+dest

    print("Source Folder: ",src)
    print("Destination Folder: ",dest)
    

    shutil.copytree(src=src,dst=dest)

    '''
    try:
        shutil.copytree(src=src,dst=dest)
        print("Successfull Cloned Repository")
        print("Source Folder: ",src)
        print("Destination Folder: ",dest)
    except:
        print("Something Went Wrong")
        print("Could Not Clone Repository")
        print("Source Folder: ",src)
        print("Destination Folder: ",dest)
    '''