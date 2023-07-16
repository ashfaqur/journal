import matplotlib.pyplot as plt
import numpy as np


def analyze(months):
    for month in months:
        days = month.get_days()
        total_num_days = len(days)
        days_with_notes = [day for day in days if day.get_notes()]
        num_days_with_notes = len(days_with_notes)
        y = np.array([num_days_with_notes, total_num_days - num_days_with_notes])
        labels = ["Journal Entries", "No Journal Entries"]
        plt.title(f"Month of {month}")
        plt.pie(y, labels=labels, autopct='%1.1f%%')
        plt.show()
