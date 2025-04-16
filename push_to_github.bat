@echo off
cd /d %~dp0
echo Git Auto Push Script...

:: Đặt tên commit
set COMMIT_MSG=auto up

:: Bước 1: git add .
git add .
echo add all file

:: Bước 2: commit
git commit -m "%COMMIT_MSG%"
echo Commit content: %COMMIT_MSG%

:: Bước 3: kiểm tra xem remote đã tồn tại chưa
git remote show origin >nul 2>&1
if errorlevel 1 (
    echo link remote origin...
    git remote add origin https://github.com/Kurtt806/HOP_XOAY_DECOR.git
)

:: Bước 4: đảm bảo nhánh chính là main
git branch -M main

:: Bước 5: push lên GitHub
git push -u origin main

echo DONEEEEEEEEEEEE
pause
