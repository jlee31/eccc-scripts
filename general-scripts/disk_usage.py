import psutil

def bytes_to_gb(bytes_value):
    return bytes_value / (1024 ** 3)

def monitor_disk_usage(threshold=80):
    print(f"Checking disk usage (warning if usage > {threshold}%)...\n")

    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            total_gb = bytes_to_gb(usage.total)
            used_gb = bytes_to_gb(usage.used)
            free_gb = bytes_to_gb(usage.free)
            percent_used = usage.percent

            print(f"Drive {partition.device} ({partition.mountpoint}):")
            print(f"  Total: {total_gb:.2f} GB")
            print(f"  Used: {used_gb:.2f} GB")
            print(f"  Free: {free_gb:.2f} GB")
            print(f"  Usage: {percent_used}%")

            if percent_used > threshold:
                print(f"  ⚠️ WARNING: Drive usage over {threshold}%!")

            print()
        except PermissionError:
            print(f"Skipping {partition.device} due to permission error.\n")

if __name__ == "__main__":
    monitor_disk_usage()

partitions2 = psutil.disk_partitions(all=False)
print(partitions2)
