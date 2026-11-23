import os
import sys
import subprocess

# Configuration: prefixes of files to search and execute recursively
# You can add or modify the prefixes here. The script will look for .py files
# that start with these names within the base folder and its subfolders.
SCRIPT_PREFIXES = ("crea_json", "crea_dataset", "creaDataset")

def main():
    # Takes the base folder (e.g. '3-Shot', '9-Shot', 'zeroShot')
    if len(sys.argv) > 1:
        base_dir = sys.argv[1]
    else:
        # If not specified, uses the folder where this script is located
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
    base_dir = os.path.abspath(base_dir)
    print(f"Starting recursive exploration of base folder: {base_dir}")
    
    if not os.path.exists(base_dir):
        print(f"The specified folder does not exist: {base_dir}")
        sys.exit(1)
    
    # os.walk recursively explores all folders and subfolders
    for root, dirs, files in os.walk(base_dir):
        # Skip system or cache folders (modify dirs in-place to not enter them at all)
        dirs[:] = [d for d in dirs if not d.startswith("__")]
        
        # Search and execute .py files that match the prefixes
        for filename in sorted(files):
            if filename.endswith(".py") and filename.startswith(SCRIPT_PREFIXES):
                print(f"\n{'='*60}")
                print(f" SCRIPT FOUND: {filename}")
                print(f" FOLDER:       {root}")
                print(f"{'='*60}")
                
                # Executes the script setting the working directory to `root`
                result = subprocess.run([sys.executable, filename], cwd=root)
                
                if result.returncode != 0:
                    print(f"!!! ERROR during execution of {filename} in {root}")
                else:
                    print(f"---> {filename} successfully executed.") 

    print(f"\n{'*'*60}\nGLOBAL EXECUTION TERMINATED\n{'*'*60}")

if __name__ == "__main__":
    main()
