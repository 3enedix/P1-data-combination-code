#import time
#start_time = time.process_time()

from geoslurp.datapull.ftp import Uri as ftp
from geoslurp.datapull.ftp import Crawler
from geoslurp.db.settings import Credentials
from geoslurp.config import setInfoLevel
setInfoLevel()

from coastal_data import data_preparation as prep
import os

datapath_in = '../../data_temp/'
datapath_out = '/home/aschennellers/data_out/'

url='ftp://ftp.itc.nl/incoming/aschenneller/'
dist2coast = 100 * 1e3 # [m]

auth=Credentials(alias="ftpitc",user="ftpguest",passw="ftp4you",url=url,ftptls=True)

crw = Crawler(auth.url,auth=auth,pattern="S3B.*nc")
gen = crw.ls()

for item in gen:
    filename_input = ''
    filename_output = ''
    filename_reprocessed = ''
    
    url_temp = url + item[0] + 'processing/'
    
    crw2 = Crawler(url_temp)
    gen2 = crw2.ls()
    for item2 in gen2:
        url_file = url_temp + item2[0]
        geturi = ftp(url_file)
        geturi.download(datapath_in, True)
        
        if '_enhanced' in item2[0]:
            filename_reprocessed = item2[0]
            filename_output = item2[0].replace('_enhanced', '_mod')
        else:
            filename_input = item2[0]

    prep.prepare_s3_data(datapath_in, datapath_out, filename_reprocessed, filename_input, filename_output, dist2coast)
    
    os.system("smbclient //ad.utwente.nl/ITC/WRS/Group -D 2_Research/PhDs/Aschenneller/Sentinel-3B/ -c 'lcd " + datapath_out + "; put " + filename_output + "'")
#end_time = time.process_time()
#ex_time = end_time - start_time
#rint("Done. Needed ", ex_time, "seconds.")

