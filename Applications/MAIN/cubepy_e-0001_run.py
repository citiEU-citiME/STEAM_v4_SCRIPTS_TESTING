import sys
sys.path.append('C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01')

import cubepy_e

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
   "ConvertUtility":"C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01/CubeConvert.exe",
   "CubeInstallationPath":"C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01"
   }

   input_files = {
   }

   output_files = {
   "ODME":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCVA1843NVDS.cube-matrix",
   "Print File":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCC0X8M6ED9K7.prn"
   }

   cubepy_e.run(input_files, output_files, keys)
