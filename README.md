# check_stuck_files
Monitoring file transfer directory for stack files

The core business system creates files in a folder (and in its subfolders). A managed file transfer program monitors these folders and transfers all the files to their target. Upon completion of the file transfer, the files are erased from the folder.
The program checks the folders for stuck files.
The external scheduler runs the program every N minutes. If any file exists during two consecutive runs, then this file is marked as stuck. 
