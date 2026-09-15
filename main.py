from datetime import date


project_name = "Система управления этапами разработки"
stage_name = "Реализация начального сценария"
responsible_person = "Студент"
deadline = date(2026, 9, 20)
completion_percent = 65
is_approved = False


def get_stage_status(percent, approved):
    if approved and percent == 100:
        return "Этап завершен и согласован"
    if percent == 100:
        return "Этап завершен, но ожидает согласования"
    if percent >= 50:
        return "Этап находится в работе"
    return "Этап только начат"


def check_deadline(stage_deadline):
    today = date.today()

    if today > stage_deadline:
        return "Срок выполнения этапа нарушен"
    if today == stage_deadline:
        return "Сегодня последний день выполнения этапа"
    return "Срок выполнения этапа еще не истек"


def calculate_remaining_work(percent):
    remaining_percent = 100 - percent

    if remaining_percent < 0:
        return 0
    return remaining_percent


def get_recommendation(percent, approved, stage_deadline):
    today = date.today()

    if approved and percent == 100:
        return "Можно переходить к следующему этапу разработки"
    if today > stage_deadline:
        return "Необходимо ускорить выполнение и пересмотреть срок этапа"
    if percent >= 80:
        return "Рекомендуется завершить оставшиеся задачи и отправить этап на проверку"
    return "Рекомендуется продолжить выполнение задач текущего этапа"


print(f"Проект: {project_name}")
print(f"Этап: {stage_name}")
print(f"Ответственный: {responsible_person}")
print(f"Срок выполнения: {deadline}")
print(f"Готовность: {completion_percent}%")
print(f"Статус: {get_stage_status(completion_percent, is_approved)}")
print(f"Контроль срока: {check_deadline(deadline)}")
print(f"Осталось выполнить: {calculate_remaining_work(completion_percent)}%")
print(f"Рекомендация: {get_recommendation(completion_percent, is_approved, deadline)}")
