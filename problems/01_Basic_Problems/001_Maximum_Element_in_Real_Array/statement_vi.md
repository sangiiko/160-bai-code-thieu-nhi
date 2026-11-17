# 001 - Bài 1: Giá trị lớn nhất trong mảng số thực

* **Giới hạn thời gian:** 1.00 s
* **Giới hạn bộ nhớ:** 256 MB

Cho mảng $a$ gồm $n$ số thực $a_0, a_1, \dots, a_{n-1}$. Hãy tìm giá trị lớn nhất trong mảng $a$.

# Dữ liệu vào

- Dòng đầu tiên chứa số nguyên dương $n$.
- Dòng thứ hai chứa $n$ số thực $a_0, a_1, \dots, a_{n-1}$.

# Kết quả

- In ra một số thực duy nhất là giá trị lớn nhất của mảng.
- Đáp án được coi là đúng nếu sai số tuyệt đối hoặc tương đối không vượt quá $10^{-6}$.

# Giới hạn

- $1 \le n \le 10^5$
- $-10^9 \le a_i \le 10^9$

# Ví dụ 1

Dữ liệu vào:

```text
5
-2.5 3.14 0.0 7.8 5.2
```

Kết quả:

```text
7.800000
```

# Ví dụ 2

Dữ liệu vào:

```text
4
-12.5 -3.4 -9.1 -0.25
```

Kết quả:

```text
-0.250000
```

# Ví dụ 3

Dữ liệu vào:

```text
1
42.75
```

Kết quả:

```text
42.750000
```

# Giải thích

- **Ví dụ 1:** Trong mảng $[-2.5, 3.14, 0.0, 7.8, 5.2]$, giá trị lớn nhất là $7.8$.
- **Ví dụ 2:** Mọi phần tử đều âm; giá trị lớn nhất (gần $0$ nhất) là $-0.25$.
- **Ví dụ 3:** Mảng chỉ có một phần tử duy nhất là $42.75$.
- **Lưu ý:** Khi khởi tạo biến lưu giá trị lớn nhất, không nên khởi tạo bằng $0$ vì tất cả các phần tử của mảng đều có thể mang giá trị âm (như ở Ví dụ 2).
