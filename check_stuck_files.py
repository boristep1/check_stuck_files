#! python3

import os
import sys
import re
from datetime import datetime
from datetime import timezone
from datetime import timedelta

import csf_config


# check if file is stuck
def check_file(inf, logf, ilist, folder,file):

# check if file exists in permanent list (regexp)
    for fexp in csf_config.PERMANENT_FILES:
        p = re.compile(fexp)
        m = p.match(file)
        if m != None:
            print('match-', m, ' to ', fexp)
            return

# write the file name and created time
    path2file = folder+'\\'+file
    statinfo = os.stat(path2file)
    ctime = statinfo.st_ctime
    rec = path2file+' '+str(ctime)
    inf.write(rec +'\n')

    for sfile in ilist:
        if sfile == rec :
            # write to LOG
            logf.write(rec +'\n')
            break


def check_folder(inf,logf, ilist, folder):
    cont = 0
    for folderName, subfolders, filenames in os.walk(folder):
        try:
            csf_config.EXCLUDE_FOLDERS.index(folderName)
            cont = 0
        except ValueError:
            cont = 1
        if cont == 0:
            continue


        for filename in filenames:
            check_file(inf,logf, ilist, folderName,filename)

def build_ilist(inf ):

    try:
        # save result of the previous run to list
      ilist = [line.rstrip('\n') for line in inf]

        # clean the file by reopen command
      return(ilist)
    except IOError:
        #todo write to log
        print ("Could not read file:")
        sys.exit()

def main():

    logf = open(csf_config.LOGF, 'w')
    inf = open(csf_config.INTERIM)
    ilist  =  build_ilist(inf)
    inf.close()
    inf = open(csf_config.INTERIM, 'w')
    for folder in csf_config.MFOLDERS:
        check_folder(inf, logf, ilist, folder)


if __name__=="__main__":
    main()