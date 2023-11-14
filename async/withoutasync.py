# Concurrency is a concept that opposes to parallelism; it means executing multiple tasks at the same time but not necessarily simultaneously while parallelism means executing tasks simultaneously.

import logging
import time
import requests

logging.getLogger().setLevel(logging.INFO)

def fet_url(p_url):
    try:
        resp = requests.get(p_url)
    except Exception as e:
        logging.info("Fetched")
    else:
        return resp.content