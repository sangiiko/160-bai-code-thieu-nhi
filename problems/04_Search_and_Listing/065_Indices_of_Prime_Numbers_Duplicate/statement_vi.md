# 065 - Bài 65: Liệt kê vị trí số nguyên tố (2)

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy liệt kê tất cả các vị trí (chỉ số) mà giá trị tại đó là **số nguyên tố**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có số nguyên tố.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
3 6 7 10 13
```

Kết quả:

```text
0 2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 4 8 12
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-2 2 0
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố là $3, 7, 13$ nằm tại các chỉ số $0, 2, 4$.
- **Ví dụ 2:** Không có số nguyên tố nào nên in `EMPTY`.
- **Ví dụ 3:** Chỉ có $a_1 = 2$ là số nguyên tố (chỉ số $1$).
