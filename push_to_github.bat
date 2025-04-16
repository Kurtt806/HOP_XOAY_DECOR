@echo off
cd /d %~dp0
echo 🔄 Đang chạy Git Auto Push Script...

:: Đặt tên commit
set COMMIT_MSG=up step

:: Bước 1: git add .
git add .
echo ✅ Đã add tất cả file

:: Bước 2: commit
git commit -m "%COMMIT_MSG%"
echo ✅ Commit với nội dung: %COMMIT_MSG%

:: Bước 3: kiểm tra xem remote đã tồn tại chưa
git remote show origin >nul 2>&1
if errorlevel 1 (
    echo 🔗 Thêm remote origin...
    git remote add origin https://github.com/Kurtt806/HOP_XOAY_DECOR.git
) else (
    echo 🔗 Remote origin đã tồn tại, bỏ qua...
)

:: Bước 4: đảm bảo nhánh chính là main
git branch -M main

:: Bước 5: push lên GitHub
git push -u origin main

echo 🎉 Hoàn tất Git Push!
pause
