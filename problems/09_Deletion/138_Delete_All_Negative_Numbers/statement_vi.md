# 138 - Bài 138: Xóa tất cả số âm trong mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy xóa tất cả các phần tử mang giá trị **âm** ($a_i < 0$) khỏi mảng, giữ nguyên thứ tự của các phần tử còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu mọi phần tử đều bị xóa.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-2.0 3.5 0.0 -1.5 4.0
```

Kết quả:

```text
3.500000 0.000000 4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-1.0 -2.5 -0.1
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0.0 1.5 2.0
```

Kết quả:

```text
0.000000 1.500000 2.000000
```

# Giải thích

- **Ví dụ 1:** $-2.0$ và $-1.5$ bị xóa; $0.0$ không âm nên được giữ lại: $[3.5, 0.0, 4.0]$.
- **Ví dụ 2:** Tất cả phần tử đều âm nên kết quả là `EMPTY`.
- **Ví dụ 3:** Không có phần tử âm nào nên mảng giữ nguyên.
