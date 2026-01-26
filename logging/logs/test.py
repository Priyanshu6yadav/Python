from logger import logging

def add(a,b):
    logging.debug("The addition operation is taling place")
    return a+b

logging.debug("The addidtion function is call")
add(10,15)