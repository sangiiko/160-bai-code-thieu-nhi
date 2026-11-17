# 109 - Bài 109: Kiểm tra không có số hoàn thiện lớn hơn 256

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy kiểm tra xem mảng có thỏa mãn tính chất: **không tồn tại số hoàn thiện nào lớn hơn hẳn $256$** hay không.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra `1` nếu mảng thỏa mãn tính chất (không có số hoàn thiện $> 256$), ngược lại in ra `0`.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
4
6 28 500 10
```

Kết quả:

```text
1
```

# Ví dụ 2

Dữ liệu vào:

```text
4
6 28 496 10
```

Kết quả:

```text
0
```

# Ví dụ 3

Dữ liệu vào:

```text
3
8128 1 2
```

Kết quả:

```text
0
```

# Giải thích

- **Ví dụ 1:** $6$ và $28$ là số hoàn thiện nhưng đều $\le 256$; $500$ không phải số hoàn thiện. Tính chất thỏa mãn (`1`).
- **Ví dụ 2:** $496$ là số hoàn thiện và $496 > 256$ nên tính chất bị vi phạm (`0`).
- **Ví dụ 3:** $8128$ là số hoàn thiện $> 256$ (`0`).
