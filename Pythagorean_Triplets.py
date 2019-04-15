##--Pythagorean Triplets--####
def pythagoreanTriplets(limits) : 
    c, m = 0, 2
    arr=[]
    while c < limits : 
          
        # Now loop on n from 1 to m-1 
        for n in range(1, m) : 
            a = m * m - n * n 
            b = 2 * m * n 
            c = m * m + n * n 
  
            # if c is greater than 
            # limit then break it 
            if c > limits : 
                break
  
            arr.append([a, b, c]) 
  
        m = m + 1
    return arr
  
  
if __name__ == '__main__' : 
      
    limit = 1000
    table=pythagoreanTriplets(limit)
    for i in table:
        if (i[0]+i[1]+i[2]==1000):
            print (i[0]*i[1]*i[2])
