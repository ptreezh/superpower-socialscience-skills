#!/usr/bin/env python3
"""
为每个技能创建 ZIP 包并上传到服务器
执行日期：2026-03-23
"""

import os
import zipfile
import subprocess
from pathlib import Path

# 配置
SKILLS_DIR = Path("D:/socienceAI/agentskills")
FTP_HOST = "103.99.40.226"
FTP_USER = "3njf8mh28i222"
FTP_PASS = "4GrdQlUW38"

# 获取所有 expert 目录
expert_dirs = [d for d in SKILLS_DIR.iterdir() if d.is_dir() and d.name.endswith("-expert")]

print(f"📦 找到 {len(expert_dirs)} 个技能包")
print("=" * 60)

uploaded = 0
failed = 0
skipped = 0

for expert_dir in expert_dirs:
    skill_name = expert_dir.name
    print(f"\n处理：{skill_name}")
    
    # 创建 ZIP 文件
    zip_path = SKILLS_DIR / f"{skill_name}.zip"
    
    # 检查是否已存在且有效
    if zip_path.exists() and zip_path.stat().st_size > 1000:
        print(f"  ⏭️  跳过：ZIP 已存在")
        skipped += 1
        # 直接上传已存在的 ZIP
    else:
        try:
            # 创建 ZIP 包
            print(f"  创建 ZIP 包...")
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                # 添加关键文件
                files_to_add = [
                    "SKILL.md",
                    "skill.yaml",
                    "soul.md",
                    "README.md",
                ]
                
                for filename in files_to_add:
                    file_path = expert_dir / filename
                    if file_path.exists():
                        zipf.write(file_path, f"{skill_name}/{filename}")
                        print(f"    ✅ {filename}")
                
                # 添加 tools 目录
                tools_dir = expert_dir / "tools"
                if tools_dir.exists():
                    for py_file in tools_dir.glob("*.py"):
                        zipf.write(py_file, f"{skill_name}/tools/{py_file.name}")
                        print(f"    ✅ tools/{py_file.name}")
                
                # 添加 templates 目录
                templates_dir = expert_dir / "templates"
                if templates_dir.exists():
                    for tmpl_file in templates_dir.glob("*"):
                        if tmpl_file.is_file():
                            zipf.write(tmpl_file, f"{skill_name}/templates/{tmpl_file.name}")
                            print(f"    ✅ templates/{tmpl_file.name}")
            
            # 检查 ZIP 文件大小
            zip_size = zip_path.stat().st_size
            if zip_size < 100:
                print(f"  ❌ ZIP 文件太小 ({zip_size} 字节)，跳过")
                failed += 1
                if zip_path.exists():
                    zip_path.unlink()
                continue
            
            print(f"  ✅ ZIP 创建成功 ({zip_size / 1024:.1f} KB)")
            
        except Exception as e:
            print(f"  ❌ 创建 ZIP 失败：{e}")
            failed += 1
            if zip_path.exists():
                zip_path.unlink()
            continue
    
    # 上传 ZIP 文件到服务器
    print(f"  上传到服务器...")
    
    # 先创建远程目录
    mkdir_cmd = f'curl -X MKD "ftp://{FTP_HOST}/web/{skill_name}" --user {FTP_USER}:{FTP_PASS} --ftp-pasv 2>&1'
    subprocess.run(mkdir_cmd, shell=True, capture_output=True)
    
    # 上传 ZIP
    upload_cmd = f'curl -T "{zip_path}" "ftp://{FTP_HOST}/web/{skill_name}/{skill_name}.zip" --user {FTP_USER}:{FTP_PASS} --ftp-pasv --retry 3 --connect-timeout 10'
    
    result = subprocess.run(upload_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0 or "550" in result.stderr:  # 550 表示文件已存在
        print(f"  ✅ 上传成功")
        uploaded += 1
        # 删除本地 ZIP 文件
        if zip_path.exists() and zip_path.stat().st_size > 1000:
            zip_path.unlink()
    else:
        print(f"  ❌ 上传失败")
        print(f"     {result.stderr[:100]}")
        failed += 1
        if zip_path.exists():
            zip_path.unlink()

print("\n" + "=" * 60)
print(f"✅ 上传完成：{uploaded} 个技能包")
print(f"⏭️  跳过：{skipped} 个")
print(f"❌ 失败：{failed} 个")
print("=" * 60)
