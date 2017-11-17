#!/usr/bin/python3
 
# The MIT License (MIT)
# Copyright (c) 2017 "Laxminarayan Kamath G A"<kamathln@gmail.com>
 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
 
"""
Command line interface to pystray library. SOmehwat incomplete now.
TODO: Implement menus
 
Requirements: python3, pystray and PIL
"""
 
import PIL.Image
import sys
import pystray
 
 
def perr(s):
    sys.stderr.write(s)
    sys.stderr.flush()
 
 
def pout(s):
    sys.stdout.write(s)
    sys.stdout.flush()
 
 
def checkstat(icon):
    try:
        while True:
            commandline = sys.stdin.readline()
            command = commandline.strip().split(':')
 
            found = False
            if command[0] in ['tray_exit', '']:
                icon.stop()
                break
 
            if command[0] == 'tray_iconpath':
                try:
                    icons[command[1]] = PIL.Image.open(command[2])
                except FileNotFoundError:
                    perr("File {} not found\n".format(command[2]))
 
                found = True
 
            if command[0] == 'tray_icon':
                try:
                    icon.icon = icon.icons[command[1]]
                except KeyError:
                    perr("Icon name {} not set. Use seticon first\n".format(
                                                                    command[1]
                                                                    ))
                found = True
 
            if command[0] == 'tray_show':
                icon.visible = True
                found = True
 
            if command[0] == 'tray_hide':
                icon.visible = False
                found = True
 
            if command[0] == 'tray_warn':
                icon.warnings = command[1].lower() in ['1',
                                                       'true',
                                                       'yes',
                                                       'on']
                found = True
 
            if not found:
                if icon.warnings:
                    perr("Command passed to {} not found: {}".format(
                                                              sys.argv[0],
                                                              commandline
                                                              ))
                else:
                    pout(commandline)
 
    except BrokenPipeError: 
        perr("Exiting\n")
        icon.stop()
        sys.exit(0)
 
    except KeyboardInterrupt:
        perr("Exiting\n")
        icon.stop()
        sys.exit(0)
 
if __name__ == '__main__':
        if len(sys.argv) > 1:
            name = sys.argv[1]
        else:
            name = "testapp"
            perr(sys.argv[0] + ": WARNING: App name not set. Setting app name to testapp. To set app name, pass it as first argument on command line\n")
 
        icons = {
            'default': PIL.Image.open('39567a-cool-24.ico')
        }
 
        trayicon = pystray.Icon(name=name, icon=icons['default'], title=name)
        trayicon.icons = icons
        trayicon.warnings = True
        
        try:
            trayicon.run(checkstat)
        except KeyboardInterrupt:
            perr("Exiting due to interrupt\n")
        except Exception as e:
            perr("Exception Occured \n" + str(e))
        finally:
            trayicon.stop()
            sys.exit(0)