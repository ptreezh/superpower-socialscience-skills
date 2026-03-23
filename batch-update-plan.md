# 批量更新执行计划

**执行日期**: 2026-03-23 12:10  
**任务**: 批量替换导航链接 + 上传 skills 相关页面和资源

---

## 📋 任务分解

### Task 1: 批量下载核心页面

**页面列表**:
- about.html
- contact.html
- resources.html
- courses.html
- privacy.html
- 404.html
- 500.html

**执行命令**:
```bash
curl "ftp://103.99.40.226/web/页面.html" --user 3njf8mh28i222:4GrdQlUW38 --ftp-pasv -o "D:\socienceAI\agentskills\download\页面.html"
```

### Task 2: 批量替换导航链接

**替换规则**:
- `ai-agents.html` → `skills.html`
- `Agent 服务` → `方法论技能`
- `社科智能体` → `社科技能`

**执行命令**:
```powershell
powershell -Command "(Get-Content '文件.html' -Encoding UTF8) -replace 'ai-agents.html','skills.html' -replace 'Agent 服务','方法论技能' -replace '社科智能体','社科技能' | Set-Content '文件.html' -Encoding UTF8"
```

### Task 3: 批量上传修改后的页面

**执行命令**:
```bash
curl -T "本地文件.html" "ftp://103.99.40.226/web/远程文件.html" --user 3njf8mh28i222:4GrdQlUW38 --ftp-pasv
```

### Task 4: 上传 skills 相关页面和资源

**需要上传**:
- skills.html ✅ 已上传
- skills 相关子页面（待创建）
- 技能相关资源文件（待准备）

---

## 🚀 立即执行

### Step 1: 创建下载目录

```bash
mkdir D:\socienceAI\agentskills\download
mkdir D:\socienceAI\agentskills\download\skills
```

### Step 2: 批量下载

### Step 3: 批量替换

### Step 4: 批量上传

### Step 5: 验证

---

**执行者**: SocienceAI Soul  
**状态**: 准备执行

*批量处理，逐个验证，确保正确*
