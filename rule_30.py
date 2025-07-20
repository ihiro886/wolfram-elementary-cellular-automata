import pygame
import sys

# Rule 30のルールを定義
def rule30(left, center, right):
    pattern = (left << 2) | (center << 1) | right
    return (0b00011110 >> pattern) & 1  # Rule 30のビットマスク

# メイン関数
def main(steps=float('inf')):  # ステップ数をパラメータで指定可能（デフォルト無制限）
    width = 1600  # 幅を広くして境界影響を遅らせる
    height = 600
    cell_size = 1  # 各セルのサイズ（ピクセル）

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Rule 30 Cellular Automaton')

    # 初期状態: 幅の中央に1を置く
    cells = [0] * width
    cells[width // 2] = 1

    clock = pygame.time.Clock()
    y = 0  # 開始行を画面の上端に設定

    screen.fill((255, 255, 255))  # 画面を白でクリア

    step_count = 0
    running = True
    while running and step_count < steps:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 現在の行を描画（初期状態を含む）
        for x in range(width):
            if cells[x] == 1:
                pygame.draw.rect(screen, (0, 0, 0), (x * cell_size, y * cell_size, cell_size, cell_size))

        # 新しい行を計算
        new_cells = [0] * width
        for x in range(1, width - 1):
            new_cells[x] = rule30(cells[x-1], cells[x], cells[x+1])
        # 端は0とする
        new_cells[0] = rule30(0, cells[0], cells[1])
        new_cells[width-1] = rule30(cells[width-2], cells[width-1], 0)

        cells = new_cells
        y = (y + 1) % height  # 次行を下に移動、画面端でループ

        if y == 0:  # 上端に戻ったら画面をクリア（ループ時）
            screen.fill((255, 255, 255))

        pygame.display.flip()
        clock.tick(60)  # フレームレート

        step_count += 1

    # ステップ数終了後、ウィンドウを閉じないよう待機
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main(steps=599)
