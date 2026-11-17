# 142 - Bài 142: Xóa tất cả số nguyên tố

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xóa tất cả các **số nguyên tố** khỏi mảng, giữ nguyên thứ tự các phần tử còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng trở nên rỗng.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 4 5 9 11
```

Kết quả:

```text
4 9
```

# Ví dụ 2

Dữ liệu vào:

```text
3
2 3 7
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-5 0 1 15
```

Kết quả:

```text
-5 0 1 15
```

# Giải thích

- **Ví dụ 1:** Xóa $2, 5, 11$, còn lại $4, 9$.
- **Ví dụ 2:** Toàn bộ là số nguyên tố nên kết quả là `EMPTY`.
- **Ví dụ 3:** $-5, 0, 1, 15$ đều không phải số nguyên tố nên mảng giữ nguyên.
