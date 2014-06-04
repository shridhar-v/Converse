from Selenium2Library import Selenium2Library

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
          
        
