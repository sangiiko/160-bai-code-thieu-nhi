# 030 - Bài 30: Số chính phương đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số chính phương** đầu tiên xuất hiện trong mảng. Nếu mảng không có số chính phương nào, in ra `-1`.

*Định nghĩa:* Một số nguyên không âm $x$ được gọi là **số chính phương** nếu tồn tại số nguyên $k \ge 0$ sao cho $x = k^2$ (ví dụ: $0, 1, 4, 9, 16, \dots$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số chính phương đầu tiên trong mảng, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-4 3 10 16 25
```

Kết quả:

```text
16
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-9 -1 2 7
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
5 0 9 4
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $-4$ là số âm, $3$ và $10$ không chính phương; số chính phương đầu tiên là $16 = 4^2$.
- **Ví dụ 2:** Các số âm không thể là số chính phương; $2, 7$ cũng không chính phương nên in `-1`.
- **Ví dụ 3:** $0 = 0^2$ là số chính phương đầu tiên trong mảng.
