# 024 - Bài 24: Tìm đoạn [a, b] chứa tất cả phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng một chiều gồm $n$ số thực $arr_0, arr_1, \dots, arr_{n-1}$. Hãy tìm đoạn $[a, b]$ ngắn nhất (tức $b - a$ nhỏ nhất) sao cho mọi phần tử của mảng đều thuộc đoạn $[a, b]$ (tức $a \le arr_i \le b$ với mọi $i$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $arr_0, arr_1, \dots, arr_{n-1}$.

# Kết quả

- In ra hai số thực $a$ và $b$ cách nhau bởi một dấu cách (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le arr_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-4.5 2.1 9.8 0.0 -1.2
```

Kết quả:

```text
-4.500000 9.800000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
3.0 7.5 2.0 10.0
```

Kết quả:

```text
2.000000 10.000000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
-5.5
```

Kết quả:

```text
-5.500000 -5.500000
```

# Giải thích

- **Ví dụ 1:** Giá trị nhỏ nhất là $-4.5$ và lớn nhất là $9.8$, nên đoạn ngắn nhất là $[-4.5, 9.8]$.
- **Ví dụ 2:** Đoạn $[2.0, 10.0]$ chứa toàn bộ các số dương trong mảng.
- **Ví dụ 3:** Mảng có 1 phần tử nên $a = b = -5.5$.
