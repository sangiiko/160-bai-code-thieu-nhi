# 160 Bài Code Thiếu Nhi

Bộ **160 bài tập mảng 1 chiều** (C/C++) được chuẩn hóa theo định dạng **Codeforces / Polygon**, kèm theo đề bài tiếng Việt (`statement_vi.md`), lời giải chuẩn (`solution.cpp`), bộ test (`tests/` gồm 3 ví dụ + 12 test ẩn mỗi bài) và custom checker (`checker.cpp` sử dụng `testlib.h` cho 44 bài số thực; 116 bài còn lại dùng `std::wcmp.cpp`).

## Nguồn đề & Ghi nhận (Credits)

- **Tác giả bộ đề gốc:** **Thạc sĩ Tống Thanh Văn** — *Học viện Bưu chính Viễn thông cơ sở Hồ Chí Minh* (PTIT HCM).
- Chuyển thể định dạng Codeforces, bộ test, lời giải chuẩn và công cụ đồng bộ Polygon bởi [@sangiiko](https://github.com/sangiiko).

## Cấu trúc thư mục

```text
160-bai-code-thieu-nhi/
├── .env.example              # Mẫu cấu hình API Key / Secret của Polygon
├── .gitignore
├── README.md
├── scripts/
│   ├── inspect_repo.py       # Kiểm tra số lượng bài, đề, lời giải, test và checker
│   └── polygon_sync.py       # Đồng bộ đề bài, checker, solution và test lên Polygon
└── problems/
    ├── CHECKER_MANIFEST.json # Danh sách phân loại checker.cpp vs std::wcmp.cpp
    ├── 01_Basic_Problems/    # Bài 1 – 8
    ├── 02_Practice_Problems/ # Bài 9 – 21
    ├── 03_Thinking_Problems/ # Bài 22 – 42
    ├── 04_Search_and_Listing/# Bài 43 – 65
    ├── 05_Sum_and_Average/   # Bài 66 – 81
    ├── 06_Counting_and_Checking/ # Bài 82 – 119 (chia 2 contest: 082–107 & 108–119)
    ├── 07_Sorting/           # Bài 120 – 130
    ├── 08_Insertion/         # Bài 131 – 135
    ├── 09_Deletion/          # Bài 136 – 144
    └── 10_Array_Manipulation/# Bài 145 – 160
```

## Hướng dẫn nhanh

1. Kiểm tra tính đầy đủ của 160 bài:
   ```bash
   python3 scripts/inspect_repo.py
   ```
2. Tạo file `.env` từ `.env.example` và điền `POLYGON_API_KEY`, `POLYGON_API_SECRET`.
3. Chạy thử (dry-run) hoặc đồng bộ lên Polygon:
   ```bash
   python3 scripts/polygon_sync.py --category 01_Basic_Problems --dry-run
   python3 scripts/polygon_sync.py --all --upload
   ```
