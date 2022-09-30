import logging
logging.basicConfig(filename="log.txt", level=logging.DEBUG)

def run():
    while True:
        logging.debug("Debug logging test...")

run()