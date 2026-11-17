# 031 - Bài 31: Số gánh đầu tiên

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$. Hãy tìm **số gánh** (số đối xứng) đầu tiên xuất hiện trong mảng. Nếu mảng không có số gánh nào, in ra `-1`.

*Định nghĩa:* Một số nguyên không âm $x$ là **số gánh** nếu khi viết ở hệ thập phân và đọc ngược các chữ số từ phải sang trái ta vẫn thu được chính số $x$ (ví dụ: $0, 7, 121, 1331$).

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số nguyên $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra số gánh đầu tiên trong mảng, hoặc `-1` nếu không tồn tại.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
12 45 121 34 88
```

Kết quả:

```text
121
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-121 10 23 100
```

Kết quả:

```text
-1
```

# Ví dụ 3

Dữ liệu vào:

```text
3
24 7 99
```

Kết quả:

```text
7
```

# Giải thích

- **Ví dụ 1:** $12$ và $45$ không đối xứng; số gánh đầu tiên là $121$.
- **Ví dụ 2:** $-121$ là số âm, các số còn lại không đối xứng nên kết quả là `-1`.
- **Ví dụ 3:** Số có 1 chữ số $7$ cũng đối xứng, nên kết quả là $7$.
