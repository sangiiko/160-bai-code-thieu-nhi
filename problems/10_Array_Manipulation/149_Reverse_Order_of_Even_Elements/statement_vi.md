# 149 - Bài 149: Đảo ngược thứ tự các số chẵn

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đảo ngược thứ tự của riêng các **số chẵn** trên tập vị trí ban đầu của chúng, trong khi các số lẻ giữ nguyên vị trí.

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
2 3 4 5 6 7
```

Kết quả:

```text
6 3 4 5 2 7
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 3 5 7
```

Kết quả:

```text
1 3 5 7
```

# Ví dụ 3

Dữ liệu vào:

```text
4
8 4 2 0
```

Kết quả:

```text
0 2 4 8
```

# Giải thích

- **Ví dụ 1:** Các số chẵn $[2, 4, 6]$ tại chỉ số $0, 2, 4$ đảo thành $[6, 4, 2]$; các số lẻ $3, 5, 7$ giữ nguyên.
- **Ví dụ 2:** Không có số chẵn nào nên mảng giữ nguyên.
- **Ví dụ 3:** Cả mảng là số chẵn nên đảo ngược toàn bộ.
