import sys
sys.path.append('C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01')

import cubepy_a

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
   "m1":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATBX6ZDUJ352.MAT"
   }

   output_files = {
   "Print File":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCGPUYGZ2D0O.prn",
   "outputcubematrix":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCTZE8HJHGDO.cube-matrix"
   }

   cubepy_a.run(input_files, output_files, keys)
