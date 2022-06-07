import matplotlib.pyplot as plt
import math
import matplotlib.ticker as mticker


x_label = []

Disabling_file_read = open('GPUDirect Disabling.txt','r')
D_lines = Disabling_file_read.readlines()
D_data = []

write_latency = open('latency_write.txt','r')
write_lines = write_latency.readlines()
w_data = []

read_latency = open('latency_read.txt','r')
read_lines = read_latency.readlines()
r_data = []

for d_line in D_lines:
    d_line = d_line.strip()
    D_data.append(float(d_line.split(" ")[1]))

for w_line in write_lines:
    w_line = w_line.strip()
    w_data.append(float(w_line.split(" ")[1]))
    x_label.append(w_line.split(" ")[0])

for r_line in read_lines:
    r_line = r_line.strip()
    r_data.append(float(r_line.split(" ")[1]))

# add
Disabling_read = []
for i in range(23):
    Disabling_read.append(D_data[i] + r_data[i])

# add
Disabling_write = []
for i in range(23):
    Disabling_write.append(D_data[i] + w_data[i])

# Read
plt.plot(x_label,r_data,label='GPUDirect Enable')
plt.plot(x_label,Disabling_read,label='GPUDirect Disable')
plt.legend()
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.title("Operation: RDMA READ")
plt.ylabel("Latency (μs)")
plt.xlabel("I/O Size (B)")
plt.xticks(rotation=90)
plt.show()

bandwidth_read = []
bandwidth_disable_read = []

# Data bandwidth
for i in range(23):
    size = math.pow(2,i+1)

    bandwidth_read.append( size / r_data[i] )
    bandwidth_disable_read.append( size / Disabling_read[i] )


plt.plot(x_label,bandwidth_read,label='GPUDirect Enable')
plt.plot(x_label,bandwidth_disable_read,label='GPUDirect Disable')
plt.legend()
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.title("Operation: RDMA READ")
plt.ylabel("Bandwidth (MBps)")
plt.xlabel("I/O Size (B)")
plt.xticks(rotation=90)
plt.show()

# Write
plt.figure(figsize=(8,3))
plt.plot(x_label,w_data,label='GPUDirect enabled',color='forestgreen')
plt.plot(x_label,Disabling_write,label='GPUDirect disabled')
plt.legend(fontsize=13)
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
#plt.title("Operation: RDMA WRITE")
plt.ylabel("Latency (μs)")
plt.xlabel("I/O Size (B)")
plt.xticks(rotation=90)
plt.show()

bandwidth_write = []
bandwidth_disable_write = []

# Data bandwidth
for i in range(23):
    size = math.pow(2,i+1)

    bandwidth_write.append( size / r_data[i] )
    bandwidth_disable_write.append( size / Disabling_read[i] )

plt.figure(figsize=(8,3))
plt.plot(x_label,bandwidth_write,label='GPUDirect enabled',color='forestgreen')
plt.plot(x_label,bandwidth_disable_write,label='GPUDirect disabled')
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.legend(fontsize=13)
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
#plt.title("Operation: RDMA WRITE")
plt.ylabel("Bandwidth (MBps)")
plt.xlabel("I/O Size (B)")
plt.xticks(rotation=90)
plt.show()



