# 155 - Bài 155: Đảo ngược thứ tự chẵn và lẻ giữ vị trí tương đối

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đảo ngược thứ tự của nhóm các số chẵn trên các vị trí chẵn ban đầu, đồng thời đảo ngược thứ tự của nhóm các số lẻ trên các vị trí lẻ ban đầu (giữ nguyên mẫu phân bố vị trí chẵn/lẻ của mảng).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
2 1 4 3 6 5
```

Kết quả:

```text
6 5 4 3 2 1
```

# Ví dụ 2

Dữ liệu vào:

```text
5
2 4 1 3 8
```

Kết quả:

```text
8 4 3 1 2
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7 9 11
```

Kết quả:

```text
11 9 7
```

# Giải thích

- **Ví dụ 1:** Chẵn $[2, 4, 6] \to [6, 4, 2]$ tại chỉ số $0, 2, 4$; lẻ $[1, 3, 5] \to [5, 3, 1]$ tại chỉ số $1, 3, 5$.
- **Ví dụ 2:** Chẵn $[2, 4, 8] \to [8, 4, 2]$ tại chỉ số $0, 1, 4$; lẻ $[1, 3] \to [3, 1]$ tại chỉ số $2, 3$.
- **Ví dụ 3:** Chỉ có số lẻ nên đảo ngược cả mảng.
