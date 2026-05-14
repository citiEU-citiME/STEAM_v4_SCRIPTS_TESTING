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

    # Manually specify the names of the 20 matrices
    matrix_names = [
        'Custom_Matrix_1', 'Custom_Matrix_2', 'Custom_Matrix_3', 'Custom_Matrix_4', 'Custom_Matrix_5',
        'Custom_Matrix_6', 'Custom_Matrix_7', 'Custom_Matrix_8', 'Custom_Matrix_9', 'Custom_Matrix_10',
        'Custom_Matrix_11', 'Custom_Matrix_12', 'Custom_Matrix_13', 'Custom_Matrix_14', 'Custom_Matrix_15',
        'Custom_Matrix_16', 'Custom_Matrix_17', 'Custom_Matrix_18', 'Custom_Matrix_19', 'Custom_Matrix_20'
    ]

    # Full linkage for the matrices and CSV rows/columns
    matrix_linkage = {
        'Custom_Matrix_1': {'csv1_row': 0, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'Custom_Matrix_2': {'csv1_row': 0, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'Custom_Matrix_3': {'csv1_row': 0, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'Custom_Matrix_4': {'csv1_row': 0, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'Custom_Matrix_5': {'csv1_row': 0, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'Custom_Matrix_6': {'csv1_row': 1, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'Custom_Matrix_7': {'csv1_row': 1, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'Custom_Matrix_8': {'csv1_row': 1, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'Custom_Matrix_9': {'csv1_row': 1, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'Custom_Matrix_10': {'csv1_row': 1, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'Custom_Matrix_11': {'csv1_row': 2, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'Custom_Matrix_12': {'csv1_row': 2, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'Custom_Matrix_13': {'csv1_row': 2, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'Custom_Matrix_14': {'csv1_row': 2, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'Custom_Matrix_15': {'csv1_row': 2, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
        'Custom_Matrix_16': {'csv1_row': 3, 'csv1_col': 1, 'csv2_row': 0, 'csv2_col': 1},
        'Custom_Matrix_17': {'csv1_row': 3, 'csv1_col': 2, 'csv2_row': 1, 'csv2_col': 1},
        'Custom_Matrix_18': {'csv1_row': 3, 'csv1_col': 3, 'csv2_row': 2, 'csv2_col': 1},
        'Custom_Matrix_19': {'csv1_row': 3, 'csv1_col': 4, 'csv2_row': 3, 'csv2_col': 1},
        'Custom_Matrix_20': {'csv1_row': 3, 'csv1_col': 5, 'csv2_row': 4, 'csv2_col': 1},
    }

    # Function to update matrices based on the first matrix and CSV coefficients
    def update_matrices():
        # Only consider the first matrix in the input Cube matrix file
        matrix_name = cube_matrix_file.matrixNames()[0]
        print(f"Processing matrix: {matrix_name}")

        # Read the matrix into a NumPy array
        matrix = cube_matrix_file.matrix(matrix_name)
        data_type = matrix.dataType()
        numpy_array = np.zeros((num_zones, num_zones), dtype=data_type_cp_to_np[data_type])
        matrix.readNumpyMatrix(numpy_array)

        # Generate 20 output matrices, each being the product of the first matrix and CSV coefficients
        for i, matrix_name_to_use in enumerate(matrix_names):
            # Get the coefficient and factor from CSV files for the current matrix
            linkage = matrix_linkage[matrix_name_to_use]
            row_csv1, col_csv1 = linkage['csv1_row'], linkage['csv1_col']
            row_csv2, col_csv2 = linkage['csv2_row'], linkage['csv2_col']

            coefficient = csv_1.iloc[row_csv1, col_csv1]
            factor = csv_2.iloc[row_csv2, col_csv2]

            # Multiply the matrix values by the coefficient and factor
            updated_matrix = numpy_array * coefficient * factor

            # Write the updated matrix to the output file
            tmp_matrix = output_matrix_file.addMatrix(matrix_name_to_use, data_type, cp.CubeMatrixCompressionLevel_Level_2)
            tmp_matrix.writeNumpyMatrix(updated_matrix)
            print(f"Matrix {matrix_name_to_use} written to output.")

    # Update matrices with the first matrix and CSV coefficients
    update_matrices()

    # Close all files
    cube_matrix_file.close()
    output_matrix_file.close()

    print("Matrix update complete!")
