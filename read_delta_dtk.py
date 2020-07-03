#!/usr/bin/env python

import minimalmodbus

PORT='/dev/cu.usbserial-1420'
SLAVE_ID=1
PV_REG=0x1000

instrument = minimalmodbus.Instrument(PORT,SLAVE_ID,mode=minimalmodbus.MODE_RTU)

instrument.serial.baudrate = 38400
instrument.serial.bytesize = 8
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE
instrument.serial.stopbits = 1
instrument.serial.timeout = 1

instrument.close_port_after_each_call = True
instrument.clear_buffers_before_each_transaction = True

bt_data = instrument.read_register(PV_REG)

instrument.address = 2

et_data = instrument.read_register(PV_REG)

print(et_data / 10, ',', bt_data / 10)
