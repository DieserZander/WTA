from models.model_manager import ModelManager


class Workday(ModelManager):
    def __init__(self):
        self.table_name = "workday"
        self.columns = {
            'date' : {'unique': True},
            'on_holiday' : {'unique': False}
        }
            # ["date", "on_holiday"]
        super().__init__(table_name=self.table_name, columns=self.columns)

    # def validate_entry(self):

