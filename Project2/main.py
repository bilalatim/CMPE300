from mpi4py import MPI
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
world_size = comm.Get_size()
worker_size = world_size - 1

test_uni=dict()
test_bi=dict()
test = open(sys.argv[6], "r")
test_lines = test.readlines()

for test_line in test_lines:
    test_words = test_line.strip().split()
    test_uni[test_words[0]] = 0 
    test_bi[test_words[0]+" "+test_words[1]] = 0

if rank == 0: # master process
    file = open(sys.argv[2], "r")
    lines = file.readlines()
    size = len(lines)
    line_per_rank = size / worker_size

    worker_first=0
    for i in range(1,world_size): # split and send data equally to the workers
        worker_last = round(i * line_per_rank)
        comm.send(lines[worker_first:worker_last], dest=i, tag=11)
        worker_first=worker_last
    
    if (sys.argv[4]=="MASTER"): # if the merge-method is MASTER, receive from all
        for j in range(1,world_size):
            data_come = comm.recv(source=j, tag=10)
            for i in data_come[0].keys():
                test_uni[i]+= data_come[0][i]
            for i in data_come[1].keys():
                test_bi[i]+= data_come[1][i]

    elif (sys.argv[4]=="WORKERS"): # if the merge-method is WORKERS, receive from with the highest rank
        data_come = comm.recv(source=worker_size, tag=10)
        test_uni = data_come[0]
        test_bi = data_come[1]
    print()
    print("bigrams : conditional probabilities")
    print("-----------------------------------")
    for i in test_bi.keys():
        print("{}:   {}".format(i, test_bi[i] / test_uni[i.split()[0]]))

else: # workers
    data = comm.recv(source=0, tag=11)
    print("Rank: {}, Number of sentences: {}".format(rank, len(data)))

    for k in data: # counting
        sentence = k.strip().split()
        for i in range(len(sentence)-1):
            word = sentence[i]
            double_word = word +" "+ sentence[i+1]
            if word in test_uni.keys():
                test_uni[word]+=1
                if double_word in test_bi.keys():
                    test_bi[double_word]+=1

    if (sys.argv[4]=="WORKERS"): # if the merge-method is WORKERS, receive from the previous worker and sum
        if (rank!=1):
            data_come = comm.recv(source=rank-1, tag=10)
            for i in data_come[0].keys():
                test_uni[i]+= data_come[0][i]
            for i in data_come[1].keys():
                test_bi[i]+= data_come[1][i]

    result=[test_uni,test_bi] # data to send

    if(sys.argv[4]=="WORKERS"): # if the merge-method is WORKERS, send the data to the next worker
        if (rank==worker_size): # if the highest ranked worker, send to the master process
            comm.send(result, dest=0, tag=10)
        else:
            comm.send(result, dest=rank+1, tag=10)
    else: # if the merge-method is MASTER, send to the master process
        comm.send(result, dest=0, tag=10)
