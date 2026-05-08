import sys
sys.path.append('C:/Program Files/Bentley/OpenPaths/CUBE 25.00.01')

import cubepy_c

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
   "Input File 1":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATSM7RLNUYNF.MAT",
   "Input File 2":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATC22X49DY2T.MAT",
   "Input File 3":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATHTBF822EBM.MAT",
   "Input File 4":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0MATO05VLPYIIZ.MAT"
   }

   output_files = {
   "Output File 1":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCC1FA9GINL4N.mat",
   "Output File 2":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCM0KPPN3SI9.mat",
   "Output File 3":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCCIMQZL817A6.mat",
   "Output File 4":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCC1BYUFQDQVC.mat",
   "Print File":"D:/STEAM_v4_SCRIPTS_TESTING/Scenarios/Base-0001/G0CCC7YXM5WHNNX.prn"
   }

   cubepy_c.run(input_files, output_files, keys)
