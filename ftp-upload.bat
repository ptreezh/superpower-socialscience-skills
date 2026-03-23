@echo off
REM FTP 自动上传脚本
REM 执行日期：2026-03-22

echo ========================================
echo SocienceAI 网站更新 FTP 上传
echo ========================================
echo.

REM 创建临时 FTP 命令文件
echo open 103.99.40.226 21 > ftp_commands.txt
echo 3njf8mh28i222 >> ftp_commands.txt
echo 4GrdQlUW38 >> ftp_commands.txt
echo binary >> ftp_commands.txt
echo cd /htdocs >> ftp_commands.txt
echo put index.html >> ftp_commands.txt
echo quit >> ftp_commands.txt

echo 正在上传 index.html...
echo.

REM 执行 FTP 上传
ftp -s:ftp_commands.txt

echo.
echo ========================================
echo 上传完成！
echo ========================================

REM 删除临时文件
del ftp_commands.txt

pause
