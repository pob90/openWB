#!/usr/bin/python3
from typing import List
import os, sys, traceback, time, struct, binascii
try: # make script callable from command line and LRS
    from bezug_rct2 import rct_lib
except:
    import rct_lib

# Entry point with parameter check
def main(argv: List[str]):
    start_time = time.time()
    rct = rct_lib.RCT(argv)

    if rct.connect_to_server() == True:
        try:
            # generate id list for fast bulk read
            MyTab = []
            cell0       = rct.add_by_name(MyTab, 'battery.cells[0]')

            # read all parameters
            response = rct.read(MyTab)
            rct.close()
            
            for i in range(0, len(cell0.value), 8):
                vbytes = cell0.value[i:i+8].decode("utf-8")
                print(vbytes)
                b8 = bytearray.fromhex(vbytes) #float.fromhex(vbytes)
                print(b8)
                f = struct.unpack('<f', b8)
                print("{:3d} {:s} {:f}".format(i, vbytes, f))

            # debug output of processing time and all response elements
            rct.dbglog(response.format_list(time.time() - start_time))
        except:
            print("-"*100)
            traceback.print_exc(file=sys.stdout)
            rct.close()

    rct = None

if __name__ == "__main__":
    main(sys.argv[1:])
