# ------------------------------------------------------------
# clock.py
# ------------------------------------------------------------
import time
from typing import Optional


class Clock:
    """
    Simple framerate‑controller.

    * `fps` – gewünschte Bildrate (Frames per Second).
    * `frame_time` – intern berechnet als ``1 / fps``.
    * `last_update` – Zeitstempel des letzten gerenderten Frames.
    * `next_update` – optional, kann von außen gesetzt werden, um
      ein sofortiges Rendern zu erzwingen (z. B. nach einem Resize‑Event).

    Die Klasse bietet:
    * ``time_to_render()`` – prüft, ob genug Zeit seit dem letzten Frame vergangen ist.
    * ``reset()`` – setzt den Timer zurück (z. B. beim Spiel‑Start).
    * ``sleep_until_next_frame()`` – schläft den Rest der Frame‑Zeit,
      um die CPU zu entlasten (non‑blocking‑Verhalten).
    """

    def __init__(self, fps: int = 20, start_immediately: bool = True) -> None:
        if fps <= 0:
            raise ValueError("FPS must be > 0")
        self.fps: int = fps
        self.frame_time: float = 1.0 / fps
        self.last_update: float = 0.0
        self.next_update: Optional[float] = None

        if start_immediately:
            # Beim Erzeugen sofort einen gültigen Timestamp setzen,
            # sodass das erste ``time_to_render`` sofort True liefert.
            self.last_update = time.time()

    # -----------------------------------------------------------------
    def reset(self) -> None:
        """Setzt den internen Timer zurück – nützlich beim Neustart des Spiels."""
        self.last_update = time.time()
        self.next_update = None

    # -----------------------------------------------------------------
    def time_to_render(self) -> bool:
        """
        Gibt ``True`` zurück, wenn seit ``last_update`` mindestens
        ``frame_time`` vergangen ist **oder** ``next_update`` gesetzt wurde.
        """
        now = time.time()

        # ``next_update`` kann von außen (z. B. Resize‑Event) gesetzt werden,
        # um ein sofortiges Rendern zu erzwingen.
        if self.next_update is not None:
            if now >= self.next_update:
                self.next_update = None
                self.last_update = now
                return True
            return False

        if now - self.last_update >= self.frame_time:
            self.last_update = now
            return True
        return False

    # -----------------------------------------------------------------
    def force_next_frame(self, delay: float = 0.0) -> None:
        """
        Erzwingt, dass das nächste ``time_to_render`` nach ``delay`` Sekunden
        True zurückgibt.  ``delay=0`` bedeutet „sofort rendern“.
        """
        self.next_update = time.time() + delay

    # -----------------------------------------------------------------
    def sleep_until_next_frame(self) -> None:
        """
        Blockiert nur den Rest der aktuellen Frame‑Zeit.
        Aufruf am Ende einer Loop‑Iteration, um die CPU‑Auslastung zu reduzieren.
        """
        now = time.time()
        remaining = self.frame_time - (now - self.last_update)
        if remaining > 0:
            time.sleep(remaining)

    # -----------------------------------------------------------------
    # Convenience‑Properties (optional, aber praktisch)
    # -----------------------------------------------------------------
    @property
    def fps_lock(self) -> int:
        """Alias für ``fps`` – bleibt aus Kompatibilitätsgründen erhalten."""
        return self.fps

    @property
    def frame_time_seconds(self) -> float:
        """Alias für ``frame_time``."""
        return self.frame_time
