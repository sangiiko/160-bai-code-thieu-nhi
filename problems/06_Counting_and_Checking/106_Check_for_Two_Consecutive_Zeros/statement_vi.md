# 106 - Bài 106: Kiểm tra mảng có 2 giá trị 0 liên tiếp

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem trong mảng có tồn tại ít nhất hai phần tử đứng liền kề nhau cùng bằng `0` ($a_i = 0$ và $a_{i+1} = 0$ với $0 \le i \le n - 2$) hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu có $2$ giá trị `0` liên tiếp, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 0 0 2 0
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
5
0 1 0 2 0
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $a_1 = a_2 = 0$ là hai số $0$ liên tiếp nên kết quả là `1`.
- **Ví dụ 2:** Có ba số $0$ nhưng không có hai số nào đứng kề nhau nên kết quả là `0`.
- **Ví dụ 3:** Mảng chỉ có $1$ phần tử nên không thể có $2$ phần tử liên tiếp (`0`).
