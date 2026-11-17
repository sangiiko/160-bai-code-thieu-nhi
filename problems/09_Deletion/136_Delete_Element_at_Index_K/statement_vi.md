# 136 - Bài 136: Xóa phần tử tại chỉ số k

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ và chỉ số $k$ ($0 \le k < n$, đánh số từ $0$). Hãy xóa phần tử tại chỉ số $k$ khỏi mảng (dịch các phần tử phía sau sang trái $1$ vị trí).

# Dữ liệu vào

- Dòng đầu tiên chứa hai số nguyên $n$ và $k$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra $n - 1$ phần tử còn lại cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng trở nên rỗng.

# Giới hạn

- $1 \le n \le 10^5$
- $0 \le k < n$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5 2
10 20 30 40 50
```

Kết quả:

```text
10 20 40 50
```

# Ví dụ 2

Dữ liệu vào:

```text
1 0
99
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4 0
1 2 3 4
```

Kết quả:

```text
2 3 4
```

# Giải thích

- **Ví dụ 1:** Xóa phần tử ở chỉ số $2$ ($30$), mảng còn $[10, 20, 40, 50]$.
- **Ví dụ 2:** Xóa phần tử duy nhất khiến mảng rỗng (`EMPTY`).
- **Ví dụ 3:** Xóa phần tử đầu tiên ($k = 0$) còn $[2, 3, 4]$.
