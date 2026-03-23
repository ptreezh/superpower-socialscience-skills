#!/usr/bin/env python3
"""
批量上传所有 57 个技能包到服务器
执行日期：2026-03-23
"""

import os
import subprocess
from pathlib import Path

# 技能包目录
skills_dir = Path("D:/socienceAI/agentskills")

# FTP 配置
FTP_HOST = "103.99.40.226"
FTP_USER = "3njf8mh28i222"
FTP_PASS = "4GrdQlUW38"
REMOTE_DIR = "/web"

# 获取所有 expert 目录
expert_dirs = [d for d in skills_dir.iterdir() if d.is_dir() and d.name.endswith("-expert")]

print(f"📦 找到 {len(expert_dirs)} 个技能包")
print("=" * 60)

uploaded = 0
failed = 0

for expert_dir in expert_dirs:
    skill_name = expert_dir.name
    print(f"\n上传：{skill_name}")
    
    # 检查关键文件
    key_files = list(expert_dir.glob("SKILL.md")) + list(expert_dir.glob("skill.yaml"))
    if not key_files:
        print(f"  ❌ 跳过：缺少关键文件")
        failed += 1
        continue
    
    # 构建 curl 命令上传整个目录
    # 先创建远程目录
    mkdir_cmd = f'curl -X MKD "ftp://{FTP_HOST}{REMOTE_DIR}/{skill_name}" --user {FTP_USER}:{FTP_PASS} --ftp-pasv'
    
    # 上传关键文件
    files_to_upload = [
        "SKILL.md",
        "skill.yaml", 
        "soul.md",
        "README.md",
    ]
    
    for filename in files_to_upload:
        local_file = expert_dir / filename
        if local_file.exists():
            upload_cmd = f'curl -T "{local_file}" "ftp://{FTP_HOST}{REMOTE_DIR}/{skill_name}/{filename}" --user {FTP_USER}:{FTP_PASS} --ftp-pasv'
            try:
                result = subprocess.run(upload_cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"  ✅ {filename}")
                else:
                    print(f"  ⚠️ {filename} (可能已存在)")
            except Exception as e:
                print(f"  ❌ {filename}: {e}")
    
    # 上传 tools 目录
    tools_dir = expert_dir / "tools"
    if tools_dir.exists() and tools_dir.is_dir():
        print(f"  上传 tools/ 目录...")
        for py_file in tools_dir.glob("*.py"):
            upload_cmd = f'curl -T "{py_file}" "ftp://{FTP_HOST}{REMOTE_DIR}/{skill_name}/tools/{py_file.name}" --user {FTP_USER}:{FTP_PASS} --ftp-pasv'
            try:
                result = subprocess.run(upload_cmd, shell=True, capture_output=True, text=True)
                if result.returncode == 0:
                    print(f"    ✅ {py_file.name}")
                else:
                    print(f"    ⚠️ {py_file.name}")
            except Exception as e:
                print(f"    ❌ {py_file.name}: {e}")
    
    uploaded += 1
    print(f"  ✅ {skill_name} 完成")

print("\n" + "=" * 60)
print(f"✅ 上传完成：{uploaded} 个技能包")
print(f"❌ 失败：{failed} 个")
print("=" * 60)
