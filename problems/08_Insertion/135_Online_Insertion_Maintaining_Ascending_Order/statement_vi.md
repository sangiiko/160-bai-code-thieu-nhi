# 135 - Bài 135: Nhập mảng sắp xếp tăng dần

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho lần lượt $n$ số nguyên được nhập vào theo thứ tự $a_0, a_1, \dots, a_{n-1}$. Hãy xây dựng mảng sao cho sau khi nhập xong, các phần tử trong mảng tự động được sắp xếp theo thứ tự **tăng dần** (không giảm).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng tăng dần gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
5 2 8 1 4
```

Kết quả:

```text
1 2 4 5 8
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1 -5 0 -1
```

Kết quả:

```text
-5 -1 -1 0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
7
```

Kết quả:

```text
7
```

# Giải thích

- **Ví dụ 1:** Quá trình chèn: $[5] \to [2, 5] \to [2, 5, 8] \to [1, 2, 5, 8] \to [1, 2, 4, 5, 8]$.
- **Ví dụ 2:** Mảng sau khi sắp không giảm là $[-5, -1, -1, 0]$.
- **Ví dụ 3:** Mảng có 1 phần tử $7$.
