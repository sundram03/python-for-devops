import psutil

cpu = int(input("please enter cpu thresold :"))
cpu_utilization = psutil.cpu_percent(interval=1)
print(cpu_utilization)

if cpu_utilization > cpu:
    print("Alert cpu utilizatin is high")
else:
    print("cpu is normal state")


disk = int(input("please enter disk thresold :"))
disk_utilization = psutil.disk_usage('/').percent
print(disk_utilization)

if disk_utilization> cpu:
    print("Alert disk utilizatin is high")
else:
    print("disk is normal state" )

memory = int(input("please enter memory thresold :"))
memory_utilization =  psutil.virtual_memory().percent
print(memory_utilization)

if memory_utilization > cpu:
    print("Alert memory_utilizationis high")
else:
    print("memory is normal state" )