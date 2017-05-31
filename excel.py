import pandas as pd
data1 = pd.read_excel('测试匹配苗木.xls')
data2 = pd.read_excel('全国苗木表.xls')
data3 = pd.DataFrame(data2[data2.中文名称 == "香樟"].head(1))
n = 1
for i,j in data1.items():
    for m in j:
        if data2[data2.中文名称 == m].head(1).empty:
            data3.set_value(n, "中文名称", m)
            n -= 1
        else:
            data3 = data3.append(data2[data2.中文名称 == m].head(1))
writer = pd.ExcelWriter('匹配完成.xlsx', engine='xlsxwriter')
data3.to_excel(writer, 'Sheet1')
writer.save()