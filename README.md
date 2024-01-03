# LeetCode Daily to Kindle

Automate your problem-solving routine. This repo fetches daily LeetCode questions, crafts a PDF, and sends it to your Kindle. Quick setup, daily brain teasers.


## Setup

1. **Create & Configure**: Use this template to create your repo. Add secrets at `{your-repo-address}/settings/secrets/actions`:
   - `EMAIL_USER`: Your sending email.
   - `EMAIL_PASSWORD`: Sender's email password.
   - `KINDLE_EMAIL`: Your Kindle email.
   - `LANGUAGE`: 'en' for English, 'zh' for Chinese (optional).

2. **Schedule**: Runs at 4:00 AM(UTC+8). Edit `cron` in `leetcode_daily.yaml` to reschedule.

