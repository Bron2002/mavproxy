'''
Im here module.
todo: inherit map module
'''

from pymavlink import mavutil
import time

from MAVProxy.modules.lib import mp_module
import MAVProxy.modules.mavproxy_map as mavproxy_map
import inspect

class ImhereModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(ImhereModule, self).__init__(mpstate, "imhere", "")
        self.map = mavproxy_map.init(mpstate)
        self.add_command("imhere", self.test, "test imhere cmd")
        # print(self.map.map.app.frame.state.panel)

    def test(self, args):
        print(">clbck")
        print(mavutil.mavlink.MAV_CMD_EXTERNAL_POSITION_ESTIMATE)



def init(mpstate):
    return ImhereModule(mpstate)
