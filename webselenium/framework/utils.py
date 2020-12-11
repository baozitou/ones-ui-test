# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utils.logger import Logger

logger = Logger(logger=__name__).getlog()

def local_expected_conditions(ec_func="presence_of_element_located"):
    if ec_func == "presence_of_element_located":
        return EC.presence_of_element_located
    elif ec_func == "title_is":
        return EC.title_is
    elif ec_func == "title_contains":
        return EC.title_contains
    elif ec_func == "url_contains":
        return EC.url_contains
    elif ec_func == "url_matches":
        return EC.url_matches
    elif ec_func == "url_to_be":
        return EC.url_to_be
    elif ec_func == "url_changes":
        return EC.url_changes
    elif ec_func == "visibility_of_element_located":
        return EC.visibility_of_element_located
    elif ec_func == "visibility_of":
        return EC.visibility_of
    elif ec_func == "presence_of_all_elements_located":
        return EC.presence_of_all_elements_located
    elif ec_func == "visibility_of_any_elements_located":
        return EC.visibility_of_any_elements_located
    elif ec_func == "visibility_of_all_elements_located":
        return EC.visibility_of_all_elements_located
    elif ec_func == "text_to_be_present_in_element":
        return EC.text_to_be_present_in_element
    elif ec_func == "frame_to_be_available_and_switch_to_it":
        return EC.frame_to_be_available_and_switch_to_it
    elif ec_func == "invisibility_of_element_located":
        return EC.invisibility_of_element_located
    elif ec_func == "invisibility_of_element":
        return EC.invisibility_of_element
    elif ec_func == "element_to_be_clickable":
        return EC.element_to_be_clickable
    elif ec_func == "staleness_of":
        return EC.staleness_of
    elif ec_func == "element_to_be_selected":
        return EC.element_to_be_selected
    elif ec_func == "element_located_to_be_selected":
        return EC.element_located_to_be_selected
    elif ec_func == "element_selection_state_to_be":
        return EC.element_selection_state_to_be
    elif ec_func == "element_located_selection_state_to_be":
        return EC.element_located_selection_state_to_be
    elif ec_func == "number_of_windows_to_be":
        return EC.number_of_windows_to_be
    elif ec_func == "new_window_is_opened":
        return EC.new_window_is_opened
    elif ec_func == "alert_is_present":
        return EC.alert_is_present

    
def formart_selector(selector):
    """格式化selector

    Args:
        selector ([type]): [description]

    Raises:
        NameError: 定位元素的方式不正确

    Returns:
        formart_selector_by: 定位元素的方式
        selector_value: 定位元素的值
    """
    if "=>" not in selector:
        logger.error("'selector' is not valid!")
        return False
    selector_by = selector.split('=>')[0]
    selector_value = selector.split('=>')[1]
    formart_selector_by = None
    if selector_by == "i" or selector_by == 'id':
        formart_selector_by = By.ID
    elif selector_by == "n" or selector_by == 'name':
        formart_selector_by = By.NAME
    elif selector_by == "c" or selector_by == 'class_name':
        formart_selector_by = By.CLASS_NAME
    elif selector_by == "l" or selector_by == 'link_text':
        formart_selector_by = By.LINK_TEXT
    elif selector_by == "p" or selector_by == 'partial_link_text':
        formart_selector_by = By.PARTIAL_LINK_TEXT
    elif selector_by == "t" or selector_by == 'tag_name':
        formart_selector_by = By.TAG_NAME
    elif selector_by == "x" or selector_by == 'xpath':
        formart_selector_by = By.XPATH
    elif selector_by == "s" or selector_by == 'css':
        formart_selector_by = By.CSS_SELECTOR
    else:
        raise NameError("Please enter a valid type of targeting elements.")
    return formart_selector_by, selector_value