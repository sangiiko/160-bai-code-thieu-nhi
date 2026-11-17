# 016 - Bài 16: Số hoàn thiện cuối cùng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số hoàn thiện** xuất hiện cuối cùng trong mảng. Nếu mảng không có số hoàn thiện nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số hoàn thiện cuối cùng trong mảng, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
6 28 10 496 12
```

Kết quả:

```text
496
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-28 0 1 12
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
6 8 10
```

Kết quả:

```text
6
```

# Giải thích

- **Ví dụ 1:** Các số hoàn thiện là $6, 28, 496$; số cuối cùng là $496$.
- **Ví dụ 2:** Không có số hoàn thiện dương nào nên in `-1`.
- **Ví dụ 3:** Số hoàn thiện duy nhất (và cuối cùng) là $6$.
