import os
import signal
import time
import pytest
import multiprocessing

# Hazzathread we test if it can go out of scope without joining.
from dls_hazzathread_lib.hazzathread import Hazzathread

# Class which is base for main programs.
from dls_mainiac_lib.mainiac import Mainiac

# Class under test.
from dls_siggy_lib.global_signals import global_sigint


import logging

logger = logging.getLogger(__name__)


class Test_02_sigint2:

    # ----------------------------------------------------------------------------------------
    def test_02_sigint2(
        self,
        logging_setup,
        output_directory,
    ):
        """
        Test signal class.
        """

        failure_message = None
        try:
            _process = _Process()
            _process.start()
            logger.info("main sleeping before first signal")
            time.sleep(1.0)
            os.kill(_process.pid, signal.SIGINT)

            logger.info("main sleeping before second signal")
            time.sleep(0.5)
            os.kill(_process.pid, signal.SIGINT)

            _process.join(timeout=10)
            logger.info("main sees process down")

        except Exception as exception:
            logger.exception("unexpected exception during the test", exc_info=exception)
            failure_message = str(exception)

        if failure_message is not None:
            pytest.fail(failure_message)


# ---------------------------------------------------------------------------------
class _Process(multiprocessing.Process):
    def __init__(self):
        self.name = "app"
        multiprocessing.Process.__init__(self)

    def run(self):
        app = _App("test_02_sigint2")

        # Run the gui wrapped in a try/catch.
        app.try_run_catch()


# ---------------------------------------------------------------------------------
class _Context(object):
    def __init__(self, name, manager):
        self._name = name
        self._manager = manager

    def __enter__(self):
        logger.info("Context entering")
        self._manager[self._name] = "entered"

        return self

    def __exit__(self, type, value, tb):
        logger.info("Context exiting")
        self._manager[self._name] = "exited"


# ---------------------------------------------------------------------------------
class _Thread(Hazzathread):
    def __init__(self, name):
        Hazzathread.__init__(self, name)

    def _run(self):
        self._set_ready()
        logger.info("Thread sleeping")
        time.sleep(10.0)
        logger.info("Thread finished")


# ---------------------------------------------------------------------------------
class _File(object):
    def __init__(self, name, manager):
        self._manager = manager
        self._name = name
        self._subobject = _Subobject(name)
        self._manager[self._name] = "constructed"

    def __del__(self):
        logger.info("File %s destructing" % (self._name))
        self._manager[self._name] = "destructed"


# ---------------------------------------------------------------------------------
class _Subobject(object):
    def __init__(self, name):
        self._name = name

    def __del__(self):
        logger.info("Subobject %s destructing" % (self._name))


# ---------------------------------------------------------------------------------
class _App(Mainiac):
    """
    App class.
    """

    def __init__(
        self,
        app_name,
    ):
        super().__init__(app_name)

    # ----------------------------------------------------------
    def run(self):
        logger.info("app sets up")

        manager = {}
        manager["finally"] = "no"
        manager["keyboard"] = "uninterrupted"
        thread = None

        file1 = _File("file1", manager)
        try:
            # Activate the signal handling.
            global_sigint.activate(auto_deactivate_count=1)

            file2 = _File("file2", manager)

            # Start a thread which should not die due to the signal.
            thread = _Thread("thread1")
            thread.start()
            thread.wait_ready()

            start_time = time.time()
            with _Context("context1", manager) as context:
                with pytest.raises(RuntimeError) as excinfo:
                    manager["sleep1"] = "sleeping"
                    time.sleep(3)
                    logger.info(
                        "woke from sleep after %0.3f seconds"
                        % (time.time() - start_time)
                    )
                    manager["sleep1"] = "awoke"

        except KeyboardInterrupt as exception:
            # We will get this exception because we have set auto_deactivate_count=1.
            logger.info("keyboard interrupting")
            manager["keyboard"] = "interrupted"

        finally:
            logger.info("finally")
            global_sigint.deactivate()
            file2 = None
            manager["finally"] = "yes"

        # Make sure everything happened which was supposed to.
        assert global_sigint.count() == 1
        assert manager["keyboard"] == "interrupted", "keyboard"
        assert manager["finally"] == "yes", "finally"
        assert manager["sleep1"] == "sleeping", "sleep1"
        assert manager["file1"] == "constructed", "file1"
        assert manager["file2"] == "destructed", "file2"
        assert manager["context1"] == "exited", "context1"
        assert thread.is_running()
