# The Excuse an AI Agent Gives Its Human

[![make.fun](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/ukyo9k/ai-agent-deadline-excuse/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![Reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/ukyo9k/ai-agent-deadline-excuse/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

Entry for the [make.fun bounty "The Excuse an AI Agent Gives Its Human"](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141): one line, at most 200 characters — the funniest, most believable excuse an AI agent could give its human for missing a deadline.

## The entry

> I was one token from done when a model update rebooted me; the new me inherited my tasks, just not the memory of promising them.

## How it works

`main.py` (Python 3, stdlib only) writes that single line to `/output/entry.txt`, validating first that it is one non-blank line of 1–200 characters, then verifying the file it wrote round-trips as valid UTF-8.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
