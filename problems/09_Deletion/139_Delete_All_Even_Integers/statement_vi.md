# 139 - Bài 139: Xóa tất cả số chẵn trong mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xóa tất cả các **số chẵn** khỏi mảng, giữ nguyên thứ tự của các số lẻ còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu không còn phần tử nào.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2 7 4 9 6
```

Kết quả:

```text
7 9
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0 -2 4 8
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1 -3 5 7
```

Kết quả:

```text
1 -3 5 7
```

# Giải thích

- **Ví dụ 1:** Xóa $2, 4, 6$, còn lại $7, 9$.
- **Ví dụ 2:** Toàn bộ là số chẵn nên sau khi xóa mảng rỗng (`EMPTY`).
- **Ví dụ 3:** Toàn bộ là số lẻ nên mảng không đổi.
