# 009 - Bài 9: Giá trị nhỏ nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị nhỏ nhất trong mảng $a$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số thực duy nhất là giá trị nhỏ nhất trong mảng (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
3.5 -2.1 0.0 7.4 -2.15
```

Kết quả:

```text
-2.150000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
10.0 20.5 5.25
```

Kết quả:

```text
5.250000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
-99.5
```

Kết quả:

```text
-99.500000
```

# Giải thích

- **Ví dụ 1:** Trong các phần tử, $-2.15$ là nhỏ nhất.
- **Ví dụ 2:** Tất cả phần tử đều dương; nhỏ nhất là $5.25$.
- **Ví dụ 3:** Mảng chỉ có một phần tử là $-99.5$.
