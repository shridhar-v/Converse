from Selenium2Library import Selenium2Library
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
import random
import sys



class Selenium2Custom(Selenium2Library):
    """
    Custom wrapper for robotframework Selenium2Library to add extra functionality
    """
    

    def get_onclick(self, locator):
        """
        Returns the placeholder text of element identified by `locator`.
        """
        element = self._element_find(locator, True, False)        
        return element.get_attribute("@outerHTML")
    

    def css_should_match_x_times(self, css_locator, expected_css_count, message='', loglevel='INFO'):
        """Verifies that the page contains the given number of elements located by the given `CSS Selector`.

        See `Page Should Contain Element` for explanation about `message` and
        `loglevel` arguments.
        """

        actual_css_element_count = len( self._element_find("css=" + css_locator, False, False))
        if int(actual_css_element_count) != int(expected_css_count):
            if not message:
                message = "Css Locator %s should have matched %s times but matched %s times"\
                            %(css_locator, expected_css_count, actual_css_element_count)
            self.log_source(loglevel)
            raise AssertionError(message)
        self._info("Current page contains %s elements matching '%s'."
                   % (actual_css_element_count,css_locator))

    def switch_to_last_window(self):             
        handles = self._current_browser().get_window_handles()
        self._current_browser().switch_to_window(handles[-1])
    
    
    def drag_drop_with_offset_to_element(self, locator_source, locator_target, x_by_10=1, y_by_10=1):
        
        source = self._element_find(locator_source, True, False)
        target = self._element_find(locator_target, True, False)
        

        elms = self._element_find("css=.dummyCanvasWrapper *[id]", False, False)
        len(elms)
        elements = {}
        
        for e in elms:
            elements[e.get_attribute("id")]=e
        
        p1 = source.location
        d1 = source.size
        p2 = target.location
        d2 = target.size
                    
        x_offset = ((int(d2['width'])/10)*(int(x_by_10)))-int((d1['width'])/2)
        y_offset = ((int(d2['height'])/10)*(int(y_by_10)))-int((d1['height'])/2)
        offset = {'x':int(p2['x']-p1['x']),'y':int(p2['y']-p1['y'])}
        self.drag_and_drop_by_offset(locator_source, offset['x']+x_offset, offset['y']+y_offset)
        
        elms1 = self._element_find("css=.dummyCanvasWrapper *[id]", False, False)
        
        for e in elms1:
            if e.get_attribute("id") not in elements.keys(): return e.get_attribute("id")
        return elements.keys()

    def test_my_key(self):
        elms = self._element_find("css=#ires a[id]", False, False)
        ids = {}
        for e in elms:
            ids[e.get_attribute("id")] = e
        if "anewID" not in ids.keys():
            ids["anewID"] = None
        return str(ids)

    def click_multiple_with_ctrl_down(self, locator,numbers=5):
        
        elements = self._element_find(locator, False, True)
        actions = ActionChains(self._current_browser())
        actions.key_down(keys.Keys.CONTROL).perform()
        sampl = random.sample(elements,int(numbers))
        for e in sampl:
            e.click()
        actions.key_up(keys.Keys.CONTROL).perform()
          
        
          
        
