# ePRIME .txt to .csv converter

- ePRIME spits out an edat file once the paradigm successfully exits. It also generates a .txt file. If paradigm stops (for numerous reasons), we end up with a .txt file. .edat files can be exported manually (one by one, till all our hairs turn white) to csv or tab separated formats. At times these files need some extra pre-processing to work!

- [Taylor Salo](https://github.com/tsalo) wrote a neat converter using python :snake: to do these conversions

- This is very useful to extract metadata which can be used for behavioural data analysis (Reaction time, accuracy etc.), marker extraction and lot more

### Below is a short tutorial on doing bulk conversions

1. Download the repository [convert-eprime](https://github.com/tsalo/convert-eprime)
   

   ![](Documentation/repo.png)

2. Extract the zipped folder to some location in your system

3. Open spyder :spider_web: and click :heavy_plus_sign: Add path from PYTHONPATH manager

   ![](Documentation/path.png)

4. Navigate to the unzipped folder and **choose** the convert-eprime-main folder

   ![](/Documentation/select.png)

5. Now, we are set to convert the files to .csv. Code snipped is below

   ```python
   from convert_eprime.convert import text_to_csv
   in_file = 'subj0001_stop_signal_task-0.txt'
   out_file = 'subj0001_0.csv'
   
   text_to_csv(in_file, out_file)
   # The converted .csv file will be available in the same folder/directory from which we ran the script
   ```

   #### The text file and the converted .csv file

   ![](/Documentation/eprimetextfile.png)

Converted .csv file

![](Documentation/convertedcsv.png)

#### We can subset this one to get trial accuracy and reaction times using R/Python

---

#### The code snippet below is a wrapper to do bulk conversion of text files generated by ePRIME. Same filename is borrowed for .csv files!

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 23:18:10 2021
@author: Rahul Venugopal
Just a wrapper to automate bulk converting .txt files to .csv files
"""
# Loading library
from convert_eprime.convert import text_to_csv
from tkinter.filedialog import askopenfilenames
from tkinter import Tk
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

# Selecting multiple text files using GUI
filelist = askopenfilenames(initialdir = "cwd",title = "Select file",
                              filetypes = (("Text file","*.txt"),
                                           ("All files","*.*")))

for file in filelist:
    in_file = file
    out_file = in_file[0:-3]+str('csv')
    text_to_csv(in_file, out_file)
```

Just run the code, select multiple text files and press **OK**

![](Documentation/output.png)

# Fin.