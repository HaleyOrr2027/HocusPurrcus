⚠️This project is very much still a work in progress. Things change a lot as I experiment, break stuff, & rebuild it⚠️

Hocus Purrcus is an experimental game that replaces traditional keyboard and mouse input with a physical, wireless wand controller. Players battle opponents on screen by performing wand motions such as block, stun, fireball, etc. The game features a playful, doodle-style aesthetic inspired by wizard cats and sketchbook art.

Instead of selecting spells manually, the game recognizes predefined wand movements and gestures such as slashes, angles, and arcs as different spell inputs. Enemy spells move dynamically across the screen, requiring players to physically aim, track targets, and sometimes shift their body position left or right to avoid or deflect incoming attacks. Movement and positioning are treated as part of the input itself, not just optional flavor.

The wand itself is a small, handheld wireless controller built around a Seeed Studio XIAO ESP32. Its designed to feel more like a physical prop than a traditional controller.

Inside the wand, the ESP32 handles wireless communication with the PC, reads motion data from an onboard gyroscope, and processes a small number of button inputs used to initiate actions. An infrared LED mounted at the tip of the wand is driven directly by the ESP32 and acts as a tracking point. An external IR camera mounted near the display watches for this LED and uses its position to estimate where the wand is pointed on the screen. This approach keeps the wand hardware simple while shifting most of the spatial tracking and calibration work to the camera and software.

The wand is powered by a small 3.7 V Li-Po battery, making it fully untethered during use. Charging and basic power regulation are handled on board so the wand can be recharged without taking it apart.  

<img width="594" height="395" alt="image" src="https://github.com/user-attachments/assets/bb7ce77a-63b4-4bfa-93ba-621cb3d4598a" />

<img width="372" height="283" alt="image" src="https://github.com/user-attachments/assets/fbd14698-7831-467a-af87-3f294e3aa552" />

