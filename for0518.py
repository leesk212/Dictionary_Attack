import matplotlib.pyplot as plt
import math
import matplotlib.ticker as mticker


x_label = []

uhhu_latency = open('[Disable][Rank]HHU.txt','r')
uhhu_lines = uhhu_latency.readlines()
uhhu_data = []

uu_latency = open('[Enable][Rank]HU.txt','r')
uu_lines = uu_latency.readlines()
uu_data = []


# uhhu_latency = open('[Disable]UHHU.txt','r')
# uhhu_lines = uhhu_latency.readlines()
# uhhu_data = []
#
# uu_latency = open('[Enable]UU.txt','r')
# uu_lines = uu_latency.readlines()
# uu_data = []


for uhhu_line in uhhu_lines:
    uhhu_line = uhhu_line.strip()
    uhhu_data.append(float(uhhu_line.split(" ")[1]))
    x_label.append(uhhu_line.split(" ")[0])

for uu_line in uu_lines:
    uu_line = uu_line.strip()
    uu_data.append(float(uu_line.split(" ")[1]))

hhu_latency = open('[Disable]HHU.txt','r')
hhu_lines = hhu_latency.readlines()
hhu_data = []

hu_latency = open('[Enable]HU.txt','r')
hu_lines = hu_latency.readlines()
hu_data = []


for hhu_line in hhu_lines:
    hhu_line = hhu_line.strip()
    hhu_data.append(float(hhu_line.split(" ")[1]))

for hu_line in hu_lines:
    hu_line = hu_line.strip()
    hu_data.append(float(hu_line.split(" ")[1]))


# Read
print(x_label)
print(uhhu_data)
print(uu_data)

plt.plot(x_label,uhhu_data,label='GPUDirect Disable[H->HU]', color='dodgerblue')
plt.plot(x_label,uu_data,label='GPUDirect Enable[H->U]',color='darkorange')
#plt.plot(x_label,hhu_data,label='GPUDirect Disable[H->HU]',color='forestgreen')
#plt.plot(x_label,hu_data,label='GPUDirect Enable[H->U]',color='blueviolet')
plt.legend()
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.title("Execution Time of Cryptanalysis System\n [Fixed Data Size: 40MB]")
plt.ylabel("Time (s)")
plt.xlabel("Number of rank (worker)")
plt.xticks(rotation=90)
plt.show()


del x_label
x_label2 = []


osu_d_1 = open('[osu]Disable_type1.txt','r')
osu_d_1s = osu_d_1.readlines()
osu_d_1_data = []

osu_e_1 = open('[osu]Enable_type1.txt','r')
osu_e_1s = osu_e_1.readlines()
osu_e_1_data = []

osu_d_2 = open('[osu]Disable_type2.txt','r')
osu_d_2s = osu_d_2.readlines()
osu_d_2_data = []

osu_e_2 = open('[osu]Enable_type2.txt','r')
osu_e_2s = osu_e_2.readlines()
osu_e_2_data = []



for osu_d_1s_line in osu_d_1s:
    osu_d_1s_line = osu_d_1s_line.strip()
    osu_d_1_data.append(float(osu_d_1s_line.split(" ")[-1]))
    x_label2.append(osu_d_1s_line.split(" ")[0])

for osu_e_1s_line in osu_e_1s:
    osu_e_1s_line = osu_e_1s_line.strip()
    osu_e_1_data.append(float(osu_e_1s_line.split(" ")[-1]))

for osu_d_2s_line in osu_d_2s:
    osu_d_2s_line = osu_d_2s_line.strip()
    osu_d_2_data.append(float(osu_d_2s_line.split(" ")[-1]))

for osu_e_2s_line in osu_e_2s:
    osu_e_2s_line = osu_e_2s_line.strip()
    print(float(osu_e_2s_line.split(" ")[-1]))
    osu_e_2_data.append(float(osu_e_2s_line.split(" ")[-1]))


plt.plot(x_label2,osu_d_1_data,label='[osu]Disable_type1.txt', color='forestgreen')
plt.plot(x_label2,osu_e_1_data,label='[osu]Enable_type1.txt',color='blueviolet')
#plt.plot(x_label2,osu_d_2_data,label='[osu]Disable_type2.txt',color='forestgreen')
#plt.plot(x_label2,osu_e_2_data,label='[osu]Enable_type2.txt',color='blueviolet')
plt.legend()
plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
plt.gca().spines['top'].set_visible(False) #위 테두리 제거
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
plt.title("OSU Benchmarking\n")
plt.ylabel("Latency (us)")
plt.xlabel("Data size transmitted to each rank (MB)")
plt.xticks(rotation=90)
plt.show()


# bandwidth_read = []
# bandwidth_disable_read = []
#
# # Data bandwidth
# for i in range(23):
#     size = math.pow(2,i+1)
#
#     bandwidth_read.append( size / uhhu_data[i] )
#     bandwidth_disable_read.append( size / uu_data[i] )
#
#
# plt.plot(x_label,bandwidth_read,label='GPUDirect Disable[UH->HU]')
# plt.plot(x_label,bandwidth_disable_read,label='GPUDirect Enable[U->U]')
# plt.legend()
# plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
# plt.gca().spines['top'].set_visible(False) #위 테두리 제거
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
# plt.title("Execution Time of Cryptanalysis System\n [Number of workers: 4]")
# plt.ylabel("Bandwidth (MBps)")
# plt.xlabel("I/O Size (B)")
# plt.xticks(rotation=90)
# plt.show()
#
#
# bandwidth_write = []
# bandwidth_disable_write = []
#
# # Data bandwidth
# for i in range(23):
#     size = math.pow(2,i+1)
#
#     bandwidth_write.append( size / hhu_data[i] )
#     bandwidth_disable_write.append( size / hu_data[i] )
#
# plt.figure(figsize=(8,3))
# plt.plot(x_label,bandwidth_write,label='GPUDirect enabled',color='forestgreen')
# plt.plot(x_label,bandwidth_disable_write,label='GPUDirect disabled')
# plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
# plt.legend(fontsize=13)
# plt.gca().spines['right'].set_visible(False) #오른쪽 테두리 제거
# plt.gca().spines['top'].set_visible(False) #위 테두리 제거
# plt.title("Execution Time of Cryptanalysis System\n [Number of workers: 4]")
# plt.ylabel("Bandwidth (MBps)")
# plt.xlabel("I/O Size (B)")
# plt.xticks(rotation=90)
# plt.show()
#


