# 051 - Bài 51: Liệt kê vị trí các số nguyên tố

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy liệt kê tất cả các vị trí (chỉ số) mà giá trị tại đó là **số nguyên tố**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng không có số nguyên tố nào.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
4 2 9 11 15
```

Kết quả:

```text
1 3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-3 0 1 9
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
2 3 5 7
```

Kết quả:

```text
0 1 2 3
```

# Giải thích

- **Ví dụ 1:** $a_1 = 2$ và $a_3 = 11$ là các số nguyên tố.
- **Ví dụ 2:** Số âm, $0, 1, 9$ không phải số nguyên tố nên in `EMPTY`.
- **Ví dụ 3:** Cả $4$ phần tử đều nguyên tố nên in ra các chỉ số $0, 1, 2, 3$.
