#!/usr/bin/env python3
"""
SocienceAI 网站一键部署脚本
构建 VitePress 并上传到 www.socienceAI.com

用法:
    python deploy-to-web.py              # 构建 + 部署
    python deploy-to-web.py --build-only # 仅构建
    python deploy-to-web.py --deploy-only # 仅部署（使用已有构建）
"""

import os
import sys
import subprocess
from pathlib import Path
from ftplib import FTP

# ============================================================
# 配置
# ============================================================
FTP_HOST = "103.99.40.226"
FTP_USER = "3njf8mh28i222"
FTP_PASS = "4GrdQlUW38"
REMOTE_DIR = "/web"

WEBSITE_DIR = Path(r"D:\socienceAI\agentskills\website")
DIST_DIR = WEBSITE_DIR / "docs" / ".vitepress" / "dist"

uploaded = 0
failed = 0


def build():
    """构建 VitePress 站点"""
    print("=" * 60)
    print("  Step 1: Build VitePress")
    print("=" * 60)
    result = subprocess.run(
        ["npm", "run", "build"], cwd=str(WEBSITE_DIR), capture_output=True, text=True
    )
    if result.returncode != 0:
        print(f"Build FAILED:\n{result.stderr}")
        sys.exit(1)
    print(result.stdout)
    count = len(list(DIST_DIR.rglob("*.*")))
    print(f"Build complete: {count} files in dist/")


def deploy():
    """通过 FTP 部署到 /web/"""
    global uploaded, failed

    print("\n" + "=" * 60)
    print("  Step 2: Deploy to FTP")
    print("=" * 60)

    ftp = FTP()
    ftp.connect(FTP_HOST, 21, timeout=30)
    ftp.login(FTP_USER, FTP_PASS)
    ftp.cwd(REMOTE_DIR)
    print(f"Connected to {FTP_HOST}:{REMOTE_DIR}")

    # Phase 1: directories
    print("\nCreating directories...")
    for root, dirs, files in os.walk(DIST_DIR):
        rel = Path(root).relative_to(DIST_DIR)
        rd = (
            REMOTE_DIR
            if str(rel) == "."
            else REMOTE_DIR + "/" + str(rel).replace("\\", "/")
        )
        if rd != REMOTE_DIR:
            parts = rd.strip("/").split("/")
            cur = ""
            for p in parts:
                cur += "/" + p
                try:
                    ftp.cwd(cur)
                except Exception:
                    try:
                        ftp.mkd(cur)
                        print(f"  mkdir {cur}")
                    except Exception:
                        pass
            ftp.cwd("/")

    # Phase 2: upload files
    print("\nUploading files...")
    for root, dirs, files in os.walk(DIST_DIR):
        rel = Path(root).relative_to(DIST_DIR)
        rd = (
            REMOTE_DIR + "/"
            if str(rel) == "."
            else REMOTE_DIR + "/" + str(rel).replace("\\", "/") + "/"
        )
        for fname in files:
            local_path = Path(root) / fname
            remote_path = rd + fname
            try:
                with open(str(local_path), "rb") as f:
                    ftp.storbinary("STOR " + remote_path, f)
                uploaded += 1
                if uploaded % 100 == 0 or fname == "index.html":
                    print(f"  [{uploaded}] {remote_path}")
            except Exception as e:
                failed += 1
                # Retry once
                try:
                    with open(str(local_path), "rb") as f:
                        ftp.storbinary("STOR " + remote_path, f)
                    uploaded += 1
                    failed -= 1
                    print(f"  [retry ok] {remote_path}")
                except Exception:
                    print(f"  FAIL {remote_path}: {e}")

    ftp.quit()


def verify():
    """验证部署结果"""
    import urllib.request

    print("\n" + "=" * 60)
    print("  Step 3: Verify")
    print("=" * 60)

    urls = [
        "http://www.socienceAI.com/",
        "http://www.socienceAI.com/methodologies/",
        "http://www.socienceAI.com/methodologies/grounded-theory.html",
        "http://www.socienceAI.com/guide/",
    ]
    for url in urls:
        try:
            req = urllib.request.Request(url, method="HEAD")
            req.add_header("User-Agent", "Mozilla/5.0")
            resp = urllib.request.urlopen(req, timeout=8)
            size = resp.headers.get("Content-Length", "?")
            print(f"  ✅ {resp.status} {url} ({size} bytes)")
        except Exception as e:
            print(f"  ❌ {url}: {e}")


def main():
    deploy_only = "--deploy-only" in sys.argv
    build_only = "--build-only" in sys.argv

    if not deploy_only:
        build()
    if not build_only:
        deploy()
        verify()

    print(f"\n{'=' * 60}")
    print(f"  Done! Uploaded: {uploaded}, Failed: {failed}")
    print(f"  Site: http://www.socienceAI.com/")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()
