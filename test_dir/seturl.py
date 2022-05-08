import setdatetime
import setindex

def set_url():
    dt = setdatetime.set_datetime()
    index = setindex.set_index()

    test_url = dt +"$"+"a1"+"$"+index

    return(test_url)

