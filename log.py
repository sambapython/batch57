import logging  # debug, info, warn, error
logging.basicConfig(level=logging.DEBUG,
    filename="log.txt",
    format="%(asctime)s-->%(levelname)s==>%(message)s")
logging.info("welcome to the division operation")
a=input("enter a value:")
logging.info("A value entered")
b=input("Enter b value:")
logging.info("b value entered")
logging.debug(f" before conversion a={a},b={b}")
try:
    a=float(a)
    logging.info("a value converted successfully!!")
    b=float(b)
    logging.info("b value converted successfully!!")
    logging.debug(f" after conversion a={a},b={b}")
    res=a/b
    res_statment = f"result={res}"
    print(res_statment)
    logging.debug(res_statment)

except ValueError as err:
    logging.error(err)
    print("expecting digits only")
except ZeroDivisionError as err:
    logging.error(err)
    print("b!=0")
except Exception as err:
    logging.error(err)
logging.info("operation successfully completed")
print("thank you use me again")
