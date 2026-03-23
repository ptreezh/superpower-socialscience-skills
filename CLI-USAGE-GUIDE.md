# SocienceAI CLI 使用指南

> 🔴 **统一命令行接口 - 网站建设和更新**

**版本**: 1.0.0
**更新日期**: 2026-03-22

---

## 📋 快速开始

### 安装

无需安装，直接运行：

```bash
cd D:\socienceAI\agentskills
python cli-anything.py --help
```

### 首次配置

**设置 FTP 密码**（必须）:
```bash
# Windows (PowerShell)
python cli-anything.py config set ftp_password 4GrdQlUW38

# Linux/Mac
python cli-anything.py config set ftp_password 4GrdQlUW38
```

**验证配置**:
```bash
python cli-anything.py config list
```

---

## 🎯 核心命令

### 1. build - 构建网站

**功能**: 生成本地网站文件

```bash
# 构建网站（默认输出到 ./website）
python cli-anything.py build

# 指定输出目录
python cli-anything.py build --dir ./my-website
```

**输出**:
```
📁 创建目录结构...
  ✅ website/
  ✅ website/docs/
  ✅ website/docs/.vitepress/
  ✅ website/docs/methodologies/
  ...

📄 生成页面内容...
  ✅ 首页
  ✅ 扎根理论
  ✅ 社会网络分析
  ...

🔄 转换 Markdown 为 HTML...
  ✅ index.md → index.html
  ...

✅ 网站构建完成！
```

### 2. upload - 上传到服务器

**功能**: 将本地文件上传到 FTP 服务器

```bash
# 上传整个网站
python cli-anything.py upload ./website

# 上传到指定远程目录
python cli-anything.py upload ./website --remote /htdocs/new-content

# 上传特定目录
python cli-anything.py upload ./website/docs/methodologies --remote /htdocs/methods
```

**输出**:
```
📡 连接到 FTP 服务器：103.99.40.226:21
✅ FTP 连接成功

📂 上传目录：website → /htdocs
  📁 创建目录：/htdocs/docs
  📄 上传：index.html
  📄 上传：index.md
  ...

📊 上传摘要
============================================================
  成功：50 个文件
  失败：0 个文件
============================================================

✅ FTP 连接已关闭
```

### 3. update - 完整更新流程

**功能**: 构建 + 上传一站式完成

```bash
# 完整更新所有内容
python cli-anything.py update all

# 只更新内容
python cli-anything.py update content

# 只更新方法论
python cli-anything.py update methods

# 只更新博客
python cli-anything.py update blog
```

**输出**:
```
============================================================
  SocienceAI 完整更新流程
============================================================

📦 Step 1: 构建网站...
[构建输出]

📤 Step 2: 上传到服务器...
[上传输出]

✅ 完整更新流程完成！
```

### 4. status - 查看状态

**功能**: 检查本地和服务器状态

```bash
python cli-anything.py status
```

**输出**:
```
============================================================
  SocienceAI 网站状态
============================================================

📁 本地文件：150 个

⚙️ 配置状态:
  ✅ FTP 密码已配置

📡 服务器连接测试...
  ✅ 服务器连接正常

============================================================
```

### 5. config - 配置管理

**功能**: 管理 CLI 配置

```bash
# 设置配置
python cli-anything.py config set ftp_password YOUR_PASSWORD
python cli-anything.py config set ftp_host 103.99.40.226

# 获取配置
python cli-anything.py config get ftp_password
python cli-anything.py config get ftp_host

# 列出所有配置
python cli-anything.py config list
```

### 6. clean - 清理构建文件

**功能**: 删除构建生成的文件

```bash
python cli-anything.py clean
```

---

## 📚 使用场景

### 场景 1: 首次建站

```bash
# 1. 配置 FTP
python cli-anything.py config set ftp_password 4GrdQlUW38

# 2. 构建网站
python cli-anything.py build

# 3. 上传到服务器
python cli-anything.py upload ./website

# 4. 验证
访问 http://www.socienceai.com
```

### 场景 2: 日常更新

```bash
# 一键完成构建和上传
python cli-anything.py update all
```

### 场景 3: 部分更新

```bash
# 只更新方法论页面
python cli-anything.py update methods

# 只上传特定目录
python cli-anything.py upload ./website/docs/blog --remote /htdocs/blog
```

### 场景 4: 检查状态

```bash
# 检查本地和服务器状态
python cli-anything.py status
```

---

## 🔧 高级用法

### 环境变量配置

也可以使用环境变量配置：

```bash
# Windows (PowerShell)
$env:FTP_PASSWORD="4GrdQlUW38"
$env:FTP_HOST="103.99.40.226"
$env:FTP_USER="3njf8mh28i222"
$env:FTP_PORT="21"
$env:FTP_REMOTE_DIR="/htdocs"

python cli-anything.py upload ./website

# Linux/Mac
export FTP_PASSWORD="4GrdQlUW38"
export FTP_HOST="103.99.40.226"
export FTP_USER="3njf8mh28i222"
export FTP_PORT="21"
export FTP_REMOTE_DIR="/htdocs"

python cli-anything.py upload ./website
```

### 批处理脚本

**Windows 批处理** (`update.bat`):
```batch
@echo off
echo Updating SocienceAI website...
python cli-anything.py update all
pause
```

**Linux/Mac Shell** (`update.sh`):
```bash
#!/bin/bash
echo "Updating SocienceAI website..."
python cli-anything.py update all
```

### 定时任务

**Windows 任务计划程序**:
```batch
# 每天凌晨 2 点自动更新
0 2 * * * python cli-anything.py update all
```

**Linux Cron**:
```bash
# 编辑 crontab
crontab -e

# 添加每日更新任务
0 2 * * * cd /path/to/agentskills && python cli-anything.py update all
```

---

## 📊 完整命令参考

### 命令列表

| 命令 | 说明 | 示例 |
|------|------|------|
| `build` | 构建网站 | `python cli-anything.py build` |
| `upload` | 上传文件 | `python cli-anything.py upload ./website` |
| `update` | 完整更新 | `python cli-anything.py update all` |
| `status` | 查看状态 | `python cli-anything.py status` |
| `config` | 配置管理 | `python cli-anything.py config set key value` |
| `clean` | 清理文件 | `python cli-anything.py clean` |
| `help` | 显示帮助 | `python cli-anything.py --help` |

### 配置项列表

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `ftp_host` | FTP 服务器地址 | 103.99.40.226 |
| `ftp_port` | FTP 端口 | 21 |
| `ftp_user` | FTP 用户名 | 3njf8mh28i222 |
| `ftp_password` | FTP 密码 | (空) |
| `ftp_remote_dir` | 远程目录 | /htdocs |

---

## ⚠️ 注意事项

### 安全提醒

1. **密码保护**
   - 不要在代码中硬编码密码
   - 使用 `config set` 命令设置
   - 或使用环境变量

2. **备份**
   - 更新前备份线上内容
   - 保留回滚能力

3. **验证**
   - 上传后验证文件完整性
   - 检查网站功能正常

### 常见问题

**Q: FTP 密码未配置？**
```bash
python cli-anything.py config set ftp_password YOUR_PASSWORD
```

**Q: 无法连接到服务器？**
```bash
# 检查网络连接
ping 103.99.40.226

# 检查配置
python cli-anything.py config list

# 测试连接
python cli-anything.py status
```

**Q: 上传失败？**
```bash
# 检查文件权限
# 检查远程目录是否存在
# 查看错误信息
```

---

## 📞 故障排查

### 错误代码

| 错误 | 原因 | 解决方案 |
|------|------|---------|
| `FTP 密码未配置` | 未设置密码 | `config set ftp_password` |
| `连接失败` | 网络问题 | 检查网络连接 |
| `权限拒绝` | 文件权限 | 检查 FTP 用户权限 |
| `文件不存在` | 路径错误 | 检查文件路径 |

### 调试模式

启用详细日志：

```bash
# Windows
set DEBUG=1
python cli-anything.py update all

# Linux/Mac
export DEBUG=1
python cli-anything.py update all
```

---

## 📚 相关文档

- [WEBSITE-UPDATE-PLAN.md](WEBSITE-UPDATE-PLAN.md) - 详细更新计划
- [QUICK-EXECUTION-GUIDE.md](QUICK-EXECUTION-GUIDE.md) - 快速执行指南
- [VPS-ACCOUNT-INFO.md](VPS-ACCOUNT-INFO.md) - 账户信息管理

---

**版本**: 1.0.0
**更新日期**: 2026-03-22
**维护**: SocienceAI Team

*让社会科学研究人人可为*
