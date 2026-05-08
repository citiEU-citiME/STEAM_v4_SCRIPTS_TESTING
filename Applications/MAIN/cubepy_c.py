"""
Description: 

Input and Output files may be edited here, but using the Application Editor is recommended.
```cubepy-metadata
@input
   Input File 1 : *
   Input File 2 : *
   Input File 3 : *
   Input File 4 : *
@output
   Output File 1 : mat
   Output File 2 : mat
   Output File 3 : mat
   Output File 4 : mat
   Print File : prn
```
"""

import os
import contextlib
import subprocess
from datetime import datetime
from pathlib import Path
from shutil import copyfile
import cubepy as cp



def run(input_files, output_files, keys):

    mat_file = [str()] * 4
    mat_file[0] = input_files["Input File 1"]
    mat_file[1] = input_files["Input File 2"]
    mat_file[2] = input_files["Input File 3"]
    mat_file[3] = input_files["Input File 4"]

    
    cube_mat_file = [str()] * 4
    cube_mat_file[0] = f"{keys['Scenario_Dir']}/tmp_cubepypttranspose_a0b2c3c_ix0.cube-matrix"
    cube_mat_file[1] = f"{keys['Scenario_Dir']}/tmp_cubepypttranspose_a0b2c3c_ix1.cube-matrix"
    cube_mat_file[2] = f"{keys['Scenario_Dir']}/tmp_cubepypttranspose_a0b2c3c_ix2.cube-matrix"
    cube_mat_file[3] = f"{keys['Scenario_Dir']}/tmp_cubepypttranspose_a0b2c3c_ix3.cube-matrix"

    print_file = open(output_files["Print File"], "w")
    out_mat_file = [str()] * 4
    out_mat_file[0] = output_files["Output File 1"]
    out_mat_file[1] = output_files["Output File 2"]
    out_mat_file[2] = output_files["Output File 3"]
    out_mat_file[3] = output_files["Output File 4"]

    installation_folder = f"{keys['CubeInstallationPath']}"
    
    
            
    def convert_from_6(cube_installation_folder, source_matrix_file, destination_matrix_file):
        if not source_matrix_file or not destination_matrix_file:
            raise ValueError(f"Invalid matrix file paths: Source: {source_matrix_file}, Destination: {destination_matrix_file}")
        
        cube_convert = f"{cube_installation_folder}/CubeConvert.exe"
        cmd = f'{cube_convert} -f mat-from6 -s "{source_matrix_file}" -d "{destination_matrix_file}" -c 0'
        
        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(cmd, file=print_file)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code, {e.returncode}", file=print_file)
            print(f"Error occurred:, {e}", file=print_file)
            print(f"Output:, {e.output.encode('utf-8')}", file=print_file)
            raise e
        except Exception as e:
            print(f"An unexpected error occurred:, {e}", file=print_file)
            raise e            
                     
    def convert_to_6(cube_installation_folder, source_matrix_file, destination_matrix_file):

        cube_convert = f"{cube_installation_folder}/CubeConvert.exe"
        cmd = f'{cube_convert} -f mat-to6 -s "{source_matrix_file}" -d "{destination_matrix_file}'

        try:
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            print(cmd, file=print_file)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with return code, {e.returncode}", file=print_file)
            print(f"Error occurred:, {e}", file=print_file)
            print(f"Output:, {e.output.encode('utf-8')}", file=print_file)
            raise e
        except Exception as e:
            print(f"An unexpected error occurred:, {e}", file=print_file)
            raise e


    start_time = datetime.now()

    for mat in mat_file:

        mat_ix = mat_file.index(mat)
        
        with contextlib.suppress(FileNotFoundError):
            try:
                os.remove(cube_mat_file[mat_ix])
                os.remove(out_mat_file[mat_ix])
            except PermissionError as e:
                print(f"Permission error: {e}", file=print_file)
        
        tmp_start_time = datetime.now()
            
        convert_from_6(installation_folder, mat_file[mat_ix], cube_mat_file[mat_ix])

        tmp_end_time = datetime.now()
        tmp_run_time = tmp_end_time - tmp_start_time
        print(f"Run Time for convert_from_6 {mat}: {tmp_run_time}", file=print_file)
        
        tmp_start_time = datetime.now()
        
        cube_mat = cp.CubeMatrixFile(cube_mat_file[mat_ix])
        cube_mat.open()

        cube_mat_names = cube_mat.matrixNames()
        print(cube_mat_names, file=print_file)
        for mat_name in cube_mat_names:
            if cube_mat.matrixNameExists(f"{mat_name}_T"):
                cube_mat.removeMatrix(f"{mat_name}_T")
            cube_mat.transpose(mat_name, f"{mat_name}_T")
            cube_mat.removeMatrix(f"{mat_name}")

        cube_mat.close()
        
        tmp_end_time = datetime.now()
        tmp_run_time = tmp_end_time - tmp_start_time
        print(f"Run Time for transposing {mat}: {tmp_run_time}", file=print_file)
        
        tmp_start_time = datetime.now()
        
        convert_to_6(installation_folder, cube_mat_file[mat_ix], out_mat_file[mat_ix])
        
        tmp_end_time = datetime.now()
        tmp_run_time = tmp_end_time - tmp_start_time
        print(f"Run Time for convert_to_6 {mat}: {tmp_run_time}", file=print_file)
        
        with contextlib.suppress(FileNotFoundError):
            Path(cube_mat_file[mat_ix]).unlink()
            
        with contextlib.suppress(FileNotFoundError):
            try:
                os.remove(cube_mat_file[mat_ix])
            except PermissionError as e:
                print(f"Permission error: {e}", file=print_file)            
            

    end_time = datetime.now()
    runtime = end_time - start_time

    print(f"Total Run Time: {runtime}", file=print_file)
    print_file.close()
    
    
