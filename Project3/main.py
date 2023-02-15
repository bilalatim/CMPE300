from argparse import ArgumentParser
import random
import sys
import time

def initiate(size, case, rang): # This method initiates inputs accordingly
    ret = []

    for i in range(size):
        c = int(rang*size)
        if(c < 1):
            c = 1
        ret.append(random.randint(1, c))

    if case == 'worst':
        ret.sort()

    return ret

def quickSort(arr, low, high, version): # This methods applies quickSort algorithm with specified version to the given interval of the given array
    if low < high:
        if(version == 'classical' or version == 'randomized_permutation'):
            pivot = low
        elif(version == 'randomized_pivot'):
            pivot = random.randint(low, high)
        elif(version == 'median'):
            pivot = int((low + high)/2)
            if low == high - 1:
                medList = [arr[low], arr[high]]
                medList.sort()
                arr[low], arr[high] = medList[0], medList[1]
            else:
                medList = [arr[low], arr[pivot], arr[high]]
                medList.sort()
                arr[low], arr[pivot], arr[high] = medList[0], medList[1], medList[2]
        
        arr[high], arr[pivot] = arr[pivot], arr[high]

        q = reArrange(arr, low, high)
        quickSort(arr, low, q - 1, version)
        quickSort(arr, q + 1, high, version)

def reArrange(arr, low, high): # This method is called in quickSort and swaps the data to sort in given interval of the given array. This is where the actual job of the quickSort is done actually.
    x = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return (i + 1)

parser = ArgumentParser()
parser.add_argument('-v', '--version', type=str, choices=['classical', 'randomized_pivot', 'randomized_permutation', 'median', 'all'], default='all') # Argument for the version of the quickSort algorithm
parser.add_argument('-n', '--size', type=int, default= -1) # Argument for the data size
parser.add_argument('-r', '--range', type=float, default= -1) # Argument for the data range rate
parser.add_argument('-c', '--case', type=str, choices=['average', 'worst', 'both'], default='both') # Argument for the input case
parser.add_argument('-p', '--print', type=bool, choices=[True, False], default=False) # Argument for printing the input
args = parser.parse_args()

sys.setrecursionlimit(999999999) # Setting recursion limit to a huge number to make sure this doesn't block the program

version, size, rang, case, print_input_bool = args.version, args.size, args.range, args.case, args.print # Taking arguments to variables

# Arranging the arguments accordingly
sizes = [100, 1000, 10000] if size == -1 else [size]
rangs = [10, 0.75, 0.25, -1] if rang == -1 else [rang]
cases = ['average', 'worst'] if case == 'both' else [case]
versions = ['classical', 'randomized_pivot', 'randomized_permutation', 'median'] if version == 'all' else [version]

# The main part of the program
for n in sizes: # Iterate over data sizes wanted
    print("Data size {}:".format(n))
    for r in rangs: # Iterate over the input range rates wanted
        inputType = ""
        if r == 10:
            inputType = "InpType1"
        elif r == 0.75:
            inputType = "InpType2"
        elif r == 0.25:
            inputType = "InpType3"
        elif r == -1:
            inputType = "InpType4"
        else:
            inputType = "Custom"

        print("\tInput type {} with range {}:".format(inputType, "[1, " + str(max(1, int(n*r))) + "]"))
        averageDatas = []
        worstData = []
        for c in cases: # Iterate over input cases wanted, to create and arrange inputs
            if c == 'average':
                for i in range(5):
                    averageDatas.append(initiate(n, c, r))
            else:
                worstData = initiate(n, c, r)
        
        if print_input_bool: # Print the inputs if they are wanted
            for d in averageDatas:
                print("\t\tInput{} (average): {}".format(averageDatas.index(d) + 1, d))
            
            if len(worstData) != 0:
                print("\t\tInput (worst): {}".format(worstData))
            print()
        
        for v in versions: # Iterate over wanted versions of the quickSort algorithm
            print("\t\tAlgorithm {} as version of {}:".format(v, "Ver" + str(versions.index(v) + 1)))

            for c in cases: # Iterate over the wanted input cases, to execute the algorithm
                caseNum = 0
                datas = []
                if c == 'average':
                    caseNum = 1
                    datas = averageDatas
                elif c == 'worst':
                    caseNum = 2
                    datas = [worstData]
                results = []
                input_index=1
                for dat in datas: # Iterate over the generated data and take the durations
                    d = dat.copy()
                    if v == 'randomized_permutation':
                        random.shuffle(d)
                    startTime = time.perf_counter_ns()
                    quickSort(d, 0, len(d) - 1, v)
                    endTime = time.perf_counter_ns()
                    results.append(endTime - startTime)
                    input_index += 1
                average = time.time_ns()
                average = average - average
                for i in results:
                    average += i
                
                average /= len(results)

                print("\t\t\tDuration for Case{} ({} case): {}".format(caseNum, c, average))
            print()
        
        print()
    
    print()


            
        