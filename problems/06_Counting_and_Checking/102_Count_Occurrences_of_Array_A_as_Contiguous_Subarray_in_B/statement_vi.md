# 102 - Bài 102: Đếm số lần mảng a xuất hiện trong mảng b

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số nguyên $a$ (gồm $n$ phần tử) và $b$ (gồm $m$ phần tử). Hãy đếm số lần mảng $a$ xuất hiện như một **mảng con liên tiếp** trong mảng $b$, tức là số chỉ số $i$ ($0 \le i \le m - n$) sao cho $b_i = a_0, b_{i+1} = a_1, \dots, b_{i+n-1} = a_{n-1}$ (các lần xuất hiện có thể chồng lấn nhau).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên dương $n$ và $m$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, \dots, a_{n-1}$.
- Dòng thứ ba chứa $m$ số nguyên $b_0, \dots, b_{m-1}$.

# Kết quả

- In ra số lần mảng $a$ xuất hiện liên tiếp trong mảng $b$.

# Giới hạn

- $1 \le n \le m \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
2 6
1 2
1 2 1 2 1 2
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
2 4
1 1
1 1 1 1
```

Kết quả:

```text
3
```

# Ví dụ 3

Dữ liệu vào:

```text
3 5
1 2 3
1 3 2 1 2
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $a = [1, 2]$ xuất hiện tại các vị trí bắt đầu $0, 2, 4$ (3 lần).
- **Ví dụ 2:** $a = [1, 1]$ xuất hiện tại các vị trí bắt đầu $0, 1, 2$ (có chồng lấn, tổng cộng $3$ lần).
- **Ví dụ 3:** $[1, 2, 3]$ không xuất hiện liên tiếp trong $b$ nên kết quả là $0$.
