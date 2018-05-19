# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/) ~~and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).~~

## [Unreleased]

### Added
- Clickable links in the MOTD
- Line-wrapping in the MOTD
- Option to blur background of Click GUI frames
- Button to open Click GUI from the Impact gui menu
- Colored sign text exploit
- Option to save logout positions in Log Position
- Movement speed widget in the HUD
- Opacity option for Click GUI
- Jump option for the strafe speed mode
- Skylight option for light module to prevent skylight lag machines from working
- Totem counter option to Auto Totem
- Customization for suffixes in module list
- Auto Break option for nuker
- Origin option for nuker to choose the break origin
- Target option for nuker to choose the blocks targetted
- Filter option for nuker to use the nuker ID list
- Crosshair prioritization mode for Kill Aura
- Swing option for Scaffold

### Changed
- Automatically focus the username field in the alt creation screen
- Alts are now stored in a json format
- Significantly improve scaffold in all movement directions
- Improve jitter on Auto Clicker
- Added mineplex support for team check
- Freecam is now always in first person view

### Removed
- Mode option for nuker

### Fixed
- Fixed incorrect angle calculations in combat modules
- No Fall Bucket mode getting stuck on the collection stage
- Xray GUI arrows not displaying with a transparent background
- Issues caused when disabling the Click GUI
- drop command not targetting correct slots
- Chams affecting models in the alt manager
- Smooth aim targetting incorrect positions
- Friends GUI causing a crash
- Alt GUI having transparent background when in-game
- Some vertical spacing problems with the HUD
- Cycler boxes in Click GUI not properly encasing children
- Freecam causing weird behavior while riding entities
- ChestStealer not functioning as expected