# 040 - Bài 40: Chữ số xuất hiện ít nhất trong mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Xét tất cả các chữ số thập phân (`0` đến `9`) có xuất hiện ít nhất $1$ lần trong biểu diễn thập phân của các phần tử $|a_i|$. Hãy tìm chữ số xuất hiện **ít lần nhất**. Nếu có nhiều chữ số có cùng số lần xuất hiện ít nhất, hãy chọn chữ số **nhỏ nhất**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một chữ số (`0`–`9`) xuất hiện ít nhất trong mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
12 23 11 42
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
3
105 -50 15
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
2
0 0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Số lần xuất hiện: `1` (3 lần), `2` (3 lần), `3` (1 lần), `4` (1 lần). `3` và `4` cùng ít nhất; chọn chữ số nhỏ hơn là `3`.
- **Ví dụ 2:** Số lần xuất hiện: `0` (2 lần), `1` (2 lần), `5` (3 lần). `0` và `1` cùng ít nhất; chọn `0`.
- **Ví dụ 3:** Chỉ có chữ số `0` xuất hiện trong mảng.
