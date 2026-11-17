# 075 - Bài 75: Tổng các số đối xứng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tính tổng tất cả các **số đối xứng** (số nguyên không âm có biểu diễn thập phân đọc xuôi và ngược giống nhau) trong mảng.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra tổng các số đối xứng dưới dạng số nguyên 64-bit.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
12 121 33 45 7
```

Kết quả:

```text
161
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-11 10 23 123
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
0 1001 99
```

Kết quả:

```text
1100
```

# Giải thích

- **Ví dụ 1:** Các số đối xứng là $121, 33, 7$; tổng $= 121 + 33 + 7 = 161$.
- **Ví dụ 2:** Không có số đối xứng không âm nào nên tổng bằng $0$.
- **Ví dụ 3:** $0, 1001, 99$ đều đối xứng; tổng $= 1100$.
