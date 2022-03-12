import matplotlib.pyplot as plt

files = ["for_plot_SM2SI_write_gpu_x.txt",
         "for_plot_SM2SI_write_gpu_o.txt",
         "for_plot_SI2SM_read_gpu_x.txt",
         "for_plot_SI2SM_read_gpu_o.txt"
         ]

for file in files:
    open_file = open(file)
    lines = open_file.readlines()
    labels = []
    labels_r = []
    x_data=[]
    label1_data=[]
    label2_data=[]
    label3_data=[]

    for _, line in enumerate(lines):
        line = line.strip()
        if _ == 0:
            plt.title(line+'\nAmphere 40 (GA 40), ConnectX-5 EDR')
        elif _ == 1: # labels (xlabel -> byte, iterations-> same,
            tmps = line.split(" ")
            for tmp in tmps:
                if len(tmp)!=0:
                    labels.append(tmp)
            #plt.xlabel(labels[0])
            del labels[0:2]
            label1 = labels[0] +" "+labels[1]
            label2 = labels[2] +" "+labels[3]
            label3 = labels[4]
            labels_r = [label1,label2,label3]
        else: # datas
            if line[0] != 'C': #only numeric
                data_r = []
                datas = line.split(" ")
                for data in datas:
                    if len(data)!=0:
                        data_r.append(data)
                #print(data_r[2])


                x_data.append(data_r[0])
                label1_data.append(float(data_r[2]))
                label2_data.append(float(data_r[3]))
                label3_data.append(float(data_r[4]))

    print(x_data)
    print(label1_data)
    print(label2_data)
    print(label3_data)

    plt.plot(x_data,label1_data,label=labels_r[0])
    plt.plot(x_data,label2_data,label=labels_r[1])
#    plt.plot(x_data,label3_data,label=labels_r[2])
    plt.xticks(rotation=90)
    plt.ylabel("Bandwidth (MB/s)")
    plt.legend()
    plt.show()
