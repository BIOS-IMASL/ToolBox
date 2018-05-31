'''FInd and fetch BMRBs from PDBs'''

'''This Python script is useful when you need to find the corresponding 
	BMRB entries (i.e. chemical shifts) from a list of PDB ids.'''

from IPython.display import HTML
#import pprint #in Python 2
import urllib #urllib2 #in Python 2
import os

#A list with the PDB ids you want to find their correspondig BMRB entry/entries and nmrstar file/s
pdb_list = ['1ldz', '1ubq'] 


not_found = []

#Creates two directories named 'BMRBs' an 'Files', if they don't exist
dir_list = ['BMRBs', 'Files']
for directory in dir_list:
    if not os.path.exists(directory):
        os.makedirs(directory)
        
#Creates a csv file with the PDB ids and their corresponding BMRB ids (if found)       
fdd = open('Files/pdbs_bmrbs.csv' , 'w')
fdd.write("PDBID,BMRBID\n")

#Operates over the provided list of PDB ids
for pdb_id in pdb_list[:]:
    
    #Fetches PDB file as a 'temporary file'
    fd = open('pdb.temp', 'w')
    page = urllib.request.urlopen('https://www.rcsb.org/structure/{}'.
                                  format(pdb_id)).read() #urllib2.urlopen() in Python 2
    fd.write('{}'.format(page))
    fd.close()
    
    #Searches for a realated BMRB id inside the PDB file
    if 'bmrbId=' in open('pdb.temp').read():
        for line in open('pdb.temp').readlines():
            if "bmrbId=" in line:
                bmrb_id = line.split('bmrbId=')[1][:6].split('"')[0]
                
    elif '/pdb/rss/' in open('pdb.temp').read():
        for line in open('pdb.temp').readlines():
            if '/pdb/rss/' in line:
                bmrb_id = line.split('pdb/rss/')[1][0:5]

    #If a BMRB id is found, it fetches the nmrstar file from the BMRB  
    if bmrb_id != 'LastL' and bmrb_id is not None :

        fdd.write('{},{}\n'.format(pdb_id,bmrb_id))
        try:
            page = r'{}'.format(urllib.request.urlopen('http://rest.bmrb.wisc.edu/bmrb/NMR-STAR3/{}'
                                                       .format(bmrb_id)).read()) #urllib2.urlopen() in Python 2
            page = page.replace("\\'", "'")
            fb = open('BMRBs/bmr{}.str'.format(bmrb_id), 'w')
            fb.write('{}'.format(page[2:-1].replace('\\n', '\n')))
            fb.close()
            print('The PDB id {} has an associated BMRB Entry: {}\n'
                   'The corresponding nmrstar file was downloaded'.format(pdb_id,bmrb_id))
        except:
            not_found.append(pdb_id)
            print('The PDB id {} has an associated BMRB Entry: {}\n'
                'but it does not exist or is not yet publicly available'.format(pdb_id,bmrb_id))
    
    else:
        not_found.append(pdb_id)
        print('The PDB id {} has no associated BMRB id'.format(pdb_id))


    bmrb_id = None
    os.remove('pdb.temp')
fdd.close()
