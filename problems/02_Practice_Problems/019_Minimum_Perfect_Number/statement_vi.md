# 019 - Bài 19: Số hoàn thiện nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số hoàn thiện nhỏ nhất** trong mảng. Nếu mảng không có số hoàn thiện nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số hoàn thiện nhỏ nhất trong mảng, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
496 28 12 6 8128
```

Kết quả:

```text
6
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-6 0 1 10
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
2
28 28
```

Kết quả:

```text
28
```

# Giải thích

- **Ví dụ 1:** Các số hoàn thiện là $496, 28, 6, 8128$; nhỏ nhất là $6$.
- **Ví dụ 2:** Không có số hoàn thiện nào nên in `-1`.
- **Ví dụ 3:** Số hoàn thiện nhỏ nhất là $28$.
