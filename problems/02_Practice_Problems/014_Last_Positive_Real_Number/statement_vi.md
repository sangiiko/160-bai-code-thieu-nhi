# 014 - Bài 14: Số dương cuối cùng trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **dương** ($a_i > 0$) xuất hiện **cuối cùng** trong mảng. Nếu mảng không có giá trị dương nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị dương cuối cùng (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1.5 -2.0 8.25 0.0 -4.1
```

Kết quả:

```text
8.250000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-5.0 0.0 -1.2
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0.5 0.0 3.0 0.25
```

Kết quả:

```text
0.250000
```

# Giải thích

- **Ví dụ 1:** Các giá trị dương là $1.5$ và $8.25$; giá trị cuối cùng là $8.25$.
- **Ví dụ 2:** Không có giá trị dương nào nên kết quả là `-1`.
- **Ví dụ 3:** Giá trị dương cuối cùng là $0.25$.
