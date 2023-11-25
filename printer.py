import win32print



# Get the name of the installed printer
printer_name = win32print.GetDefaultPrinter()

# Get a printer handle to retrieve information about the printer
hPrinter = win32print.OpenPrinter(printer_name)

# Get the printer status information
printer_info = win32print.GetPrinter(hPrinter, 2)
print(printer_info)
printer_status = printer_info['Status']
print(printer_status)


if printer_status == win32print.PRINTER_STATUS_PAUSED:
    print('Принтер приостановлен')
elif printer_status == win32print.PRINTER_STATUS_PENDING_DELETION:
    print('Принтер ожидает удаления')
elif printer_status == win32print.PRINTER_STATUS_ERROR:
    print('Принтер не работает из-за ошибки')
elif printer_status == win32print.PRINTER_STATUS_BUSY:
    print('Принтер занят')
elif printer_status == win32print.PRINTER_STATUS_OFFLINE:
    print('Принтер офлайн')
