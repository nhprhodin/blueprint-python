import logging
import argparse

# --- Format logger for print statements
FORMAT = "%(asctime)-15s %(levelname)-7s %(message)s"
TIMESTAMP = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=FORMAT, datefmt=TIMESTAMP)
logger = logging.getLogger(__name__)

# --- Define log levels
_LOG_LEVEL_STRINGS = ["CRITICAL", "ERROR", "WARNING", "INFO", "DEBUG"]


def _log_level_options(log_level_string):
    if log_level_string not in _LOG_LEVEL_STRINGS:
        message = "Invalid choice: {0} (choose from {1})".format(
            log_level_string, _LOG_LEVEL_STRINGS
        )
        raise argparse.ArgumentTypeError(message)
    return log_level_string


def main():
    # --- Import libraries
    from blueprint.blueprint import Blueprint
    import configparser

    # --- Parse arguments
    parser = argparse.ArgumentParser(description="Parses input.")
    parser.add_argument(
        "-c", "--config", dest="config", required=True, help="Path to config file."
    )
    parser.add_argument(
        "-l",
        "--loglevel",
        dest="log_level",
        required=False,
        default="INFO",
        type=_log_level_options,
        help="Set log level. {0}".format(_LOG_LEVEL_STRINGS),
    )
    args = parser.parse_args()
    logging.getLogger().setLevel(args.log_level)
    if args.config:
        logger.debug("Parsed config file from %s", args.config)

    # --- Read configuration
    config = configparser.ConfigParser()
    try:
        config.read_file(open(args.config))
        logger.debug("Reading config file from %s", args.config)
    except IOError as e:
        logger.exception("Could not find config file: %s", args.config)

    # --- Instantiate object
    blueprinter = Blueprint(config=config)

    # --- Run method
    result = blueprinter.multiply_numbers(5, 4)
    logger.info("Result is: %s", result)


if __name__ == "__main__":
    main()
