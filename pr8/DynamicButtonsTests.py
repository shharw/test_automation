import pytest
from DynamicButtonsPages import SearchHelper

@pytest.mark.usefixtures("driver_setup")
class TestDynamicButtons:
    def test_dynamic_buttons(self):
        search_helper = SearchHelper(self.driver)

        search_helper.go_to_site()

        search_helper.click_button_0()
        search_helper.click_button_1()
        search_helper.click_button_2()
