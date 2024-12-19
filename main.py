import get_and_del_hosts

def main():
    # save result
    dns_records = get_and_del_hosts.check_records(get_and_del_hosts.input_your_host)
    
    if dns_records:
        print("Записи найдены!")
        while True:
            input_your_answer = input("Вы хотите УДАЛИТЬ найденные записи (ДА или НЕТ)?: ")
            
            if input_your_answer == "ДА":
                get_and_del_hosts.del_records(dns_records)
            elif input_your_answer == "НЕТ":
                print (dns_records)
            break
    else:
        print("Записи не найдены или ")

main()