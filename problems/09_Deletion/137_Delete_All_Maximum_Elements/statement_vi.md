# 137 - Bài 137: Xóa tất cả số lớn nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy xóa **tất cả** các phần tử bằng giá trị lớn nhất của mảng, giữ nguyên thứ tự tương đối của các phần tử còn lại.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử còn lại cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu toàn bộ phần tử bị xóa.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2.5 9.0 3.0 9.0 1.5
```

Kết quả:

```text
2.500000 3.000000 1.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
5.0 5.0 5.0 5.0
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-5.0 -2.0 -10.0 -2.0
```

Kết quả:

```text
-5.000000 -10.000000
```

# Giải thích

- **Ví dụ 1:** Giá trị lớn nhất là $9.0$; xóa cả hai lần xuất hiện còn $[2.5, 3.0, 1.5]$.
- **Ví dụ 2:** Mọi phần tử đều bằng giá trị lớn nhất $5.0$ nên sau khi xóa mảng rỗng (`EMPTY`).
- **Ví dụ 3:** Giá trị lớn nhất là $-2.0$; còn lại $[-5.0, -10.0]$.
