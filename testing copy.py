import os
import sys
import time
import shutil
import threading
import requests
import urllib
import os
import shutil
import downloadacc
import numpy as np
import pandas as pd

def test(urls):
    file_sizes=[5,10,20, 50, 100, 200, 512]
    conns_list=[1,2,4,8,15,50]
    url_list = [boi.strip() for boi in urls.split(',')]
    k=0
    arr=np.zeros([7,6],dtype=float)
    temp_arr=[]
    for i in url_list:
        for j in conns_list:
            start=time.time()
            response = downloadacc.download_links(i,j)
            end=time.time()
            # s="Total time taken for download of file size "+ str(file_sizes[k]) +" and conns value "+ str(j) +" is "+str(end-start)
            # arr.append(s)
            temp_arr.append(end-start)
        k+=1

    k=0
    for i in range(len(file_sizes)):
        for j in range(len(conns_list)):
            arr[i][j]=temp_arr[k]
            k+=1

    DF = pd.DataFrame(arr)

    DF.to_csv("data.csv")
        