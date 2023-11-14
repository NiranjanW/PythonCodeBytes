import logging 
import re 
from munch import Munch

class SrcFileData:

    HDR_LINE_PATTERN = 'PIKH'
    DTL_LINE_PATTERN = 'PIKD'

    def __init__(self, src_file):
        self.f_data = SrcFileData._get_hdr_dtl_Data(src_file)

    @classmethod
    def _get_hdr_dtl_Data(cls, src_file):
        file_data =Munch()
        file_data.file_hdr_rows = []
        file_data.file_dtl_rows = []

        for data in src_file:
            if data[:4] ==SrcFileData.HDR_LINE_PATTERN:
                file_data.file_hdr_rows.append(data)
            elif data[:4] == SrcFileData.DTL_LINE_PATTERN:
                file_data.file_dtl_rows.append(data)
        file_data.file_name = src_file.name
        return file_data





