# Blocklists
Download iBlocklists' lists in .dat (aMule/eMule) or .p2p (qBittorrent)

#### WARNING: 

1) Since I'm not a developer and I'm not even good in programming, these scripts are super-easy. 
They only download Blocklist's lists and merge them into a single file.
2) You need Python 3 to run them. I've tested these scripts on Ubuntu and Fedora.
3) They can work fine (as for me) or not. I'm not responsible of any error/bug/data loss/anything else.
4) I don't share or distribute any Blocklists' list. It's just a script to download some of the *public* and *free* lists.
5) Please make sure to run the scripts in a folder where no other .txt file is saved. The script merges all the .txt files in the folder


The 2 simple scripts allows you to download iBlocklists' list and save them in .dat or .p2p formats. The 2 scripts have a single difference: the format of the output file. Choose the one you need:
- .dat format: used by aMule/eMule/Deluge (not tested on Deluge)
- .p2p format: used by qBittorrent

#### HOW TO RUN THE SCRIPT ON LINUX:

###### If you want to save the file in the same folder where the script is saved
1) Open a terminal
2) move to the folder where you saved the script (eg. `cd /home/USER/Download`)
3) run the script (eg. `python3 blocklist_dat.py`)

###### If you want to save the file to another specific folder
1) Open a terminal
2) Make sure that no other .txt file is saved on that folder (or it will be merged)
3) move to the folder where you want to save the .dat/.p2p file (eg. `cd /home/.aMule/`)
4) run the script (eg. `python3 blocklist_dat.py`)


#### WHERE TO SAVE THE .DAT/.P2P:

- aMule: save the .dat file to `/home/USER/.aMule/`
- qBittorrent: open qBittorrent and go to `Tools > Options > Connection > IP filtering` select the path of the file and refresh (DON'T USE THE .DAT FILE BECAUSE IT'S NOT CORRECTLY DETECTED. USE THE .P2P FILE)


#### HOW TO MODIFY THE SCRIPT: ####
It's really simple to add the lists you want or remove the defalut lists. You just need to add/remove the following strings in the proprer section of the script:

- Section: "Download the file from url and save it locally under file_name"

`urllib.request.urlretrieve("LIST_URL", "CUSTOM_LIST_NAME.GZ")`

- Section: "Unzip the GZ"

`with gzip.open("CUSTOM_LIST_NAME.GZ", 'rb') as infile:
        with open("CUSTOM_TXT_NAME.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)`

- Section: "Delete GZ files"

`os.remove("CUSTOM_LIST_NAME.GZ")`

- Section: "CUSTOM_TXT_NAME.GZ"

`os.remove("CUSTOM_TXT_NAME.txt")`
