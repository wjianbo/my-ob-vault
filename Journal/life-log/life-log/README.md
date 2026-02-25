# Life Log System

This folder stores Jianbo's running life log collected via chat with Claw. All records stay local.

## Structure

- `records/` – Raw chronological entries captured from chat (`YYYY-MM-DD.md`).
- `reports/daily/` – AI-generated daily journals (`YYYY-MM-DD.md`).
- `reports/weekly/` – Weekly reports (`YYYY-WW.md`).
- `reports/monthly/` – Monthly reports (`YYYY-MM.md`).
- `reports/annual/` – Annual reports (`YYYY.md`).
- `categories/` – Rolling category notebooks for quick lookup.
  - `categories/finances.md` – 收支明细 (income & expenses).
  - `categories/writing-themes.md` – 值得继续的写作主题。
  - `categories/todos.md` – 待办事项（含状态标记）。
  - `categories/habits.md` – 习惯跟踪与备注。

## Workflow

1. Jianbo drops notes here in chat. Claw files them immediately into the current day's record and updates category notebooks as needed.
2. At 22:00 Asia/Tokyo every day, Claw assembles the day's record into a structured daily journal and saves it under `reports/daily/` while replying with a summary.
3. On Mondays (covering the previous week), the first day of each month, and the first day of each year, Claw produces weekly, monthly, and annual syntheses respectively. All reports include references back to source entries.

## Categories Format

Each category file is Markdown with dated bullet entries. For example:

```markdown
## 2026-02-13
- [Type] Description (metadata)
```

Todos use checkboxes (`- [ ] task` / `- [x] task`). Habits include quick metrics or observations per day.

## Automation Schedule

- Daily journal: 22:00 JST in main chat.
- Weekly report: Mondays 08:30 JST covering previous Monday–Sunday.
- Monthly report: 1st of each month at 09:00 JST.
- Annual report: January 1st at 10:00 JST.

(Actual cron jobs are defined via OpenClaw `cron` once Jianbo confirms.)

---

Feel free to adjust categories or schedule anytime—just tell Claw.

## 更新规则（2026-02-14）
1. 即刻输入仅做追加：不读取旧文件、不进行分类、不写总结，只在相应记录文件末尾 append 并回复确认。
2. 日报生成仅读取当天 `records/` 文件；
3. 周报生成仅读取上周 7 天的日报（`reports/daily/`），不再触碰原始记录；
4. 月报仅基于上月周报；
5. 年报仅基于上一年月报。

## 日报补充规则（2026-02-23）
- 生成日报前，先在 Obsidian vault 下执行 `git pull`。
- 若 `git pull` 发现有内容更新（拉取变更），将新增内容并入当日日报。
- 若更新内容为较长文章，只提取标题与简介即可。
