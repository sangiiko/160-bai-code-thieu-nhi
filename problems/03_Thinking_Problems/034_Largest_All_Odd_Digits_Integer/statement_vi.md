# 034 - Bài 34: Giá trị lớn nhất toàn chữ số lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **lớn nhất** trong mảng mà **tất cả các chữ số** (trong biểu diễn thập phân của $|a_i|$) đều là chữ số lẻ. Nếu không có phần tử nào thỏa mãn, in ra `0`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra phần tử lớn nhất toàn chữ số lẻ, hoặc `0` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
123 357 901 79 1359
```

Kết quả:

```text
1359
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 24 103 89
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-13 -5 22
```

Kết quả:

```text
-5
```

# Giải thích

- **Ví dụ 1:** $123$ chứa $2$, $901$ chứa $0$; các số toàn chữ số lẻ là $357, 79, 1359$, lớn nhất là $1359$.
- **Ví dụ 2:** Không có số nào toàn chữ số lẻ nên kết quả là `0`.
- **Ví dụ 3:** Cả $-13$ và $-5$ đều toàn chữ số lẻ; giá trị lớn hơn là $-5$.
