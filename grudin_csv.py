with open("client_import.csv", 'r', encoding='utf-8') as file:
    lines=file.readlines()
    for i in range(1,len(lines)):
        arrr=lines[i].strip()
        data_arrr=(arrr.strip(";"))
        surname = data_arrr[0].strip()
        fio = surname.split()
        if len(fio) > 1:
            data_arrr[0] = fio[0]
            data_arrr[1] = fio[1]
            data_arrr[2] = fio[2]
        surname = data_arrr[0].strip()
        name = data_arrr[1].strip()
        otchestvo = data_arrr[2].strip()
        gender = data_arrr[3].strip().lower()
        if gender == 'м':
            gender = 1
        else:
            gender = 2
        phone = data_arrr[4].strip().replace("(", "").replace(")", "").replace("-", "")
        file_name = data_arrr[5].strip().split("\\")[1]
        brth = data_arrr[6].strip()
        email = data_arrr[7].strip()
        date = data_arrr[8].strip()
        print(data_arrr)
with open("clientservice_s_import.csv", 'r', encoding='utf-8') as file:
    arr=file.readlines()
    for i in range(1,len(arr)):
        result=[]
        num=i+1
        time_date=arr[i]
        data=time_date.split(";")
        tock_zap=data[1].split()
        text=data[2]
        result.append(num)
        result.append(tock_zap[0])
        result.append(tock_zap[1])
        result.append(text)
        print(result)
