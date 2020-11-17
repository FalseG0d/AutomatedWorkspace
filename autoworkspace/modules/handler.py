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
        print("Last Backup Created At: ",current_time)
        print("Source Folder: ",source)
        print("Destination Folder: ",dest)
    except expression as identifier:
        print("Something Went Wrong In Creating The Backup At: ",current_time)
        print("Check Logs To View Last Backup")