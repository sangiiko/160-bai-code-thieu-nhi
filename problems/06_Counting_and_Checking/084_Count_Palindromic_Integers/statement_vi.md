# 084 - Bài 84: Đếm số đối xứng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy đếm số lượng **số đối xứng** có trong mảng.

*Định nghĩa:* Số nguyên không âm $x$ là số đối xứng nếu biểu diễn thập phân của nó đọc từ trái sang phải hay từ phải sang trái đều giống nhau (ví dụ: $0, 9, 55, 121$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số lượng số đối xứng trong mảng.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
121 34 55 10 9
```

Kết quả:

```text
3
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-121 12 23 100
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
4
0 11 101 1221
```

Kết quả:

```text
4
```

# Giải thích

- **Ví dụ 1:** Các số đối xứng là $121, 55, 9$ (có $3$ số).
- **Ví dụ 2:** $-121 < 0$ không tính, các số còn lại không đối xứng nên kết quả là $0$.
- **Ví dụ 3:** Cả $4$ số $0, 11, 101, 1221$ đều đối xứng.
