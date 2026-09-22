import csv
import numpy as np
import matplotlib.pyplot as plt
# 设置中文显示
plt.rcParams["font.family"] = ["SimHei", "WenQuanYi Micro Hei", "Heiti TC"]
plt.rcParams["axes.unicode_minus"] = False
def generate_raw_csv(save_path="score_raw.csv"):
    n = 120
    student_id = np.arange(1, n + 1)
    chinese = np.random.randint(40, 100, size=n).astype(float)
    math = np.random.randint(30, 100, size=n).astype(float)
    english = np.random.randint(45, 100, size=n).astype(float)
    chinese[np.random.choice(n, size=5, replace=False)] = np.nan
    math[np.random.choice(n, size=4, replace=False)] = np.nan
    math[10] = -5
    english[20] = 105
    with open(save_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["学号", "语文", "数学", "英语"])
        for i in range(n):
            writer.writerow([student_id[i], chinese[i], math[i], english[i]])
    print(f"原始数据生成完成：{save_path}")
    return save_path
def read_csv_file(file_path):
    data_list = []
    with open(file_path, "r", encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            row_numeric = []
            for val in row:
                if val == "":
                    row_numeric.append(np.nan)
                else:
                    row_numeric.append(float(val))
            data_list.append(row_numeric)
    data_arr = np.array(data_list)
    print("\n====原始数据预览（前5行）====")
    print(data_arr[:5])
    return header, data_arr
def clean_data(header, data_arr):
    data_clean = data_arr.copy()
    # 列索引：1语文，2数学，3英语
    for col_idx in [1, 2, 3]:
        col = data_clean[:, col_idx]
        mean_val = np.nanmean(col)
        # 填充缺失值
        nan_mask = np.isnan(col)
        data_clean[nan_mask, col_idx] = mean_val
        # 处理异常值 <0 或者 >100
        err_mask = (data_clean[:, col_idx] < 0) | (data_clean[:, col_idx] > 100)
        data_clean[err_mask, col_idx] = mean_val
    print("\n====清洗后数据预览（前5行）====")
    print(data_clean[:5])
    return data_clean
def calc_statistics(data_arr):
    subjects = ["语文", "数学", "英语"]
    col_index = [1, 2, 3]
    print("\n====各科统计信息====")
    for name, idx in zip(subjects, col_index):
        col_data = data_arr[:, idx]
        mean_v = np.mean(col_data)
        max_v = np.max(col_data)
        min_v = np.min(col_data)
        std_v = np.std(col_data, ddof=1)
        print(f"{name}: 平均值={mean_v:.2f}, 最大值={max_v:.2f}, 最小值={min_v:.2f}, 标准差={std_v:.2f}")


def draw_chart1(data_arr):
    plt.figure(figsize=(10,5))
    math = data_arr[:, 2]
    stdudnt_id=data_arr[:,0]
    plt.plot(stdudnt_id, math)
    plt.title('学生数学成绩',color='green')
    plt.xlabel('student_id',fontsize=20)
    plt.ylabel('math',fontsize=20)
    plt.show()
def draw_chart2(data_arr):
    plt.figure(figsize=(10,5))
    math = data_arr[:, 2]
    stdudnt_id=data_arr[:,0]
    plt.scatter(stdudnt_id, math)
    plt.title('学生数学成绩',color='green')
    plt.xlabel('student_id',fontsize=20)
    plt.ylabel('math',fontsize=20)
    plt.show()

def save_clean_csv(header, data_arr, out_path="score_clean.csv"):
    with open(out_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data_arr.tolist())
    print(f"\n清洗后数据保存成功：{out_path}")


def main():
    raw_file = generate_raw_csv()
    header, raw_data = read_csv_file(raw_file)
    clean_data_arr = clean_data(header, raw_data)
    calc_statistics(clean_data_arr)
    draw_chart1(clean_data_arr)
    draw_chart2(clean_data_arr)
    save_clean_csv(header, clean_data_arr)

if __name__ == "__main__":
    main()