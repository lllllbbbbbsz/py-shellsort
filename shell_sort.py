'''

Created on 2014年7月26日

@author: Gao
'''





def shell_sort(list,size):
    increment=size
    while(increment>1):
        increment=increment//3+1
        for i in range(increment,size):
            tmp=list[i]
            j=i
            for j in range(i,-1,-increment):
                if(tmp<list[j-increment]):
                    list[j]=list[j-increment]
                else:
                    break
            list[j]=tmp
        

 
array=[2,6,8,3,0,23,8,4,12,95,1]
print(array)
shell_sort(array,array.__len__())
print(array)             

        
    
