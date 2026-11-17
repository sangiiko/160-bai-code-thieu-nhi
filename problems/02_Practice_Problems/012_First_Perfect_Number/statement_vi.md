# 012 - Bài 12: Số hoàn thiện đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số hoàn thiện** đầu tiên xuất hiện trong mảng. Nếu mảng không có số hoàn thiện nào, in ra `-1`.

*Định nghĩa:* Số nguyên dương $x$ là số hoàn thiện nếu tổng các ước nguyên dương thực sự của nó (không kể $x$) bằng $x$ (ví dụ: $6, 28, 496, \dots$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số hoàn thiện đầu tiên tìm được, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
12 28 6 15 496
```

Kết quả:

```text
28
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
3
8 12 6
```

Kết quả:

```text
6
```

# Giải thích

- **Ví dụ 1:** $12$ không hoàn thiện ($1+2+3+4+6=16 \ne 12$); số hoàn thiện đầu tiên là $28$.
- **Ví dụ 2:** Không có số hoàn thiện nào trong mảng nên in `-1`.
- **Ví dụ 3:** Số hoàn thiện đầu tiên nằm ở cuối mảng là $6$.
