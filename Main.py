import os
import csv
import pandas as pd
import codecs
class main():
    def __init__(self):
        self.struct1NameEndlist=[]
        self.struct2NameEndlist=[]
        self.struct3NameEndlist=[]
        datarow = open("struct1FileEndWithList.txt", encoding='UTF-8')  # 读取的整个原始文件数据
        datarowlines = datarow.readlines()  # 读取的整个原始文件的数据，按行分割
        for line in datarowlines:
            if (line != ""):
                self.struct1NameEndlist.append(line.strip())

        datarow = open("struct2FileEndWithList.txt", encoding='UTF-8')  # 读取的整个原始文件数据
        datarowlines = datarow.readlines()  # 读取的整个原始文件的数据，按行分割
        for line in datarowlines:
            if (line != ""):
                self.struct2NameEndlist.append(line.strip())

        datarow = open("struct3FileEndWithList.txt", encoding='UTF-8')  # 读取的整个原始文件数据
        datarowlines = datarow.readlines()  # 读取的整个原始文件的数据，按行分割
        for line in datarowlines:
            if (line != ""):
                self.struct3NameEndlist.append(line.strip())
            
                
    def loaddata(self,datatype:int,allfilepath:str):
        rowdata = []
        # with open(filepath + "/" + f, 'r',encoding = "gbk") as csvfile:
        #     reader = csv.reader(csvfile)
        # with open(allfilepath, 'rb') as csvfile:
        #     reader = csv.reader((line.replace('\0'.encode(), ''.encode()).decode("gbk") for line in csvfile),delimiter=",")
        # print(allfilepath)
        with open(allfilepath, 'r') as file:
            reader = csv.reader(file)
            rows = [row for row in reader]

        # with open(allfilepath, 'rb') as csvfile:
        #     reader = csv.reader((line.replace('\0'.encode(), ''.encode()).decode("gb18030") for line in csvfile),delimiter=",")
        #     rows = [row for row in reader]
        # print(reader.line_num)
        # if reader.line_num==0:
        #     errorfilelist.append(f)
        #     # continue
        if datatype==1:
            rowdata.append(rows[0][0].split(";")[1])

            rowdata.append(rows[122][0].split(";")[1])
            rowdata.append(rows[122][0].split(";")[2])
            rowdata.append(rows[123][0].split(";")[1])
            rowdata.append(rows[123][0].split(";")[2])
            rowdata.append(rows[124][0].split(";")[1])
            rowdata.append(rows[124][0].split(";")[2])
            rowdata.append(rows[125][0].split(";")[1])
            rowdata.append(rows[125][0].split(";")[2])
            rowdata.append(rows[126][0].split(";")[1])
            rowdata.append(rows[126][0].split(";")[2])

            # 要提取12个数据列索引
            multindex1 = list()
            multindex1.extend(range(129, 135))
            multindex1.extend(range(137, 143))
            multindex1.extend(range(145, 151))
            multindex1.extend([153, 154])
            multindex1.extend(range(157, 163))
            multindex1.extend(range(165, 169))
            multindex1.extend([171, 172])
            for ii in multindex1:
                for iii in range(1, 12):
                    rowdata.append(rows[ii][0].split(";")[iii])
        elif datatype==2:
            rowdata.append(rows[0][0].split(";")[1])

            rowdata.append(rows[121][0].split(";")[1])
            rowdata.append(rows[122][0].split(";")[1])

            rowdata.append(rows[125][0].split(";")[1])
            rowdata.append(rows[125][0].split(";")[2])
            rowdata.append(rows[126][0].split(";")[1])
            rowdata.append(rows[126][0].split(";")[2])
            rowdata.append(rows[127][0].split(";")[1])
            rowdata.append(rows[127][0].split(";")[2])
            rowdata.append(rows[128][0].split(";")[1])
            rowdata.append(rows[128][0].split(";")[2])
            rowdata.append(rows[129][0].split(";")[1])
            rowdata.append(rows[129][0].split(";")[2])
            rowdata.append(rows[130][0].split(";")[1])
            rowdata.append(rows[130][0].split(";")[2])
            rowdata.append(rows[131][0].split(";")[1])
            rowdata.append(rows[131][0].split(";")[2])
            rowdata.append(rows[132][0].split(";")[1])
            rowdata.append(rows[132][0].split(";")[2])
            rowdata.append(rows[133][0].split(";")[1])
            rowdata.append(rows[133][0].split(";")[2])
            rowdata.append(rows[134][0].split(";")[1])
            rowdata.append(rows[134][0].split(";")[2])
        elif datatype==3:
            rowdata.append(rows[0][0].split(";")[1])
            for i in range(122, 146):
                if (len(rows[i][0].split(";")) > 1):
                    rowdata.append(rows[i][0].split(";")[1])
                else:
                    rowdata.append(" ")
        return rowdata

    def loadFile(self,filepath):
        #获取所有文件名
        filenames = []
        files = os.listdir(filepath)
        # 排除隐藏文件和文件夹
        for f in files:
            if (os.path.isfile(filepath + '/' + f)):
                # 添加文件
                if (os.path.splitext(f)[1] == ".csv"):
                    filenames.append(f)

        struct1data=[[] for i in range(len(self.struct1NameEndlist))]
        struct2data=[[] for i in range(len(self.struct2NameEndlist))]
        struct3data=[[] for i in range(len(self.struct3NameEndlist))]
        struct1title=[
                      "名称",
                      "足印长度mm(左)","足印长度mm(右)",
                      "压力中心连线增量mm(左)","压力中心连线增量mm(右)",
                      "整个压力中心连线占脚印长度比例(左)","整个压力中心连线占脚印长度比例(右)",
                      "开始时压力中心指标(左)","开始时压力中心指标(右)",
                      "结束时压力中心指标(左)","结束时压力中心指标(右)",
                      "面积cm2;T1(左最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "面积cm2;T1(右最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "面积cm2;T1(左最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "面积cm2;T1(右最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "面积cm2;T1(左平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "面积cm2;T1(右平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(左最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(右最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(左最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(右最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(左平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "最大压强gr/cm2;T1(右平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(左最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(右最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(左最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(右最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(左平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "平均压强g/cm2;T1(右平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "负荷分布%;T1(左)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "负荷分布%;T1(右)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(左最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(右最大值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(左最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(右最小值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(左平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "力的最大值(N);T1(右平均值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "时间 ms;T1(左数值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "时间 ms;T1(右数值)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "时间 ms;T1(左%)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "时间 ms;T1(右%)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "压力-时间积分(N*s);T1(左)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L",
                      "压力-时间积分(N*s);T1(右)","T 2-3-4-5","MH1","MH2","MH3","MH4","MH5","MF_M","MF_L","RF_M","RF_L"
                      ]
        struct2title=["名称","压力中心错位","左-右压力中心错位","足翻角°(左)","足翻角°(右)","足部轴角°(左)","足部轴角°(右)","前足面积cm2(左)","前足面积cm2(右)","前脚负荷%(左)","前脚负荷%(右)","后脚/前脚比率%(左)","后脚/前脚比率%(右)",
                      "后足面积cm2(左)","后足面积cm2(右)","后脚负荷%(左)","后脚负荷%(右)","后脚/前脚比率%(左)","后脚/前脚比率%(右)","整足面积cm2(左)","整足面积cm2(右)","负荷%(左)","负荷%(右)"]
        struct3title=["名称","球长度","椭圆面积mm2","椭圆倾斜角度°","椭圆离心率","L/S比例","Delta X mm","DeltaYmm","长轴mm","短轴mm","最大摆动mm","最小摆动mm","平均值","平均速度mm/s","均方根mm",
                      "均方根Xmm","均方根Ymm","标准偏差Xmm","标准偏差Ymm","椭圆中心","平均Xmm","平均Ymm","多边形几何中心","平均Xmm","平均Ymm"]


        for f in filenames:
            if f.endswith(tuple(self.struct1NameEndlist)):
                for i in range(len(self.struct1NameEndlist)):

                    if f.endswith(self.struct1NameEndlist[i]):
                        print(f,self.struct1NameEndlist[i])
                        struct1data[i].append(self.loaddata(1,filepath + "/" + f))
            if f.endswith(tuple(self.struct2NameEndlist)):
                for i in range(len(self.struct2NameEndlist)):
                    if f.endswith(self.struct2NameEndlist[i]):
                        print(f, self.struct2NameEndlist[i])
                        struct2data[i].append(self.loaddata(2,filepath + "/" + f))
            if f.endswith(tuple(self.struct3NameEndlist)):
                for i in range(len(self.struct3NameEndlist)):
                    if f.endswith(self.struct3NameEndlist[i]):
                        print(f, self.struct3NameEndlist[i])
                        struct3data[i].append(self.loaddata(3,filepath + "/" + f))



        if not os.path.exists(filepath+"/数据整合结果"):
            os.makedirs(filepath+"/数据整合结果")
        fileexist=False
        for elem in self.struct2NameEndlist:
            if os.path.exists(filepath + "/数据整合结果/"+elem):
                fileexist=True
                break
        flag = "w"
        if fileexist:
            flag = input("整理结果已存在，是否覆盖？追加请输入a，覆盖请输入w：")
            while (flag != "a" and flag != "w"):
                flag = input("输入错误，请重新输入！\n整理结果已存在，是否覆盖？追加请输入a，覆盖请输入w：")

        print("文件总数：" + str(len(filenames)))

        for i in range(len(struct1data)):
            if len(struct1data[i]) != 0:
                data = pd.DataFrame(struct1data[i])
                data.columns = struct1title
                data.to_csv(filepath + "/数据整合结果/"+self.struct1NameEndlist[i], index=0, mode=flag)
                print("<"+self.struct1NameEndlist[i][0:-5]+"> \t数据量：" + str(len(struct1data[i])) + " 提取特征数：" + str(len(struct1title)))

        for i in range(len(struct2data)):
            if len(struct2data[i]) != 0:
                data = pd.DataFrame(struct2data[i])
                data.columns = struct2title
                data.to_csv(filepath + "/数据整合结果/"+self.struct2NameEndlist[i], index=0, mode=flag)
                print("<" + self.struct2NameEndlist[i][0:-5] + "> \t数据量：" + str(len(struct2data[i])) + " 提取特征数：" + str(len(struct2title)))

        for i in range(len(struct3data)):
            if len(struct3data[i]) != 0:
                data = pd.DataFrame(struct3data[i])
                data.columns = struct3title
                data.to_csv(filepath + "/数据整合结果/"+self.struct3NameEndlist[i], index=0, mode=flag)
                print("<" + self.struct3NameEndlist[i][0:-5] + "> \t数据量：" + str(len(struct3data[i])) + " 提取特征数：" + str(len(struct3title)))


if __name__ == '__main__':
    print("请输入文件夹路径\n")
    path = input()
    # loadFile('D:/工作文件2/董晶晶数据/')
    a = main()
    a.loadFile(path)
    print("完成，任意键退出！")
    path = input()
