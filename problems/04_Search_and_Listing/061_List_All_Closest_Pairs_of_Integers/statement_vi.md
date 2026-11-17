# 061 - Bài 61: Liệt kê các cặp giá trị gần nhau nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ ($n > 2$). Gọi $d = \min_{0 \le i < j < n} |a_i - a_j|$ là khoảng cách nhỏ nhất giữa hai phần tử ở hai vị trí khác nhau trong mảng. Hãy liệt kê tất cả các cặp $(a_i, a_j)$ với $i < j$ và $|a_i - a_j| = d$.

Mỗi cặp được viết theo dạng `(giá trị nhỏ hơn, giá trị lớn hơn)` và sắp xếp theo thứ tự tăng dần của giá trị thứ nhất (giữ thứ tự xuất hiện nếu bằng nhau).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mỗi cặp gần nhau nhất trên một dòng gồm hai số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $3 \le n \le 1000$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1 5 3 7
```

Kết quả:

```text
1 3
3 5
5 7
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10 2 8 2
```

Kết quả:

```text
2 2
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5 0 5
```

Kết quả:

```text
-5 0
0 5
```

# Giải thích

- **Ví dụ 1:** Khoảng cách nhỏ nhất là $d = 2$, đạt được tại $(1, 3)$, $(3, 5)$ và $(5, 7)$.
- **Ví dụ 2:** Có hai số $2$ bằng nhau nên $d = 0$; cặp duy nhất đạt $d = 0$ là $(2, 2)$.
- **Ví dụ 3:** Khoảng cách nhỏ nhất là $d = 5$, đạt tại $(-5, 0)$ và $(0, 5)$.
