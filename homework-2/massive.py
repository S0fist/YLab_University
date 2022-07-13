from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        c = self.dates
        s = []
        for i in c:
            first_date = i[0]
            last_date = i[1]
            s.append(first_date)
            while first_date != last_date:
                first_date += timedelta(days=1)
                s.append(first_date)
        return s

if __name__ == "__main__":
    m = Movie('sw', [
        (datetime(2020, 1, 1), datetime(2020, 1, 7)),
        (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])
    for d in m.schedule():
        print(d)
