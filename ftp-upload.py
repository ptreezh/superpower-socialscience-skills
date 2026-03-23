#!/usr/bin/env python3
"""
SocienceAI 网站 FTP 批量上传工具

使用本地生成的网站内容，自动上传到服务器

用法:
    python ftp-upload.py [directory]
    
示例:
    python ftp-upload.py ./website/docs
"""

import os
import sys
from pathlib import Path
from ftplib import FTP

# ============================================================================
# 配置（从环境变量或配置文件读取，不要硬编码）
# ============================================================================

FTP_CONFIG = {
    'host': os.getenv('FTP_HOST', '103.99.40.226'),
    'port': int(os.getenv('FTP_PORT', '21')),
    'user': os.getenv('FTP_USER', '3njf8mh28i222'),
    'password': os.getenv('FTP_PASSWORD', ''),  # 从环境变量读取
    'remote_dir': os.getenv('FTP_REMOTE_DIR', '/htdocs'),
}


class WebsiteUploader:
    """网站上传器"""
    
    def __init__(self):
        self.ftp = FTP()
        self.uploaded_count = 0
        self.failed_count = 0
    
    def connect(self):
        """连接 FTP 服务器"""
        try:
            print(f"📡 连接到 FTP 服务器：{FTP_CONFIG['host']}:{FTP_CONFIG['port']}")
            self.ftp.connect(FTP_CONFIG['host'], FTP_CONFIG['port'])
            self.ftp.login(FTP_CONFIG['user'], FTP_CONFIG['password'])
            print("✅ FTP 连接成功")
            return True
        except Exception as e:
            print(f"❌ FTP 连接失败：{e}")
            return False
    
    def ensure_directory_exists(self, dir_path):
        """确保远程目录存在"""
        if not dir_path or dir_path == '/' or dir_path == '.':
            return
        
        try:
            self.ftp.cwd(dir_path)
            # 返回上级目录，以便后续操作
            self.ftp.cwd('..')
        except:
            # 目录不存在，递归创建
            parent = str(Path(dir_path).parent)
            if parent != dir_path:
                self.ensure_directory_exists(parent)
            try:
                self.ftp.mkd(dir_path)
                print(f"  📁 创建目录：{dir_path}")
            except Exception as e:
                print(f"  ⚠️ 创建目录失败 {dir_path}: {e}")
    
    def upload_file(self, local_path, remote_path):
        """上传单个文件"""
        try:
            with open(local_path, 'rb') as f:
                self.ftp.storbinary(f'STOR {remote_path}', f)
            self.uploaded_count += 1
            return True
        except Exception as e:
            print(f"  ❌ 上传失败 {remote_path}: {e}")
            self.failed_count += 1
            return False
    
    def upload_directory(self, local_dir, remote_dir):
        """上传整个目录"""
        local_dir = Path(local_dir)
        
        print(f"\n📂 上传目录：{local_dir} → {remote_dir}")
        
        # 确保远程目录存在
        self.ensure_directory_exists(remote_dir)
        
        # 遍历本地目录
        for root, dirs, files in os.walk(local_dir):
            # 计算相对路径
            rel_root = Path(root).relative_to(local_dir)
            
            # 创建远程子目录
            for dir_name in dirs:
                remote_subdir = str(Path(remote_dir) / rel_root / dir_name)
                self.ensure_directory_exists(remote_subdir)
            
            # 上传文件
            for file_name in files:
                local_path = Path(root) / file_name
                remote_subdir = Path(remote_dir) / rel_root
                remote_path = str(remote_subdir / file_name)
                
                print(f"  📄 上传：{file_name}")
                self.upload_file(str(local_path), remote_path)
    
    def close(self):
        """关闭连接"""
        try:
            self.ftp.quit()
            print("\n✅ FTP 连接已关闭")
        except:
            pass
    
    def print_summary(self):
        """打印上传摘要"""
        print("\n" + "="*60)
        print("📊 上传摘要")
        print("="*60)
        print(f"  成功：{self.uploaded_count} 个文件")
        print(f"  失败：{self.failed_count} 个文件")
        print("="*60)


def main():
    """主函数"""
    print("\n" + "="*60)
    print("  SocienceAI 网站 FTP 上传工具")
    print("="*60)
    
    # 检查密码是否配置
    if not FTP_CONFIG['password']:
        print("\n⚠️ 错误：FTP 密码未配置")
        print("请设置环境变量 FTP_PASSWORD 或在脚本中配置")
        print("\n使用方法:")
        print("  set FTP_PASSWORD=your_password  # Windows")
        print("  export FTP_PASSWORD=your_password  # Linux/Mac")
        print("  python ftp-upload.py ./website/docs")
        return
    
    # 获取上传目录
    if len(sys.argv) > 1:
        upload_dir = sys.argv[1]
    else:
        upload_dir = './website/docs'
    
    # 检查目录是否存在
    if not os.path.exists(upload_dir):
        print(f"\n❌ 错误：目录不存在 {upload_dir}")
        return
    
    # 创建上传器
    uploader = WebsiteUploader()
    
    # 连接
    if not uploader.connect():
        return
    
    # 上传
    uploader.upload_directory(upload_dir, FTP_CONFIG['remote_dir'])
    
    # 打印摘要
    uploader.print_summary()
    
    # 关闭连接
    uploader.close()
    
    print("\n✅ 上传完成！\n")


if __name__ == '__main__':
    main()
