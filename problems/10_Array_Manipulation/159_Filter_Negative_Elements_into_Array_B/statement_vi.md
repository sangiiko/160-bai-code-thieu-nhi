# 159 - Bài 159: Tạo mảng b chỉ chứa số âm từ mảng a

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tạo mảng $b$ chỉ chứa các giá trị **âm** ($a_i < 0$) lấy từ mảng $a$ theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử của mảng $b$ cách nhau bởi dấu cách (sai số $\le 10^{-6}$), hoặc `EMPTY` nếu mảng $b$ rỗng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-1.5 0.0 2.3 -4.0 5.1
```

Kết quả:

```text
-1.500000 -4.000000
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0.0 1.2 3.4
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-0.5 -2.5 -10.0
```

Kết quả:

```text
-0.500000 -2.500000 -10.000000
```

# Giải thích

- **Ví dụ 1:** Các giá trị âm là $-1.5$ và $-4.0$ ($0.0$ không âm).
- **Ví dụ 2:** Không có giá trị âm nào nên $b$ rỗng (`EMPTY`).
- **Ví dụ 3:** Toàn bộ các phần tử đều âm.
