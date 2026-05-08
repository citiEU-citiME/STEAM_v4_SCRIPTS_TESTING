*cmd /c ""C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "D:/STEAM_v4_SCRIPTS_TESTING/venv/exec.py" "-p" "C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "-v" "-m" "-r" "D:/STEAM_v4_SCRIPTS_TESTING/pip-requirements.txt" "-u" "D:/STEAM_v4_SCRIPTS_TESTING/venv/venv311" "
REPORT_SCRIPT_LOCATION LOCATION_ID='RUNSTART'
; Initialization of Branch Controls:
; -------------------------------------------------------------------
; Entering Group: ROOT
; MATRIX Script
REPORT_SCRIPT_LOCATION LOCATION_ID='4'
RUN PGM=MATRIX PRNFILE="D:\STEAM_v4_SCRIPTS_TESTING\Scenarios\Base-0001\G0MATNBAPNC8ZFR.PRN" MSG='create dummy files' STEP_ID='4'




FILEO PRINTO[2] = "D:\STEAM_v4_SCRIPTS_TESTING\Scenarios\Base-0001\G0MATUGV5X4TN7I.csv"
FILEO PRINTO[1] = "D:\STEAM_v4_SCRIPTS_TESTING\Scenarios\Base-0001\G0MAT2OMQT6HPVO.csv"

FILEO MATO[1] = "D:\STEAM_v4_SCRIPTS_TESTING\Scenarios\Base-0001\G0MATBX6ZDUJ352.MAT",MO=11-15,21-25,31-35,41-45, NAME= T1P1, T1P2, T1P3, T1P4, T1P5, T2P1, T2P2, T2P3, T2P4, T2P5, T3P1, T3P2, T3P3, T3P4, T3P5, T4P1, T4P2, T4P3, T4P4, T4P5 

PAR ZONES=10


MW[11] = 1
MW[12] = 1
MW[13] = 1
MW[14] = 1
MW[15] = 1

MW[21] = 1
MW[22] = 1
MW[23] = 1
MW[24] = 1
MW[25] = 1

MW[31] = 1
MW[32] = 1
MW[33] = 1
MW[34] = 1
MW[35] = 1

MW[41] = 1
MW[42] = 1
MW[43] = 1
MW[44] = 1
MW[45] = 1


IF (I=1)
PRINT PRINTO=1, CSV=T, LIST = 'time','purp1','purp2','purp3','purp4','purp5'
PRINT PRINTO=1,FORM=4.0, CSV=T, LIST = 1,10,20,30,40,50
PRINT PRINTO=1,FORM=4.0, CSV=T, LIST = 2,10,20,30,40,50
PRINT PRINTO=1,FORM=4.0, CSV=T, LIST = 3,10,20,30,40,50
PRINT PRINTO=1,FORM=4.0, CSV=T, LIST = 4,10,20,30,40,50

PRINT PRINTO=2, CSV=T, LIST = 'purp','fact'
PRINT PRINTO=2, CSV=T, LIST = 1(4.0),0.1
PRINT PRINTO=2, CSV=T, LIST = 2(4.0),0.2
PRINT PRINTO=2, CSV=T, LIST = 3(4.0),0.3
PRINT PRINTO=2, CSV=T, LIST = 4(4.0),0.4
PRINT PRINTO=2, CSV=T, LIST = 5(4.0),0.5


ENDIF

ENDRUN
; End of MATRIX Script
; CubePy Script
REPORT_SCRIPT_LOCATION LOCATION_ID='209'
*cmd /c ""C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "D:/STEAM_v4_SCRIPTS_TESTING/venv/cubepy_exec.py" "-p" "C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "-v" "-u" "D:/STEAM_v4_SCRIPTS_TESTING/venv/venv311" "-s" "D:/STEAM_v4_SCRIPTS_TESTING/Applications/MAIN/cubepy_a-0001_run.py" "
REPORT_SCRIPT_LOCATION LOCATION_ID='IDEND:209'
if (RETURNCODE > 0) ABORT
; End of CubePy
; CubePy Script
REPORT_SCRIPT_LOCATION LOCATION_ID='219'
*cmd /c ""C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "D:/STEAM_v4_SCRIPTS_TESTING/venv/cubepy_exec.py" "-p" "C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "-v" "-u" "D:/STEAM_v4_SCRIPTS_TESTING/venv/venv311" "-s" "D:/STEAM_v4_SCRIPTS_TESTING/Applications/MAIN/cubepy_b-0001_run.py" "
REPORT_SCRIPT_LOCATION LOCATION_ID='IDEND:219'
if (RETURNCODE > 0) ABORT
; End of CubePy
; Leaving Group: ROOT
; -------------------------------------------------------------------
REPORT_SCRIPT_LOCATION LOCATION_ID='RUNEND'
