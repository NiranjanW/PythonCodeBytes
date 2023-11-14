from srcRow import SrcRow
import logging
from pathlib import Path
import os
from SrcFileData import SrcFileData


def main():
    logger = logging.getLogger()
    logger.setLevel = logging.INFO
    data_folder =Path(os.path.dirname(__file__)+"/data")
    file ='PIKHDIWT.GOOD'
    file_to_open = data_folder/file
    file_data =[]
    
    # with open(file_to_open, 'r') as f:
    #      print(f.read)
    try:
        file_Data(file_to_open)

        # with open(file_to_open, 'r') as f:
        #     for data in f:
        #         print(data)
        #     # for line in f:
            #     file_data.append(line.strip())
            #     sample_lst = [SrcRow.fields("hdr" , line) for line in file_data ]
            #     for l in sample_lst:
            #         for k,v in l.items():
            #             print(k,v)
    except FileNotFoundError:
        logger.info(f"file not found{file}" )

def file_Data(f):
    with open(f,'r',encoding='utf8') as f:
        data = SrcFileData(f)
        fdo = data.f_data
        print (fdo.file_hdr_rows)
        print (fdo.file_dtl_rows)
    return data

if __name__ == "__main__":
    main()