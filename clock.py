import time
import datetime

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.legacy import show_message
from luma.core.legacy.font import (
    proportional,
    LCD_FONT,
)


def run():
    try:
        print("running clock...")

        serial = spi(port=0, device=0, gpio=noop())
        device = max7219(
            serial,
            cascaded=4,
            block_orientation=-90,
            rotate=0,
            blocks_arranged_in_reverse_order=False,
        )

        while True:
            now = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
            print("date and time:", now)
            show_message(
                device,
                now,
                fill="white",
                font=proportional(LCD_FONT),
                scroll_delay=0.02,
            )

    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    try:
        time.sleep(5)
        run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print("Error in main: ", e)
