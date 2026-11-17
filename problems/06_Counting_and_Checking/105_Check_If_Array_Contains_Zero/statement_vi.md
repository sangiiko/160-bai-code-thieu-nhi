# 105 - Bài 105: Kiểm tra mảng có giá trị 0

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem trong mảng có tồn tại phần tử nào bằng `0` hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng có giá trị `0`, ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1 0 -2 5
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
10 -10 20 30
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
1
0
```

Kết quả:

```text
1
```

# Giải thích

- **Ví dụ 1:** $a_1 = 0$ nên kết quả là `1`.
- **Ví dụ 2:** Không có phần tử nào bằng $0$ nên kết quả là `0`.
- **Ví dụ 3:** Mảng chỉ có một phần tử là $0$ nên kết quả là `1`.
