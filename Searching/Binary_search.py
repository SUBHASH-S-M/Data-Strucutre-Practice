
def rec(arr,low,high,key):
   low=low
   high=high
   mid=(low+high)//2

   if(arr[mid]==key):
       return(mid)
   elif(low==high):
        return ("elemnt not found") 
   elif(key>mid):
        return rec(arr,mid+1,high,key)
   elif(key<mid):
        return rec(arr,low,mid-1,key)
   
        
	
arr=[5,3,1,6,4]
key=4
print(rec(arr,0,len(arr)-1,key))  