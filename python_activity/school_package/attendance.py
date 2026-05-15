def attendance_status(status):
    if status.lower() == "present":
        return "Student is present."
    return "Student is absent."