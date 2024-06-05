"""Constants for the SwitchBot Cloud integration."""

from datetime import timedelta
from enum import Enum
from typing import Final

from homeassistant.components.button import ButtonEntityDescription
from homeassistant.components.sensor import (
    SensorDeviceClass,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import PERCENTAGE, UnitOfTemperature

DOMAIN: Final = "switchbot_cloud"
ENTRY_TITLE = "SwitchBot Cloud"
DEFAULT_SCAN_INTERVAL = timedelta(seconds=600)

ENTITY_KIND_TEMPERATURE = "temperature"
ENTITY_KIND_HUMIDITY = "humidity"
ENTITY_KIND_BATTERY = "battery"
ENTITY_KIND_BUTTON = "button"

BATTERY_SENSOR_DESCRIPTION = SensorEntityDescription(
    key=ENTITY_KIND_BATTERY,
    device_class=SensorDeviceClass.BATTERY,
    state_class=SensorStateClass.MEASUREMENT,
    native_unit_of_measurement=PERCENTAGE,
)

HUMIDITY_SENSOR_DESCRIPTION = SensorEntityDescription(
    key=ENTITY_KIND_HUMIDITY,
    device_class=SensorDeviceClass.HUMIDITY,
    state_class=SensorStateClass.MEASUREMENT,
    native_unit_of_measurement=PERCENTAGE,
)

TEMPERATURE_SENSOR_DESCRIPTION = SensorEntityDescription(
    key=ENTITY_KIND_TEMPERATURE,
    device_class=SensorDeviceClass.TEMPERATURE,
    state_class=SensorStateClass.MEASUREMENT,
    native_unit_of_measurement=UnitOfTemperature.CELSIUS,
)

BUTTON_DESCRIPTION = ButtonEntityDescription(
    key=ENTITY_KIND_BUTTON,
)


class BotCommands(Enum):
    """Commands for SwitchBot Bot device."""

    PRESS = "press"
    TURN_ON = "turnOn"
    TURN_OFF = "turnOff"
