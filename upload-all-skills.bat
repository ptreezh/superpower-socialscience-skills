@echo off
REM 批量上传所有技能包到服务器
REM 执行日期：2026-03-23

echo ========================================
echo 批量上传 57 个技能包
echo ========================================
echo.

cd /d D:\socienceAI\agentskills

REM 创建临时 FTP 命令文件
echo open 103.99.40.226 21 > ftp_upload.txt
echo 3njf8mh28i222 >> ftp_upload.txt
echo 4GrdQlUW38 >> ftp_upload.txt
echo binary >> ftp_upload.txt
echo cd /web >> ftp_upload.txt

REM 上传每个技能包
for /d %%i in (*-expert) do (
    echo 上传：%%i
    echo mkdir %%i >> ftp_upload.txt
    echo cd %%i >> ftp_upload.txt
    
    REM 上传关键文件
    for %%f in (SKILL.md skill.yaml soul.md README.md) do (
        if exist "%%i\%%f" (
            echo put "%%i\%%f" >> ftp_upload.txt
        )
    )
    
    REM 上传工具目录
    if exist "%%i\tools" (
        echo mkdir tools >> ftp_upload.txt
        cd "%%i\tools"
        for %%t in (*.py) do (
            echo put "%%t" >> ..\..\ftp_upload.txt
        )
        cd ..\..
    )
    
    echo cd .. >> ftp_upload.txt
    echo.
)

echo quit >> ftp_upload.txt

REM 执行 FTP 上传
echo.
echo 开始上传...
ftp -s:ftp_upload.txt

REM 清理临时文件
del ftp_upload.txt

echo.
echo ========================================
echo 上传完成！
echo ========================================
pause
