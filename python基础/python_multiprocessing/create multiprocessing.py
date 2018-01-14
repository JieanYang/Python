import multiprocessing as mp
import threading as td


# t1 = td.Thread(target=job,args=(1,2))
# t1.start()
# t1.join()

def job(a,d):
    print('aaaaa')

if __name__=='__main__':
	# multiprocessing
	# add
    p1 = mp.Process(target=job,args=(1,2))
    p1.start()
    # join
    p1.join()