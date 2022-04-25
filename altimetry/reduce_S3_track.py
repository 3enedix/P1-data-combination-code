#import time
#start_time = time.process_time()

from geoslurp.datapull.ftp import Uri as ftp
from geoslurp.datapull.ftp import Crawler
from coastal_data import data_preparation as prep

datapath_in = '~/data_temp/'
datapath_out = '~/data_out/'

url='ftp://ftp.itc.nl/incoming/aschenneller/'
dist2coast = 100 * 1e3; # [m]

crw = Crawler(url)
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
        
        if '_enhanced' in item2[0]
            filename_input = item2[0]
            filename_output = item2[0].replace('_enhanced', '_mod')
        else
            filename_reprocessed = item2[0]

prep.prepare_s3_data(datapath_in, filename_reprocessed, filename_input, datapath_out + filename_output, dist2coast)

#end_time = time.process_time()
#ex_time = end_time - start_time
#rint("Done. Needed ", ex_time, "seconds.")
