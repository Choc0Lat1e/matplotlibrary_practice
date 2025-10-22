# matplotlib로 하트 모양을 그리는 간단한 스크립트
# 실행: python heart_plot.py
# --save PATH 옵션으로 이미지를 파일로 저장할 수 있습니다. 예: python heart_plot.py --save heart.png

import numpy as np
import matplotlib.pyplot as plt
import argparse

def draw_heart(ax, style="gradient", edge=True, cmap="Reds"):
    """
    하트 곡선을 그리고 채우기(그라데이션 또는 단색)를 합니다.
    style: "gradient" or "solid"
    edge: 외곽선 표시 여부
    """
    t = np.linspace(0, 2 * np.pi, 2000)
    # 고전적인 하트형 파라메트릭 방정식
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    # 축 크기에 맞게 약간 스케일 조정 (선택 사항)
    x = x / 17.0
    y = y / 17.0

    if style == "solid":
        ax.fill(x, y, color="#e31b23")  # 진한 빨강 단색
    else:
        # 그라데이션: 점들을 y값 기준 컬러맵으로 채움
        # 더 부드러운 그라데이션을 위해 많은 점을 찍음
        points = np.vstack((x, y)).T
        # 색상 값을 y에 따라 정렬하면 위쪽이 밝게, 아래쪽이 진하게 보임
        sc = ax.scatter(x, y, c=y, cmap=cmap, s=8, edgecolors='none', alpha=0.9)

    if edge:
        ax.plot(x, y, color="#7a0b0b", linewidth=2)

    # 예쁘게 보이도록 축 정리
    ax.set_aspect("equal")
    ax.axis("off")

def main():
    parser = argparse.ArgumentParser(description="matplotlib으로 하트 그리기")
    parser.add_argument("--save", "-s", default=None,
                        help="이미지를 저장할 파일 경로 (예: heart.png)")
    parser.add_argument("--style", default="gradient", choices=["gradient", "solid"],
                        help="채우기 스타일: gradient(기본) 또는 solid")
    parser.add_argument("--dpi", type=int, default=200, help="저장/출력 해상도 DPI")
    args = parser.parse_args()

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    draw_heart(ax, style=args.style, edge=True, cmap="Reds")

    # 제목을 넣고 싶으면 아래 주석 해제
    # ax.set_title("Love", fontsize=20, fontweight="bold")

    plt.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=args.dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"이미지를 저장했습니다: {args.save}")

    plt.show()

if __name__ == "__main__":
    main()
