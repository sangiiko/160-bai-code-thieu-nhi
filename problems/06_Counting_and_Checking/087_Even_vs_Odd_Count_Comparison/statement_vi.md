# 087 - Bài 87: Tương quan số lượng chẵn và lẻ

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Gọi $E$ là số lượng phần tử chẵn và $O$ là số lượng phần tử lẻ trong mảng. Hãy cho biết tương quan giữa $E$ và $O$:
- Trả về `-1` nếu số lượng chẵn **nhiều hơn** số lượng lẻ ($E > O$).
- Trả về `0` nếu số lượng chẵn **bằng** số lượng lẻ ($E = O$).
- Trả về `1` nếu số lượng chẵn **ít hơn** số lượng lẻ ($E < O$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một trong ba giá trị `-1`, `0`, hoặc `1`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 4 6 1 3
```

Kết quả:

```text
-1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 3 4
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1 -3 5
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** Có $3$ số chẵn ($2, 4, 6$) và $2$ số lẻ ($1, 3$). Vì $3 > 2$ nên kết quả là `-1`.
- **Ví dụ 2:** Có $2$ số chẵn và $2$ số lẻ ($2 = 2$) nên kết quả là `0`.
- **Ví dụ 3:** Có $0$ số chẵn và $3$ số lẻ ($0 < 3$) nên kết quả là `1`.
