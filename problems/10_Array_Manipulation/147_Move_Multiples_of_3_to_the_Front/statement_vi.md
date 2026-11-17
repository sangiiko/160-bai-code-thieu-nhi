# 147 - Bài 147: Đưa các số chia hết cho 3 về đầu mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đưa tất cả các phần tử **chia hết cho $3$** về đầu mảng, và các phần tử còn lại về sau, đồng thời giữ nguyên thứ tự tương đối trong từng nhóm.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
5 6 2 9 1 3
```

Kết quả:

```text
6 9 3 5 2 1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 4 5
```

Kết quả:

```text
1 2 4 5
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 -3 7 12
```

Kết quả:

```text
0 -3 12 7
```

# Giải thích

- **Ví dụ 1:** Các số chia hết cho $3$ (`6, 9, 3`) lên đầu, theo sau là `5, 2, 1`.
- **Ví dụ 2:** Không có số nào chia hết cho $3$ nên mảng giữ nguyên.
- **Ví dụ 3:** $0, -3, 12$ đều chia hết cho $3$ nên đứng trước $7$.
