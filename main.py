import pandas as pd
import matplotlib.pyplot as plt


def get_combined_employee_data(file_path):
    df = pd.read_csv(file_path, encoding='latin-1')
    dfc = df.drop(['location_name', 'location_latitude', 'location_longitude', 'comments', 'salary_id', 'submitted_at',
                   'job_title_rank', 'job_title'], axis=1)
    apple_employees = dfc[dfc['employer_name'] == 'apple']
    google_employees = dfc[dfc['employer_name'] == 'google']
    amazon_employees = dfc[dfc['employer_name'] == 'amazon']
    combined_employees = pd.concat([apple_employees, google_employees, amazon_employees])
    combined_employees["total_pay"] = combined_employees["annual_base_pay"].fillna(0) + combined_employees["annual_bonus"].fillna(0)
    result = combined_employees.groupby(["employer_name", "total_experience_years", "job_title_category"])["total_pay"].mean().reset_index()
    return result


def create_pay_experience_scatter(data):
    plt.figure(figsize=[12, 6])

    # Scatter plot for Apple employees
    plt.subplot(1, 3, 1)
    apple_data = data[data["employer_name"] == "apple"]
    job_categories = apple_data["job_title_category"].unique()
    for category in job_categories:
        category_data = apple_data[apple_data["job_title_category"] == category]
        plt.scatter(category_data["total_experience_years"], category_data["total_pay"], label=category, alpha=0.7)
    plt.xlabel("Experience Years")
    plt.ylabel("Average Pay")
    plt.title("Pay vs. Experience for Apple Employees")
    plt.legend()

    # Scatter plot for Google employees
    plt.subplot(1, 3, 2)
    google_data = data[data["employer_name"] == "google"]
    job_categories = google_data["job_title_category"].unique()
    for category in job_categories:
        category_data = google_data[google_data["job_title_category"] == category]
        plt.scatter(category_data["total_experience_years"], category_data["total_pay"], label=category, alpha=0.7)
    plt.xlabel("Experience Years")
    plt.ylabel("Average Pay")
    plt.title("Pay vs. Experience for Google Employees")
    plt.legend()

    # Scatter plot for Amazon employees
    plt.subplot(1, 3, 3)
    amazon_data = data[data["employer_name"] == "amazon"]
    job_categories = amazon_data["job_title_category"].unique()
    for category in job_categories:
        category_data = amazon_data[amazon_data["job_title_category"] == category]
        plt.scatter(category_data["total_experience_years"], category_data["total_pay"], label=category, alpha=0.7)
    plt.xlabel("Experience Years")
    plt.ylabel("Average Pay")
    plt.title("Pay vs. Experience for Amazon Employees")
    plt.legend()

    plt.tight_layout()
    plt.show()


# Usage
file_path = 'cleaned_salaries.csv'
employee_data = get_combined_employee_data(file_path)
create_pay_experience_scatter(employee_data)
