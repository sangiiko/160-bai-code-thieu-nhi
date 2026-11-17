# 146 - Bài 146: Đưa chẵn về đầu, 0 ở giữa, lẻ về cuối

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy sắp xếp lại mảng theo 3 nhóm thứ tự:
1. Các số chẵn khác `0` nằm ở **đầu mảng**.
2. Các phần tử bằng `0` nằm ở **giữa mảng**.
3. Các số lẻ nằm ở **cuối mảng**.

Trong nội bộ từng nhóm, giữ nguyên thứ tự xuất hiện ban đầu của các phần tử.

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
7
3 0 4 5 0 2 7
```

Kết quả:

```text
4 2 0 0 3 5 7
```

# Ví dụ 2

Dữ liệu vào:

```text
5
0 -2 1 0 -3
```

Kết quả:

```text
-2 0 0 1 -3
```

# Ví dụ 3

Dữ liệu vào:

```text
4
1 3 5 7
```

Kết quả:

```text
1 3 5 7
```

# Giải thích

- **Ví dụ 1:** Chẵn khác $0$: `[4, 2]`; số $0$: `[0, 0]`; số lẻ: `[3, 5, 7]`.
- **Ví dụ 2:** Chẵn khác $0$: `[-2]`; số $0$: `[0, 0]`; số lẻ: `[1, -3]`.
- **Ví dụ 3:** Toàn số lẻ nên thứ tự không đổi.
