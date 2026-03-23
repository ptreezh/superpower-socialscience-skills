# 创建 GitHub 仓库 - 分步操作指南

**目标**: 使用 `ptreezh` 账号创建 `superpower-socialscience-skills` 仓库

---

## 📋 准备工作

### 1. 确认登录状态

**检查是否已登录 GitHub**:
1. 打开浏览器
2. 访问：https://github.com
3. 右上角应显示 `ptreezh` 头像

**如未登录**:
1. 访问：https://github.com/login
2. 输入 `ptreezh` 账号密码
3. 登录

---

## 🚀 创建仓库（3 分钟）

### 步骤 1: 打开创建页面

**访问**: https://github.com/new

或直接：
1. 打开 GitHub 首页
2. 点击右上角 **+** 按钮
3. 选择 **New repository**

### 步骤 2: 填写仓库信息

**Repository name**:
```
superpower-socialscience-skills
```

**Description**:
```
60 种社会科学方法论技能包 - SocienceAI

包含：
- 质性研究方法 (20 个)
- 定量研究方法 (15 个)
- 混合方法与商业分析 (25 个)

每个技能包包含 SKILL.md, skill.yaml, tools/, templates/

网站：http://www.socienceai.com
```

**Visibility**:
- ✅ **Public** (公开可见)

**Initialize this repository with**:
- ❌ **不要勾选** (我们已有本地代码)

### 步骤 3: 创建仓库

点击绿色按钮：**Create repository**

创建成功后会看到：
```
Quick setup
git remote add origin https://github.com/ptreezh/superpower-socialscience-skills.git
```

---

## 📤 推送代码（2 分钟）

### 方法 1: 使用命令行（推荐）

**打开命令提示符**:
```bash
cd D:\socienceAI\agentskills
```

**执行以下命令**:

```bash
# 1. 初始化 Git（如已执行可跳过）
git init

# 2. 添加所有文件
git add .

# 3. 提交
git commit -m "Initial commit: 60 种社会科学方法论技能包"

# 4. 添加远程仓库
git remote add origin https://github.com/ptreezh/superpower-socialscience-skills.git

# 5. 重命名分支为 main
git branch -M main

# 6. 推送到 GitHub
git push -u origin main
```

**输入凭证**:
- 如提示输入密码，使用 GitHub Personal Access Token
- 或配置 SSH key

### 方法 2: 使用批处理脚本

**执行脚本**:
```bash
cd D:\socienceAI\agentskills
create-github-repo.bat
```

脚本会自动：
1. 初始化 Git
2. 添加所有文件
3. 提交
4. 配置远程仓库
5. 重命名分支

**然后手动执行**:
```bash
git push -u origin main
```

### 方法 3: 使用 GitHub Desktop

**步骤**:
1. 打开 GitHub Desktop
2. 使用 `ptreezh` 账号登录
3. **File** → **Add Local Repository**
4. 选择：`D:\socienceAI\agentskills`
5. 点击 **Add repository**
6. 点击 **Publish repository**
7. 填写：
   - Name: `superpower-socialscience-skills`
   - Description: `60 种社会科学方法论技能包`
8. 点击 **Publish repository**

---

## ✅ 验证推送成功

### 检查仓库页面

**访问**: https://github.com/ptreezh/superpower-socialscience-skills

**应看到**:
- ✅ README.md 文件
- ✅ 60 个技能包目录
- ✅ 最近提交记录

### 检查文件结构

**应包含**:
```
superpower-socialscience-skills/
├── README.md
├── grounded-theory-expert/
├── social-network-analysis-expert/
├── qca-analysis-expert/
├── did-analysis-expert/
├── ... (60 个技能包)
└── ...
```

---

## 🔧 常见问题

### 问题 1: 推送失败 - 认证错误

**错误信息**:
```
remote: Support for password authentication was removed on August 13, 2021.
```

**解决**:

**方案 A: 使用 Personal Access Token**
1. 访问：https://github.com/settings/tokens
2. 点击 **Generate new token**
3. 填写描述
4. 勾选 **repo** 权限
5. 点击 **Generate token**
6. 复制 token
7. 推送时使用 token 作为密码

**方案 B: 配置 SSH**
```bash
# 生成 SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# 添加 SSH key 到 GitHub
# 访问：https://github.com/settings/ssh/new
# 复制 ~/.ssh/id_ed25519.pub 内容

# 测试连接
ssh -T git@github.com
```

### 问题 2: 仓库已存在

**错误**: 仓库名已被使用

**解决**:
1. 访问：https://github.com/ptreezh
2. 查找是否已有该仓库
3. 如有，删除或重命名
4. 或改用其他仓库名

### 问题 3: 文件太大

**错误**:
```
remote: error: File xxx is 150.00 MB; this exceeds GitHub's file size limit
```

**解决**:
```bash
# 检查大文件
git rev-parse HEAD | xargs git ls-tree -r | awk '$3 > 10485760 { print $4 }'

# 删除大文件
git filter-branch --force --index-filter \
  'git rm --cached --ignore-unmatch PATH/TO/LARGE-FILE' \
  --prune-empty --tag-name-filter cat -- --all

# 清理
git reflog expire --expire=now --all
git gc --prune=now --aggressive

# 强制推送
git push origin main --force
```

---

## 📊 预期结果

### 仓库信息

**URL**: https://github.com/ptreezh/superpower-socialscience-skills

**名称**: `superpower-socialscience-skills`

**描述**: `60 种社会科学方法论技能包 - SocienceAI`

**可见性**: Public

**文件数**: 约 2000+ 个

**大小**: 约 50-100 MB

---

## 📞 推送后行动

### 1. 更新 README

**添加内容**:
- 技能包列表
- 使用说明
- 网站链接

### 2. 更新网站

**修改 skills.html**:
- 添加 GitHub 下载链接
- 修改下载按钮指向

### 3. 分享

**分享链接**:
- Twitter
- LinkedIn
- 学术社区
- 微信群

---

## 📋 检查清单

### 推送前

- [ ] Git 已初始化
- [ ] 所有文件已添加 (`git add .`)
- [ ] 已提交 (`git commit -m "..."`)
- [ ] 远程仓库已配置
- [ ] 分支名为 `main`

### 推送后

- [ ] 仓库页面可访问
- [ ] 文件完整
- [ ] README 正确显示
- [ ] 所有技能包目录可见

---

**创建日期**: 2026-03-23 22:00  
**执行者**: SocienceAI Soul  
**状态**: 等待手动创建

*按步骤操作，5 分钟完成*
