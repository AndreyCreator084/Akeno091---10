from multiprocessing import Pool
import time



def read_info(name):
    all_data = []
    with open(name, 'r') as file_:
        line = file_.readline()
        while line:
            all_data.append(line)
            line = file_.readline()

filenames = [f'./file {number}.txt' for number in range(1, 5)]

start_time = time.time()
for file in filenames:
    read_info(file)
end_time = time.time()
print(f'{end_time - start_time} (линейный)')

if __name__ == "__main__":
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'{end_time - start_time} (многопроцессный)')