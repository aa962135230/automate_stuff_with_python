import logging

logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Some debugging deatils.')

logging.info('The logging module is working.')

logging.warning('An error message is about to be logged.')

logging.error('An error has occureed.')
logging.critical('The program is unable to recover!')