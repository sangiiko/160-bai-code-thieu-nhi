# 160 - Bài 160: Tạo mảng b chỉ chứa số nguyên tố từ mảng a

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tạo mảng $b$ chỉ chứa các **số nguyên tố** lấy từ mảng $a$ theo đúng thứ tự xuất hiện.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra các phần tử của mảng $b$ cách nhau bởi dấu cách, hoặc `EMPTY` nếu mảng $b$ rỗng.

# Giới hạn

- $1 \le n \le 10^4$
- $-10^6 \le a_i \le 10^6$

# Ví dụ 1

Dữ liệu vào:

```text
6
1 2 4 5 9 13
```

Kết quả:

```text
2 5 13
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-3 0 1 9
```

Kết quả:

```text
EMPTY
```

# Ví dụ 3

Dữ liệu vào:

```text
4
2 3 2 7
```

Kết quả:

```text
2 3 2 7
```

# Giải thích

- **Ví dụ 1:** Các số nguyên tố theo thứ tự là $2, 5, 13$.
- **Ví dụ 2:** Không có số nguyên tố nào nên mảng $b$ rỗng (`EMPTY`).
- **Ví dụ 3:** Cả $4$ số (bao gồm cả $2$ lặp lại) đều được đưa vào $b$.
