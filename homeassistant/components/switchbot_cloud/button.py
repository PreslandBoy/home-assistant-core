"""Platform for button integration."""

from switchbot_api import Device, SwitchBotAPI

from homeassistant.components.button import ButtonEntity, ButtonEntityDescription
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from . import SwitchbotCloudData
from .const import BUTTON_DESCRIPTION, DOMAIN, BotCommands
from .coordinator import SwitchBotCoordinator
from .entity import SwitchBotCloudEntity


async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up SwitchBot Cloud entry."""
    data: SwitchbotCloudData = hass.data[DOMAIN][config.entry_id]
    for device, coordinator in data.devices.buttons:
        async_add_entities(
            [SwitchBotButton(data.api, device, coordinator, BUTTON_DESCRIPTION)]
        )


class SwitchBotButton(SwitchBotCloudEntity, ButtonEntity):
    """Representation of a SwitchBot switch."""

    def __init__(
        self,
        api: SwitchBotAPI,
        device: Device,
        coordinator: SwitchBotCoordinator,
        description: ButtonEntityDescription,
    ) -> None:
        """Initialize SwitchBot Cloud sensor entity."""
        super().__init__(api, device, coordinator)
        self.entity_description = description

    async def async_press(self) -> None:
        """Send command to press button."""
        await self.send_command(BotCommands.PRESS)
