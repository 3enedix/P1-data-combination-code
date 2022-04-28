from geoslurp.datapull.ftp import Uri as ftp
from geoslurp.datapull.ftp import Crawler
from geoslurp.db.settings import Credentials
from geoslurp.config import setInfoLevel
setInfoLevel()

from coastal_data import data_preparation as prep
import os

#datapath_in = '../../data_temp/'
#datapath_out = '/home/aschennellers/data_out/'
datapath_in = '../../data_temp/'
datapath_out = '../../data_out/'

url='ftp://ftp.itc.nl/incoming/aschenneller/'
dist2coast = 100 * 1e3 # [m]

auth=Credentials(alias="ftpitc",user="ftpguest",passw="ftp4you",url=url,ftptls=True)

crw = Crawler(auth.url,auth=auth) # 1st crawler to get the name of the folder (1 folder = 1 EarthConsole task)
folder_crawler = crw.ls()

for folder in folder_crawler:
    url_temp = url + folder[0] + 'processing/'
    
    #crw2 = Crawler(url_temp, auth=auth, pattern="*xy*") # 2nd crawler to get the filenames # giving a pattern does not change the output?
    crw2 = Crawler(url_temp, auth=auth)
    files = list(crw2.ls())
    
    related_filenames = [] # list of tuples, each tuple contains the filenames of the two corresponding .nc-files, 1st element: input file, 2nd element: reprocessed file

    for i in range(0, len(files)):
        if '_enhanced' in files[i][0]:
            repr_fname_temp = files[i][0]
            orig_filename_temp = repr_fname_temp.replace('_enhanced', '')
            related_filenames.append((orig_filename_temp, repr_fname_temp))
            
    for i in range(0, len(related_filenames)):
        filename_input = related_filenames[i][0]
        filename_reprocessed = related_filenames[i][1]
        filename_output = filename_reprocessed.replace('_enhanced', '_mod')

        geturi_in = ftp(url_temp + filename_input)
        geturi_re = ftp(url_temp + filename_reprocessed)

        geturi_in.download(datapath_in, True)
        geturi_re.download(datapath_in, True)

        prep.prepare_s3_data(datapath_in, datapath_out, filename_reprocessed, filename_input, filename_output, dist2coast)
    
    #os.system("smbclient -A ~/.smbclient.conf //ad.utwente.nl/ITC/WRS/Group -D 2_Research/PhDs/Aschenneller/Sentinel-3B/ -c 'lcd " + datapath_out + "; put " + filename_output + "'")
    #os.system("rm " + datapath_in + "/* " + datapath_out + "/*")