"""
Description: 

Input and Output files may be edited here, but using the Application Editor is recommended.
```cubepy-metadata
@input
@output
   ODME : cube-matrix
   Print File : prn
```
"""


import os
import numpy as np
from datetime import datetime
import cubepy as cp
import traceback

def run(input_files, output_files, keys):

    with open(output_files["Print File"], "w") as print_file:
        print("Craating matrix", file=print_file)
        
        
        output_cube_matrix_path = output_files['ODME']
        
        # Mapping Cube data types to NumPy data types
        data_type_cp_to_np = {
            cp.CubeMatrixDataType_Int8: np.int8,
            cp.CubeMatrixDataType_Int16: np.int16,
            cp.CubeMatrixDataType_Int32: np.int32,
            cp.CubeMatrixDataType_Int64: np.int64,
            cp.CubeMatrixDataType_Float: np.float32,
            cp.CubeMatrixDataType_Double: np.float64
        }


        #matrix_names = ["AUTO_ODME", "MOTO_ODME", "TPL_ODME", "MISTO_ODME"]
        matrix_names = ["AUTO_ODME"]
        num_zones =  10 #int(keys['Num_zone_modello_domanda'])
        data_type = cp.CubeMatrixDataType_Double  # Use appropriate type (int16 is usually safe)
                   # Remove output file if it already exists
        if os.path.exists(output_cube_matrix_path):
          os.remove(output_cube_matrix_path)

        output_matrix_file = cp.CubeMatrixFile(output_cube_matrix_path)
        output_matrix_file.openWithCreate(num_zones)  


        # Generate and write each matrix
        for name in matrix_names:
            print_file.write(f"Creating matrix: {name}\n") 
            mat = output_matrix_file.addMatrix(name, data_type, cp.CubeMatrixCompressionLevel_Level_2)
            #arr = np.zeros(num_zones*num_zones, dtype="float64")  #full((zones, zones), constant_value, dtype="int16")
            arr = np.ones(num_zones*num_zones, dtype="float64")  #full((zones, zones), constant_value, dtype="int16")
            arr.resize((num_zones, num_zones))
            mat.writeNumpyMatrix(arr)
          

