import h5py
import os
import matplotlib.pyplot as plt
import numpy as np
cwd = os.getcwd();

# Opening data file
filepath = cwd + "/competitionfiles/COOLCAT_20091219_074253_24_20091219_074253_240.hdf"
f = h5py.File(filepath, 'r')

# Getting the channel IDs
chanIDs = f['DYNAMIC DATA']

# Putting all of the data from one file into a list
data_list = []
count = len(chanIDs['ch_1']['MEASURED'])
channel_count = 1
for chanID in chanIDs:
    item_count = 0
    print(chanID, ": ")
    for data in chanIDs[chanID]['MEASURED']:
        print(data, item_count)
        item_count += 1
        # data_list.append(data)
    channel_count += 1

# Reshaping the list into an np array where every row represents a channel
data_array = np.array(data_list).reshape(count, len(data_list) / count)

print(data_array)

# Closing data file
f.close();
