"""
Make sure the TradeStation client is up by verifying expected processes are running
"""

import wmi

ts = ['ORCAL.exe', 'orchart.exe', 'ORCLPrxy.exe', 'ORDllHst.exe', 'ORPlat.exe']


def running():
    processes = [str(p.Name) for p in wmi.WMI().Win32_Process()]
    for p in ts:
        if p not in processes:
            return False
    return True

