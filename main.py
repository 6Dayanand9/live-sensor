from sensor.exception import SensorException
import sys
from sensor.logger import logging

if(__name__)=="__main__":
    try:
        logging.info("Divided By Zero")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys) 