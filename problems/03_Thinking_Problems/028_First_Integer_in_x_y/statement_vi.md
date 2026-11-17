# 028 - Bài 28: Giá trị đầu tiên trong đoạn [x, y]

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và hai số nguyên $x, y$ ($x \le y$). Hãy tìm phần tử **đầu tiên** trong mảng thuộc đoạn $[x, y]$ (tức $x \le a_i \le y$). Nếu không có giá trị nào thỏa mãn, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa ba số nguyên $n, x, y$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra phần tử đầu tiên thuộc $[x, y]$, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le x \le y \le 10^9$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6 10 20
3 25 15 12 8 19
```

Kết quả:

```text
15
```

# Ví dụ 2

Dữ liệu vào:

```text
4 10 20
1 9 21 30
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4 5 5
1 5 7 5
```

Kết quả:

```text
5
```

# Giải thích

- **Ví dụ 1:** $3 < 10$ và $25 > 20$ đều ngoài đoạn $[10, 20]$; phần tử đầu tiên thuộc $[10, 20]$ là $15$.
- **Ví dụ 2:** Không có phần tử nào nằm trong $[10, 20]$ nên in `-1`.
- **Ví dụ 3:** Đoạn $[5, 5]$ chỉ chứa giá trị $5$; tìm thấy $5$.
