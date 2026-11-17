# 002 - Bài 2: Giá trị dương đầu tiên trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **dương** ($a_i > 0$) đầu tiên xuất hiện trong mảng theo thứ tự từ trái sang phải. Nếu mảng không có phần tử dương nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị dương đầu tiên tìm được (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
-3.5 0.0 2.75 -1.0 9.5 4.2
```

Kết quả:

```text
2.750000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-5.2 0.0 -0.01 -100.0
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0.0 0.0 0.001
```

Kết quả:

```text
0.001000
```

# Giải thích

- **Ví dụ 1:** Hai phần tử đầu $-3.5$ và $0.0$ không dương ($\le 0$). Phần tử dương đầu tiên là $a_2 = 2.75$.
- **Ví dụ 2:** Tất cả phần tử đều nhỏ hơn hoặc bằng $0$ nên kết quả là `-1`.
- **Ví dụ 3:** Số $0.0$ không phải số dương; phần tử dương đầu tiên là $0.001$ ở cuối mảng.
