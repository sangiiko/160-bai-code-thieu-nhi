# 064 - Bài 64: Liệt kê vị trí giá trị lớn nhất (2)

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy liệt kê tất cả các vị trí (chỉ số) mà giá trị tại đó bằng giá trị lớn nhất của mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) theo thứ tự tăng dần, cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
5.5 1.0 5.5 2.0 5.5
```

Kết quả:

```text
0 2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-1.0 -2.0 -3.0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
10.0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất $5.5$ xuất hiện tại các chỉ số $0, 2, 4$.
- **Ví dụ 2:** Giá trị lớn nhất $-1.0$ nằm ở chỉ số $0$.
- **Ví dụ 3:** Chỉ có một phần tử tại chỉ số $0$.
