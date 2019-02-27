import logging


try:
    a = input("number")
    print(int(a)**2)

except Exception:
    logging.getLogger().error("Something bad happened", exc_info=True)

