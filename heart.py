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
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    x = x / 17.0
    y = y / 17.0

    if style == "solid":
        ax.fill(x, y, color="#e31b23")
    else:
        ax.scatter(x, y, c=y, cmap=cmap, s=8, edgecolors='none', alpha=0.9)

    if edge:
        ax.plot(x, y, color="#7a0b0b", linewidth=2)

    ax.set_aspect("equal")
    ax.axis("off")

def create_arg_parser():
    parser = argparse.ArgumentParser(description="matplotlib으로 하트 그리기")
    parser.add_argument("--save", "-s", default=None,
                        help="이미지를 저장할 파일 경로 (예: heart.png)")
    parser.add_argument("--style", default="gradient", choices=["gradient", "solid"],
                        help="채우기 스타일: gradient(기본) 또는 solid")
    parser.add_argument("--dpi", type=int, default=200, help="저장/출력 해상도 DPI")
    return parser

def main(argv=None):
    parser = create_arg_parser()
    if argv is None:
        args, unknown = parser.parse_known_args()
    else:
        args, unknown = parser.parse_known_args(argv)

    fig, ax = plt.subplots(figsize=(6, 6), facecolor="white")
    draw_heart(ax, style=args.style, edge=True, cmap="Reds")
    plt.tight_layout()

    if args.save:
        fig.savefig(args.save, dpi=args.dpi, bbox_inches="tight", facecolor=fig.get_facecolor())
        print(f"이미지를 저장했습니다: {args.save}")

    plt.show()

if __name__ == "__main__":
    main()
