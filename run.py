import os
import logging

# --- Format logger for print statements
FORMAT = '%(asctime)-15s %(levelname)-7s %(message)s'
TIMESTAMP = '%Y-%m-%d %H:%M:%S'
LOGVERBOSITY = 'DEBUG'
logging.basicConfig(level=os.getenv("LOGLEVEL", LOGVERBOSITY), format=FORMAT, datefmt=TIMESTAMP)
logger = logging.getLogger(__name__)

if __name__ == "__main__":

    # --- Import module
    from blueprint.blueprint import Blueprint

    # --- Instantiate object
    blueprinter = Blueprint()

    # --- Run method
    result = blueprinter.multiply_numbers(5, 7)
    logger.info('Result is: %s', result)
