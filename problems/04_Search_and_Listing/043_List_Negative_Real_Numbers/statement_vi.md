# 043 - Bài 43: Liệt kê các số âm trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy liệt kê tất cả các phần tử mang giá trị **âm** ($a_i < 0$) theo đúng thứ tự xuất hiện trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các số âm tìm được trên một dòng, cách nhau bởi một dấu cách (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$).
- Nếu mảng không có số âm nào, in ra `EMPTY`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-1.5 2.0 0.0 -3.2 -0.5
```

Kết quả:

```text
-1.500000 -3.200000 -0.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0.0 1.2 3.5 9.0
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-0.01 -100.0 -2.5
```

Kết quả:

```text
-0.010000 -100.000000 -2.500000
```

# Giải thích

- **Ví dụ 1:** Các phần tử nhỏ hơn hẳn $0$ theo thứ tự là $-1.5, -3.2, -0.5$ (số $0.0$ không phải số âm).
- **Ví dụ 2:** Không có phần tử âm nào nên in ra `EMPTY`.
- **Ví dụ 3:** Tất cả các phần tử đều âm nên in ra toàn bộ mảng.
