# 154 - Bài 154: Xuất mảng chẵn hàng trên, lẻ hàng dưới

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy xuất các phần tử của mảng thành $2$ hàng: hàng thứ nhất gồm tất cả các **số chẵn** (theo đúng thứ tự xuất hiện), hàng thứ hai gồm tất cả các **số lẻ** (theo đúng thứ tự xuất hiện). Nếu một trong hai hàng không có phần tử nào, in ra `EMPTY` ở hàng đó.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- Dòng 1: các số chẵn cách nhau bởi dấu cách (hoặc `EMPTY`).
- Dòng 2: các số lẻ cách nhau bởi dấu cách (hoặc `EMPTY`).

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
6
1 4 3 8 5 2
```

Kết quả:

```text
4 8 2
1 3 5
```

# Ví dụ 2

Dữ liệu vào:

```text
3
2 4 6
```

Kết quả:

```text
2 4 6
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
3
-1 3 5
```

Kết quả:

```text
EMPTY
-1 3 5
```

# Giải thích

- **Ví dụ 1:** Hàng 1 là các số chẵn `4 8 2`, hàng 2 là các số lẻ `1 3 5`.
- **Ví dụ 2:** Không có số lẻ nên hàng 2 in `EMPTY`.
- **Ví dụ 3:** Không có số chẵn nên hàng 1 in `EMPTY`.
