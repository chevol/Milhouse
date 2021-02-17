import time
import walmart
import target
import bestbuy
import amazon
import logging

logging.basicConfig(filename='milhouse.log', format='%(asctime)s - %(message)s', datefmt='%B %d, %Y %I:%M:%S %p')

def check_inventory():
    walmartchecker = walmart.WalmartChecker()
    targetchecker = target.TargetChecker()
    bestbuychecker = bestbuy.BestBuyChecker()
    #amazonchecker = amazon.AmazonChecker()

    walmartchecker.check_inventory()
    targetchecker.check_inventory()
    bestbuychecker.check_inventory()
    #amazonchecker.check_inventory()

while True:
    try:
        logging.warning('Starting Milhouse Stock Checker')
        check_inventory()
        logging.warning('Finished Checking Stock')
        time.sleep(165)
    except Exception as e:
        logging.error("An error occured trying to check inventory", exc_info=True)
