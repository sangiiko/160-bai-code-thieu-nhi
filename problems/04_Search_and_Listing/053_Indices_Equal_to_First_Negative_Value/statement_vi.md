# 053 - Bài 53: Liệt kê vị trí bằng giá trị âm đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Gọi $v$ là giá trị **âm** ($a_i < 0$) xuất hiện đầu tiên trong mảng. Hãy liệt kê tất cả các vị trí (chỉ số) $i$ mà $a_i = v$. Nếu mảng không có số âm nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các chỉ số (tính từ $0$) thỏa mãn theo thứ tự tăng dần cách nhau bởi dấu cách, hoặc `-1` nếu mảng không có giá trị âm.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
1.0 -2.5 3.0 -2.5 -4.0 -2.5
```

Kết quả:

```text
1 3 5
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0.0 1.5 2.0 3.0
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5.0 0.0 1.0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Giá trị âm đầu tiên là $-2.5$, xuất hiện tại các chỉ số $1, 3, 5$.
- **Ví dụ 2:** Không có số âm nào trong mảng nên kết quả là `-1`.
- **Ví dụ 3:** Giá trị âm đầu tiên là $-5.0$, chỉ xuất hiện tại chỉ số $0$.
