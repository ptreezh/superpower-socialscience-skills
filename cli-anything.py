#!/usr/bin/env python3
"""
SocienceAI 网站更新 CLI 工具

整合所有网站建设和更新功能的统一命令行接口

用法:
    python cli-anything.py [command] [options]

示例:
    python cli-anything.py build              # 构建网站
    python cli-anything.py upload             # 上传到服务器
    python cli-anything.py update all         # 完整更新流程
    python cli-anything.py status             # 查看状态
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from ftplib import FTP

# 导入本地模块
sys.path.insert(0, str(Path(__file__).parent))


# ============================================================================
# 配置管理
# ============================================================================

class Config:
    """配置管理器"""
    
    def __init__(self):
        self.config_file = Path(__file__).parent / '.cli-config.json'
        self.config = self.load()
    
    def load(self):
        """加载配置"""
        if self.config_file.exists():
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def save(self):
        """保存配置"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)
    
    def get(self, key, default=None):
        """获取配置项"""
        return self.config.get(key, default)
    
    def set(self, key, value):
        """设置配置项"""
        self.config[key] = value
        self.save()


# ============================================================================
# 网站构建器
# ============================================================================

class WebsiteBuilder:
    """网站构建器"""
    
    def __init__(self, working_dir='./website'):
        self.working_dir = Path(working_dir)
        self.docs_dir = self.working_dir / 'docs'
    
    def build(self):
        """构建网站"""
        print("\n" + "="*60)
        print("  SocienceAI 网站构建器")
        print("="*60)
        
        # 创建目录结构
        self._create_directories()
        
        # 生成页面
        self._generate_pages()
        
        # 转换 Markdown 为 HTML
        self._convert_to_html()
        
        print("\n✅ 网站构建完成！")
    
    def _create_directories(self):
        """创建目录结构"""
        print("\n📁 创建目录结构...")
        
        dirs = [
            self.working_dir,
            self.docs_dir,
            self.docs_dir / '.vitepress',
            self.docs_dir / 'methodologies',
            self.docs_dir / 'guide',
            self.docs_dir / 'about',
            self.docs_dir / 'blog',
            self.docs_dir / 'tools',
        ]
        
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)
            print(f"  ✅ {d}")
    
    def _generate_pages(self):
        """生成页面内容"""
        print("\n📄 生成页面内容...")
        
        # 生成首页
        self._generate_homepage()
        
        # 生成方法论页面
        self._generate_methodology_pages()
        
        # 生成关于页面
        self._generate_about_page()
    
    def _generate_homepage(self):
        """生成首页"""
        content = """---
layout: home
hero:
  name: SocienceAI
  text: 让社会科学研究人人可为
  tagline: 通过 AI 技术推动社会科学研究的范式革新
  actions:
    - theme: brand
      text: 开始使用
      link: /guide/quick-start
    - theme: alt
      text: 方法论
      link: /methodologies/
features:
  - icon: 📚
    title: 12 种方法论专家
    details: 扎根理论、社会网络分析等
  - icon: 🤖
    title: AI 辅助分析
    details: 智能编码、自动验证
  - icon: ✅
    title: 严格质量保证
    details: 所有报告经过严格测试
---

## 什么是 SocienceAI？

SocienceAI 是一个基于 AI 技术的社会科学方法论支持平台。

## 核心能力

### 方法论专家
- 扎根理论
- 社会网络分析
- 行动者网络理论
- 布迪厄场域分析
- QCA、DID、回归分析
- 混合方法研究
- 数字马克思/涂尔干/韦伯

### AI 辅助功能
- 智能编码
- 自动验证
- 持续进化
- 质量保证

[查看详细使用指南](/guide/quick-start)
"""
        
        with open(self.docs_dir / 'index.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✅ 首页")
    
    def _generate_methodology_pages(self):
        """生成方法论页面"""
        methodologies = {
            'grounded-theory': '扎根理论',
            'sna': '社会网络分析',
            'ant': '行动者网络理论',
            'bourdieu': '布迪厄场域分析',
            'qca': 'QCA 定性比较分析',
            'did': 'DID 双重差分',
            'regression': '回归分析',
            'survey': '问卷设计',
            'mixed-methods': '混合方法研究',
            'digital-marx': '数字马克思分析',
            'digital-durkheim': '数字涂尔干分析',
            'digital-weber': '数字韦伯分析',
        }
        
        for slug, name in methodologies.items():
            content = f"""# {name}

## 概述

{name}是一种社会科学研究方法。

## 核心概念

- 核心概念 1
- 核心概念 2
- 核心概念 3

## 适用场景

- 应用场景 1
- 应用场景 2

## 如何使用

```bash
qwen "使用{name}分析以下数据..."
```

## 对标学者

[待补充]

## 学习资源

- [使用指南](/guide/quick-start)
- [案例研究](/blog/)

---

*由 SocienceAI 提供*
"""
            
            page_path = self.docs_dir / 'methodologies' / f'{slug}.md'
            with open(page_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  ✅ {name}")
        
        # 生成方法论索引页
        index_content = """# 方法论

SocienceAI 提供 12 种社会科学方法论的 AI 专家支持。

## 质性研究方法

- [扎根理论](/methodologies/grounded-theory)
- [社会网络分析](/methodologies/sna)
- [行动者网络理论](/methodologies/ant)
- [布迪厄场域分析](/methodologies/bourdieu)

## 定量研究方法

- [QCA](/methodologies/qca)
- [DID](/methodologies/did)
- [回归分析](/methodologies/regression)
- [问卷设计](/methodologies/survey)

## 混合方法与社会理论

- [混合方法研究](/methodologies/mixed-methods)
- [数字马克思分析](/methodologies/digital-marx)
- [数字涂尔干分析](/methodologies/digital-durkheim)
- [数字韦伯分析](/methodologies/digital-weber)

---

*由 SocienceAI 提供*
"""
        
        with open(self.docs_dir / 'methodologies' / 'index.md', 'w', encoding='utf-8') as f:
            f.write(index_content)
        print("  ✅ 方法论索引")
    
    def _generate_about_page(self):
        """生成关于页面"""
        content = """# 关于 SocienceAI

## 我们的使命

通过 AI 技术推动社会科学研究的范式革新，让严谨的社会科学方法论不再高深，让高质量的研究人人可为。

## 核心价值观

1. **学术卓越** - 学术质量是第一追求
2. **社会影响** - 研究必须服务于社会福祉
3. **可及性** - 让方法论人人可为
4. **技术创新** - 用 AI 推动范式革新
5. **伦理责任** - 技术发展遵循伦理规范

## 质量保证

- 所有报告必须经过严格测试和验证
- 绝不夸大、绝不无根据、没测试、没验证时报告
- 分析过程必须可重复，结果必须可验证

## 联系我们

- 网站：http://www.socienceai.com
- 邮箱：contact@socienceai.com

---

*让社会科学研究人人可为*
"""
        
        with open(self.docs_dir / 'about' / 'index.md', 'w', encoding='utf-8') as f:
            f.write(content)
        print("  ✅ 关于页面")
    
    def _convert_to_html(self):
        """转换 Markdown 为 HTML"""
        print("\n🔄 转换 Markdown 为 HTML...")
        
        # 简单转换（实际应该使用 markdown 库）
        for md_file in self.docs_dir.rglob('*.md'):
            html_file = md_file.with_suffix('.html')
            
            # 读取 Markdown
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # 简单转换为 HTML（实际应该使用 markdown 库）
            html_content = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SocienceAI</title>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 40px; line-height: 1.6; }}
        h1, h2, h3 {{ color: #333; }}
        code {{ background: #f4f4f4; padding: 2px 6px; border-radius: 3px; }}
        pre {{ background: #f4f4f4; padding: 15px; border-radius: 5px; overflow-x: auto; }}
    </style>
</head>
<body>
{md_content}
</body>
</html>
"""
            
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"  ✅ {md_file.name} → {html_file.name}")


# ============================================================================
# FTP 上传器
# ============================================================================

class FTPUploader:
    """FTP 上传器"""
    
    def __init__(self, config: Config):
        self.config = config
        self.ftp = FTP()
        self.uploaded_count = 0
        self.failed_count = 0
    
    def upload(self, local_dir, remote_dir='/htdocs'):
        """上传文件到服务器"""
        print("\n" + "="*60)
        print("  SocienceAI FTP 上传器")
        print("="*60)
        
        # 获取 FTP 配置
        host = self.config.get('ftp_host', '103.99.40.226')
        port = self.config.get('ftp_port', 21)
        user = self.config.get('ftp_user', '3njf8mh28i222')
        password = self.config.get('ftp_password', '')
        
        if not password:
            print("\n⚠️ 错误：FTP 密码未配置")
            print("请使用：python cli-anything.py config set ftp_password YOUR_PASSWORD")
            return
        
        # 连接服务器
        if not self._connect(host, port, user, password):
            return
        
        # 上传文件
        self._upload_directory(Path(local_dir), remote_dir)
        
        # 打印摘要
        self._print_summary()
        
        # 关闭连接
        self._close()
    
    def _connect(self, host, port, user, password):
        """连接 FTP 服务器"""
        try:
            print(f"\n📡 连接到 FTP 服务器：{host}:{port}")
            self.ftp.connect(host, port)
            self.ftp.login(user, password)
            print("✅ FTP 连接成功")
            return True
        except Exception as e:
            print(f"❌ FTP 连接失败：{e}")
            return False
    
    def _upload_directory(self, local_dir, remote_dir):
        """上传整个目录"""
        print(f"\n📂 上传目录：{local_dir} → {remote_dir}")
        
        # 确保远程目录存在
        self._ensure_remote_dir(remote_dir)
        
        # 遍历本地目录
        for root, dirs, files in os.walk(local_dir):
            rel_root = Path(root).relative_to(local_dir)
            
            # 创建子目录
            for dir_name in dirs:
                remote_subdir = str(Path(remote_dir) / rel_root / dir_name)
                self._ensure_remote_dir(remote_subdir)
            
            # 上传文件
            for file_name in files:
                local_path = Path(root) / file_name
                remote_subdir = Path(remote_dir) / rel_root
                remote_path = str(remote_subdir / file_name)
                
                print(f"  📄 上传：{file_name}")
                self._upload_file(str(local_path), remote_path)
    
    def _ensure_remote_dir(self, dir_path):
        """确保远程目录存在"""
        if not dir_path or dir_path == '/' or dir_path == '.':
            return
        
        try:
            self.ftp.cwd(dir_path)
            self.ftp.cwd('..')
        except:
            parent = str(Path(dir_path).parent)
            if parent != dir_path:
                self._ensure_remote_dir(parent)
            try:
                self.ftp.mkd(dir_path)
                print(f"  📁 创建目录：{dir_path}")
            except:
                pass
    
    def _upload_file(self, local_path, remote_path):
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
    
    def _print_summary(self):
        """打印上传摘要"""
        print("\n" + "="*60)
        print("📊 上传摘要")
        print("="*60)
        print(f"  成功：{self.uploaded_count} 个文件")
        print(f"  失败：{self.failed_count} 个文件")
        print("="*60)
    
    def _close(self):
        """关闭连接"""
        try:
            self.ftp.quit()
            print("\n✅ FTP 连接已关闭")
        except:
            pass


# ============================================================================
# CLI 主程序
# ============================================================================

class CLI:
    """CLI 主程序"""
    
    def __init__(self):
        self.config = Config()
        self.parser = self._create_parser()
    
    def _create_parser(self):
        """创建参数解析器"""
        parser = argparse.ArgumentParser(
            description='SocienceAI 网站更新 CLI 工具',
            prog='cli-anything'
        )
        
        subparsers = parser.add_subparsers(dest='command', help='可用命令')
        
        # build 命令
        build_parser = subparsers.add_parser('build', help='构建网站')
        build_parser.add_argument('--dir', default='./website', help='输出目录')
        
        # upload 命令
        upload_parser = subparsers.add_parser('upload', help='上传到服务器')
        upload_parser.add_argument('dir', help='本地目录')
        upload_parser.add_argument('--remote', default='/htdocs', help='远程目录')
        
        # update 命令
        update_parser = subparsers.add_parser('update', help='完整更新流程')
        update_parser.add_argument('target', choices=['all', 'content', 'methods', 'blog'],
                                  help='更新目标')
        
        # config 命令
        config_parser = subparsers.add_parser('config', help='配置管理')
        config_subparsers = config_parser.add_subparsers(dest='config_action')
        
        config_set = config_subparsers.add_parser('set', help='设置配置')
        config_set.add_argument('key', help='配置键')
        config_set.add_argument('value', help='配置值')
        
        config_get = config_subparsers.add_parser('get', help='获取配置')
        config_get.add_argument('key', help='配置键')
        
        config_list = config_subparsers.add_parser('list', help='列出所有配置')
        
        # status 命令
        subparsers.add_parser('status', help='查看状态')
        
        # verify 命令
        subparsers.add_parser('verify', help='验证网站')
        subparsers.add_parser('test', help='本地测试')
        
        # backup 命令
        subparsers.add_parser('backup', help='备份线上内容')
        
        # rollback 命令
        subparsers.add_parser('rollback', help='回滚到备份')
        
        # clean 命令
        subparsers.add_parser('clean', help='清理构建文件')
        
        return parser
    
    def run(self, args=None):
        """运行 CLI"""
        parsed_args = self.parser.parse_args(args)
        
        if parsed_args.command == 'build':
            self.cmd_build(parsed_args)
        elif parsed_args.command == 'upload':
            self.cmd_upload(parsed_args)
        elif parsed_args.command == 'update':
            self.cmd_update(parsed_args)
        elif parsed_args.command == 'config':
            self.cmd_config(parsed_args)
        elif parsed_args.command == 'status':
            self.cmd_status()
        elif parsed_args.command == 'verify':
            self.cmd_verify()
        elif parsed_args.command == 'test':
            self.cmd_test()
        elif parsed_args.command == 'backup':
            self.cmd_backup()
        elif parsed_args.command == 'rollback':
            self.cmd_rollback()
        elif parsed_args.command == 'clean':
            self.cmd_clean()
        else:
            self.parser.print_help()
    
    def cmd_build(self, args):
        """build 命令"""
        builder = WebsiteBuilder(args.dir)
        builder.build()
    
    def cmd_upload(self, args):
        """upload 命令"""
        print("\n⚠️ 上传前验证...")
        
        # 1. 先验证
        from verify_website import WebsiteVerifier
        
        verifier = WebsiteVerifier(args.dir)
        success = verifier.verify_all()
        
        if not success:
            print("\n❌ 验证失败！禁止上传，请先修复错误")
            print("\n💡 建议：")
            print("  1. 查看上面的错误列表")
            print("  2. 修复所有错误")
            print("  3. 重新运行：python cli-anything.py verify")
            print("  4. 验证通过后再上传")
            sys.exit(1)
        
        # 2. 确认备份
        print("\n⚠️ 重要提醒：")
        print("  上传前请确保已备份线上内容")
        print("  如需备份，请先运行：python cli-anything.py backup")
        
        response = input("\n是否已备份？(y/n): ")
        if response.lower() != 'y':
            print("\n⚠️ 已取消上传")
            print("💡 请先备份：python cli-anything.py backup")
            return
        
        # 3. 上传
        uploader = FTPUploader(self.config)
        uploader.upload(args.dir, args.remote)
        
        print("\n✅ 上传完成！")
        print("\n📝 下一步:")
        print("  1. 访问 http://www.socienceai.com 验证")
        print("  2. 检查所有页面是否正常")
        print("  3. 如有问题，运行：python cli-anything.py rollback")
    
    def cmd_update(self, args):
        """update 命令"""
        print("\n" + "="*60)
        print("  SocienceAI 完整更新流程")
        print("="*60)
        
        if args.target == 'all':
            # Step 1: 验证
            print("\n🔍 Step 1: 验证本地内容...")
            from verify_website import WebsiteVerifier
            verifier = WebsiteVerifier()
            success = verifier.verify_all()
            
            if not success:
                print("\n❌ 验证失败！禁止上传，请先修复错误")
                return
            
            print("\n✅ 验证通过")
            
            # Step 2: 备份确认
            print("\n💾 Step 2: 备份确认...")
            print("⚠️ 重要：上传前必须备份线上内容")
            response = input("是否已备份？(y/n): ")
            if response.lower() != 'y':
                print("\n⚠️ 请先备份：python cli-anything.py backup")
                return
            
            # Step 3: 构建
            print("\n📦 Step 3: 构建网站...")
            builder = WebsiteBuilder()
            builder.build()
            
            # Step 4: 上传
            print("\n📤 Step 4: 上传到服务器...")
            uploader = FTPUploader(self.config)
            uploader.upload('./website', '/htdocs')
            
            print("\n✅ 完整更新流程完成！")
            print("\n📝 下一步:")
            print("  1. 访问 http://www.socienceai.com 验证")
            print("  2. 检查所有页面是否正常")
            print("  3. 如有问题，运行：python cli-anything.py rollback")
        
        elif args.target in ['content', 'methods', 'blog']:
            # 部分更新也需要验证
            print(f"\n📝 更新 {args.target}...")
            print("⚠️ 部分更新功能待实现")
    
    def cmd_config(self, args):
        """config 命令"""
        if args.config_action == 'set':
            self.config.set(args.key, args.value)
            print(f"✅ 已设置 {args.key} = {args.value}")
        
        elif args.config_action == 'get':
            value = self.config.get(args.key)
            if value is not None:
                print(f"{args.key} = {value}")
            else:
                print(f"⚠️ 配置项 {args.key} 不存在")
        
        elif args.config_action == 'list':
            print("\n当前配置:")
            for key, value in self.config.config.items():
                if 'password' in key.lower():
                    print(f"  {key} = ***")
                else:
                    print(f"  {key} = {value}")
        
        else:
            print("使用：python cli-anything.py config [set|get|list]")
    
    def cmd_status(self):
        """status 命令"""
        print("\n" + "="*60)
        print("  SocienceAI 网站状态")
        print("="*60)
        
        # 检查本地文件
        website_dir = Path('./website')
        if website_dir.exists():
            files = list(website_dir.rglob('*.*'))
            print(f"\n📁 本地文件：{len(files)} 个")
        else:
            print(f"\n⚠️ 本地目录不存在：{website_dir}")
        
        # 检查配置
        print("\n⚙️ 配置状态:")
        if self.config.get('ftp_password'):
            print("  ✅ FTP 密码已配置")
        else:
            print("  ❌ FTP 密码未配置")
        
        # 检查服务器连接
        print("\n📡 服务器连接测试...")
        try:
            ftp = FTP()
            ftp.connect(
                self.config.get('ftp_host', '103.99.40.226'),
                self.config.get('ftp_port', 21)
            )
            ftp.login(
                self.config.get('ftp_user', '3njf8mh28i222'),
                self.config.get('ftp_password', '')
            )
            ftp.quit()
            print("  ✅ 服务器连接正常")
        except:
            print("  ❌ 无法连接到服务器")
        
        print("\n" + "="*60)
    
    def cmd_verify(self):
        """verify 命令"""
        print("\n🔍 验证网站...")
        
        # 导入验证模块
        import importlib.util
        spec = importlib.util.spec_from_file_location("verify_website", "verify-website.py")
        verify_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(verify_module)
        
        verifier = verify_module.WebsiteVerifier()
        success = verifier.verify_all()
        
        if success:
            print("\n✅ 验证通过！可以安全上传")
        else:
            print("\n❌ 验证失败！请先修复错误")
            sys.exit(1)
    
    def cmd_test(self):
        """test 命令"""
        print("\n🧪 启动本地测试服务器...")
        
        import importlib.util
        spec = importlib.util.spec_from_file_location("verify_website", "verify-website.py")
        verify_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(verify_module)
        
        verifier = verify_module.WebsiteVerifier()
        verifier.start_local_server(port=8080)
    
    def cmd_backup(self):
        """backup 命令"""
        print("\n💾 创建线上内容备份...")
        
        # TODO: 实现备份功能
        print("⚠️ 备份功能待实现")
        print("\n临时方案：使用 FTP 客户端手动下载备份")
        print("  1. 连接 FTP: 103.99.40.226:21")
        print("  2. 用户名：3njf8mh28i222")
        print("  3. 密码：[已配置]")
        print("  4. 下载 /htdocs/ 目录到本地 backup/ 目录")
    
    def cmd_rollback(self):
        """rollback 命令"""
        print("\n⚠️ 回滚到备份...")
        
        # TODO: 实现回滚功能
        print("⚠️ 回滚功能待实现")
        print("\n临时方案：使用 FTP 客户端手动上传备份")
        print("  1. 从 backup/ 目录选择要恢复的文件")
        print("  2. 上传到 FTP 服务器 /htdocs/ 目录")
    
    def cmd_clean(self):
        """clean 命令"""
        print("\n🧹 清理构建文件...")
        
        # 删除构建目录
        build_dir = Path('./website')
        if build_dir.exists():
            import shutil
            shutil.rmtree(build_dir)
            print(f"  ✅ 已删除：{build_dir}")
        
        # 删除状态文件
        state_file = Path('./website/build-state.json')
        if state_file.exists():
            state_file.unlink()
            print(f"  ✅ 已删除：{state_file}")
        
        print("\n✅ 清理完成！")


# ============================================================================
# 主程序
# ============================================================================

if __name__ == '__main__':
    cli = CLI()
    cli.run()
