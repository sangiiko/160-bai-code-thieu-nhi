# 026 - Bài 26: Giá trị đầu tiên lớn hơn 2003

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **đầu tiên** trong mảng lớn hơn hẳn $2003$ ($a_i > 2003$). Nếu không có phần tử nào thỏa mãn, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị đầu tiên lớn hơn $2003$ (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
100.5 2003.0 2003.5 3000.0 1500.0
```

Kết quả:

```text
2003.500000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-10.0 0.0 2003.0 2002.99
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
2
2004.0 2005.0
```

Kết quả:

```text
2004.000000
```

# Giải thích

- **Ví dụ 1:** $2003.0$ không lớn hơn hẳn $2003$; phần tử đầu tiên thỏa mãn $a_i > 2003$ là $2003.5$.
- **Ví dụ 2:** Không có phần tử nào lớn hơn hẳn $2003$ nên in `-1`.
- **Ví dụ 3:** $2004.0$ ở ngay đầu mảng lớn hơn $2003$.
