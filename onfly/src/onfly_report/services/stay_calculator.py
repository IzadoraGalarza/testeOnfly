"""Cálculo de noites ocupadas."""

from __future__ import annotations

from datetime import date


def calculate_room_nights(checkin: date, checkout: date, rooms: int) -> int:
    """Calcula noites de quarto: diferença de dias (não inclusiva) vezes quartos."""
    return (checkout - checkin).days * rooms 

"""Aqui eu alterei apenas a linha 10
tirei o ".day" de checout e checkin, e adicionei o .days apos o parenteces"""