from psutil import net_io_counters


print('hello world')
#s = psutil.cpu_count()


def rcv_data():
    return net_io_counters()

def main():
    net_data = rcv_data()
    print(net_data)



if __name__ == "__main__":
    main()

