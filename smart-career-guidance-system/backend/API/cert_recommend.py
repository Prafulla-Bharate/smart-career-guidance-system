def get_certifications(career: str):
    platforms = [
        ("Coursera", f"https://www.coursera.org/search?query={career}"),
        ("Udemy", f"https://www.udemy.com/courses/search/?q={career}"),
        ("edX", f"https://www.edx.org/search?q={career}"),
        ("LinkedIn Learning", f"https://www.linkedin.com/learning/search?keywords={career}"),
        ("Skillshare", f"https://www.skillshare.com/search?query={career}")
    ]

    return [{"name": f"Learn {career.title()} on {platform}", "link": url} for platform, url in platforms]
