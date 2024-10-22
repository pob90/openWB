#!/usr/bin/python3
from typing import List
import os, sys, traceback, time
try: # make script callable from command line and LRS
    from bezug_rct2 import rct_lib
except:
    import rct_lib

import getopt

# Entry point with parameter check
def main(argv: List[str]):
    start_time = time.time()
    rct = rct_lib.RCT(argv)

    if rct.connect_to_server() == True:
        power = -100
        power_extern = False

        try:
            rct.battery_power_ctrl(power_extern, power)

            # generate id list for fast bulk read
            MyTab = []
            soc_strategy = rct.add_by_name(MyTab, 'power_mng.soc_strategy')
            battery_power_extern = rct.add_by_name(MyTab, 'power_mng.battery_power_extern')

            # read all parameters
            #response = rct.read(MyTab)
            rct.close()
            
            # debug output of processing time and all response elements
            #rct.dbglog(response.format_list(time.time() - start_time))
        except:
            print("-"*100)
            traceback.print_exc(file=sys.stdout)
            rct.close()

    rct = None

if __name__ == "__main__":
    main(sys.argv[1:])