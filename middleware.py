from fastapi import Request
import logging
import sys
import time

async def log_request(request: Request, call_next):
    """
    Middleware to log request details.

    Parameters:
        request (Request): The incoming request object.
        call_next (function): The function to call to continue processing the request.

    Returns:
        Response: The response to the request.
    """
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    log_dict = {
        "url": request.url.path,
        "method": request.method,
        "process_time": process_time,
        "host": request.client.host,
        "ip": request.client.host
    }
    logger.info(log_dict, extra=log_dict)

    return response

file_path = "log.txt"

logger = logging.getLogger()
logger.setLevel(logging.INFO)

formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)

file_handler = logging.FileHandler(file_path)
file_handler.setFormatter(formatter)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)