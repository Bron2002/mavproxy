from MAVProxy.modules.lib import mp_module
from threading import Timer


class GimbalTrackModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(GimbalTrackModule, self).__init__(mpstate, "gimbaltrack", "tracker for gimbal")
        print("init track gimbal")
        self.test_gimbal()

    def update_gimbal(self, y, p, r):
        print('test')
        for mp in self.module_matching('map*'):
            from MAVProxy.modules.mavproxy_map import mp_slipmap
            mp.map.add_object(mp_slipmap.SlipCircle(2323, 3,
                                                    (0, 0),
                                                    200,
                                                    (2, 222, 222),
                                                    linewidth=2))

    def test_gimbal(self):
        self.update_gimbal(1, 3, 4)
        self.t = Timer(1, self.test_gimbal).start()

def init(mpstate):
    return GimbalTrackModule(mpstate)