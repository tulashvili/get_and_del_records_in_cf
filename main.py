import get_hosts
import del_hosts

def main():
    dns_records = get_hosts.check_records(get_hosts.input_your_host)  # save result

    if dns_records:  # check result
        print("Записи найдены!")
        while True:
            input_your_answer = input('Вы хотите УДАЛИТЬ найденные записи?: ').strip().upper()

            if input_your_answer == "ДА":
                del_hosts.del_records(get_hosts.dns_records)
                break  # stop cycle
            elif input_your_answer == "НЕТ":
                print("Окей")
                break # stop cycle
            else:
                print("Неверный ввод. Попробуйте снова (Введите ДА ИЛИ НЕТ).")
    else:
        print("Записей не найдено.")

main()