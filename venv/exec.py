import subprocess
import sys
import getopt
import os
import hashlib
def check_return_code(result):
    if result.returncode > 0:
        sys.exit(2)
def create_virtual_environment(py_exe, venv_path, out):
    check_return_code(subprocess.run([py_exe, '-m', 'venv', venv_path], stdout=out, stderr=subprocess.STDOUT))
def install_requirements(py_exe, req_path, out):
    if req_path == '':
        return
    check_return_code(subprocess.run([py_exe, '-m', 'pip', 'install', '--upgrade', 'pip'], stdout=out, stderr=subprocess.STDOUT))
    check_return_code(subprocess.run([py_exe, '-m', 'pip', 'install', '-r', req_path], stdout=out, stderr=subprocess.STDOUT))
def main(argv):
    py_exe = ''
    venv_path = ''
    venv_enabled = False
    req_path = ''
    create_venv = False
    cube_managed = False
    out = subprocess.DEVNULL
    opts, args = getopt.getopt(argv, 'p:vcmu:r:l')
    for opt, arg in opts:
        if opt == '-p':
            py_exe = arg
        elif opt == '-v':
            venv_enabled = True
        elif opt == '-u':
            venv_path = arg
        elif opt == '-r':
            req_path = arg
        elif opt == '-c':
            create_venv = True
        elif opt == '-m':
            cube_managed = True
        elif opt == '-l':
            out = None
    if create_venv and cube_managed:
        create_virtual_environment(py_exe, venv_path, out)
    if venv_enabled:
        py_exe = os.path.join(venv_path, 'Scripts/python.exe')
        if not os.path.exists(py_exe):
            py_exe = os.path.join(venv_path, 'bin/python.exe')
        if not os.path.exists(py_exe):
            py_exe = os.path.join(venv_path, 'python.exe')
    if cube_managed and os.path.exists(req_path):
        old_checksum = ''
        if os.path.exists(os.path.join(venv_path, os.pardir, 'pip_req_checksum')):
            file = open(os.path.join(venv_path, os.pardir, 'pip_req_checksum'), 'r')
            old_checksum = file.read()
        file = open(req_path, 'r')
        new_checksum = hashlib.md5(bytes(file.read(), encoding='utf-8')).hexdigest()
        if new_checksum != old_checksum:
            install_requirements(py_exe, req_path, out)
            file = open(os.path.join(venv_path, os.pardir, 'pip_req_checksum'), 'w')
            file.write(new_checksum)
if __name__ == '__main__':
    main(sys.argv[1:])
