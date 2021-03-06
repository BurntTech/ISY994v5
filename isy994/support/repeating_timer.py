import time
from threading import Event, Thread

import logging

logger = logging.getLogger(__name__)


class Repeating_Timer(object):

    """Repeat `function` every `interval` seconds."""

    def __init__(self, interval):
        self.interval = interval

        self.start = time.time()
        self.event = Event()

        self.thread = Thread(target=self._target)
        self.thread.setDaemon(True)
        self.thread.start()

        self.callbacks = []

    def _target(self):
        while not self.event.wait(self._time):
            for callback in self.callbacks:
                # print ('start')
                try:
                    callback()
                except Exception as e:
                    logger.error("Error in timer callback: {}".format(e))
                # print ('end')

    @property
    def _time(self):
        return self.interval - ((time.time() - self.start) % self.interval)

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def stop(self):
        self.event.set()
        self.thread.join()
