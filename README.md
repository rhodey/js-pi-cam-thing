
## Upstart
  1. all upstart configs go into /etc/init/
  2. camera archiver script is /etc/init/pi-camera.conf
  3. to reload all upstart configs use: sudo initctl reload-configuration
  4. to manually start pi-camera: sudo start pi-camera
  5. to manually stop pi-camera: sudo stop pi-camera
