# 151 - Bài 151: Dịch trái xoay vòng k phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và một số nguyên không âm $k$. Hãy dịch **trái xoay vòng** mảng $k$ bước (tức mỗi lần dịch $1$ bước sang trái thì phần tử đầu mảng chuyển ra cuối mảng; chú ý $k$ có thể lớn hơn $n$).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên $n$ và $k$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng sau khi dịch trái xoay vòng gồm $n$ số nguyên cách nhau bởi dấu cách.

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
3 4 5 1 2
```

# Ví dụ 2

Dữ liệu vào:

```text
5 7
10 20 30 40 50
```

Kết quả:

```text
30 40 50 10 20
```

# Ví dụ 3

Dữ liệu vào:

```text
4 0
1 2 3 4
```

Kết quả:

```text
1 2 3 4
```

# Giải thích

- **Ví dụ 1:** Dịch trái $2$ bước đưa $[1, 2]$ ra cuối mảng $\to [3, 4, 5, 1, 2]$.
- **Ví dụ 2:** Vì $7 \bmod 5 = 2$, dịch trái $7$ bước tương đương dịch trái $2$ bước $\to [30, 40, 50, 10, 20]$.
- **Ví dụ 3:** Với $k = 0$, mảng không thay đổi.
