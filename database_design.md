# Supabase 数据库设计 - pet-five 内容管理系统

## 1. posts 表（文章）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | uuid (自动) | 主键 |
| title | text | 文章标题 |
| slug | text (唯一) | URL友好名，如 arthritis-care-tips |
| content | text | 文章正文（Markdown格式） |
| summary | text | 摘要，用于列表页展示 |
| category | text | 病例分类：arthritis / hip-dysplasia / cataracts |
| is_featured | boolean | 是否置顶 |
| published_at | timestamp | 发布时间 |
| created_at | timestamp (自动) | 创建时间 |

## 2. affiliate_links 表（联盟营销链接）
| 字段 | 类型 | 说明 |
|------|------|------|
| id | uuid (自动) | 主键 |
| post_id | uuid (外键→posts) | 关联文章 |
| placeholder | text | 占位符，如 joint-supplement |
| anchor_text | text | 锚文本，如 "最佳关节保健品" |
| url | text | 联盟链接URL（可后期填入） |
| is_active | boolean | 是否启用 |
| created_at | timestamp (自动) | |

## 3. 联盟链接热替换原理
文章内容中写 `[aff:joint-supplement]`
→ 系统自动查找 affiliate_links 表
→ 替换为 `<a href="URL">锚文本</a>`
→ 后期只改链接表，所有文章自动更新

## 4. API接口（Supabase自动生成）
- GET /posts → 获取文章列表
- GET /posts?id=eq.xxx → 获取单篇文章
- POST /posts → 创建文章
- PATCH /posts?id=eq.xxx → 更新文章
- DELETE /posts?id=eq.xxx → 删除文章
