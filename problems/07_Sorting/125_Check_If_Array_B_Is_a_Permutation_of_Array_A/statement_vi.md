# 125 - Bài 125: Kiểm tra mảng b có là hoán vị của mảng a

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho hai mảng số nguyên $a$ và $b$, mỗi mảng gồm $n$ phần tử. Hãy kiểm tra xem mảng $b$ có phải là một **hoán vị** (cách sắp xếp lại thứ tự các phần tử) của mảng $a$ hay không (tức là mỗi giá trị xuất hiện ở $a$ và $b$ với số lần bằng nhau).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, \dots, a_{n-1}$.
- Dòng thứ ba chứa $n$ số nguyên $b_0, \dots, b_{n-1}$.

# Kết quả

- In ra `YES` nếu $b$ là hoán vị của $a$, ngược lại in ra `NO`.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i, b_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
4
1 2 2 3
2 3 1 2
```

Kết quả:

```text
YES
```

# Ví dụ 2

Dữ liệu vào:

```text
4
1 2 2 3
1 2 3 3
```

Kết quả:

```text
NO
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-5 0 5
5 -5 0
```

Kết quả:

```text
YES
```

# Giải thích

- **Ví dụ 1:** Cả hai mảng đều gồm một số $1$, hai số $2$ và một số $3$ (`YES`).
- **Ví dụ 2:** Mảng $a$ có hai số $2$ và một số $3$, còn $b$ có một số $2$ và hai số $3$ (`NO`).
- **Ví dụ 3:** Cùng tập phần tử với số lần xuất hiện giống nhau (`YES`).
