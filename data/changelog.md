# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) ~~and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).~~

## Unreleased

### Added
- Tower option for Scaffold
- Lethal option for No Fall Bucket mode to only place water when the fall is lethal
- Debug option for Scaffold to allow for better visualization of block placement
- Delay option for Auto Clicker to use 1.9 attack cooldown
  - Also added TPS Sync sub-option to sync swing delay with TPS
- Discord RPC support
- No SRP module, prevents servers from forcing resource packs
- Added name case change exploit as a command (.rename)
- Added ESP color types (Custom, Team, Health)
- Allow Auto Totem to access crafting slots to retrieve Totems
  - Should be combined with Inventory's "Extra Slots" feature
- Added Fancy Chat module to type in alternative latin charsets
- Added command to check fall damage to a block (.falldamage)
  - Checks the fall damage to the block you are looking at
- Added Ping Spoof module
- Integration with Baritone
- Added Bot option to Auto Mine (Automatically mine to ores)
- Added Lava and Portals to Xray by default

### Changed
- Separated horizontal and vertical speed in Freecam
- Changed Fast Interact's Fast Break option from breaking blocks faster to lowering block break delay
- Made latency compensation in the Minestrike module optional
- Xray and Nuker config files will now use namespace block ids instead of numerical

### Fixed
- Fixed uncommon crash caused by GuiTextContainingLinks
- Fixed Scaffold not working on NCP due to bad angles
- Fixed Scaffold providing server with suspicious looking packets
- Fixed Scaffold crashing under specific conditions
- Fixed Riding causing boats to bob if the swim option is checked
- Step working when in water or lava
- Fixed enum type values not saving/loading properly
  - Only affected options for HUD module
- Fixed bug with Auto Tool that caused game to crash under specific circumstances
  - Crashed when there was not a valid tool on the hotbar and it has not previously succeeded
- Fixed boat rotation in the Riding module
  - Boats now rotate to the direction that you're looking
  - Fixed "strafing" while in boats
- Fixed Anti Vanish causing the game to crash
- Fixed Flowing option for Jesus Solid mode
- Fixed ColorType values loading with 0 opacity
- Fixed Criticals not working while sprinting
- Fixed issues caused by Fast Render by forcefully disabling it
- Fixed hopper and furnace minecarts not being shown by Storage ESP

## 4.3

### Added
- Button to open Click GUI from the Impact menu
- Ability to open chat while Click GUI is open
- "Main Menu" entry in Click GUI's Render section
  - Toggle using Impact's custom main menu
  - Toggle using Impact's replacement menu wallpaper
- Clickable links and line-wrapping in the MOTD header
- Colored sign text exploit
- Movement speed widget in the HUD
- Customization for suffixes in module list
- Pause option for Click GUI
- Opacity option for Click GUI
- Option to blur background of Click GUI frames
- Option to save logout positions in Log Position
- Rank option for Nametags to show team prefix and suffix
- Catch Delay option for AutoFish (might help with fussy servers)
- Jump option for the strafe speed mode
- Skylight option for light module to prevent skylight lag machines from working
- Totem counter option to Auto Totem
- Auto Break option for nuker
- Origin option for nuker to choose the break origin
- Target option for nuker to choose the blocks targetted
- Filter option for nuker to use the nuker ID list
- Crosshair prioritization mode for Kill Aura
- Swing option for Scaffold
- Shulker Tooltip option for Inventory to change the tooltip length
- Shulker Coallate option for Inventory to group item stacks together in the tooltip
- Option to only shoot when scoped for Minestrike module
- Option to ignore attacking friends for Minestrike module
- Support for offhand in Scaffold
  - Added option to prioritize offhand which is on by default
- Swing option for breaker to show breaking on the client side
- "Reconnect" command that quickly disconnects and reconnects the user from their current server

### Changed
- Use player's team color in Nametags
- AutoFish options should be clearer now
- AutoFish AutoCast is now off by default
- Automatically focus the username field when creating an Alt
- Alts are now stored in a json format to enable future fanciness
- Significantly improve scaffold in all movement directions
- Improve jitter on Auto Clicker
- Added mineplex support for team check
- Freecam is now always in first person view
- Moved Inventory to the Misc category, updated its description and made move an option
- Click GUI menus now stay on the screen at all times
- Click GUI menus are now easier to navigate
  - Clicking the arrows next to modules will open the submen
  - Double clicking the menus will open them (like right click)
  - Move menus around by dragging anywhere within them (hold `Ctrl` or use middle mouse)
- Click GUI's keybind widget now has a tooltip and is easier to use
  - Left click to modify the bind
  - Clicking again (or pressing `Esc` will cancel)
  - Right click to delete/reset the bind
- `.set` command can now use option id as an alternative to name
- Removed all server-side changes (should make singleplayer more stable)

### Removed
- Mode option for nuker

### Fixed
- Absorption not being shown by Nametags
- `.set` command not finding nested options
- Fixed incorrect angle calculations in combat modules
- Incorrect murderer detection on Hypixel's Murder Mystery
- Incorrect murderer detection on PlayMCM
- No Fall Bucket mode getting stuck on the collection stage
- Dolphin Jesus jumping while in GUIs, even when out of water
- Xray GUI arrows not displaying with a transparent background
- Not being able to toggle mods or open Click GUI after toggling fullscreen mode
- Click GUI not always being saved on shutdown
- Issues caused when disabling the Click GUI
- Click GUI not rendering closed menus correctly until they are re-closed
- drop command not targetting correct slots
- Chams affecting models in the alt manager
- Smooth aim targetting incorrect positions
- Friends GUI causing a crash
- Alt GUI having transparent background while in-game
- Some vertical spacing problems with the HUD
- Cycler boxes in Click GUI not properly encasing children
- Freecam causing weird behavior while riding entities
- ChestStealer not functioning as expected
- Forge and Optifine support ~~(probably)~~
- AntiAFK "jump" option not working when a GUI is open
- AutoTool not applying to Nuker
- Fixed Riding "Entity Speed" not applying to boats
- Fixed Scaffold not placing glass blocks
