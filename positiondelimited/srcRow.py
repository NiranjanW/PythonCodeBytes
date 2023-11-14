import os
from pathlib import Path
import logging


class SrcRow:

    hdrRow = {
        "hdr_record_type": 4,
        "hdr_from_depot": 7,
        "hdr_filler1": 5,
        "hdr_order_num": 5,
        "hdr_filler2": 6,
        "hdr_storenum": 5,
        "hdr_filler3": 5,
        "hdr_external_ref": 10,
        "hdr_route": 4,
        "hdr_shipto_storenum": 5,
        "hdr_filler4": 5,
        "hdr_order_type": 2,
        "hdr_unit_of_measure": 1,
        "hdr_order_priority": 6,
        "hdr_filler5": 10,
        "hdr_orig_order_date": 8,
        "hdr_order_date": 8,
        "hdr_order_time": 6,
        "hdr_delivery_date": 8,
        "hdr_filler6": 177,
    }

    dtlRow = {}


    @classmethod
    def fields(cls, row_type, row):
        field_type = cls.hdrRow
        start_pos = 0
        row_dict = {}
        for field, width in field_type.items():
            field_val = row[start_pos : start_pos + width]
            row_dict[field] = str(field_val).strip()
            start_pos += width

        return row_dict

