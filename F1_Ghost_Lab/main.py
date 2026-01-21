from config import YEAR_1, YEAR_2
from load_data import load_fastest_lap
from analysis import define_sectors, sector_times
from visualization import animate_ghost

tel1 = load_fastest_lap(YEAR_1)
tel2 = load_fastest_lap(YEAR_2)

total_distance = tel2["Distance"].max()
sectors = define_sectors(total_distance)

times1 = sector_times(tel1, sectors)
times2 = sector_times(tel2, sectors)

animate_ghost(tel1, tel2, sectors, times1, times2)