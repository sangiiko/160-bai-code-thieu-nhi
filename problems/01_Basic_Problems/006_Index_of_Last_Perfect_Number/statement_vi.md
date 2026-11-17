# 006 - Bài 6: Vị trí số hoàn thiện cuối cùng

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm vị trí (chỉ số) của **số hoàn thiện** xuất hiện cuối cùng trong mảng. Nếu mảng không có số hoàn thiện nào, in ra `-1`.

*Định nghĩa:* Một số nguyên dương $x$ được gọi là **số hoàn thiện** (số hoàn hảo) nếu tổng các ước nguyên dương thực sự của nó (nhỏ hơn $x$) bằng chính $x$ (ví dụ: $6 = 1 + 2 + 3$, $28 = 1 + 2 + 4 + 7 + 14$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra chỉ số (tính từ $0$) của số hoàn thiện cuối cùng trong mảng, hoặc `-1` nếu không có.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
6 12 28 15 496 7
```

Kết quả:

```text
4
```

# Ví dụ 2

Dữ liệu vào:

```text
5
-6 0 1 10 24
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
8128 10 20
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** Các số hoàn thiện là $a_0 = 6$, $a_2 = 28$ và $a_4 = 496$. Chỉ số cuối cùng là $4$.
- **Ví dụ 2:** Số âm, $0$ và $1$ không phải số hoàn thiện; không có số hoàn thiện nào trong mảng nên in `-1`.
- **Ví dụ 3:** $8128$ là số hoàn thiện tại chỉ số $0$.
