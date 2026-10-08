class Tariff:
    def get_rate(self, usage):
        if usage <= 100:
            return 0.00
        elif usage <= 200:
            return 2.35
        elif usage <= 400:
            return 4.70
        else:
            return 6.30

    def calculate_bill(self, units_consumed):
        if units_consumed <= 100:
            return 0.00
        elif units_consumed <= 200:
            return (units_consumed - 100) * 2.35
        elif units_consumed <= 400:
            return (100 * 2.35) + (units_consumed - 200) * 4.70
        else:
            return (100 * 2.35) + (200 * 4.70) + (units_consumed - 400) * 6.30