# 153 - Bài 153: Xuất mảng chẵn vàng, lẻ trắng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Yêu cầu xuất các phần tử theo quy ước màu sắc: **số chẵn màu vàng**, **số lẻ màu trắng**.

*(Chuyển sang định dạng văn bản chuẩn để chấm tự động: in mỗi phần tử dưới dạng `giá_trị(Y)` nếu chẵn (Yellow), hoặc `giá_trị(W)` nếu lẻ (White).)*

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n$ chuỗi cách nhau bởi dấu cách, mỗi chuỗi có dạng `val(Y)` hoặc `val(W)`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
2 5 8 3
```

Kết quả:

```text
2(Y) 5(W) 8(Y) 3(W)
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0 -4 -7
```

Kết quả:

```text
0(Y) -4(Y) -7(W)
```

# Ví dụ 3

Dữ liệu vào:

```text
2
1 -1
```

Kết quả:

```text
1(W) -1(W)
```

# Giải thích

- **Ví dụ 1:** $2$ và $8$ chẵn gắn `(Y)`; $5$ và $3$ lẻ gắn `(W)`.
- **Ví dụ 2:** $0$ và $-4$ chẵn (`Y`); $-7$ lẻ (`W`).
- **Ví dụ 3:** Cả $1$ và $-1$ đều lẻ (`W`).
