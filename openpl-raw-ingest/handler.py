import datetime
import logging
import sys
import os
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[1])
sys.path.insert(0, project_root)

from scripts import ingest_openpwl

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):

    repo_dir = "../data/opl-repo"
    out_dir = "../data/download-out"

    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your cron function " + name + " ran at " + str(current_time))

    ingest_openpwl.download_openpwl_data(out_dir, repo_dir)

