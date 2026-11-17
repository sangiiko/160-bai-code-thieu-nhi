# 038 - Bài 38: Ước chung lớn nhất của mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (không đồng thời bằng $0$). Hãy tìm ước chung lớn nhất dương (UCLN / $\gcd$) của tất cả các phần tử trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số nguyên dương $\gcd(|a_0|, |a_1|, \dots, |a_{n-1}|)$.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$, có ít nhất một $a_i \ne 0$

# Ví dụ 1

Dữ liệu vào:

```text
4
12 18 24 30
```

Kết quả:

```text
6
```

# Ví dụ 2

Dữ liệu vào:

```text
3
-15 0 25
```

Kết quả:

```text
5
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7 11 13
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $\gcd(12, 18, 24, 30) = 6$.
- **Ví dụ 2:** $\gcd(15, 0, 25) = 5$.
- **Ví dụ 3:** Các số nguyên tố cùng nhau nên UCLN bằng $1$.
