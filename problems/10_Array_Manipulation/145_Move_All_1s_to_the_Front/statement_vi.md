# 145 - Bài 145: Đưa số 1 về đầu mảng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy biến đổi mảng bằng cách đưa tất cả các phần tử có giá trị bằng `1` về **đầu mảng**, đồng thời giữ nguyên thứ tự tương đối của tất cả các phần tử khác `1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra mảng kết quả gồm $n$ số nguyên cách nhau bởi dấu cách.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
3 1 5 1 2 4
```

Kết quả:

```text
1 1 3 5 2 4
```

# Ví dụ 2

Dữ liệu vào:

```text
4
2 4 6 8
```

Kết quả:

```text
2 4 6 8
```

# Ví dụ 3

Dữ liệu vào:

```text
3
1 1 1
```

Kết quả:

```text
1 1 1
```

# Giải thích

- **Ví dụ 1:** Hai số `1` được đưa lên đầu, các phần tử `3, 5, 2, 4` giữ nguyên thứ tự.
- **Ví dụ 2:** Không có số `1` nào nên mảng không thay đổi.
- **Ví dụ 3:** Toàn bộ mảng là số `1`.
