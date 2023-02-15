import random
import time

def example(arr):

    arr2=[0,0,0,0,0]
    n= len(arr)

    for i in range(n):
        if(arr[i]==0):
            for t1 in range(i, n):
                p1=t1**(1/2)
                x1=n+1
                while(x1>=1):
                    x1=x1//2
                    arr2[i%5] += 1

        elif(arr[i]==1):
            for j in range(n):
                t2=n-j
                for p2 in range(1, n + 1):
                    x2=n+1
                    while(x2>0):
                        x2=x2//2
                        arr2[i%5] += 1


        elif(arr[i]==2):
            for t3 in range(1,n+1):
                x3=t3+1
                for p3 in range(t3**2):
                    arr2[i%5] += 1


    return arr2



def average_case(size):

    case=[]
    for i in range(0,size):
        case += [random.randint(0, 2)]
    return case

def best_case(size):
    case=[]
    for i in range(size):
        case+=[0]
    return case
def worst_case(size):
    case=[]
    for i in range(size):
        case+=[2]
    return case


cases=[1,5,10,25,50,75,100,150,200,250]

for i in range(10):
    best_array = best_case(cases[i])
    worst_array = worst_case(cases[i])


    start = time.time_ns()
    example(best_array)
    end = time.time_ns()
    print('Case: best Size: ' + str(cases[i]) + ' Elapsed Time: ' + str((end - start)))

    start = time.time_ns()
    example(worst_array)
    end = time.time_ns()
    print('Case: worst Size: ' + str(cases[i]) + ' Elapsed Time: ' + str((end - start)))
    
    average_array = average_case(cases[i])
    start1 = time.time_ns()
    example(average_array)
    end1 = time.time_ns()

    average_array = average_case(cases[i])
    start2 = time.time_ns()
    example(average_array)
    end2 = time.time_ns()

    average_array = average_case(cases[i])
    start3 = time.time_ns()
    example(average_array)
    end3 = time.time_ns()

    
    print('Case: average Size: ' + str(cases[i]) + ' Elapsed Time: ' + str(((end1 - start1)+(end2 - start2)+(end3 - start3))/3))