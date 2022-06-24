from db.database import Database
from models.workday import Workday
from ui.main import MainWindow

if __name__ == "__main__":
    # win = MainWindow()
    mm = Workday()
    data = {'date': '2022-06-21', 'on_holiday': False}
    mm.post_entry(data)