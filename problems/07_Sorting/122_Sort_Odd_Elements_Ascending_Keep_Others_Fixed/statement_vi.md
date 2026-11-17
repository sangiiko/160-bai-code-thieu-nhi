# 122 - Bài 122: Sắp xếp số lẻ tăng dần, giữ nguyên vị trí khác

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp các phần tử mang giá trị **lẻ** theo thứ tự tăng dần trên chính tập các vị trí ban đầu của số lẻ, đồng thời **giữ nguyên vị trí** của các phần tử không phải số lẻ (tức các số chẵn).

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
9 4 3 8 1 6
```

Kết quả:

```text
1 4 3 8 9 6
```

# Ví dụ 2

Dữ liệu vào:

```text
4
2 4 6 8
```

Kết quả:

```text
2 4 6 8
```

# Ví dụ 3

Dữ liệu vào:

```text
5
5 -3 2 1 -7
```

Kết quả:

```text
-7 -3 2 1 5
```

# Giải thích

- **Ví dụ 1:** Các số lẻ ở chỉ số $0, 2, 4$ có giá trị $[9, 3, 1]$ được sắp xếp thành $[1, 3, 9]$; các số chẵn $4, 8, 6$ giữ nguyên vị trí.
- **Ví dụ 2:** Không có số lẻ nào nên mảng giữ nguyên hoàn toàn.
- **Ví dụ 3:** Các số lẻ $[5, -3, 1, -7]$ được sắp xếp tăng dần thành $[-7, -3, 1, 5]$, số $2$ giữ nguyên ở chỉ số $2$.
