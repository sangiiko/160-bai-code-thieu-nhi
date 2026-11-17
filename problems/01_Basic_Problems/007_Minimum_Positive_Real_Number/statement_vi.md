# 007 - Bài 7: Giá trị dương nhỏ nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **dương** ($a_i > 0$) nhỏ nhất trong mảng. Nếu mảng không có giá trị dương nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị dương nhỏ nhất tìm được (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không có phần tử dương.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-5.0 3.2 0.0 1.25 4.8
```

Kết quả:

```text
1.250000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1.0 0.0 -3.5 -0.2
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
10.5 0.005 0.05
```

Kết quả:

```text
0.005000
```

# Giải thích

- **Ví dụ 1:** Các phần tử dương là $3.2, 1.25, 4.8$; nhỏ nhất là $1.25$.
- **Ví dụ 2:** Không có phần tử nào lớn hơn $0$ nên kết quả là `-1`.
- **Ví dụ 3:** Phần tử dương nhỏ nhất là $0.005$.
