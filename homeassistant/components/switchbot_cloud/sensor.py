"""Platform for sensor integration."""

from switchbot_api import Device, SwitchBotAPI

from homeassistant.components.sensor import SensorEntity, SensorEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import SwitchbotCloudData
from .const import (
    BATTERY_SENSOR_DESCRIPTION,
    DOMAIN,
    HUMIDITY_SENSOR_DESCRIPTION,
    TEMPERATURE_SENSOR_DESCRIPTION,
)
from .coordinator import SwitchBotCoordinator
from .entity import SwitchBotCloudEntity

METER_PLUS_SENSOR_DESCRIPTIONS = (
    BATTERY_SENSOR_DESCRIPTION,
    HUMIDITY_SENSOR_DESCRIPTION,
    TEMPERATURE_SENSOR_DESCRIPTION,
)


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SwitchBot Cloud entry."""
    data: SwitchbotCloudData = hass.data[DOMAIN][config.entry_id]
    for device, coordinator in data.devices.sensors:
        if device.device_type in [
            "Meter",
            "MeterPlus",
            "WoIOSensor",
        ]:
            async_add_entities(
                SwitchBotCloudSensor(data.api, device, coordinator, description)
                for description in METER_PLUS_SENSOR_DESCRIPTIONS
            )
        elif device.device_type == "Bot":
            async_add_entities(
                [
                    SwitchBotCloudSensor(
                        data.api, device, coordinator, BATTERY_SENSOR_DESCRIPTION
                    )
                ]
            )


class SwitchBotCloudSensor(SwitchBotCloudEntity, SensorEntity):
    """Representation of a SwitchBot Cloud sensor entity."""

    def __init__(
        self,
        api: SwitchBotAPI,
        device: Device,
        coordinator: SwitchBotCoordinator,
        description: SensorEntityDescription,
    ) -> None:
        """Initialize SwitchBot Cloud sensor entity."""
        super().__init__(api, device, coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{device.device_id}_{description.key}"

    @callback
    def _handle_coordinator_update(self) -> None:
        """Handle updated data from the coordinator."""
        if not self.coordinator.data:
            return
        self._attr_native_value = self.coordinator.data.get(self.entity_description.key)
        self.async_write_ha_state()
