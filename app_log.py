#!/usr/bin/python
# ! encoding=utf-8

import logging.handlers
import time
import zipfile
import os.path


def namer(name):
    return name.replace(".", "-") + ".zip"


def rotator(source, dst):
    with zipfile.ZipFile(dst, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        parent_path, name = os.path.split(source)
        zf.write(name, arcname=name)


# logging.config.fileConfig("conf/logging.conf")
LOG_FILE = './testRotate.log'
logger = logging.getLogger("simpleExample")
handler = logging.handlers.TimedRotatingFileHandler(LOG_FILE, 's', 1, 720, None, False, True)

# set callback function for namer and rotator method in TimedRotatingFileHandler
# the two method is called in doRollover method which is for rotation log process
"""
    def rotation_filename(self, default_name):
        if not callable(self.namer):
            result = default_name
        else:
            result = self.namer(default_name)
        return result

    def rotate(self, source, dest):
        if not callable(self.rotator):
            # Issue 18940: A file may not have been created if delay is True.
            if os.path.exists(source):
                os.rename(source, dest)
        else:
            self.rotator(source, dest)
"""

handler.namer = namer
handler.rotator = rotator
logger.addHandler(handler)

currentTime = int(time.time())
logger.warning("warning message" + str(currentTime))
logger.error("error message" + str(currentTime))
logger.critical("critical message" + str(currentTime))
