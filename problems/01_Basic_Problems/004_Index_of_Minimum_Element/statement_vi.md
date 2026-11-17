# 004 - Bài 4: Vị trí giá trị nhỏ nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm một vị trí (chỉ số) $i$ sao cho $a_i$ đạt giá trị nhỏ nhất trong mảng. Nếu có nhiều vị trí cùng đạt giá trị nhỏ nhất, hãy in ra **chỉ số nhỏ nhất**.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số nguyên duy nhất là chỉ số (tính từ $0$) đầu tiên đạt giá trị nhỏ nhất.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
4.2 -1.5 3.0 -1.5 2.1
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 3.0 2.0 1.0
```

Kết quả:

```text
3
```

# Ví dụ 3

Dữ liệu vào:

```text
3
7.0 7.0 7.0
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Giá trị nhỏ nhất là $-1.5$, xuất hiện tại các chỉ số $1$ và $3$. Chỉ số nhỏ nhất là $1$.
- **Ví dụ 2:** Giá trị nhỏ nhất là $1.0$ nằm ở cuối mảng (chỉ số $3$).
- **Ví dụ 3:** Tất cả phần tử bằng nhau nên chỉ số đầu tiên đạt giá trị nhỏ nhất là $0$.
