"""쉬운 한국어 규칙 실험 측정기. 사용: python3 -I measure.py <dir> [<dir> ...]  -> JSON 출력"""
import json
import re
import sys
from pathlib import Path

TRANSLATIONESE = {
    "를/을 통해": r"[을를]\s?통해|통한",
    "에 대해/대한": r"에\s?대[해한]",
    "에 있어(서)": r"에\s?있어",
    "로 인해": r"으?로\s?인[해한]",
    "을 가지다": r"[을를]\s?가지[고는며]|가지고\s?있",
    "되어지다": r"되어지|되어진",
    "것이 중요/좋다": r"것이\s?(중요|좋|권장)",
    "필요가 있다": r"필요가\s?있|주의가\s?필요",
    "것으로 보/파악/판단/기대": r"것으로\s?(보|파악|판단|기대|예상)",
    "이러한/그러한/해당": r"이러한|그러한|해당",
}
SINO_VERBS = r"(수행|진행|활용|제공|발생|존재|위치|실시|생성|방지|확보|보장|절감)(하|했|합|되|된|됩|함|을|를|이|\b)"
EMPHASIS = r"매우|핵심|획기적|체계적|효율적|원활|다양한|강력|혁신|극대화|크게|반드시|근본적"
OPENER_CLOSER = r"좋은 질문|물론입니다|도움이 되셨|궁금한 점이 있|언제든지?\s?말씀"
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")


def strip_code(text):
    return re.sub(r"`[^`]*`", "CODE", text)


def sentences(text):
    out = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        line = re.sub(r"^(#+|[-*]|\d+\.)\s*", "", line)
        line = line.replace("**", "")
        for s in re.split(r"(?<=[.!?。])\s+", line):
            s = s.strip()
            if len(s) >= 2:
                out.append(s)
    return out


def facts(text):
    code = set(re.findall(r"`([^`]+)`", text))
    nums = set(re.findall(r"\d[\d,:.]*\d|\d", text))
    return code | nums


def measure(path):
    raw = Path(path).read_text(encoding="utf-8")
    t = strip_code(raw)
    sents = sentences(t)
    lens = [len(s) for s in sents]
    lines = raw.splitlines()
    m = {
        "file": Path(path).name,
        "chars": len(re.sub(r"\s", "", raw)),
        "sentences": len(sents),
        "avg_len": round(sum(lens) / len(lens), 1) if lens else 0,
        "max_len": max(lens) if lens else 0,
        "over60": sum(1 for x in lens if x > 60),
        "bold": raw.count("**") // 2,
        "bullets": sum(1 for l in lines if re.match(r"^\s*([-*]|\d+\.)\s", l)),
        "headers": sum(1 for l in lines if re.match(r"^#+\s", l)),
        "emoji": len(EMOJI.findall(raw)),
        "emdash": raw.count("—"),
        "opener_closer": len(re.findall(OPENER_CLOSER, t)),
        "emphasis": len(re.findall(EMPHASIS, t)),
        "sino_verbs": len(re.findall(SINO_VERBS, t)),
        "jeok": len(re.findall(r"[가-힣]적(인|으로|이)", t)),
    }
    tr = {k: len(re.findall(v, t)) for k, v in TRANSLATIONESE.items()}
    m["translationese"] = sum(tr.values())
    m["translationese_detail"] = tr
    m["facts"] = sorted(facts(raw))
    return m


if __name__ == "__main__":
    res = {}
    for d in sys.argv[1:]:
        res[Path(d).name] = [measure(p) for p in sorted(Path(d).glob("*.md"))]
    print(json.dumps(res, ensure_ascii=False, indent=1))
