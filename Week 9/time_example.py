import time

def main():
    while True:
        epoch = time.time()
        print(f"Seconds since Epoch: {epoch}")

        print(f"Date: {time.ctime(epoch)}\n")

        time.sleep(1.5)

if __name__ == "__main__":
    main()