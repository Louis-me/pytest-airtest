import pytest
from pages.my_page import MyPage


class TestCaseTestMy(object):

    @pytest.mark.finished1
    def test_my_01(self, poco):
        MyPage.home(poco)

    @pytest.mark.finished
    def test_my_02(self, poco):
        MyPage.home(poco)

    @pytest.mark.finished
    def test_my_03(self, poco):
        MyPage.home(poco)

    @pytest.mark.finished
    def test_my_04(self, poco):
        MyPage.home(poco)

    @pytest.mark.finished
    def test_my_05(self, poco):
        MyPage.home(poco)
    @pytest.mark.finished
    def test_my_06(self, poco):
        MyPage.home(poco)

    # @pytest.mark.finished
    # def test_my_07(self, poco):
    #     MyPage.home(poco)
    # @pytest.mark.finished
    # def test_my_08(self, poco):
    #     MyPage.home(poco)
    # @pytest.mark.finished
    # def test_my_09(self, poco):
    #     MyPage.home(poco)
    # @pytest.mark.finished
    # def test_my_10(self, poco):
    #     MyPage.home(poco)
    # @pytest.mark.finished
    # def test_my_11(self, poco):
    #     MyPage.home(poco)
    # @pytest.mark.finished
    # def test_my_12(self, poco):
    #     MyPage.home(poco)







