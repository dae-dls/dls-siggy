import os
import shutil
import json
import pytest

# The device version.
from dls_siggy_lib.version import meta as version_meta

# Formatting of testing log messages.
from dls_logform.dls_logform import DlsLogform

import logging

logger = logging.getLogger(__name__)


# --------------------------------------------------------------------------------
@pytest.fixture(scope="session")
def logging_setup(request):
    """
    Override the logger provided by pytest to set the format and log level.
    """

    print("")

    handler = logging.StreamHandler()
    handler.setFormatter(DlsLogform())
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.DEBUG)

    # Cover the version.
    logger.info("\n%s", (json.dumps(version_meta(), indent=4)))


# --------------------------------------------------------------------------------
@pytest.fixture(scope="function")
def output_directory(request):

    # Tmp directory which we can write into.
    output_directory = "/tmp/%s/%s/%s" % (
        "/".join(__file__.split("/")[-3:-1]),
        request.cls.__name__,
        request.function.__name__,
    )

    # Tmp directory which we can write into.
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory, ignore_errors=False, onerror=None)
    os.makedirs(output_directory)

    logger.debug("setup @fixture output_directory yields %s" % (output_directory))

    yield output_directory
