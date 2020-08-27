import time

def calcProd():
    product = 1
    for i in range(1, 100000):
        product *= i
    return product

start_time = time.time()
prod = calcProd()
end_time = time.time()

print("The result is %s digits long. " % (len(str(prod))))
print("Took %s seconds to calculate." % (end_time - start_time ))

