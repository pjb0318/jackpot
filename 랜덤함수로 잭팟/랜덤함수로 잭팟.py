import random
from pathlib import Path

import pygame

BASE_DIR = Path(__file__).resolve().parent
SCREEN_SIZE = (1920, 1080)
SLOT_POSITIONS = [(280, 200), (735, 200), (1190, 200)]
REVEAL_DELAY_MS = 1000
FPS = 60

SYMBOLS = [
    f"{grade}_{fruit}"
    for grade in ["silver", "golden", "copper"]
    for fruit in ["banana", "cherry", "coin", "watermelon"]
]
# 기존 확률 유지: 일반 그림은 각각 두 번, poop은 한 번.
OTHER_SYMBOLS = SYMBOLS * 2 + ["poop"]


def load_images():
    images = {}
    for name in ["background", "background1", "jackpot", "poop"] + SYMBOLS:
        images[name] = pygame.image.load(BASE_DIR / "image" / f"{name}.png")
    return images


def draw_symbol():
    """슬롯 하나를 추첨한다. jackpot 확률은 1/5이다."""
    if random.choice([0, 1, 1, 1, 1]) == 0:
        return "jackpot"
    return random.choice(OTHER_SYMBOLS)


def draw_screen(screen, images, slots, revealed_count):
    background = "background1" if slots else "background"
    screen.blit(images[background], (0, 0))

    for i in range(revealed_count):
        screen.blit(images[slots[i]], SLOT_POSITIONS[i])


def main():
    pygame.init()
    try:
        screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption("파칭코 게임")
        images = load_images()
        button_click = pygame.mixer.Sound(BASE_DIR / "music" / "buttonclick.wav")
        clock = pygame.time.Clock()

        running = True
        slots = []  # 비어 있으면 시작 화면, 결과가 있으면 게임 화면.
        revealed_count = 0
        next_action_at = None

        while running:
            now = pygame.time.get_ticks()

            # 1초 뒤 슬롯 공개 또는 시작 화면 복귀. 기다리는 동안에도 입력 처리.
            if next_action_at is not None and now >= next_action_at:
                if revealed_count < len(slots):
                    revealed_count += 1
                else:
                    slots = []
                    revealed_count = 0
                next_action_at = None

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                if event.type != pygame.KEYDOWN or event.key != pygame.K_SPACE:
                    continue
                # 공개 대기 중에는 스페이스 중복 입력을 무시한다.
                if next_action_at is not None:
                    continue

                if not slots:
                    slots = [draw_symbol() for _ in SLOT_POSITIONS]
                else:
                    if revealed_count < len(slots):
                        button_click.play()
                    next_action_at = now + REVEAL_DELAY_MS

            if not running:
                break
            draw_screen(screen, images, slots, revealed_count)
            pygame.display.update()
            clock.tick(FPS)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
