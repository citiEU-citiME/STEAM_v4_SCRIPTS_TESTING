import subprocess
import sys
import getopt
import os
def check_return_code(result):
    if result.returncode > 0:
        sys.exit(2)
def main(argv):
    py_exe = ''
    venv_path = ''
    venv_enabled = False
    cube_py_script = ''
    opts, args = getopt.getopt(argv, 'p:vu:s:')
    for opt, arg in opts:
        if opt == '-p':
            py_exe = arg
        elif opt == '-v':
            venv_enabled = True
        elif opt == '-u':
            venv_path = arg
        elif opt == '-s':
            cube_py_script = arg
    if venv_enabled:
        py_exe = os.path.join(venv_path, 'Scripts/python.exe')
        if not os.path.exists(py_exe):
            py_exe = os.path.join(venv_path, 'bin/python.exe')
        if not os.path.exists(py_exe):
            py_exe = os.path.join(venv_path, 'python.exe')
    check_return_code(subprocess.run([py_exe, cube_py_script], stderr=subprocess.STDOUT))
if __name__ == '__main__':
    main(sys.argv[1:])
