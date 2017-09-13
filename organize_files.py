##
## It will take all the files in the directory to year/month/date formatted directory
## Just in case organize_files.py is move the the root directory this program will be ommited
##
import glob
import os
import time
from datetime import datetime
from time import gmtime, strftime
import shutil
import sys
files = glob.glob('*')
fullpath=os.path.abspath('./')
for file in files:
    create_time = datetime.fromtimestamp(os.path.getmtime(file)).strftime("%Y/%m/%d")
    if os.path.isdir(file) or os.path.basename(file)=='organize_files.py':
        continue
    if not os.path.exists(create_time):
        os.makedirs(create_time);
    dst = os.path.join(create_time,os.path.basename(file))
    shutil.move(file,dst)

