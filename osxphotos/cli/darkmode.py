"""Detect dark mode on MacOS >= 10.14 or fake it elsewhere"""

from osxphotos.utils import is_macos


if is_macos:
    import objc
    import Foundation

    def theme():
        with objc.autorelease_pool():
            user_defaults = Foundation.NSUserDefaults.standardUserDefaults()
            system_theme = user_defaults.stringForKey_("AppleInterfaceStyle")
            return "dark" if system_theme == "Dark" else "light"

    def is_dark_mode():
        return theme() == "dark"

    def is_light_mode():
        return theme() == "light"

else:

    def theme():
        return "light"

    def is_dark_mode():
        return theme() == "dark"

    def is_light_mode():
        return theme() == "light"
