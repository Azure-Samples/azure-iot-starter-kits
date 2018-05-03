# The MIT License (MIT)
# Copyright (c) 2014-18 Richard Hull and contributors
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in 
# the Software without restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
# Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# Adapted from https://github.com/rm-hull/luma.examples/blob/master/examples/demo_opts.py
#

import logging
import os
import sys

from luma.core import cmdline, error
import luma.core.virtual as lumac
from PIL import ImageFont


class OledDisplay(object):

    def __init__(self, font=None):
        self.font = font if font else self.get_default_font()
        self.device = self.get_device()
        self.term = lumac.terminal(self.device, self.font, animate=False)

    def println(self, text):
        self.term.println(text)

    def get_default_font(self):
        font_name = "FreePixel.ttf"
        font_size = 9
        font_path = os.path.abspath(os.path.join(
            os.path.dirname(__file__), 'fonts', font_name))
        return ImageFont.truetype(font_path, font_size)

    def display_settings(self, args):
        """
        Display a short summary of the settings.

        :rtype: str
        """
        iface = ''
        display_types = cmdline.get_display_types()
        if args.display not in display_types['emulator']:
            iface = 'Interface: {}\n'.format(args.interface)

        lib_name = cmdline.get_library_for_display_type(args.display)
        if lib_name is not None:
            lib_version = cmdline.get_library_version(lib_name)
        else:
            lib_name = lib_version = 'unknown'

        import luma.core
        version = 'luma.{} {} (luma.core {})'.format(
            lib_name, lib_version, luma.core.__version__)

        return 'Version: {}\nDisplay: {}\n{}Dimensions: {} x {}\n{}'.format(
            version, args.display, iface, args.width, args.height, '-' * 60)

    def get_device(self, actual_args=None):
        """
        Create device from command-line arguments and return it.
        """
        if actual_args is None:
            actual_args = sys.argv[1:]
        parser = cmdline.create_parser(description='luma.examples arguments')
        args = parser.parse_args(actual_args)

        if args.config:
            # load config from file
            config = cmdline.load_config(args.config)
            args = parser.parse_args(config + actual_args)

        print(self.display_settings(args))

        # create device
        try:
            device = cmdline.create_device(args)
        except error.Error as e:
            parser.error(e)

        return device
