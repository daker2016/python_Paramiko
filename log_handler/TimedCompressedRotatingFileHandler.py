import logging.handlers
import zipfile
import os


def namer(name):
    return name.replace(".", "-") + ".zip"


def rotator(source, dst):
    with zipfile.ZipFile(dst, mode='w', compression=zipfile.ZIP_DEFLATED) as zf:
        parent_path, name = os.path.split(source)
        zf.write(name, arcname=name)


class TimedCompressedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    """
    this class is not used.There are some problems when use it.it needs debug.
    """
    namer = namer
    rotator = rotator

#
#     def doRollover(self):
#         """
#         do a rollover; in this case, a date/time stamp is appended to the filename
#         when the rollover happens.  However, you want the file to be named for the
#         start of the interval, not the current time.  If there is a backup count,
#         then we have to get a list of matching filenames, sort them and remove
#         the one with the oldest suffix.
#         """
#
#         self.stream.close()
#         # get the time that this sequence started at and make it a TimeTuple
#         t = self.rolloverAt - self.interval
#         timeTuple = time.localtime(t)
#         dfn = self.baseFilename + "." + time.strftime(self.suffix, timeTuple)
#         if os.path.exists(dfn):
#             os.remove(dfn)
#         os.rename(self.baseFilename, dfn)
#         if self.backupCount > 0:
#             # find the oldest log file and delete it
#             s = glob.glob(self.baseFilename + ".20*")
#             if len(s) > self.backupCount:
#                 s.sort()
#                 os.remove(s[0])
#         # print "%s -> %s" % (self.baseFilename, dfn)
#         if self.encoding:
#             # self.baseFilename = os.path.abspath(filename)
#             self.stream = codecs.open(self.baseFilename, 'w', self.encoding)
#         else:
#             self.stream = open(self.baseFilename, 'w')
#         self.rolloverAt = self.rolloverAt + self.interval
#         if os.path.exists(dfn + ".zip"):
#             os.remove(dfn + ".zip")
#         file = zipfile.ZipFile(dfn + ".zip", "w")
#         file.write(dfn, os.path.basename(dfn), zipfile.ZIP_DEFLATED)
#         file.close()
#         os.remove(dfn)
#
#
# if __name__ == '__main__':
#
#     # Demo of using TimedCompressedRotatingFileHandler() to log every 5 seconds,
#     # to one uncompressed file and five rotated and compressed files
#
#     os.nice(19)  # I always nice test code
#
#     # Total of six rotated log files, rotating every 5 secs
#     logHandler = TimedCompressedRotatingFileHandler("mylog", when="S", interval=5, backupCount=5)
#
#     logFormatter = logging.Formatter(
#         fmt='%(asctime)s.%(msecs)03d %(message)s',
#         datefmt='%Y-%m-%d %H:%M:%S'
#     )
#     logHandler.setFormatter(logFormatter)
#     mylogger = logging.getLogger('MyLogRef')
#     mylogger.addHandler(logHandler)
#     mylogger.setLevel(logging.DEBUG)
#
#     # Write lines non-stop into the logger and rotate every 5 seconds
#     ii = 0
#     while True:
#         mylogger.debug("Test {0}".format(ii))
#         ii += 1
