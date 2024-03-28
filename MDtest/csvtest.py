import pandas as pd

# 创建DataFrame
data = {
    'Table1': {
        'Brand': ['Toyota', 'Honda'],
        'Model': ['Camry', 'Accord'],
        'Price': ['$24,425', '$24,270'],
        'Horsepower': [203, 192],
        'Displacement': ['2.5L', '1.5L']
    },
    'Table2': {
        'Brand': ['Toyota', 'Honda'],
        'Model': ['Camry', 'Accord'],
        'Safety Features': ['Lane Departure Alert, Pre-Collision System', 'Honda Sensing, Collision Mitigation Braking System'],
        'Body Colors': ['Silver, Black, White, Gray', 'White Pearl, Black, Silver, Deep Blue'],
        'Audio System': ['JBL Audio System', '450-Watt Premium Audio System']
    }
}

df_table1 = pd.DataFrame(data['Table1'])
df_table2 = pd.DataFrame(data['Table2'])

# 添加图注
df_table1.columns = pd.MultiIndex.from_tuples([('车辆信息', '品牌'), ('车辆信息', '车型'), ('车辆价格', '价格'), ('车辆参数', '马力'), ('车辆参数', '排量')])
df_table2.columns = pd.MultiIndex.from_tuples([('配置信息', '品牌'), ('配置信息', '车型'), ('安全配置', '安全装备'), ('车身颜色', '可选颜色'), ('音响系统', '音响配置')])

# 展示数据
print("Table 1:")
print(df_table1)
print("\nTable 2:")
print(df_table2)