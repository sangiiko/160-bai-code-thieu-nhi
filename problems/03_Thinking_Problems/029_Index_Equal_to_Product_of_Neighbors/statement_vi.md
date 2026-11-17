# 029 - Bài 29: Vị trí có giá trị bằng tích hai lân cận

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm một vị trí $i$ ($1 \le i \le n - 2$) thỏa mãn cả hai điều kiện:
1. Phần tử $a_i$ có đủ hai phần tử lân cận là $a_{i-1}$ và $a_{i+1}$.
2. $a_i = a_{i-1} \times a_{i+1}$.

Nếu có nhiều vị trí thỏa mãn, in ra **chỉ số nhỏ nhất**. Nếu không tồn tại, in ra `-1`.

*(Để tránh sai số dấu phẩy động, điều kiện bằng nhau được kiểm tra với sai số $|a_i - a_{i-1} \times a_{i+1}| \le 10^{-9}$.)*

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra chỉ số (tính từ $0$) nhỏ nhất thỏa mãn điều kiện, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
5
2.0 6.0 3.0 12.0 4.0
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
2
5.0 5.0
```

Kết quả:

```text
-1
```

# Giải thích

- **Ví dụ 1:** Tại $i = 1$: $a_1 = 6.0 = 2.0 \times 3.0$. Tại $i = 3$: $a_3 = 12.0 = 3.0 \times 4.0$. Chọn chỉ số nhỏ nhất là $1$.
- **Ví dụ 2:** Không có vị trí nào bằng tích hai phần tử kề bên nên in `-1`.
- **Ví dụ 3:** Với $n = 2$, không có phần tử nào có đủ 2 phần tử lân cận nên in `-1`.
