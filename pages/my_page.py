from airtest.core.api import snapshot, start_app, sleep, stop_app
import logging
from datetime import datetime
class MyPage(object):



    @classmethod
    def home(cls, poco):
        logging.info("开始测试"+ datetime.now().strftime("%H:%M:%S"))
        try:
            stop_app('com.jianshu.haruki')
            start_app('com.jianshu.haruki')
            sleep(5)
        except Exception:
            pass

        # from poco.drivers.android.uiautomation import AndroidUiautomationPoco
        # poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
        try:
            # poco("com.android.systemui:id/scrim_behind").wait_for_appearance(1)
            # if poco("com.jianshu.haruki:id/dialog_lucky_prize_close").exists():
            #     poco("com.jianshu.haruki:id/dialog_lucky_prize_close").click()

            poco("com.jianshu.haruki:id/iv_home_page").wait(10).click()
            logging.info("点击了首页"+ datetime.now().strftime("%H:%M:%S"))

        except Exception as e:
            snapshot(msg="报错后截图")
            raise e

    @classmethod
    def info(cls):
        pass