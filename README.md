# Python-prime-number-generator-optimization-
Python script to generate first n prime numbers . Optimized by levels . Detailed time and optimization info given

## The various optimizations done in each level are:    
  v1 - no optimization  
  v2 - added break  
  v3 - filter out even   
  v4 - filter out even in for loop directly   
  v5 - limit search to half of i   
  v6 - limit search to square root of i   
  v7 - limit search to only previous prime numbers   
  v8 - limit search to only previous prime numbers but checking for less than directly at list addition rather than during modulus check   
  v9 - taking finding of sqrt of final number as constant outside   
  
 
 ## Their respective time required are:  
    258.44545817375183    
    24.8780837059021   
    23.12345814704895   
    22.465441465377808  
    11.63539743423462    
    0.11180853843688965   
    0.09911322593688965   
    0.03931570053100586   
    0.03710675239562988   
    0.020193815231323242  
    0.015111684799194336     


