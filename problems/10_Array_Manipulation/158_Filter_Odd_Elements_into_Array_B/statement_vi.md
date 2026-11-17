# 158 - Bài 158: Tạo mảng b chỉ chứa số lẻ từ mảng a

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tạo mảng $b$ chỉ chứa các phần tử **lẻ** lấy từ mảng $a$ theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử của mảng $b$ cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng $b$ rỗng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 7 -4 9 6
```

Kết quả:

```text
7 9
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 2 4 8
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-1 3 -5
```

Kết quả:

```text
-1 3 -5
```

# Giải thích

- **Ví dụ 1:** Các số lẻ trong $a$ theo thứ tự là $7$ và $9$.
- **Ví dụ 2:** Mảng $a$ không có số lẻ nào nên $b$ rỗng (`EMPTY`).
- **Ví dụ 3:** Cả ba số $-1, 3, -5$ đều lẻ.
