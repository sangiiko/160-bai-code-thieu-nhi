# 088 - Bài 88: Đếm các phần tử cực trị

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ ($n \ge 2$). Một phần tử $a_i$ được gọi là **cực trị** nếu nó lớn hơn hẳn tất cả các phần tử xung quanh nó, **hoặc** nhỏ hơn hẳn tất cả các phần tử xung quanh nó (mỗi phần tử trong mảng có tối đa $2$ phần tử xung quanh là $a_{i-1}$ và $a_{i+1}$). Hãy đếm số lượng phần tử cực trị trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng phần tử cực trị trong mảng.

# Giới hạn

- $2 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
1.0 3.0 2.0 2.0 5.0
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1.0 2.0 3.0 4.0
```

Kết quả:

```text
2
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

- **Ví dụ 1:** $a_0 = 1.0 < 3.0$ (cực tiểu), $a_1 = 3.0 > 1.0, 2.0$ (cực đại), $a_4 = 5.0 > 2.0$ (cực đại). Còn $a_2 = a_3 = 2.0$ không phải cực trị. Tổng là $3$.
- **Ví dụ 2:** Mảng tăng dần nên chỉ có hai đầu mút $1.0$ và $4.0$ là cực trị.
- **Ví dụ 3:** Mọi phần tử bằng nhau nên không có cực trị nào ($0$).
