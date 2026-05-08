"""
Description: 

Input and Output files may be edited here, but using the Application Editor is recommended.
```cubepy-metadata
@input
   m1 : cube-matrix
   csv1 : csv
   csv2 : csv
@output
   outputcubematrix : cube-matrix
```
"""


import os
import cubepy as cp
import numpy as np
import pandas as pd

def run(input_files, output_files, keys):
    # Paths for the input files
    input_cube_matrix_path = input_files['m1']
    input_csv_1_path = input_files['csv1']
    input_csv_2_path = input_files['csv2']
    
    # Path for the output file
    output_cube_matrix_path = output_files['outputcubematrix']
    
    # Load the CSV files for coefficients and factors
    csv_1 = pd.read_csv(input_csv_1_path)
    csv_2 = pd.read_csv(input_csv_2_path)
    
    # Mapping Cube data types to NumPy data types
    data_type_cp_to_np = {
        cp.CubeMatrixDataType_Int8: np.int8,
        cp.CubeMatrixDataType_Int16: np.int16,
        cp.CubeMatrixDataType_Int32: np.int32,
        cp.CubeMatrixDataType_Int64: np.int64,
        cp.CubeMatrixDataType_Float: np.float32,
        cp.CubeMatrixDataType_Double: np.float64
    }

    # Remove output file if it already exists
    if os.path.exists(output_cube_matrix_path):
        os.remove(output_cube_matrix_path)

    # Open the input cube-matrix file
    cube_matrix_file = cp.CubeMatrixFile(input_cube_matrix_path)
    cube_matrix_file.open()
    num_zones = cube_matrix_file.zones()

    # Create the output matrix file
    output_matrix_file = cp.CubeMatrixFile(output_cube_matrix_path)
    output_matrix_file.openWithCreate(num_zones)

 
    # Manually define the linkage between matrices and CSV rows/columns
    # For example, T1P1 uses the first row, second column in both CSV files
    matrix_linkage = {
        'T1P1': {'csv1_row': 0, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'T1P2': {'csv1_row': 0, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'T1P3': {'csv1_row': 0, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'T1P4': {'csv1_row': 0, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'T1P5': {'csv1_row': 0, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'T2P1': {'csv1_row': 1, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'T2P2': {'csv1_row': 1, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'T2P3': {'csv1_row': 1, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'T2P4': {'csv1_row': 1, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'T2P5': {'csv1_row': 1, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'T3P1': {'csv1_row': 2, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'T3P2': {'csv1_row': 2, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'T3P3': {'csv1_row': 2, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'T3P4': {'csv1_row': 2, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'T3P5': {'csv1_row': 2, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'T4P1': {'csv1_row': 3, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'T4P2': {'csv1_row': 3, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'T4P3': {'csv1_row': 3, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'T4P4': {'csv1_row': 3, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'T4P5': {'csv1_row': 3, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
    }

    # Function to update matrices based on manual linkage from CSVs
    def update_matrices():
        matrix_names = cube_matrix_file.matrixNames()
        for matrix_name in matrix_names:
            print(f"Processing matrix: {matrix_name}")
            matrix = cube_matrix_file.matrix(matrix_name)
            data_type = matrix.dataType()

            # Create the numpy_array with the correct dtype
            numpy_array = np.zeros((num_zones, num_zones), dtype=data_type_cp_to_np[data_type])

            # Read the matrix into the numpy array
            matrix.readNumpyMatrix(numpy_array)

            # Use the manual linkage to fetch the row/column indices
            if matrix_name in matrix_linkage:
                linkage = matrix_linkage[matrix_name]
                row_csv1, col_csv1 = linkage['csv1_row'], linkage['csv1_col']
                row_csv2, col_csv2 = linkage['csv2_row'], linkage['csv2_col']

                # Get the coefficient and factor from CSV files
                coefficient = csv_1.iloc[row_csv1, col_csv1]
                factor = csv_2.iloc[row_csv2, col_csv2]

                # Multiply the matrix values by the coefficient and factor
                numpy_array *= coefficient * factor

                # Write the updated matrix to the output file
                matrix_name_to_use = matrix_name
                tmp_matrix = output_matrix_file.addMatrix(matrix_name_to_use, data_type, cp.CubeMatrixCompressionLevel_Level_2)
                tmp_matrix.writeNumpyMatrix(numpy_array)

            else:
                print(f"Warning: No linkage found for {matrix_name}. Skipping matrix.")

    # Update matrices with manually defined linkage
    update_matrices()

    # Close all files
    cube_matrix_file.close()
    output_matrix_file.close()

    print("Matrix update complete!")
