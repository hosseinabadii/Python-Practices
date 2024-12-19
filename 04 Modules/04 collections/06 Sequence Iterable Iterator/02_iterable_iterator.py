"""
The implementation with an iterable will use less memory, but it takes up to O(n)
to get an element, whereas implementing a sequence will use more memory (because
we have to hold everything at once), but supports indexing in constant time, O(1).
"""

from collections.abc import Iterable, Iterator, Sequence
from datetime import date, timedelta


class DateRangeContainerIterable(Iterable):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def __iter__(self):
        """This method is responsible for returning the iterator object."""
        current_day = self.start_date
        while current_day < self.end_date:
            yield current_day
            current_day += timedelta(days=1)


class DateRangeIterator(Iterator):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._present_day = start_date

    def __next__(self):
        """This method is responsible for returning the next element."""
        if self._present_day >= self.end_date:
            raise StopIteration()
        today = self._present_day
        self._present_day += timedelta(days=1)
        return today


class DateRangeSequence(Sequence):
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self._range = self._create_range()

    def _create_range(self):
        days = []
        current_day = self.start_date
        while current_day < self.end_date:
            days.append(current_day)
            current_day += timedelta(days=1)
        return days

    def __getitem__(self, day_no):
        return self._range[day_no]

    def __len__(self):
        return len(self._range)


def main():
    print("-" * 50)
    print("Using: DateRangeContainerIterable(Iterable)")
    r1 = DateRangeContainerIterable(date(2024, 2, 1), date(2024, 2, 5))
    for day in r1:
        print(day)

    try:
        print(f"max(r1) : {max(r1)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("-" * 50)
    print("Using: DateRangeIterator(Iterator)")
    r2 = DateRangeIterator(date(2024, 1, 1), date(2024, 1, 5))
    for day in r2:
        print(day)

    try:
        print(f"max(r2) : {max(r2)}")
    except ValueError as e:
        print(f"Error: {e}")

    print("-" * 50)
    print("Using: DateRangeSequence(Sequence)")
    r3 = DateRangeSequence(date(2024, 3, 1), date(2024, 3, 5))
    for day in r3:
        print(day)

    try:
        print(f"max(r3) : {max(r3)}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
