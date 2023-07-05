import os, shutil

def sprint(content):
    print("[Automated_App_Builder] " + content)
    
def prun(command):
    os.system(f"powershell {command}")
    return
    
def clearTempFile():
    try:
        prun(f"rm ./dist_electron/win-unpacked/resources/{ASAP_OLD}")
    except:
        sprint("Old temp file has been deleted. Continue")
        
    try:
        prun(f"rm ./dist_electron/win-unpacked/resources/{EXT_FOLDER}")
    except:
        sprint("Old temp folder has been deleted. Continue")
    
ASAP_OLD = "app_old.asar"
ASAP_NEW = "app_new.asar"
ASAP_USE = "app.asar"
EXT_FOLDER = "temp"

def main_process(skip_build:bool):
    
    clearTempFile()
    
    if (not skip_build):
        sprint("Starting the electron-build process...")
        # build
        os.system("npm run electron:build")
        sprint("Build finished.")
    else:
        sprint("Script announced to skip building process. Continuing...")

    # modify and change the asap file
    sprint("Starting the process of exchanging asap file.")
    sprint("Unzipping asap file...")

    prun(f"mkdir ./{EXT_FOLDER}")
    prun(f"asar e ./dist_electron/win-unpacked/resources/{ASAP_USE} ./dist_electron/win-unpacked/resources/{EXT_FOLDER}")
    sprint("File unzipped. Start file insertion")
    prun(f"mkdir ./{EXT_FOLDER}/config")
    try:
        # Copy the files to the dir
        shutil.copytree(f".\\dist_electron\\config", f".\\dist_electron\\win-unpacked\\resources\\{EXT_FOLDER}\\config")
        shutil.copytree(f".\\dist_electron\\projects", f".\\dist_electron\\win-unpacked\\resources\\{EXT_FOLDER}\\projects")
        shutil.copytree(f".\\dist_electron\\public", f".\\dist_electron\\win-unpacked\\resources\\{EXT_FOLDER}\\public")
        shutil.copy(f".\\dist_electron\\preload.js", f".\\dist_electron\\win-unpacked\\resources\\{EXT_FOLDER}")
        # =========================
        sprint("File insertion finished.")
    except:
        sprint("Insertion Error. Exiting...")
        
    sprint("Preparing to exchange the legacy asar file...")
    prun(f"mv ./dist_electron/win-unpacked/resources/{ASAP_USE} ./dist_electron/win-unpacked/resources/{ASAP_OLD}")
    sprint("Packing...")
    prun(f"asar p ./dist_electron/win-unpacked/resources/{EXT_FOLDER} ./dist_electron/win-unpacked/resources/{ASAP_USE}")
    sprint("Cleaning up...")
    prun(f"rmdir ./dist_electron/win-unpacked/resources/{EXT_FOLDER}")
    sprint("Packed finished! Script running sequences finished! Enjoy your application!")
    return
    
if __name__ == "__main__":
    main_process(skip_build=False)