# 127 - Bài 127: Sắp xếp chẵn, lẻ tăng dần giữ vị trí tương đối

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các phần tử chẵn tăng dần trên các vị trí ban đầu của số chẵn, và sắp xếp các phần tử lẻ tăng dần trên các vị trí ban đầu của số lẻ (tức vị trí nào ban đầu là số chẵn vẫn chứa số chẵn, vị trí nào ban đầu là số lẻ vẫn chứa số lẻ).

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
8 7 2 5 4 1
```

Kết quả:

```text
2 1 4 5 8 7
```

# Ví dụ 2

Dữ liệu vào:

```text
4
9 7 5 3
```

Kết quả:

```text
3 5 7 9
```

# Ví dụ 3

Dữ liệu vào:

```text
5
4 -1 0 -3 -2
```

Kết quả:

```text
-2 -3 0 -1 4
```

# Giải thích

- **Ví dụ 1:** Các vị trí chẵn $\{0, 2, 4\}$ chứa $[8, 2, 4] \to [2, 4, 8]$; các vị trí lẻ $\{1, 3, 5\}$ chứa $[7, 5, 1] \to [1, 5, 7]$.
- **Ví dụ 2:** Chỉ có các số lẻ nên toàn bộ được sắp tăng dần.
- **Ví dụ 3:** Các số chẵn $[4, 0, -2] \to [-2, 0, 4]$; các số lẻ $[-1, -3] \to [-3, -1]$.
