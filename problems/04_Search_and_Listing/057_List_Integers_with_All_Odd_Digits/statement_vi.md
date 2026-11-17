# 057 - Bài 57: Liệt kê số nguyên toàn chữ số lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử có **toàn bộ các chữ số** (trong biểu diễn thập phân của $|a_i|$) đều là chữ số lẻ theo thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thỏa mãn cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
13 25 -791 305 9
```

Kết quả:

```text
13 -791 9
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 12 45 88
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
135 79 1
```

Kết quả:

```text
135 79 1
```

# Giải thích

- **Ví dụ 1:** $25$ chứa $2$ (chẵn) và $305$ chứa $0$ (chẵn); các số toàn chữ số lẻ là $13, -791, 9$.
- **Ví dụ 2:** Không có số nào toàn chữ số lẻ nên in `EMPTY`.
- **Ví dụ 3:** Cả ba số đều chỉ gồm các chữ số lẻ.
