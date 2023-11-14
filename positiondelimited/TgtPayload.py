from SrcFileData import SrcFileData
from srcRow import SrcRow

def _src_file(data, datatype, fname):
    _dict_final ={}
    for line in data:
        v = SrcRow.fields(datatype, line,fname)
        if not v:
            continue
        else:
            _dict_final.append(v)


