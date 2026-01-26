import logging

# Configure logging to show DEBUG level logs, with timestamp, logger name, level, and message
# Logs are sent to both a file (app1.log) and the console
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    force=True,  # Forces reconfiguration in interactive environments like Jupyter
    handlers=[
        logging.FileHandler('app1.log'),  # Writes logs to a file for later analysis
        logging.StreamHandler()            # Displays logs in the console in real time
    ]
)

# Create a named logger for the application
logger = logging.getLogger('ArithmethicsApp')

def add(a, b):
    """Adds two numbers and logs the operation."""
    result = a + b
    logger.debug(f'Adding {a} + {b} = {result}')
    return result

def subtract(a, b):
    """Subtracts second number from first and logs the operation."""
    result = a - b
    logger.debug(f'Subtracting {a} - {b} = {result}')
    return result

def multiply(a, b):
    """Multiplies two numbers and logs the operation."""
    result = a * b
    logger.debug(f'Multiplying {a} * {b} = {result}')
    return result

def divide(a, b):
    """Divides two numbers and logs the result or error."""
    try:
        result = a / b
        logger.debug(f'Dividing {a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Division by zero error')
        return None

# Function calls to generate logs
add(10, 15)
subtract(10, 15)
multiply(10, 15)
divide(10, 2)