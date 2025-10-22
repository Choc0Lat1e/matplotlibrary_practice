import math
import pandas as pd
from IPython.display import display, HTML, clear_output

def input_int(prompt, default=None):
    while True:
        val = input(prompt).strip()
        if val == "" and default is not None:
            return default
        try:
            n = int(val)
            if n <= 0:
                print("양의 정수를 입력하세요.")
                continue
            return n
        except ValueError:
            print("정수를 입력해주세요.")

def input_score(prompt):
    while True:
        val = input(prompt).strip()
        if val == "":
            print("값을 입력해주세요.")
            continue
        try:
            s = float(val)
            if s < 0 or s > 100:
                print("점수는 0에서 100 사이여야 합니다.")
                continue
            return s
        except ValueError:
            print("숫자로 입력해주세요. 예: 85 또는 92.5")

def main():
    num_students = input_int("학생 수를 입력하세요 (기본 5): ", default=5)
    subj_input = input("과목을 쉼표로 구분하여 입력하세요 (기본: 국어,수학,과학) : ").strip()
    if subj_input == "":
        subjects = ["국어", "수학", "과학"]
    else:
        subjects = [s.strip() for s in subj_input.split(",") if s.strip() != ""]
        if len(subjects) == 0:
            subjects = ["국어", "수학", "과학"]

    rows = []
    for i in range(1, num_students + 1):
        name = input(f"{i}번째 학생 이름: ").strip()
        while name == "":
            print("이름을 비워둘 수 없습니다.")
            name = input(f"{i}번째 학생 이름: ").strip()
        scores = {}
        for subj in subjects:
            scores[subj] = input_score(f"{name}의 {subj} 점수 (0-100): ")
        row = {"이름": name}
        row.update(scores)
        rows.append(row)

    df = pd.DataFrame(rows)
    df["합계"] = df[subjects].sum(axis=1)
    df["평균"] = df[subjects].mean(axis=1)

    subject_stats = df[subjects].agg(["mean", "median", "std"]).T
    subject_stats = subject_stats.rename(columns={"mean": "평균", "median": "중앙값", "std": "표준편차"})
    subject_stats = subject_stats[["평균", "중앙값", "표준편차"]]

    clear_output(wait=True)

    fmt_students = {s: "{:.2f}" for s in subjects}
    fmt_students.update({"합계": "{:.2f}", "평균": "{:.2f}"})
    fmt_stats = {"평균": "{:.2f}", "중앙값": "{:.2f}", "표준편차": "{:.2f}"}

    display(HTML("<h4>학생별 점수 표</h4>"))
    styled_df = df.style.format(fmt_students).set_table_styles([
        {"selector": "th", "props": [("text-align", "center")]},
        {"selector": "td", "props": [("text-align", "center")]}
    ])
    display(styled_df)

    display(HTML("<br><h4>과목별 통계</h4>"))
    styled_stats = subject_stats.style.format(fmt_stats).set_table_styles([
        {"selector": "th", "props": [("text-align", "center")]},
        {"selector": "td", "props": [("text-align", "center")]}
    ])
    display(styled_stats)

if __name__ == "__main__":

    main()
