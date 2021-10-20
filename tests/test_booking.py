from typing import Collection, Dict, Tuple

from event_packing.booking import book_meetings


def test_book_meetings(
    example_meetings: Dict[str, Tuple[Collection[Collection[int]], int]]
) -> None:
    for test_name, (meetings, num_attendees) in example_meetings.items():
        booked_meetings, booked_attendees = book_meetings(meetings)
        assert (
            len(booked_attendees) == num_attendees
        ), f"Failed {test_name}: {booked_meetings} with {booked_attendees}"
