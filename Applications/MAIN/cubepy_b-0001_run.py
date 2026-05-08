import sys
sys.path.append('C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01')

import cubepy_b

if __name__ == "__main__":
   keys = {
   "App_Dir":"D:/STEAM_v4_SCRIPTS_TESTING/Applications/MAIN",
   "Group_Dir":"{Group_Dir}",
   "Project_Dir":"D:/STEAM_v4_SCRIPTS_TESTING",
   "Project_Name":"STEAM_v4_SCRIPTS_TESTING",
   "Catalog_Dir":"D:/STEAM_v4_SCRIPTS_TESTING",
   "Scenario_Dir":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001",
   "App_Name":"MAIN",
   "Scenario_Code":"0001",
   "Scenario_FullName":"Base",
   "Scenario_ShortName":"Base",
   "ConvertUtility":"C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/CubeConvert.exe"
   }

   input_files = {
   "m1":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCTZE8HJHGDO.cube-matrix",
   "csv1":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MAT2OMQT6HPVO.csv",
   "csv2":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATUGV5X4TN7I.csv"
   }

   output_files = {
   "outputcubematrix":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCJF5JSQAXDX.cube-matrix"
   }

   cubepy_b.run(input_files, output_files, keys)
