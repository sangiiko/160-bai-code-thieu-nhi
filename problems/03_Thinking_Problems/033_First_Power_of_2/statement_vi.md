# 033 - Bài 33: Giá trị đầu tiên có dạng 2^k

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **đầu tiên** trong mảng có dạng $2^k$ với $k$ là số nguyên không âm ($k \ge 0$, tức là thuộc tập $\{1, 2, 4, 8, 16, \dots\}$). Nếu mảng không có giá trị nào dạng $2^k$, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra phần tử đầu tiên có dạng $2^k$, hoặc `0` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3 6 16 8 10
```

Kết quả:

```text
16
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-4 0 3 6
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
5 1 4
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $3$ và $6$ không phải lũy thừa của $2$; phần tử đầu tiên thỏa mãn là $16 = 2^4$.
- **Ví dụ 2:** Số âm và $0$ không có dạng $2^k$ nên kết quả là `0`.
- **Ví dụ 3:** $1 = 2^0$ có dạng $2^k$ với $k = 0$.
