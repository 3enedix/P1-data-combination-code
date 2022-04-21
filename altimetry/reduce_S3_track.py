import time
start_time = time.process_time()

from coastal_data import data_preparation as prep

datapath = '../../2_data_copies/2_altimetry/1_Sentinel-3/2_S3B_ters/'
filename_reprocessed = 'S3B_SR_2_WAT____20181126T201732_20181126T210147_20181222T115028_2654_019_099______MAR_O_NT_003_enhanced.nc'
filename_input = 'S3B_SR_2_WAT____20181126T201732_20181126T210147_20181222T115028_2654_019_099______MAR_O_NT_003.nc'
filename_output = 'S3B_SR_2_WAT____20181126T201732_20181126T210147_20181222T115028_2654_019_099______MAR_O_NT_003_mod.nc'
dist2coast = 100 * 1e3; # [m]

prep.prepare_s3_data(datapath, filename_reprocessed, filename_input, filename_output, dist2coast)

end_time = time.process_time()
ex_time = end_time - start_time
print("Done. Needed ", ex_time, "seconds.")
