# 080 - Bài 80: Trung bình nhân các giá trị dương

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tính **trung bình nhân** của tất cả các giá trị dương ($a_i > 0$) có trong mảng, được định nghĩa là $\left(\prod_{a_i > 0} a_i\right)^{1/k}$ với $k$ là số lượng phần tử dương. Nếu $k = 0$, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra trung bình nhân các số dương (sai số $\le 10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
4
-5.0 2.0 8.0 0.0
```

Kết quả:

```text
4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-1.0 0.0 -2.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1.0 3.0 9.0
```

Kết quả:

```text
3.000000
```

# Giải thích

- **Ví dụ 1:** Các số dương là $2.0$ và $8.0$; trung bình nhân $= \sqrt{2.0 \times 8.0} = 4.0$.
- **Ví dụ 2:** Không có phần tử dương nào ($k = 0$) nên kết quả bằng $0$.
- **Ví dụ 3:** $\sqrt[3]{1 \times 3 \times 9} = \sqrt[3]{27} = 3.0$.
