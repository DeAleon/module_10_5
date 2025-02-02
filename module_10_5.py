import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        for line in file:
            all_data.append(line.rstrip())


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end = datetime.datetime.now()
# print(end - start)
# 0:00:05.272113

if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)
    #0:00:02.133557