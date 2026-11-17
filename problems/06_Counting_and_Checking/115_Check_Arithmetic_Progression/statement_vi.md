# 115 - Bài 115: Kiểm tra cấp số cộng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Hãy kiểm tra xem các phần tử theo đúng thứ tự trong mảng có lập thành một **cấp số cộng** hay không (tức hiệu $a_{i+1} - a_i = d$ là hằng số với mọi $0 \le i \le n - 2$). Nếu có, hãy chỉ ra công sai $d$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `YES d` nếu mảng lập thành cấp số cộng với công sai $d$, ngược lại in ra `NO`.

# Giới hạn

- $2 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 5 8 11 14
```

Kết quả:

```text
YES 3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10 5 0 -5
```

Kết quả:

```text
YES -5
```

# Ví dụ 3

Dữ liệu vào:

```text
5
1 5 2 8 3
```

Kết quả:

```text
NO
```

# Giải thích

- **Ví dụ 1:** Hiệu hai phần tử liên tiếp luôn bằng $3$, nên là cấp số cộng với công sai $d = 3$.
- **Ví dụ 2:** Công sai có thể âm: $d = -5$.
- **Ví dụ 3:** Các hiệu liên tiếp không bằng nhau nên in `NO`.
