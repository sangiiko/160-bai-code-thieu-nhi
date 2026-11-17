# 111 - Bài 111: Kiểm tra mảng đối xứng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem mảng $a$ có **đối xứng** hay không, tức là $a_i = a_{n - 1 - i}$ với mọi $0 \le i < n$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng đối xứng, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1 3 5 3 1
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 3 1
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
10 20 20 10
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $a_0 = a_4 = 1$, $a_1 = a_3 = 3$ nên mảng đối xứng (`1`).
- **Ví dụ 2:** $a_1 = 2 \ne a_2 = 3$ nên mảng không đối xứng (`0`).
- **Ví dụ 3:** Mảng có độ dài chẵn nhưng $a_0 = a_3 = 10$ và $a_1 = a_2 = 20$ nên đối xứng (`1`).
