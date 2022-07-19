def BestFit(weight, n, c):
    
    res = 0;
 
    bin_rem = [0]*n;
 
    for i in range(n):
         
        j = 0;
         
        min = c + 1;
        bi = 0;
 
        for j in range(res):
            if (bin_rem[j] >= weight[i] and bin_rem[j] -
                                       weight[i] < min):
                bi = j;
                min = bin_rem[j] - weight[i];
             
        if (min == c + 1):
            bin_rem[res] = c - weight[i];
            res += 1;
        else:
            bin_rem[bi] -= weight[i];
    return res;
 
if __name__ == '__main__':
    weight = [ 2, 5, 4, 7, 1, 3, 8 ];
    c = 10;
    n = len(weight);
    print("Number of bins required in Best Fit: ",
                             BestFit(weight, n, c));
