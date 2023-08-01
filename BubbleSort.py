def bubbleSort(arr) : 
    n = len(arr)
    swapped = False
    
    for i in range (n-1):
        for j in range (0 , n-i-1):
            
            if arr[j] > arr[j+1] : 
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
            
            if not swapped:
                break
                
    print("sorted array")

    for i in range(len(arr)):
        print("%d" % arr[i], end=" ")
        
            
if __name__ == "__main__":
    
    arr = [1,5,4,3,2]
    
    bubbleSort(arr)
    
   
