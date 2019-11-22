# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 2019

@author: CheongRoach
"""

import pandas
import numpy as np

jobs_url = "./DeepLearningHelper/jobs.xlsx"
concerned ="./DeepLearningHelper/parameters_concerned.txt"

def main():
    jobs = ""
    try:
        jobs = pandas.read_excel(jobs_url, index="index")
    except:
        print("read fail")
        quit()
          
    for index, row in jobs.iterrows():
        print(row)
        row['[job_status]'] = 123
        if np.isnan(row['[job_status]']) or row['[job_status]'] in ('pending', ''):
            row['[job_status]'] = 'running'
        elif row['[job_status]'] == 'running':
            row['[job_status]'] = 'finish'
    
    jobs.to_excel(jobs_url)
    
if __name__ == '__main__':
    main()