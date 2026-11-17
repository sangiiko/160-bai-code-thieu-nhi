# 017 - Bài 17: Giá trị âm lớn nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **âm lớn nhất** (tức là số âm $a_i < 0$ gần $0$ nhất) trong mảng. Nếu mảng không có giá trị âm nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị âm lớn nhất (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không có số âm.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-10.5 -2.3 0.0 4.1 -5.0
```

Kết quả:

```text
-2.300000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0.0 1.2 3.4 5.6
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-0.01 -100.0 -1.0
```

Kết quả:

```text
-0.010000
```

# Giải thích

- **Ví dụ 1:** Các giá trị âm là $-10.5, -2.3, -5.0$; lớn nhất trong số đó là $-2.3$.
- **Ví dụ 2:** Mảng không có số âm nên in `-1`.
- **Ví dụ 3:** Số âm lớn nhất là $-0.01$.
