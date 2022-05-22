import serial
import argparse
import sys
import requests


def get_parser() -> argparse.ArgumentParser:
    """
    Функция подготовки парсера для аргументов командной строки.
    В парсер добавляются два аргумента: номер порта и скорость
    передачи данных
    """
    parser = argparse.ArgumentParser(
        description="Программа для сборки данных с датчика и передачи на сервер")

    parser.add_argument(
        '-p', '--port',
        type=str,
        help='название порта для чтения, по умолчанию: %(default)s',
        default='COM3')

    parser.add_argument(
        '-b', '--baudrate',
        type=int,
        help='установка скорости передачи данных, по умолчанию: %(default)s',
        default=9600)

    parser.add_argument(
        '-d', '--sensor-id',
        type=int,
        help='номер датчика, с которого производится чтение, по умолчанию: %(default)s',
        default=1)


    parser.add_argument(
        '-s', '--server-address',
        type=str,
        help='Адрес сервера для хранения данных, по умолчанию: %(default)s',
        default='http://localhost:8000/api/postdata/')
    
    return parser


def send_data(data: bytes, host: str) -> None:
    # Преобразуем массив байт в строку
    s = data.decode('utf-8')
    # Убираем символ перевода строки в конце
    h_t = s.replace('\r\n', '')
    # Разделяем строку на подстроки
    (h, t) = h_t.split(';')
    # Подготавливаем тело запроса
    payload = {'temperature': t,
               'humidity': h,
               'sensor': args.sensor_id}
    r = requests.post(host, json=payload)
    # В случае возникновения ошибок, вызываем исключение
    r.raise_for_status()
    


if __name__ == '__main__':

    # Получаем подготовленный парсер для командной строки
    parser = get_parser()

    # Разбираем переданные аргументы из командной строки
    args = parser.parse_args()

    # Открываем порт. Если произошла ошибка, то выводим сообщение
    # об ошибке и завершаем программу
    try:
        ser = serial.Serial(port=args.port, baudrate=args.baudrate)
    except serial.SerialException as e:
        sys.stderr.write(f'Ошибка открытия порта {args.port}: {e}')
        sys.exit(1)

    print('Чтение данных... Нажмите Ctrl+C для завершения')
    while True:
        try:
            # Пока данных нет, ничего не делаем
            while ser.inWaiting() == 0:
                pass
            data = ser.readline()
            send_data(data, args.server_address)
        except requests.exceptions.HTTPError as e:
            print(f'Ошибка отправки данных на сервер: {e}')
        except requests.exceptions.ConnectionError as e:
            print(f'Ошибка подключения к серверу сбора данных: {e}')
        except KeyboardInterrupt:
            print('Чтение данных прервано пользователем')
            break;    


    # Перед выходом из программы закрываем открытый порт
    print(f'Закрываем порт {args.port}')
    ser.close()
