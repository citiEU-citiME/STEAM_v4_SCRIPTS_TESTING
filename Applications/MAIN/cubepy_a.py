"""
Description: 

Input and Output files may be edited here, but using the Application Editor is recommended.
```cubepy-metadata
@input
   m1 : mat
@output
   Print File : prn
   outputcubematrix : cube-matrix
```
"""

import cubepy as cp
from datetime import datetime
import sys
import contextlib
import os
import subprocess



def run(input_files, output_files, keys):

    with open(output_files["Print File"], "w") as print_file:

        print("CubePy Program: Convert Tempo LogSum to cube-matrix", file=print_file)
        print(f"Start: {datetime.now()} \n", file=print_file)

        cube_convert = keys["ConvertUtility"]
        in_mat = input_files["m1"]
        out_mat = output_files["outputcubematrix"]
                              
        with contextlib.suppress(FileNotFoundError):
            os.remove(out_mat)

        cmd = f'"{cube_convert}" -f mat-from6 -s "{in_mat}" -d "{out_mat}" -c 2'
        print(cmd, file=print_file)

        if not os.path.exists(cube_convert):
            print(f"ERROR: File {cube_convert} does not exist. Check the key definition for the CubeConvert utility.", file=print_file)
            sys.exit(f"ERROR: File {cube_convert} does not exist. Check the key definition for the CubeConvert utility.")

        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT).stdout
        except subprocess.CalledProcessError as exception:
            print(f"ERROR for subprocess: {exception}", file=print_file)
            print(f"Full error message: {exception.output.decode('utf-8')}", file=print_file)
            raise exception.returncode
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}", file=print_file)
            raise e
        else:
            print("Matrix converted successfully", file=print_file)
            
        print("", file=print_file)
        print(f"End: {datetime.now()}", file=print_file)
        
