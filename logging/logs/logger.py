# Configuring logging
import logging

logging.basicConfig(
    filename='app.log',# filename='app.log' --> writes all log messages to a file named app.log instead of the console
    filemode='w', # filemode='w'--> opens the log file in write mode (overwrites the file each run)
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force='True' ## for showing time and date and year
)