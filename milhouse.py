import time
import walmart
import target
import bestbuy
import amazon

def check_inventory():
    walmartchecker = walmart.WalmartChecker()
    targetchecker = target.TargetChecker()
    bestbuychecker = bestbuy.BestBuyChecker()
    amazonchecker = amazon.AmazonChecker()

    walmartchecker.check_inventory()
    targetchecker.check_inventory()
    bestbuychecker.check_inventory()
    amazonchecker.check_inventory()

while True:
    print("----------------------------------------------")
    try:
        check_inventory()
        time.sleep(165)
    except:
        print("An error occured trying to check inventory")