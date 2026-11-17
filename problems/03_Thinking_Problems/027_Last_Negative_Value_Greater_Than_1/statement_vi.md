# 027 - Bài 27: Giá trị âm cuối cùng lớn hơn -1

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị âm xuất hiện **cuối cùng** trong mảng thỏa mãn lớn hơn hẳn $-1$ (tức là $-1 < a_i < 0$). Nếu không có giá trị nào thỏa mãn, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị cuối cùng thuộc khoảng $(-1, 0)$ (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
-0.5 -2.0 -1.0 -0.25 0.0 1.5
```

Kết quả:

```text
-0.250000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-1.0 -5.0 0.0 2.0
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-0.9 -0.1 -0.05
```

Kết quả:

```text
-0.050000
```

# Giải thích

- **Ví dụ 1:** $-1.0$ và $0.0$ không nằm trong khoảng mở $(-1, 0)$. Các số thỏa mãn là $-0.5$ và $-0.25$; số cuối cùng là $-0.25$.
- **Ví dụ 2:** Không có giá trị nào thỏa mãn $-1 < a_i < 0$ nên kết quả là `-1`.
- **Ví dụ 3:** Giá trị cuối cùng thỏa mãn là $-0.05$.
