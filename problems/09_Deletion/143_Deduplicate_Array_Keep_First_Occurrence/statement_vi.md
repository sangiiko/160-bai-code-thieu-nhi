# 143 - Bài 143: Xóa phần tử trùng nhau, giữ lại 1 phần tử

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xóa các phần tử trùng nhau sao cho mỗi giá trị phân biệt chỉ được giữ lại **duy nhất $1$ lần** (giữ lại lần xuất hiện đầu tiên và giữ nguyên thứ tự tương đối).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng sau khi loại bỏ trùng lặp, các phần tử cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
3 1 3 2 1 4
```

Kết quả:

```text
3 1 2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
5
9 9 9 9 9
```

Kết quả:

```text
9
```

# Ví dụ 3

Dữ liệu vào:

```text
4
10 20 30 40
```

Kết quả:

```text
10 20 30 40
```

# Giải thích

- **Ví dụ 1:** Giữ lại lần xuất hiện đầu của mỗi giá trị: $[3, 1, 2, 4]$.
- **Ví dụ 2:** Mọi phần tử bằng $9$ nên chỉ giữ lại một số $9$.
- **Ví dụ 3:** Không có phần tử trùng nhau nên giữ nguyên.
