*cmd /c ""C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "D:/STEAM_v4_SCRIPTS_TESTING/venv/exec.py" "-p" "C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "-v" "-m" "-r" "D:/STEAM_v4_SCRIPTS_TESTING/pip-requirements.txt" "-u" "D:/STEAM_v4_SCRIPTS_TESTING/venv/venv311" "
REPORT_SCRIPT_LOCATION LOCATION_ID='RUNSTART'
; CubePy Script
REPORT_SCRIPT_LOCATION LOCATION_ID='440'
*cmd /c ""C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "D:/STEAM_v4_SCRIPTS_TESTING/venv/cubepy_exec.py" "-p" "C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/Python/Python311/python.exe" "-v" "-u" "D:/STEAM_v4_SCRIPTS_TESTING/venv/venv311" "-s" "D:/STEAM_v4_SCRIPTS_TESTING/Applications/MAIN/cubepy_d-0001_run.py" "
REPORT_SCRIPT_LOCATION LOCATION_ID='IDEND:440'
if (RETURNCODE > 0) ABORT
; End of CubePy
REPORT_SCRIPT_LOCATION LOCATION_ID='RUNEND'
