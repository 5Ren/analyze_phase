import numpy as np
import matplotlib.pyplot as plt

# CSVファイルのパス
csv_file_path = './vibration_samples/1-9_n1_analysed_height.csv'

# CSVファイルの読み込み
data = np.genfromtxt(csv_file_path, delimiter=',')

# 指定範囲の行を設定（例: 3行目から10行目まで）
start_row = 18
end_row = 48

# 指定範囲のデータを取得
specified_range_data = data[start_row:end_row + 1, 1]

# 負の値を持つ要素を見つけ、それより前の要素を削除
neg_index = np.where(specified_range_data < 0)[0]
if len(neg_index) > 0:
    specified_range_data = specified_range_data[neg_index[-1] + 1:]

specified_range_data -= specified_range_data.mean()

# 時系列データの振幅を取得
amplitude_data = specified_range_data

# サンプリング間隔とデータ数の設定
dt = 1/2000
N = len(amplitude_data)

# フーリエ変換を実行
y_fft = np.fft.fft(amplitude_data)
freq = np.fft.fftfreq(N, dt)
amp = np.abs(y_fft / N)

# グラフのプロット
plt.figure(figsize=(10, 5))

# もとのデータのプロット
plt.subplot(1, 2, 1)
plt.plot(specified_range_data)
plt.title('Original Data')
plt.xlabel('Index')
plt.ylabel('Value')

# 周波数スペクトルのプロット
plt.subplot(1, 2, 2)
plt.plot(freq[:N//2], amp[:N//2])
plt.title('FFT Results')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Amplitude')
# plt.ylim(0, 0.5)

# グラフ表示
plt.tight_layout()
plt.show()
