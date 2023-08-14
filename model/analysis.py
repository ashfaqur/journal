import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages


def analyze(months):
    for month in months:
        pdf = PdfPages(f"{month}.pdf")
        pie_chart_entries(month, pdf)
        bar_chart_entries(month, pdf)
        pdf.close()


def pie_chart_entries(month, pdf):
    days = month.get_days()
    total_num_days = len(days)
    days_with_notes = [day for day in days if day.get_notes()]
    num_days_with_notes = len(days_with_notes)
    y = np.array([num_days_with_notes, total_num_days - num_days_with_notes])
    labels = ["Journal Entries", "No Journal Entries"]
    plt.figure()
    plt.title(f"Entries in {month}")
    plt.pie(y, labels=labels, autopct='%1.1f%%')
    pdf.savefig()


def bar_chart_entries(month, pdf):
    days = month.get_days()
    day_dates = [day.get_day_number() for day in days]
    print(day_dates)
    x_positions = np.arange(len(day_dates)) * 2
    day_entries = [len(day.get_notes()) for day in days]
    plt.figure()
    plt.bar(x_positions, day_entries)
    plt.xticks(x_positions, day_dates, fontsize=7)

    plt.xlabel('Day')
    plt.ylabel('Number of Entries')
    plt.title(f"Entries in {month}")
    pdf.savefig()
