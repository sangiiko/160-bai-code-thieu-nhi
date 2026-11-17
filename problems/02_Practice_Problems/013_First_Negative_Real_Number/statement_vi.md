# 013 - Bài 13: Giá trị âm đầu tiên trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị **âm** ($a_i < 0$) đầu tiên xuất hiện trong mảng. Nếu mảng không có giá trị âm nào, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra giá trị âm đầu tiên tìm được (sai số tuyệt đối hoặc tương đối không quá $10^{-6}$), hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
0.0 2.5 -3.75 -1.2 4.0
```

Kết quả:

```text
-3.750000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
0.0 1.5 2.0 100.0
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
5.0 0.0 -0.005
```

Kết quả:

```text
-0.005000
```

# Giải thích

- **Ví dụ 1:** $0.0$ và $2.5$ không âm; giá trị âm đầu tiên là $-3.75$.
- **Ví dụ 2:** Mảng không có giá trị âm nên in `-1`.
- **Ví dụ 3:** Giá trị âm đầu tiên là $-0.005$.
