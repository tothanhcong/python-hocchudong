docfile_log = open("/var/log/auth.log").readlines()
ghidulieu = open("/root/fail_ssh.txt", 'a')
docfile_dl_f_ssh = open("/root/fail_ssh.txt").readlines()

f_ssh_line = []
list_so_sanh = []

dl_f_ssh_date_list = []

tukhoa1 = ": Failed password"

for i in range(0,len(docfile_log)):
    if tukhoa1 in docfile_log[i]:
        f_ssh_line.append(docfile_log[i])

for i in range(0,len(docfile_dl_f_ssh)):
    k = docfile_dl_f_ssh[i].split(" ")
    sosanh1 = k[0]+" "+k[2]+" "+k[3]
    list_so_sanh.append(sosanh1)
#    print sosanh1
#    dl_f_ssh_date_list.append(docfile_dl_f_ssh[i].split(" ")[0])


#ghidulieu.truncate()
for i in f_ssh_line:
    a= True
    ngaythang = i.split(" ")
    sosanh2 = ngaythang[0]+" "+ngaythang[2]+" "+ngaythang[3]
#    print sosanh2

    for j in range(0,len(list_so_sanh)):
        if sosanh2 == list_so_sanh[j]:
            a= False
            break;
    if a:
        ghidulieu.write(i)


#    ghidulieu.write(i)
ghidulieu.close()