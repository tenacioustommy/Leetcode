import os
import pandas as pd

data_dir = './data/'
factor_dir = './factor/'

for file_name in os.listdir(data_dir):
    file_path = os.path.join(data_dir, file_name)
    # 读取数据
    data = pd.read_csv(file_path)
    # 提取股票代码与原始数据
    stock_codes = data.iloc[:, 0]  
    raw_data = data.iloc[:, 1:]     
    # 计算因子值
    factor_values = raw_data.rank(axis=0, method='min')  
    factor_data = pd.concat([stock_codes, factor_values], axis=1)
    # 保存因子值文件
    output_path = os.path.join(factor_dir, file_name)
    factor_data.to_csv(output_path, index=False)
