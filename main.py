import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# from datetime import datetime

# Data from the task schedule
data = {
    'Task': [
        'Requirement Analysis', 'Gather requirements', 'Feasibility study',
        'System Design', 'Design frontend UI mockups', 'Design backend architecture',
        'Frontend Development', 'Implement login and registration', 'Implement news search UI', 'Implement history panel UI',
        'Backend Development', 'User authentication module', 'Web scraping and data processing', 'Admin panel (CRUD operations)',
        'Database Setup', 'Create user data schema', 'Implement news data storage',
        'Testing and Debugging', 'Frontend testing', 'Backend testing', 'Integration testing',
        'Final Review and Documentation', 'Review system', 'Write documentation',
        'Project Deployment', 'Deploy application to server',
        'Buffer Time (for any delays)',
        'Project Presentation Preparation'
    ],
    'Start': [
        'Sep 19, 2024', 'Sep 19, 2024', 'Sep 22, 2024',
        'Sep 24, 2024', 'Sep 24, 2024', 'Sep 27, 2024',
        'Oct 1, 2024', 'Oct 1, 2024', 'Oct 4, 2024', 'Oct 10, 2024',
        'Oct 15, 2024', 'Oct 15, 2024', 'Oct 18, 2024', 'Oct 25, 2024',
        'Oct 29, 2024', 'Oct 29, 2024', 'Oct 31, 2024',
        'Nov 4, 2024', 'Nov 4, 2024', 'Nov 7, 2024', 'Nov 10, 2024',
        'Nov 11, 2024', 'Nov 11, 2024', 'Nov 13, 2024',
        'Nov 16, 2024', 'Nov 16, 2024',
        'Nov 18, 2024',
        'Nov 23, 2024'
    ],
    'End': [
        'Sep 23, 2024', 'Sep 21, 2024', 'Sep 23, 2024',
        'Sep 30, 2024', 'Sep 26, 2024', 'Sep 30, 2024',
        'Oct 14, 2024', 'Oct 3, 2024', 'Oct 9, 2024', 'Oct 14, 2024',
        'Oct 28, 2024', 'Oct 17, 2024', 'Oct 24, 2024', 'Oct 28, 2024',
        'Nov 1, 2024', 'Oct 30, 2024', 'Nov 1, 2024',
        'Nov 10, 2024', 'Nov 6, 2024', 'Nov 9, 2024', 'Nov 10, 2024',
        'Nov 15, 2024', 'Nov 12, 2024', 'Nov 15, 2024',
        'Nov 17, 2024', 'Nov 17, 2024',
        'Nov 22, 2024',
        'Nov 25, 2024'
    ]
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Convert the 'Start' and 'End' columns to datetime format
df['Start'] = pd.to_datetime(df['Start'], format='%b %d, %Y')
df['End'] = pd.to_datetime(df['End'], format='%b %d, %Y')

# Calculate the duration of each task
df['Duration'] = df['End'] - df['Start']

# Create a figure and axis for the Gantt chart
fig, ax = plt.subplots(figsize=(12, 8))

# Plot each task as a bar in the Gantt chart
for i, task in enumerate(df.itertuples()):
    ax.barh(task.Task, task.Duration.days, left=task.Start, color=plt.cm.tab20(i / len(df)))

# Format the x-axis to show dates properly
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d, %Y"))
plt.xticks(rotation=45)

# Add labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Task')
ax.set_title('Project Gantt Chart')

# Add grid lines
ax.grid(True, which='both', axis='both', linestyle='--', linewidth=0.5)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()
