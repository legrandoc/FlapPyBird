import pygame
import pytest

from src.utils.utils import clamp, get_hit_mask, memoize, pixel_collision


@pytest.fixture(autouse=True)
def setup_pygame():
    pygame.init()
    yield
    pygame.quit()


def test_clamp():
    # Test integer values
    assert clamp(5, 0, 10) == 5  # Within range
    assert clamp(-1, 0, 10) == 0  # Below min
    assert clamp(11, 0, 10) == 10  # Above max

    # Test float values
    assert clamp(5.5, 1.1, 7.7) == 5.5  # Within range
    assert clamp(0.5, 1.1, 7.7) == 1.1  # Below min
    assert clamp(8.8, 1.1, 7.7) == 7.7  # Above max

    # Test equal bounds
    assert clamp(5, 5, 5) == 5

    # Test when min > max (should still work by returning min)
    assert clamp(5, 10, 0) == 10


def test_memoize():
    call_count = 0

    @memoize
    def expensive_function(x, y, *, keyword=None):
        nonlocal call_count
        call_count += 1
        return x + y if keyword is None else x + y + keyword

    # Test with positional arguments
    assert expensive_function(2, 3) == 5
    assert call_count == 1

    # Test cache hit with same args
    assert expensive_function(2, 3) == 5
    assert call_count == 1

    # Test with different args
    assert expensive_function(3, 4) == 7
    assert call_count == 2

    # Test with keyword arguments
    assert expensive_function(2, 3, keyword=1) == 6
    assert call_count == 3

    # Test cache hit with same keyword args
    assert expensive_function(2, 3, keyword=1) == 6
    assert call_count == 3


@pytest.fixture
def mock_surface():
    surface = pygame.Surface((2, 2), pygame.SRCALPHA)
    surface.set_at((0, 0), (255, 255, 255, 255))  # Opaque
    surface.set_at((0, 1), (255, 255, 255, 0))  # Transparent
    surface.set_at((1, 0), (255, 255, 255, 0))  # Transparent
    surface.set_at((1, 1), (255, 255, 255, 255))  # Opaque
    return surface


def test_get_hit_mask(mock_surface):
    hit_mask = get_hit_mask(mock_surface)

    # Test dimensions
    assert len(hit_mask) == 2
    assert len(hit_mask[0]) == 2

    # Test mask values
    assert hit_mask[0][0] is True  # Top-left opaque
    assert hit_mask[0][1] is False  # Bottom-left transparent
    assert hit_mask[1][0] is False  # Top-right transparent
    assert hit_mask[1][1] is True  # Bottom-right opaque

    # Test memoization
    assert get_hit_mask(mock_surface) is hit_mask  # Should return same object


def test_pixel_collision():
    # Create test hit masks
    hitmask1 = [[True, False], [False, True]]
    hitmask2 = [[True, True], [False, False]]

    # Test complete overlap with collision
    rect1 = pygame.Rect(0, 0, 2, 2)
    rect2 = pygame.Rect(0, 0, 2, 2)
    assert pixel_collision(rect1, rect2, hitmask1, hitmask2) is True

    # Test no overlap
    rect2 = pygame.Rect(10, 10, 2, 2)
    assert pixel_collision(rect1, rect2, hitmask1, hitmask2) is False

    # Test partial overlap with no pixel collision
    rect2 = pygame.Rect(1, 1, 2, 2)
    hitmask2 = [[False, False], [False, False]]
    assert pixel_collision(rect1, rect2, hitmask1, hitmask2) is False

    # Test edge case: zero width overlap
    rect2 = pygame.Rect(2, 0, 2, 2)
    assert pixel_collision(rect1, rect2, hitmask1, hitmask2) is False

    # Test edge case: zero height overlap
    rect2 = pygame.Rect(0, 2, 2, 2)
    assert pixel_collision(rect1, rect2, hitmask1, hitmask2) is False


if __name__ == "__main__":
    pytest.main([__file__])
