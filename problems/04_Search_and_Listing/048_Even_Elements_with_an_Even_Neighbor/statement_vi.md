# 048 - Bài 48: Liệt kê số chẵn có lân cận chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử chẵn $a_i$ sao cho ít nhất một trong các phần tử lân cận của nó ($a_{i-1}$ nếu $i > 0$, hoặc $a_{i+1}$ nếu $i < n - 1$) cũng là số chẵn.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử thỏa mãn theo thứ tự xuất hiện, cách nhau bởi dấu cách, hoặc `EMPTY` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
2 3 4 6 5 8
```

Kết quả:

```text
4 6
```

# Ví dụ 2

Dữ liệu vào:

```text
5
2 1 4 3 6
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 -2 1 4
```

Kết quả:

```text
0 -2
```

# Giải thích

- **Ví dụ 1:** $a_0 = 2$ chỉ kề $3$ (lẻ), $a_5 = 8$ chỉ kề $5$ (lẻ). Chỉ có $4$ và $6$ nằm cạnh nhau.
- **Ví dụ 2:** Các số chẵn đều bị ngăn cách bởi số lẻ nên không có số nào kề số chẵn; in `EMPTY`.
- **Ví dụ 3:** $0$ và $-2$ kề nhau và đều chẵn.
