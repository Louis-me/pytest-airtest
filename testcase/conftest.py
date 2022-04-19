import pytest
from py._xmlgen import html
from airtest.core.api import *
from airtest.cli.parser import cli_setup
import base64
from airtest.core import api


def pytest_addoption(parser):
    parser.addoption("--pkg", action="store",default="包名")
    parser.addoption("--dev", action="store", dest="dev",default="设备")


@pytest.fixture(scope='session')
def pkg(request):
    return request.config.getoption("--pkg")

@pytest.fixture(scope='session')
def dev(request):
    return request.config.getoption("dev")
    # return request.getoption("dev")


_poco = None


# @pytest.fixture()
@pytest.fixture(scope='session', autouse=True)
def poco(dev):
    global _poco
    # if not cli_setup():
    #     auto_setup(__file__, logdir=True, devices=[
    #         "android://127.0.0.1:5037/ZL9LC685V86DNNMN?cap_method=MINICAP&&ori_method=MINICAPORI&&touch_method=MAXTOUCH", ])
    print("-sss--")
    print(dev)
    device = connect_device("Android://127.0.0.1:5037/%s" % dev)

    # device = connect_device("android://127.0.0.1:5037/ZL9LC685V86DNNMN")
    # device = connect_device("android://127.0.0.1:5037/emulator-5554")
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    _poco = AndroidUiautomationPoco(device, use_airtest_input=True,  screenshot_each_action=False)

    # G.DEVICE.wake()



    # 返回数据
    yield _poco
    # 实现用例后置



def pytest_html_results_table_header(cells):
    cells.insert(1, html.th('用例名称'))
    cells.insert(2, html.th('Test_nodeid'))
    cells.pop(2)


# def pytest_html_results_table_row(report, cells):
#     cells.insert(1, html.td(report.description))
#     # cells.insert(1, html.td("测试下"))
#     cells.insert(2, html.td(report.nodeid))
#     cells.pop(2)


def pytest_html_results_table_html(report, data):
    # if report.passed:
    #     del data[:]
    #     data.append(html.div('通过的用例未捕获日志输出.', class_='empty log'))
    pass


def pytest_html_report_title(report):
    report.title = "pytest示例项目测试报告"
