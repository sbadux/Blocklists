import urllib3
import urllib.request
import gzip
import glob
import os.path

...
# Download the file from `url` and save it locally under `file_name`:
urllib.request.urlretrieve("http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=p2p&archiveformat=gz", "level1.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=gyisgnzbhppbvsphucsw&fileformat=p2p&archiveformat=gz", "level2.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=uwnukjqktoggdknzrhgh&fileformat=p2p&archiveformat=gz", "level3.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=dufcxgnbjsdwmwctgfuj&fileformat=p2p&archiveformat=gz", "level4.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=cwworuawihqvocglcoss&fileformat=p2p&archiveformat=gz", "bad_peers.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=llvtlsjyoyiczbkjsxpf&fileformat=p2p&archiveformat=gz", "spyware.gz")
urllib.request.urlretrieve("http://list.iblocklist.com/?list=usrcshglbiilevmyfhse&fileformat=p2p&archiveformat=gz", "hijacked.gz")

#Unzip the GZ
with gzip.open("level1.gz", 'rb') as infile:
        with open("level1.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("level2.gz", 'rb') as infile:
        with open("level2.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("level3.gz", 'rb') as infile:
        with open("level3.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("level4.gz", 'rb') as infile:
        with open("level4.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("bad_peers.gz", 'rb') as infile:
        with open("bad_peers.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("spyware.gz", 'rb') as infile:
        with open("spyware.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

with gzip.open("hijacked.gz", 'rb') as infile:
        with open("hijacked.txt", 'wb') as outfile:
            for line in infile:
                outfile.write(line)

#Delete GZ files
os.remove("level1.gz")
os.remove("level2.gz")
os.remove("level3.gz")
os.remove("level4.gz")
os.remove("bad_peers.gz")
os.remove("spyware.gz")
os.remove("hijacked.gz")


#Merge all the TXT files in a single .p2p file
response = os.system("cat *.txt > ipfilter.p2p")

#Delete the TXT
os.remove("level1.txt")
os.remove("level2.txt")
os.remove("level3.txt")
os.remove("level4.txt")
os.remove("bad_peers.txt")
os.remove("spyware.txt")
os.remove("hijacked.txt")
