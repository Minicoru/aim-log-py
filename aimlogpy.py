from datetime import datetime


def aimlog(log_message):
    timestamp = datetime.now().isoformat()
    file_name = f"{timestamp.split('T')[0]}.log"
    typeof_object = type(log_message).__name__
    typeof_object_padded = typeof_object.ljust(14, " ")
    if not isinstance(log_message, str):
        try:
            log_message = str(log_message)
        except Exception as e:
            pass

    line_to_write = f"{timestamp} | [Type of Object]: {typeof_object_padded} | [content]: {log_message}\n"
    with open(file_name, "a") as file:
        file.write(line_to_write)

    return True
