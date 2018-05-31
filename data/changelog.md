# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) ~~and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).~~

## [Unreleased]

### Added
- Button to open Click GUI from the Impact menu
- Clickable links and line-wrapping in the MOTD header
- Colored sign text exploit
- Movement speed widget in the HUD
- Customization for suffixes in module list
- Pause option for Click GUI
- Opacity option for Click GUI
- Option to blur background of Click GUI frames
- Option to save logout positions in Log Position
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

### Changed
- AutoFish options should be clearer now
- AutoFish AutoCast is now off by default
- Automatically focus the username field when creating an Alt
- Alts are now stored in a json format to enable future fanciness
- Significantly improve scaffold in all movement directions
- Improve jitter on Auto Clicker
- Added mineplex support for team check
- Freecam is now always in first person view
- Moved Inventory to the Misc category and changed its description to fit new functionality
- Click GUI menus now stay on the screen at all times
- Click GUI menus are now easier to navigate
  - Clicking the arrows next to modules will open the submen
  - Double clicking the menus will open them (like right click)
  - Move menus around by dragging anywhere within them (hold `Ctrl` or use middle mouse)
- Click GUI's keybind widget now has a tooltip and is easier to use
  - Left click to modify the bind
  - Clicking again (or pressying `Esc` will cancel)
  - Right click to delete/reset the bind
- `.set` command can now use option id as an alternative to name

### Removed
- Mode option for nuker

### Fixed
- `.set` command not finding nested options
- Fixed incorrect angle calculations in combat modules
- No Fall Bucket mode getting stuck on the collection stage
- Dolphin Jesus jumping while in GUIs, even when out of water
- Xray GUI arrows not displaying with a transparent background
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
- Forge and Optifine support (probably)