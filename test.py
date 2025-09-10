import logging
from build import example

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s [%(pathname)s:%(lineno)d] %(message)s",
)

print(example.Session("", "", print))
