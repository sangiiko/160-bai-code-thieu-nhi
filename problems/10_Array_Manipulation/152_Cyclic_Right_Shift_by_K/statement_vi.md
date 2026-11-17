# 152 - Bài 152: Dịch phải xoay vòng k phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và một số nguyên không âm $k$. Hãy dịch **phải xoay vòng** mảng $k$ bước (mỗi lần dịch $1$ bước sang phải thì phần tử cuối mảng chuyển lên đầu mảng; chú ý $k$ có thể lớn hơn $n$).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên $n$ và $k$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng sau khi dịch phải xoay vòng gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $0 \le k \le 10^9$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 2
1 2 3 4 5
```

Kết quả:

```text
4 5 1 2 3
```

# Ví dụ 2

Dữ liệu vào:

```text
5 7
10 20 30 40 50
```

Kết quả:

```text
40 50 10 20 30
```

# Ví dụ 3

Dữ liệu vào:

```text
1 100
42
```

Kết quả:

```text
42
```

# Giải thích

- **Ví dụ 1:** Dịch phải $2$ bước đưa $[4, 5]$ lên đầu mảng $\to [4, 5, 1, 2, 3]$.
- **Ví dụ 2:** Vì $7 \bmod 5 = 2$, dịch phải $7$ bước tương đương dịch phải $2$ bước $\to [40, 50, 10, 20, 30]$.
- **Ví dụ 3:** Mảng có 1 phần tử nên luôn giữ nguyên.
