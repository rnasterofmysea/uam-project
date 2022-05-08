from random import *

def set_index():
#주안역: 37.465055,126.679690
#인하대역: 37.448474, 126.649501

    test_h1 = round(uniform(37.448474, 37.465055),6)
    test_w1 = round(uniform(126.649501, 126.679690),6)

    test_h2 = test_h1 + 0.0008936
    test_w2 = test_w1
    
    test_h3 = test_h2
    test_w3 = test_w2 + 0.001173
    
    test_index = str(test_h1) +"$" + str(test_w1) + "$"+ str(test_h2)+ "$" + str(test_w2) + "$" + str(test_h3) + "$" + str(test_w3)

    return test_index
#위도 약 100m = 0.0008936
#경도 약 100m = 0.001173

