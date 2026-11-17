# 021 - Bài 21: Vị trí giá trị âm nhỏ nhất

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$ (đánh số từ $0$ đến $n - 1$). Hãy tìm vị trí (chỉ số) của giá trị **âm nhỏ nhất** trong mảng. Nếu có nhiều vị trí cùng đạt giá trị âm nhỏ nhất, hãy chọn **chỉ số nhỏ nhất**. Nếu mảng không có số âm, in ra `-1`.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra chỉ số (tính từ $0$) của giá trị âm nhỏ nhất, hoặc `-1` nếu không tồn tại số âm.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
2.0 -3.5 -9.1 0.0 -9.1
```

Kết quả:

```text
2
```

# Ví dụ 2

Dữ liệu vào:

```text
3
0.0 1.5 2.5
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
4
-1.0 -2.0 -3.0 -4.0
```

Kết quả:

```text
3
```

# Giải thích

- **Ví dụ 1:** Giá trị âm nhỏ nhất là $-9.1$, xuất hiện lần đầu tại chỉ số $2$.
- **Ví dụ 2:** Không có phần tử âm nào nên kết quả là `-1`.
- **Ví dụ 3:** Giá trị âm nhỏ nhất là $-4.0$ tại chỉ số $3$.
